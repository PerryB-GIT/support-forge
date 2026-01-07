# AWS Services Cheat Sheet

Quick reference for essential AWS services. Bookmark this for fast lookups during development.

---

## EC2 (Elastic Compute Cloud)

### Instance Type Cheat Sheet

| Type | vCPU | Memory | Use Case | Hourly Cost* |
|------|------|--------|----------|--------------|
| t2.micro | 1 | 1 GB | Testing, low traffic | Free tier / $0.0116 |
| t3.small | 2 | 2 GB | Small apps, dev servers | $0.0208 |
| t3.medium | 2 | 4 GB | Light production | $0.0416 |
| t3.large | 2 | 8 GB | Standard web apps | $0.0832 |
| m5.large | 2 | 8 GB | General production | $0.096 |
| c5.large | 2 | 4 GB | CPU-intensive tasks | $0.085 |
| r5.large | 2 | 16 GB | Memory-intensive apps | $0.126 |

*Prices for us-east-1, Linux, on-demand. Check current pricing at aws.amazon.com/ec2/pricing

### When to Use EC2
- Full control over server configuration needed
- Long-running processes or background jobs
- Applications requiring specific software installations
- Consistent, predictable workloads

### Essential CLI Commands

```bash
# List all instances
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,InstanceType,PublicIpAddress]' --output table

# Start/Stop/Terminate instance
aws ec2 start-instances --instance-ids i-1234567890abcdef0
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0

# Get public IP
aws ec2 describe-instances --instance-ids i-1234567890abcdef0 --query 'Reservations[0].Instances[0].PublicIpAddress' --output text

# Create key pair
aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > MyKeyPair.pem

# List security groups
aws ec2 describe-security-groups --output table
```

---

## S3 (Simple Storage Service)

### Storage Classes

| Class | Use Case | Retrieval | Cost |
|-------|----------|-----------|------|
| Standard | Frequent access | Instant | $0.023/GB |
| Intelligent-Tiering | Unknown patterns | Instant | $0.023/GB + monitoring |
| Standard-IA | Infrequent access | Instant | $0.0125/GB |
| One Zone-IA | Non-critical infrequent | Instant | $0.01/GB |
| Glacier Instant | Archive, instant access | Instant | $0.004/GB |
| Glacier Flexible | Archive | 1-12 hours | $0.0036/GB |
| Glacier Deep Archive | Long-term archive | 12-48 hours | $0.00099/GB |

### Static Website Hosting Setup

```bash
# Create bucket
aws s3 mb s3://my-website-bucket

# Enable static hosting
aws s3 website s3://my-website-bucket --index-document index.html --error-document error.html

# Upload files
aws s3 sync ./build s3://my-website-bucket --delete

# Set public read policy (bucket-policy.json)
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicReadGetObject",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::my-website-bucket/*"
  }]
}

# Apply policy
aws s3api put-bucket-policy --bucket my-website-bucket --policy file://bucket-policy.json
```

### Essential CLI Commands

```bash
# List buckets
aws s3 ls

# List bucket contents
aws s3 ls s3://bucket-name --recursive --human-readable

# Copy file
aws s3 cp file.txt s3://bucket-name/

# Sync directory
aws s3 sync ./local-dir s3://bucket-name/remote-dir --delete

# Delete all objects
aws s3 rm s3://bucket-name --recursive

# Get bucket size
aws s3api list-objects-v2 --bucket bucket-name --query "sum(Contents[].Size)" --output text

# Generate presigned URL (expires in 1 hour)
aws s3 presign s3://bucket-name/file.txt --expires-in 3600
```

---

## Lambda

### Function Basics

| Memory | CPU | Timeout Max | Free Tier |
|--------|-----|-------------|-----------|
| 128 MB - 10 GB | Proportional to memory | 15 minutes | 1M requests/month |

### When to Use Lambda
- Event-driven processing (API calls, file uploads)
- Scheduled tasks (cron jobs)
- Quick, stateless operations
- Variable/unpredictable traffic

### Common Triggers
- API Gateway (REST/HTTP APIs)
- S3 (object created/deleted)
- CloudWatch Events (scheduled)
- DynamoDB Streams
- SQS/SNS messages

### Pricing Formula
```
Cost = (Requests x $0.20/million) + (GB-seconds x $0.0000166667)
```

### Essential CLI Commands

```bash
# List functions
aws lambda list-functions --query 'Functions[*].[FunctionName,Runtime,MemorySize]' --output table

# Invoke function
aws lambda invoke --function-name my-function --payload '{"key": "value"}' response.json

# Update function code (from zip)
aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip

# View function logs
aws logs tail /aws/lambda/my-function --follow

# Update memory/timeout
aws lambda update-function-configuration --function-name my-function --memory-size 512 --timeout 30
```

---

## Amplify

### Deployment Types

| Type | Best For | Build |
|------|----------|-------|
| Git-based | Full CI/CD | Automatic on push |
| Manual | Quick deploys | CLI/Console upload |

