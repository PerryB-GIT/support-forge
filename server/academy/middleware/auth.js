import jwt from 'jsonwebtoken';
import db from '../db/database.js';

const JWT_SECRET = process.env.JWT_SECRET || 'change-this-in-production-please';

/**
 * Middleware to verify JWT token and attach user to request
 * Rejects requests without valid authentication
 */
export function requireAuth(req, res, next) {
  try {
    const authHeader = req.headers.authorization;

    if (!authHeader) {
      return res.status(401).json({
        success: false,
        error: 'No authorization header provided'
      });
    }

    // Expect format: "Bearer <token>"
    const parts = authHeader.split(' ');
    if (parts.length !== 2 || parts[0] !== 'Bearer') {
      return res.status(401).json({
        success: false,
        error: 'Invalid authorization header format. Use: Bearer <token>'
      });
    }

    const token = parts[1];

    // Verify and decode the token
    const decoded = jwt.verify(token, JWT_SECRET);

    // Fetch user from database to ensure they still exist and are active
    const user = db.prepare(`
      SELECT id, email, name, is_active, created_at
      FROM users
      WHERE id = ?
    `).get(decoded.userId);

    if (!user) {
      return res.status(401).json({
        success: false,
        error: 'User not found'
      });
    }

    if (!user.is_active) {
      return res.status(403).json({
        success: false,
        error: 'Account is deactivated'
      });
    }

    // Attach user to request object
    req.user = user;
    next();
  } catch (error) {
    if (error.name === 'TokenExpiredError') {
      return res.status(401).json({
        success: false,
        error: 'Token has expired'
      });
    }

    if (error.name === 'JsonWebTokenError') {
      return res.status(401).json({
        success: false,
        error: 'Invalid token'
      });
    }

    console.error('Auth middleware error:', error);
    return res.status(500).json({
      success: false,
      error: 'Authentication error'
    });
  }
}

/**
 * Optional auth middleware - attaches user if token present, but doesn't require it
 * Useful for endpoints that show different data to logged-in vs anonymous users
 */
export function optionalAuth(req, res, next) {
  try {
    const authHeader = req.headers.authorization;

    if (!authHeader) {
      req.user = null;
      return next();
    }

    const parts = authHeader.split(' ');
    if (parts.length !== 2 || parts[0] !== 'Bearer') {
      req.user = null;
      return next();
    }

    const token = parts[1];

    try {
      const decoded = jwt.verify(token, JWT_SECRET);

      const user = db.prepare(`
        SELECT id, email, name, is_active, created_at
        FROM users
        WHERE id = ? AND is_active = 1
      `).get(decoded.userId);

      req.user = user || null;
    } catch {
      req.user = null;
    }

    next();
  } catch (error) {
    console.error('Optional auth middleware error:', error);
    req.user = null;
    next();
  }
}

/**
 * Middleware to check if user is enrolled in a specific course
 * Must be used after requireAuth middleware
 */
export function requireEnrollment(req, res, next) {
  try {
    const { slug } = req.params;
    const userId = req.user.id;

    // Get course by slug
    const course = db.prepare('SELECT id FROM courses WHERE slug = ?').get(slug);

    if (!course) {
      return res.status(404).json({
        success: false,
        error: 'Course not found'
      });
    }

    // Check enrollment
    const enrollment = db.prepare(`
      SELECT id, enrolled_at, expires_at, payment_status
      FROM enrollments
      WHERE user_id = ? AND course_id = ? AND payment_status IN ('completed', 'free')
    `).get(userId, course.id);

    if (!enrollment) {
      return res.status(403).json({
        success: false,
        error: 'You are not enrolled in this course'
      });
    }

    // Check if enrollment has expired
    if (enrollment.expires_at && new Date(enrollment.expires_at) < new Date()) {
      return res.status(403).json({
        success: false,
        error: 'Your enrollment has expired'
      });
    }

    req.enrollment = enrollment;
    req.course = course;
    next();
  } catch (error) {
    console.error('Enrollment check error:', error);
    return res.status(500).json({
      success: false,
      error: 'Error checking enrollment'
    });
  }
}

/**
 * Generate a JWT token for a user
 * @param {number} userId - The user's ID
 * @param {string} expiresIn - Token expiration time (default: '24h')
 * @returns {string} JWT token
 */
export function generateToken(userId, expiresIn = '24h') {
  return jwt.sign(
    { userId },
    JWT_SECRET,
    { expiresIn }
  );
}

/**
 * Generate a refresh token
 * @param {number} userId - The user's ID
 * @returns {string} Refresh token
 */
export function generateRefreshToken(userId) {
  return jwt.sign(
    { userId, type: 'refresh' },
    JWT_SECRET,
    { expiresIn: '30d' }
  );
}

export default {
  requireAuth,
  optionalAuth,
  requireEnrollment,
  generateToken,
  generateRefreshToken
};
