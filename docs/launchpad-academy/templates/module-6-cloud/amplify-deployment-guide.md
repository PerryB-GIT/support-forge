# AWS Amplify Deployment Guide

Step-by-step guide for deploying web applications with AWS Amplify. Covers Next.js, React, and static sites.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Connecting Your GitHub Repository](#connecting-your-github-repository)
3. [Build Settings Configuration](#build-settings-configuration)
4. [Environment Variables](#environment-variables)
5. [Custom Domain Setup](#custom-domain-setup)
6. [Automatic Deployments](#automatic-deployments)
7. [Troubleshooting Common Issues](#troubleshooting-common-issues)

---

## Prerequisites

Before starting, ensure you have:

- [ ] AWS Account with Amplify access
- [ ] GitHub account with repository
- [ ] Repository with your web application
- [ ] (Optional) Custom domain ready to configure

### Required IAM Permissions

If using a non-root account, ensure these permissions:
- `amplify:*`
- `iam:CreateServiceLinkedRole` (for first-time setup)

---

## Connecting Your GitHub Repository

### Step 1: Access Amplify Console

1. Log into [AWS Console](https://console.aws.amazon.com)
2. Search for "Amplify" or find it under "Front-end Web & Mobile"
3. Click **"Create new app"** > **"Host web app"**

### Step 2: Connect Repository

1. Select **GitHub** as your Git provider
2. Click **"Connect to GitHub"**
3. Authorize AWS Amplify in the popup
4. Select your repository from the dropdown
5. Choose the branch to deploy (usually `main` or `master`)

### Step 3: Configure Build Settings

Amplify auto-detects framework. Verify or customize:

**For Next.js:**
```yaml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*
```

**For React (Create React App):**
```yaml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: build
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*
```

### Step 4: Review and Deploy

1. Review your settings
2. Click **"Save and deploy"**
3. Wait for initial deployment (5-10 minutes typically)

### CLI Alternative

```bash
# Create new app
aws amplify create-app --name my-app --repository https://github.com/user/repo --access-token GITHUB_TOKEN

# Connect branch
aws amplify create-branch --app-id APP_ID --branch-name main

# Start deployment
aws amplify start-job --app-id APP_ID --branch-name main --job-type RELEASE
```

---

## Build Settings Configuration

### Understanding amplify.yml

Create `amplify.yml` in your repository root for version-controlled build settings.

```yaml
version: 1
applications:
  - frontend:
      phases:
        preBuild:
          commands:
            - npm ci
        build:
          commands:
            - npm run build
      artifacts:
        baseDirectory: .next
        files:
          - '**/*'
      cache:
        paths:
          - node_modules/**/*
          - .next/cache/**/*
    appRoot: /  # Use for monorepos
```

### Build Phases

| Phase | Purpose | Common Commands |
|-------|---------|-----------------|
| preBuild | Install dependencies | `npm ci`, `yarn install` |
| build | Build application | `npm run build` |
| postBuild | Post-processing | Copy files, run tests |

### Framework-Specific Settings

#### Next.js (App Router)
```yaml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci
    build:
      commands:
        - env | grep -e NEXT_PUBLIC_ >> .env.production
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*
      - .next/cache/**/*
```

#### Static Site (HTML/CSS/JS)
```yaml
version: 1
frontend:
  phases:
    build:
      commands:
        - echo "No build required"
  artifacts:
    baseDirectory: /
    files:
      - '**/*'
```

#### Monorepo Setup
```yaml
version: 1
applications:
  - frontend:
      phases:
        preBuild:
          commands:
            - cd frontend && npm ci
        build:
          commands:
            - cd frontend && npm run build
      artifacts:
        baseDirectory: frontend/build
        files:
          - '**/*'
    appRoot: frontend
```

### Build Image Settings

In Amplify Console > App Settings > Build Settings:

| Setting | Recommendation |
|---------|----------------|
| Build image | Amazon Linux 2023 |
| Node.js version | Match your local (18.x or 20.x) |
| Build timeout | 30 minutes (default) |

Set Node version in build commands:
```yaml
preBuild:
  commands:
    - nvm use 20
    - npm ci
```

---

## Environment Variables

### Adding Environment Variables

**Via Console:**
1. Go to Amplify Console > Your App
2. Click **"Hosting"** > **"Environment variables"**
3. Click **"Manage variables"**
4. Add key-value pairs
5. Select which branches can access each variable

**Via CLI:**
```bash
# Add single variable
aws amplify update-branch \
  --app-id APP_ID \
  --branch-name main \
  --environment-variables "API_KEY=your-api-key"

# Add multiple variables
aws amplify update-branch \
  --app-id APP_ID \
  --branch-name main \
  --environment-variables "API_KEY=value1,DATABASE_URL=value2"
```

### Environment Variable Best Practices

1. **Never commit secrets** - Use Amplify environment variables
2. **Use branch-specific variables** - Different API keys for staging vs production
3. **Prefix client-side variables** - `NEXT_PUBLIC_` for Next.js, `REACT_APP_` for CRA

### Accessing Variables in Build

```yaml
build:
  commands:
    # Pass to .env file for Next.js
    - env | grep -e NEXT_PUBLIC_ >> .env.production
    - npm run build
```

### Common Variables

| Variable | Purpose |
|----------|---------|
| `NEXT_PUBLIC_API_URL` | API endpoint |
| `NEXT_PUBLIC_GA_ID` | Google Analytics |
| `DATABASE_URL` | Database connection (server-side) |
| `API_KEY` | External service keys |

---

## Custom Domain Setup

### Step 1: Add Domain in Amplify

1. Go to Amplify Console > Your App
2. Click **"Hosting"** > **"Custom domains"**
3. Click **"Add domain"**
4. Enter your domain name (e.g., `example.com`)

### Step 2: Configure DNS

Amplify will provide DNS records to add. For external DNS (like GoDaddy):

**For Root Domain (example.com):**
| Type | Name | Value |
|------|------|-------|
| ANAME/ALIAS | @ | d123abc.cloudfront.net |
| CNAME | _acme-challenge | _abc123.acmvalidations.aws |

**For Subdomain (www.example.com):**
| Type | Name | Value |
|------|------|-------|
| CNAME | www | d123abc.cloudfront.net |
| CNAME | _acme-challenge.www | _abc123.acmvalidations.aws |

### Step 3: Wait for SSL Certificate

- Certificate provisioning takes 15-30 minutes
- DNS propagation can take up to 48 hours (usually faster)
- Status will show "Available" when ready

### Domain Configuration Options

**Redirect Settings:**
```
www.example.com → example.com (recommended)
or
example.com → www.example.com
```

**Branch Subdomains:**
```
main branch → example.com
develop branch → dev.example.com
feature branches → pr-123.example.com
```

### DNS Configuration for GoDaddy

1. Log into GoDaddy > My Products > DNS
2. Add CNAME records as provided by Amplify
3. For root domain, use CNAME flattening if available, or:
   - Point A record to Amplify IP (not recommended - IPs can change)
   - Use a redirect from www

### Troubleshooting Domain Issues

```bash
# Check DNS propagation
dig example.com

# Check certificate status
aws amplify get-domain-association --app-id APP_ID --domain-name example.com
```

---

## Automatic Deployments

### Branch-Based Deployments

By default, Amplify deploys on every push to connected branches.

**Configure in Console:**
1. Go to **"Hosting"** > **"Build settings"**
2. Under **"Branch autodetection"**, enable/disable auto-build

### PR Previews

Enable preview deployments for pull requests:

1. Go to **"Hosting"** > **"Previews"**
2. Click **"Enable previews"**
3. Install GitHub app when prompted
4. Configure which repos/branches get previews

PR previews create temporary deployments:
- URL format: `pr-123.d123abc.amplifyapp.com`
- Automatically deleted when PR is closed

### Webhooks for External CI/CD

Trigger builds from external systems:

```bash
# Get webhook URL
aws amplify create-webhook --app-id APP_ID --branch-name main

# Trigger build via webhook
curl -X POST https://webhooks.amplify.us-east-1.amazonaws.com/prod/webhooks?id=WEBHOOK_ID
```

### Build Notifications

Set up SNS notifications for build status:

1. Go to **"General"** > **"Notifications"**
2. Add email addresses for notifications
3. Select events: Build started, succeeded, failed

---

## Troubleshooting Common Issues

### Build Failures

#### "npm ci" fails
```
Error: npm ci can only install packages when package-lock.json exists
```

**Solution:** Commit `package-lock.json` to your repository.

#### Node version mismatch
```
Error: The engine "node" is incompatible with this module
```

**Solution:** Specify Node version in build settings:
```yaml
preBuild:
  commands:
    - nvm use 18
    - npm ci
```

#### Out of memory during build
```
FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory
```

**Solution:** Increase Node memory:
```yaml
build:
  commands:
    - NODE_OPTIONS=--max-old-space-size=4096 npm run build
```

### Deployment Issues

#### 404 on page refresh (SPA)
**Cause:** Server doesn't know to serve index.html for client routes.

**Solution:** Add rewrite rule in Amplify Console > Rewrites and redirects:
```
Source: </^[^.]+$|\.(?!(css|gif|ico|jpg|js|png|txt|svg|woff|woff2|ttf|map|json)$)([^.]+$)/>
Target: /index.html
Type: 200 (Rewrite)
```

#### Next.js API routes returning 404
**Cause:** API routes need server-side rendering enabled.

**Solution:** Ensure Amplify detects Next.js correctly. Check build settings show `.next` as artifact directory.

#### Environment variables not available
**Cause:** Variables not prefixed correctly or not passed to build.

**Solution:**
- Use `NEXT_PUBLIC_` prefix for client-side variables
- Pass to .env in build:
  ```yaml
  build:
    commands:
      - env | grep -e NEXT_PUBLIC_ >> .env.production
      - npm run build
  ```

### Domain Issues

#### SSL Certificate stuck on "Pending"
**Cause:** DNS validation records not found.

**Solution:**
1. Verify CNAME records are added correctly
2. Check for typos in record values
3. Wait for DNS propagation (use `dig` to verify)
4. If using GoDaddy, ensure no conflicting records

#### Domain shows "Pending verification"
**Solution:** Add the CNAME validation record exactly as shown in Amplify.

### Performance Issues

#### Slow initial load
**Solutions:**
1. Enable compression in build:
   ```yaml
   postBuild:
     commands:
       - find .next -name "*.js" -exec gzip -9 -k {} \;
   ```
2. Use Next.js Image optimization
3. Implement code splitting

#### Cache not working
**Solution:** Add cache headers in `next.config.js`:
```javascript
module.exports = {
  async headers() {
    return [{
      source: '/:all*(svg|jpg|png|js|css)',
      headers: [{
        key: 'Cache-Control',
        value: 'public, max-age=31536000, immutable'
      }]
    }]
  }
}
```

### Quick Diagnostic Commands

```bash
# Check app status
aws amplify get-app --app-id APP_ID

# Get build logs
aws amplify get-job --app-id APP_ID --branch-name main --job-id JOB_ID

# List recent builds
aws amplify list-jobs --app-id APP_ID --branch-name main --max-results 5

# Check domain status
aws amplify get-domain-association --app-id APP_ID --domain-name example.com
```

---

## Quick Reference

### Amplify Console Locations

| Task | Location |
|------|----------|
| View builds | Hosting > Build history |
| Environment variables | Hosting > Environment variables |
| Custom domains | Hosting > Custom domains |
| Build settings | Hosting > Build settings |
| Rewrites/Redirects | Hosting > Rewrites and redirects |
| PR previews | Hosting > Previews |
| Access control | Hosting > Access control |

### Useful CLI Commands

```bash
# List all apps
aws amplify list-apps

# Get app details
aws amplify get-app --app-id APP_ID

# Trigger new build
aws amplify start-job --app-id APP_ID --branch-name main --job-type RELEASE

# Stop running build
aws amplify stop-job --app-id APP_ID --branch-name main --job-id JOB_ID

# Delete app
aws amplify delete-app --app-id APP_ID
```

---

## Resources

- [Amplify Hosting Documentation](https://docs.aws.amazon.com/amplify/latest/userguide/)
- [Next.js on Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/ssr-nextjs.html)
- [Amplify CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/amplify/)