### Key Features
- Automatic SSL certificates
- Custom domains with auto-renewal
- PR previews
- Environment variables per branch
- Redirect/rewrite rules

### Essential CLI Commands

```bash
# List apps
aws amplify list-apps --query 'apps[*].[appId,name,defaultDomain]' --output table

# List branches
aws amplify list-branches --app-id APP_ID --query 'branches[*].[branchName,stage]' --output table

# Trigger deployment
aws amplify start-job --app-id APP_ID --branch-name main --job-type RELEASE

# Get deployment status
aws amplify get-job --app-id APP_ID --branch-name main --job-id JOB_ID

# Create environment variable
aws amplify update-branch --app-id APP_ID --branch-name main --environment-variables KEY=VALUE

# Download build artifacts
aws amplify get-artifact-url --app-id APP_ID --branch-name main --job-id JOB_ID
```

---

## CloudFront (CDN)

### Cache Behaviors

| TTL Setting | Use Case |
|-------------|----------|
| Min 0, Default 86400 | Static assets |
| Min 0, Default 0 | Dynamic content |
| Min 31536000 | Versioned assets |

### Essential CLI Commands

```bash
# List distributions
aws cloudfront list-distributions --query 'DistributionList.Items[*].[Id,DomainName,Status]' --output table

# Create invalidation (clear cache)
aws cloudfront create-invalidation --distribution-id E1234567890 --paths "/*"

# Invalidate specific paths
aws cloudfront create-invalidation --distribution-id E1234567890 --paths "/index.html" "/css/*"

# Check invalidation status
aws cloudfront get-invalidation --distribution-id E1234567890 --id I1234567890

# Get distribution config
aws cloudfront get-distribution-config --id E1234567890
```

### Common Cache Headers

```
Cache-Control: max-age=31536000, immutable  # Versioned assets
Cache-Control: no-cache, no-store           # Dynamic content
Cache-Control: max-age=86400                # Static pages
```

---

## Route53 (DNS)

### Record Types

| Type | Use Case | Example |
|------|----------|---------|
| A | IPv4 address | 1.2.3.4 |
| AAAA | IPv6 address | 2001:db8::1 |
| CNAME | Alias to another domain | www -> example.com |
| ALIAS | AWS resource (free queries) | d123.cloudfront.net |
| MX | Mail servers | mail.example.com |
| TXT | Verification, SPF | "v=spf1 include:..." |

### Essential CLI Commands

```bash
# List hosted zones
aws route53 list-hosted-zones --query 'HostedZones[*].[Id,Name]' --output table

# List records in zone
aws route53 list-resource-record-sets --hosted-zone-id Z1234567890 --output table

# Create/Update record (using JSON file)
aws route53 change-resource-record-sets --hosted-zone-id Z1234567890 --change-batch file://record.json

# record.json example:
{
  "Changes": [{
    "Action": "UPSERT",
    "ResourceRecordSet": {
      "Name": "www.example.com",
      "Type": "A",
      "TTL": 300,
      "ResourceRecords": [{"Value": "1.2.3.4"}]
    }
  }]
}

# Get change status
aws route53 get-change --id C1234567890
```

---

## IAM (Identity and Access Management)

### Best Practices

1. **Never use root account** for daily work
2. **Enable MFA** on all accounts
3. **Use roles** instead of long-lived credentials
4. **Principle of least privilege** - only grant needed permissions
5. **Rotate credentials** regularly
6. **Use groups** for user permissions
7. **Tag resources** for cost tracking

### Common Policies

```json
// S3 Read-Only
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject", "s3:ListBucket"],
    "Resource": ["arn:aws:s3:::bucket-name", "arn:aws:s3:::bucket-name/*"]
  }]
}

// Lambda Execution
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
    "Resource": "arn:aws:logs:*:*:*"
  }]
}

// EC2 Full Access (use sparingly)
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "ec2:*",
    "Resource": "*"
  }]
}
```

### Essential CLI Commands

```bash
# List users
aws iam list-users --query 'Users[*].[UserName,CreateDate]' --output table

# List roles
aws iam list-roles --query 'Roles[*].[RoleName,CreateDate]' --output table

# Create user
aws iam create-user --user-name new-user

# Attach policy to user
aws iam attach-user-policy --user-name user-name --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# Create access keys
aws iam create-access-key --user-name user-name

# List access keys
aws iam list-access-keys --user-name user-name

# Get current identity
aws sts get-caller-identity
```

---

## Quick Reference: Service Selection

| Need | Service |
|------|---------|
| Host a static website | S3 + CloudFront |
| Host a web app (Next.js, React) | Amplify |
| Run a server 24/7 | EC2 |
| Run code on-demand | Lambda |
| Store files | S3 |
| Database (SQL) | RDS |
| Database (NoSQL) | DynamoDB |
| Domain management | Route53 |
| CDN/Caching | CloudFront |
| Container hosting | ECS/Fargate |
| Serverless containers | App Runner |

---

## Useful Links

- [AWS Pricing Calculator](https://calculator.aws/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/)
- [AWS Service Health Dashboard](https://health.aws.amazon.com/health/status)
