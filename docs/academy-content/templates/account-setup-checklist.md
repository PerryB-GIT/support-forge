# AI & Automation Account Setup Checklist

**User:** [Your Name]
**Date Started:** [Date]
**Completion Target:** [Date]

---

## Instructions

Complete this checklist to set up all accounts needed for your AI automation journey. Work through each section in order. Check off items as you complete them.

---

## Part 1: Essential AI Accounts

### Claude (Anthropic)

**Purpose:** Your primary AI assistant for coding, analysis, and automation

| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://claude.ai | | |
| [ ] Create account with work email | | |
| [ ] Verify email address | | |
| [ ] Enable 2-factor authentication | | |
| [ ] Upgrade to Claude Pro ($20/mo) if needed | | Recommended for heavy use |
| [ ] Explore Claude.ai interface | | |
| [ ] Download Claude mobile app | | Optional |

**API Access (for developers):**
| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://console.anthropic.com | | |
| [ ] Add payment method | | |
| [ ] Generate API key | | |
| [ ] Store API key in password manager | | Never commit to code |
| [ ] Set usage limits/alerts | | Prevent surprise bills |

---

### Claude Code (CLI)

**Purpose:** AI-powered development assistant in your terminal

| Task | Status | Notes |
|------|--------|-------|
| [ ] Install Node.js v18+ (https://nodejs.org) | | |
| [ ] Run: `npm install -g @anthropic-ai/claude-code` | | |
| [ ] Run: `claude` to start | | |
| [ ] Complete first-run authentication | | |
| [ ] Create first CLAUDE.md file | | See templates |
| [ ] Test basic commands | | |

---

### OpenAI (ChatGPT)

**Purpose:** Alternative AI assistant, GPT models, DALL-E image generation

| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://chat.openai.com | | |
| [ ] Create account | | |
| [ ] Verify email | | |
| [ ] Enable 2FA | | |
| [ ] Upgrade to Plus ($20/mo) if needed | | For GPT-4 access |

**API Access:**
| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://platform.openai.com | | |
| [ ] Add payment method | | |
| [ ] Generate API key | | |
| [ ] Store in password manager | | |
| [ ] Set usage limits | | |

---

### Google AI Studio (Gemini)

**Purpose:** Google's AI models, good for certain tasks

| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://aistudio.google.com | | |
| [ ] Sign in with Google account | | |
| [ ] Accept terms of service | | |
| [ ] Get API key (free tier available) | | |
| [ ] Store in password manager | | |

---

## Part 2: Automation Platforms

### Zapier

**Purpose:** No-code automation, connects 5000+ apps

| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://zapier.com | | |
| [ ] Create account (free tier available) | | |
| [ ] Verify email | | |
| [ ] Enable 2FA | | |
| [ ] Complete onboarding wizard | | |
| [ ] Connect first app (Gmail or Google Sheets) | | |
| [ ] Create test Zap | | |
| [ ] Explore templates library | | |

**For Claude Code MCP:**
| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://actions.zapier.com/mcp/start | | |
| [ ] Enable MCP integration | | |
| [ ] Copy MCP URL | | |
| [ ] Add to Claude Code config | | See config templates |
| [ ] Test MCP connection | | |

---

### n8n

**Purpose:** Open-source workflow automation, more powerful than Zapier

| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://n8n.io | | |
| [ ] Create n8n Cloud account OR | | Cloud is easier |
| [ ] Self-host on your server | | More control, technical |
| [ ] Verify email | | |
| [ ] Complete setup wizard | | |
| [ ] Connect first credentials (Google) | | |
| [ ] Import a template workflow | | |
| [ ] Create test workflow | | |

**Self-Hosting (optional):**
| Task | Status | Notes |
|------|--------|-------|
| [ ] Install Docker on server | | |
| [ ] Pull n8n image | | |
| [ ] Configure docker-compose.yml | | |
| [ ] Set up reverse proxy | | For HTTPS |
| [ ] Configure environment variables | | |
| [ ] Start n8n container | | |
| [ ] Set up backups | | |

---

### Make (Integromat)

**Purpose:** Visual automation platform, great for complex workflows

| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://make.com | | |
| [ ] Create account (free tier: 1000 ops/mo) | | |
| [ ] Verify email | | |
| [ ] Complete onboarding | | |
| [ ] Connect first app | | |
| [ ] Explore templates | | |

---

## Part 3: Cloud Infrastructure

### AWS (Amazon Web Services)

**Purpose:** Cloud hosting, storage, compute, many AI services

| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://aws.amazon.com | | |
| [ ] Create account (credit card required) | | |
| [ ] Enable MFA on root account | | Critical security |
| [ ] Create IAM admin user | | Don't use root |
| [ ] Set up billing alerts | | Prevent surprise bills |
| [ ] Install AWS CLI | | |
| [ ] Configure CLI with access keys | | |
| [ ] Set default region | | e.g., us-east-1 |

**Free Tier Highlights:**
- 12 months of EC2 t2.micro
- 5GB S3 storage
- 25GB DynamoDB storage
- 1 million Lambda requests/month

---

### Vercel

**Purpose:** Frontend hosting, serverless functions, easy deployments

| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://vercel.com | | |
| [ ] Sign up with GitHub | | Recommended |
| [ ] Connect GitHub account | | |
| [ ] Deploy first project | | |
| [ ] Configure custom domain (optional) | | |
| [ ] Install Vercel CLI | | `npm i -g vercel` |

---

### Cloudflare

**Purpose:** DNS, CDN, security, R2 storage, Workers

| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://cloudflare.com | | |
| [ ] Create account | | |
| [ ] Add first domain (optional) | | |
| [ ] Explore free tier services | | |

---

## Part 4: Productivity & Collaboration

### Google Workspace

**Purpose:** Email, calendar, docs, sheets, drive - core business tools

| Task | Status | Notes |
|------|--------|-------|
| [ ] Have Google account ready | | |
| [ ] Enable Google Workspace if business | | Or use free Gmail |
| [ ] Enable 2FA | | |
| [ ] Set up Gmail labels for automation | | |
| [ ] Create API project in Google Cloud Console | | |
| [ ] Enable required APIs (Calendar, Sheets, Drive) | | |
| [ ] Create OAuth credentials | | |
| [ ] Download credentials JSON | | |

---

### Notion

**Purpose:** Documentation, knowledge base, project management

| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://notion.so | | |
| [ ] Create account | | |
| [ ] Set up workspace | | |
| [ ] Create first page | | |
| [ ] Generate integration token (Settings > Connections) | | For automation |
| [ ] Store token in password manager | | |

---

### Slack

**Purpose:** Team communication, notifications from automations

| Task | Status | Notes |
|------|--------|-------|
| [ ] Have Slack workspace access | | |
| [ ] Create dedicated channel for bot notifications | | e.g., #automation-alerts |
| [ ] Create Slack app (for custom bots) | | api.slack.com/apps |
| [ ] Generate bot token | | |
| [ ] Store token in password manager | | |

---

## Part 5: Development Tools

### GitHub

**Purpose:** Code hosting, version control, CI/CD

| Task | Status | Notes |
|------|--------|-------|
| [ ] Visit https://github.com | | |
| [ ] Create account | | |
| [ ] Enable 2FA | | Required for many features |
| [ ] Set up SSH key | | For easier git operations |
| [ ] Create first repository | | |
| [ ] Install GitHub CLI (`gh`) | | |
| [ ] Authenticate CLI: `gh auth login` | | |
| [ ] Generate Personal Access Token | | For integrations |

---

### VS Code

**Purpose:** Code editor with AI integrations

| Task | Status | Notes |
|------|--------|-------|
| [ ] Download from https://code.visualstudio.com | | |
| [ ] Install | | |
| [ ] Sign in with GitHub | | For settings sync |
| [ ] Install essential extensions | | |
| [ ]   - ESLint | | |
| [ ]   - Prettier | | |
| [ ]   - GitLens | | |
| [ ]   - GitHub Copilot (optional, $10/mo) | | |

---

### Docker

**Purpose:** Container runtime for running automation tools

| Task | Status | Notes |
|------|--------|-------|
| [ ] Download Docker Desktop | | https://docker.com |
| [ ] Install and start | | |
| [ ] Verify: `docker run hello-world` | | |
| [ ] Sign up for Docker Hub (optional) | | |

---

## Part 6: Password Manager

### 1Password / Bitwarden / LastPass

**Purpose:** Securely store all credentials from this checklist

| Task | Status | Notes |
|------|--------|-------|
| [ ] Choose password manager | | 1Password or Bitwarden recommended |
| [ ] Create account | | |
| [ ] Install browser extension | | |
| [ ] Install desktop app | | |
| [ ] Install mobile app | | |
| [ ] Create vault for AI/Automation credentials | | |
| [ ] Import any existing passwords | | |
| [ ] Enable 2FA for password manager | | Critical |
| [ ] Set up emergency access (optional) | | |

---

## Part 7: Verification Checklist

### All Accounts Created

| Service | Account Created | 2FA Enabled | Credentials Stored |
|---------|-----------------|-------------|-------------------|
| Claude | [ ] | [ ] | [ ] |
| Claude Code | [ ] | N/A | [ ] |
| OpenAI | [ ] | [ ] | [ ] |
| Google AI | [ ] | [ ] | [ ] |
| Zapier | [ ] | [ ] | [ ] |
| n8n | [ ] | [ ] | [ ] |
| AWS | [ ] | [ ] | [ ] |
| Vercel | [ ] | [ ] | [ ] |
| GitHub | [ ] | [ ] | [ ] |
| Password Manager | [ ] | [ ] | N/A |

### Integration Tests

| Test | Status | Notes |
|------|--------|-------|
| [ ] Claude Code can access MCP tools | | |
| [ ] Zapier can connect to Gmail | | |
| [ ] n8n can connect to Google Sheets | | |
| [ ] AWS CLI works: `aws sts get-caller-identity` | | |
| [ ] GitHub CLI works: `gh auth status` | | |

---

## Notes

*Account-specific notes, login URLs, or other details:*

[Add notes here]

---

## Completion

- [ ] All required accounts created
- [ ] All 2FA enabled where possible
- [ ] All credentials stored in password manager
- [ ] Integration tests passed
- [ ] Shared access granted to team members (if applicable)

**Completed on:** [Date]
**Time to complete:** [X hours/days]

---

*Template from AI Launchpad Academy - support-forge.com*
