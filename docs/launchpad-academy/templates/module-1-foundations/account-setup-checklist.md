# Account Setup Checklist

**Student Name:** _________________________________
**Start Date:** _________________________________
**Target Completion:** _________________________________

---

## Overview

This checklist guides you through setting up all the accounts and tools needed for the Launchpad Academy curriculum. Complete each section in order, as some accounts depend on others.

**Estimated Total Time:** 2-3 hours

---

## 1. GitHub Account + SSH Setup

**Purpose:** Version control, code collaboration, and CI/CD pipelines

### Account Creation
- [ ] Go to [https://github.com/signup](https://github.com/signup)
- [ ] Create account with professional email
- [ ] Choose a professional username (this will be public)
- [ ] Verify email address
- [ ] Enable two-factor authentication (2FA)
  - Settings > Password and authentication > Two-factor authentication

### SSH Key Setup
- [ ] Open terminal/command prompt
- [ ] Generate SSH key:
  ```bash
  ssh-keygen -t ed25519 -C "your_email@example.com"
  ```
- [ ] Start SSH agent:
  ```bash
  eval "$(ssh-agent -s)"
  ```
- [ ] Add SSH key to agent:
  ```bash
  ssh-add ~/.ssh/id_ed25519
  ```
- [ ] Copy public key:
  ```bash
  cat ~/.ssh/id_ed25519.pub
  ```
- [ ] Add to GitHub: Settings > SSH and GPG keys > New SSH key
- [ ] Test connection:
  ```bash
  ssh -T git@github.com
  ```

### Tips
- Use a passphrase for your SSH key for extra security
- Consider using GitHub CLI (`gh`) for easier authentication
- Set up your Git config:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your_email@example.com"
  ```

**Status:** [ ] Complete
**Date Completed:** _____________

---

## 2. Anthropic API Account

**Purpose:** Access to Claude API for AI-powered automation

### Account Creation
- [ ] Go to [https://console.anthropic.com/](https://console.anthropic.com/)
- [ ] Click "Sign Up"
- [ ] Verify email address
- [ ] Complete account setup

### API Key Setup
- [ ] Navigate to API Keys section
- [ ] Click "Create Key"
- [ ] Name your key (e.g., "launchpad-development")
- [ ] Copy and securely store the key immediately (shown only once)
- [ ] Add billing information (required for API usage)

### Billing Setup
- [ ] Go to Settings > Billing
- [ ] Add payment method
- [ ] Set usage limits to prevent unexpected charges
- [ ] Review pricing: [https://www.anthropic.com/pricing](https://www.anthropic.com/pricing)

### Tips
- Start with a low spending limit ($10-20) while learning
- Monitor usage in the dashboard regularly
- Never commit API keys to version control
- Use environment variables for key storage
- Claude Opus 4 is most capable; Claude Sonnet 4 is faster and cheaper for simpler tasks

**Status:** [ ] Complete
**Date Completed:** _____________

---

## 3. Google Cloud Console

**Purpose:** Cloud services, APIs (Gmail, Calendar, Drive, etc.), and hosting options

### Account Creation
- [ ] Go to [https://console.cloud.google.com/](https://console.cloud.google.com/)
- [ ] Sign in with Google account (or create one)
- [ ] Accept terms of service
- [ ] Set up billing account (required for most APIs)

### Project Setup
- [ ] Click "Select a project" > "New Project"
- [ ] Name: "launchpad-academy" (or similar)
- [ ] Note your Project ID (you'll need this)
- [ ] Enable billing for the project

### Enable Required APIs
Navigate to APIs & Services > Library and enable:
- [ ] Gmail API
- [ ] Google Calendar API
- [ ] Google Drive API
- [ ] Google Sheets API
- [ ] Cloud Functions API (optional)

### Create Service Account (for automation)
- [ ] Go to IAM & Admin > Service Accounts
- [ ] Click "Create Service Account"
- [ ] Name: "launchpad-automation"
- [ ] Grant appropriate roles
- [ ] Create and download JSON key file
- [ ] Store key file securely (never commit to Git)

### OAuth Setup (for user-facing apps)
- [ ] Go to APIs & Services > OAuth consent screen
- [ ] Choose External user type
- [ ] Fill in required information
- [ ] Add scopes as needed
- [ ] Create OAuth 2.0 credentials

### Tips
- Google Cloud offers $300 free credits for new accounts
- Set up budget alerts in Billing to avoid surprises
- Use the Cloud Shell for quick CLI access
- Bookmark your project dashboard

**Status:** [ ] Complete
**Date Completed:** _____________

---

## 4. AWS Account + IAM Setup

**Purpose:** Cloud hosting, S3 storage, Lambda functions, and enterprise-grade infrastructure

### Account Creation
- [ ] Go to [https://aws.amazon.com/](https://aws.amazon.com/)
- [ ] Click "Create an AWS Account"
- [ ] Enter email and account name
- [ ] Verify email and phone number
- [ ] Add payment method
- [ ] Select support plan (Free tier is fine to start)
- [ ] Complete identity verification

### Security Setup (CRITICAL)
- [ ] Sign in to AWS Console as root user
- [ ] Enable MFA on root account:
  - Account name (top right) > Security credentials
  - Assign MFA device
- [ ] Create IAM admin user (never use root for daily work):
  - Go to IAM > Users > Create user
  - Username: your-name-admin
  - Enable console access
  - Attach policy: AdministratorAccess
  - Enable MFA on this user too

### CLI Setup
- [ ] Install AWS CLI: [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/)
- [ ] Create access keys for IAM user:
  - IAM > Users > your-user > Security credentials
  - Create access key > CLI use case
- [ ] Configure CLI:
  ```bash
  aws configure
  ```
  - Enter Access Key ID
  - Enter Secret Access Key
  - Default region: us-east-1 (or your preference)
  - Default output: json

### Verify Setup
- [ ] Test CLI:
  ```bash
  aws sts get-caller-identity
  ```

### Free Tier Awareness
- [ ] Review free tier limits: [https://aws.amazon.com/free/](https://aws.amazon.com/free/)
- [ ] Set up billing alerts:
  - Billing > Budgets > Create budget
  - Set threshold (e.g., $5)

### Tips
- NEVER share or commit AWS credentials
- Use IAM roles instead of access keys when possible
- Start with us-east-1 region (most services, best pricing)
- Enable CloudTrail for audit logging
- Consider using AWS Organizations for multiple projects

**Status:** [ ] Complete
**Date Completed:** _____________

---

## 5. n8n Cloud Account

**Purpose:** Visual workflow automation, connecting services without code

### Account Creation
- [ ] Go to [https://n8n.io/cloud/](https://n8n.io/cloud/)
- [ ] Click "Start Free Trial" or "Get Started"
- [ ] Create account with email
- [ ] Verify email address
- [ ] Choose your cloud instance region

### Initial Setup
- [ ] Complete onboarding workflow
- [ ] Explore the node library
- [ ] Create your first test workflow:
  - Manual trigger > Set node > Output
- [ ] Test execution

### Connect First Integration
- [ ] Navigate to Credentials
- [ ] Add a credential (start with something simple like HTTP Request)
- [ ] Test the credential connection

### Tips
- n8n Cloud handles hosting and updates for you
- Self-hosted option available for more control (Docker)
- Free tier includes limited executions - monitor usage
- Use the community nodes for additional integrations
- Templates library has pre-built workflows to learn from
- Documentation: [https://docs.n8n.io/](https://docs.n8n.io/)

**Status:** [ ] Complete
**Date Completed:** _____________

---

## 6. Zapier Account

**Purpose:** No-code automation platform, extensive app integrations

### Account Creation
- [ ] Go to [https://zapier.com/sign-up](https://zapier.com/sign-up)
- [ ] Sign up with email or Google account
- [ ] Verify email if needed
- [ ] Complete onboarding questions

### Initial Setup
- [ ] Explore the app directory
- [ ] Connect your first app (e.g., Gmail or Google Sheets)
- [ ] Create a test Zap:
  - Trigger: New email in Gmail (or similar)
  - Action: Log to Google Sheets
- [ ] Test the Zap

### Understanding Limits
- [ ] Review your plan's task limits
- [ ] Understand multi-step Zap pricing
- [ ] Check supported apps for your use cases

### Tips
- Free plan has limitations (100 tasks/month, 5 Zaps)
- Tasks are counted per action step
- Use filters to reduce unnecessary task usage
- Zapier vs n8n: Zapier is easier but less flexible; n8n is more powerful but steeper learning curve
- Use Zapier for quick integrations, n8n for complex workflows
- MCP integration available for Claude Code connectivity

**Status:** [ ] Complete
**Date Completed:** _____________

---

## 7. Optional But Recommended Accounts

### OpenAI Account (for comparison/backup)
- [ ] Go to [https://platform.openai.com/signup](https://platform.openai.com/signup)
- [ ] Create account
- [ ] Add billing
- [ ] Generate API key

### Vercel Account (for Next.js deployments)
- [ ] Go to [https://vercel.com/signup](https://vercel.com/signup)
- [ ] Sign up with GitHub (recommended)
- [ ] Connect GitHub repositories

### Supabase Account (for database + auth)
- [ ] Go to [https://supabase.com/](https://supabase.com/)
- [ ] Create account
- [ ] Start a new project

### Cloudflare Account (for DNS/CDN)
- [ ] Go to [https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up)
- [ ] Create account
- [ ] Add your first site (optional)

---

## Completion Summary

| Service | Status | API Key Stored? | MFA Enabled? |
|---------|--------|-----------------|--------------|
| GitHub | [ ] | N/A (SSH) | [ ] |
| Anthropic | [ ] | [ ] | N/A |
| Google Cloud | [ ] | [ ] | [ ] |
| AWS | [ ] | [ ] | [ ] |
| n8n | [ ] | N/A | [ ] |
| Zapier | [ ] | N/A | [ ] |

---

## Security Reminders

- [ ] All API keys stored in password manager or credentials vault
- [ ] No credentials in any code repositories
- [ ] MFA enabled on all accounts that support it
- [ ] Billing alerts set on all cloud accounts
- [ ] Recovery codes saved for all 2FA accounts

---

## Troubleshooting Resources

| Service | Documentation | Support |
|---------|--------------|---------|
| GitHub | [docs.github.com](https://docs.github.com) | [support.github.com](https://support.github.com) |
| Anthropic | [docs.anthropic.com](https://docs.anthropic.com) | Console support chat |
| Google Cloud | [cloud.google.com/docs](https://cloud.google.com/docs) | Console support |
| AWS | [docs.aws.amazon.com](https://docs.aws.amazon.com) | Support center |
| n8n | [docs.n8n.io](https://docs.n8n.io) | Community forum |
| Zapier | [help.zapier.com](https://help.zapier.com) | In-app support |

---

**All Accounts Setup Complete:** [ ]
**Date Completed:** _____________
**Notes:** _________________________________
