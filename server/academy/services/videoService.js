import { getSignedUrl } from '@aws-sdk/cloudfront-signer';
import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl as getS3SignedUrl } from '@aws-sdk/s3-request-presigner';
import fs from 'fs';
import path from 'path';

// CloudFront configuration
const CLOUDFRONT_DOMAIN = process.env.CLOUDFRONT_DOMAIN || '';
const CLOUDFRONT_KEY_PAIR_ID = process.env.CLOUDFRONT_KEY_PAIR_ID || '';
const CLOUDFRONT_PRIVATE_KEY_PATH = process.env.CLOUDFRONT_PRIVATE_KEY_PATH || '';

// S3 configuration (fallback if CloudFront not configured)
const S3_BUCKET = process.env.VIDEO_S3_BUCKET || 'support-forge-videos';
const AWS_REGION = process.env.AWS_REGION || 'us-east-1';

// URL expiration time (4 hours)
const URL_EXPIRATION_SECONDS = 4 * 60 * 60;

// S3 client (lazy initialization)
let s3Client = null;

function getS3Client() {
  if (!s3Client) {
    s3Client = new S3Client({
      region: AWS_REGION,
      // Credentials will be picked up from environment or IAM role
    });
  }
  return s3Client;
}

// Cache for CloudFront private key
let cloudfrontPrivateKey = null;

function getCloudFrontPrivateKey() {
  if (!cloudfrontPrivateKey && CLOUDFRONT_PRIVATE_KEY_PATH) {
    try {
      // Support both file path and inline key (for Docker secrets)
      if (CLOUDFRONT_PRIVATE_KEY_PATH.startsWith('-----BEGIN')) {
        cloudfrontPrivateKey = CLOUDFRONT_PRIVATE_KEY_PATH;
      } else {
        cloudfrontPrivateKey = fs.readFileSync(CLOUDFRONT_PRIVATE_KEY_PATH, 'utf8');
      }
    } catch (error) {
      console.error('Failed to read CloudFront private key:', error.message);
    }
  }
  return cloudfrontPrivateKey;
}

/**
 * Generate a signed URL for video playback
 * Uses CloudFront if configured, falls back to S3 pre-signed URLs
 *
 * @param {string} s3Key - The S3 key of the video file
 * @param {string} cloudfrontUrl - Pre-configured CloudFront URL (optional)
 * @returns {Promise<string>} Signed URL for video access
 */
export async function generateSignedUrl(s3Key, cloudfrontUrl = null) {
  // Try CloudFront first (preferred for video delivery)
  if (isCloudFrontConfigured()) {
    return generateCloudFrontSignedUrl(s3Key, cloudfrontUrl);
  }

  // Fallback to S3 pre-signed URL
  return generateS3SignedUrl(s3Key);
}

/**
 * Check if CloudFront signing is properly configured
 */
function isCloudFrontConfigured() {
  const privateKey = getCloudFrontPrivateKey();
  return !!(CLOUDFRONT_DOMAIN && CLOUDFRONT_KEY_PAIR_ID && privateKey);
}

/**
 * Generate a CloudFront signed URL
 */
function generateCloudFrontSignedUrl(s3Key, existingUrl = null) {
  const privateKey = getCloudFrontPrivateKey();

  if (!privateKey) {
    throw new Error('CloudFront private key not available');
  }

  // Build the URL
  const url = existingUrl || `https://${CLOUDFRONT_DOMAIN}/${s3Key}`;

  // Calculate expiration date
  const dateLessThan = new Date(Date.now() + URL_EXPIRATION_SECONDS * 1000);

  // Generate signed URL using canned policy
  const signedUrl = getSignedUrl({
    url,
    keyPairId: CLOUDFRONT_KEY_PAIR_ID,
    privateKey,
    dateLessThan
  });

  return signedUrl;
}

/**
 * Generate an S3 pre-signed URL (fallback)
 */
async function generateS3SignedUrl(s3Key) {
  const client = getS3Client();

  const command = new GetObjectCommand({
    Bucket: S3_BUCKET,
    Key: s3Key
  });

  const signedUrl = await getS3SignedUrl(client, command, {
    expiresIn: URL_EXPIRATION_SECONDS
  });

  return signedUrl;
}

/**
 * Generate signed cookies for CloudFront (for HLS streaming)
 * This allows access to all video segments without individual signed URLs
 *
 * @param {string} resourcePath - The path pattern to sign (e.g., /courses/123/*)
 * @returns {object} Object containing signed cookies
 */
export function generateSignedCookies(resourcePath) {
  if (!isCloudFrontConfigured()) {
    throw new Error('CloudFront not configured for signed cookies');
  }

  const privateKey = getCloudFrontPrivateKey();
  const dateLessThan = new Date(Date.now() + URL_EXPIRATION_SECONDS * 1000);

  // Build the policy
  const policy = {
    Statement: [{
      Resource: `https://${CLOUDFRONT_DOMAIN}${resourcePath}`,
      Condition: {
        DateLessThan: {
          'AWS:EpochTime': Math.floor(dateLessThan.getTime() / 1000)
        }
      }
    }]
  };

  const policyString = JSON.stringify(policy);

  // Sign the policy
  const crypto = require('crypto');
  const sign = crypto.createSign('RSA-SHA1');
  sign.update(policyString);
  const signature = sign.sign(privateKey, 'base64');

  // Make the signature URL-safe
  const urlSafeSignature = signature
    .replace(/\+/g, '-')
    .replace(/=/g, '_')
    .replace(/\//g, '~');

  // Base64 encode the policy
  const encodedPolicy = Buffer.from(policyString)
    .toString('base64')
    .replace(/\+/g, '-')
    .replace(/=/g, '_')
    .replace(/\//g, '~');

  return {
    'CloudFront-Policy': encodedPolicy,
    'CloudFront-Signature': urlSafeSignature,
    'CloudFront-Key-Pair-Id': CLOUDFRONT_KEY_PAIR_ID
  };
}

/**
 * Verify a video exists in S3
 *
 * @param {string} s3Key - The S3 key to check
 * @returns {Promise<boolean>} Whether the video exists
 */
export async function videoExists(s3Key) {
  try {
    const client = getS3Client();
    const { HeadObjectCommand } = await import('@aws-sdk/client-s3');

    await client.send(new HeadObjectCommand({
      Bucket: S3_BUCKET,
      Key: s3Key
    }));

    return true;
  } catch (error) {
    if (error.name === 'NotFound') {
      return false;
    }
    throw error;
  }
}

/**
 * Get video metadata from S3
 *
 * @param {string} s3Key - The S3 key of the video
 * @returns {Promise<object>} Video metadata
 */
export async function getVideoMetadata(s3Key) {
  const client = getS3Client();
  const { HeadObjectCommand } = await import('@aws-sdk/client-s3');

  const response = await client.send(new HeadObjectCommand({
    Bucket: S3_BUCKET,
    Key: s3Key
  }));

  return {
    contentType: response.ContentType,
    contentLength: response.ContentLength,
    lastModified: response.LastModified,
    etag: response.ETag,
    metadata: response.Metadata
  };
}

export default {
  generateSignedUrl,
  generateSignedCookies,
  videoExists,
  getVideoMetadata,
  isCloudFrontConfigured
};
