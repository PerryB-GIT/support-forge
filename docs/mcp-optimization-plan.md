# Support Forge MCP Optimization Plan
## AI Consulting Infrastructure Strategy

**Date:** January 2, 2026
**Purpose:** Optimize MCP connections and Google services for AI consulting operations

---

## Current MCP Inventory

### Active Connections (via Claude Code ~/.claude/.mcp.json)

| MCP Server | Status | Purpose |
|------------|--------|---------|
| **Zapier** | Active | Hub for Google services + 200+ integrations |
| **claude-skills** | Active | Extended Claude capabilities |
| **Canva** | Active | Design creation |
| **filesystem** | Active | Local file access |
| **memory** | Active | Persistent memory |
| **brave-search** | Needs API Key | Web search |
| **github** | Active | Repository management |
| **sequential-thinking** | Active | Structured reasoning |

### Additional Servers (claude_mcp_config.json)

| MCP Server | Status | Purpose |
|------------|--------|---------|
| **fathom** | Active | Call transcription & analytics |
| **calendly** | Active | Client scheduling |
| **playwright** | Active | Browser automation & testing |
| **wordpress** | Active | Site management |

---

## Google Services Analysis

### Already Available via Zapier MCP (FREE with limitations)

| Service | Capabilities | Free Tier |
|---------|-------------|-----------|
| **Google Sheets** | Full CRUD, formatting, queries | Unlimited |
| **Google Calendar** | Events, scheduling, busy periods | Unlimited |
| **Google Drive** | Files, folders, sharing | Unlimited |
| **Gmail** | Search, send, drafts | Unlimited |
| **Google AI Studio (Gemini)** | Text, images, video, audio, docs | 60 req/min |
| **Google Ads** | Campaigns, conversions, audiences | Unlimited |
| **Google Meet** | Schedule meetings | Unlimited |

### Local MCP Servers (Ready to Connect)

| Server | Location | Requires | Free Tier |
|--------|----------|----------|-----------|
| **gcloud-mcp-server** | ~/gcloud-mcp-server | GCP ADC | $300 credit + always-free |
| **vertex-ai-mcp-server** | ~/vertex-ai-mcp-server | GCP Project | Limited free tier |
| **bigquery-mcp-server** | ~/bigquery-mcp-server | GCP ADC | 1TB queries/month |
| **gemini-mcp-server** | ~/gemini-mcp-server | API Key | 60 req/min |
| **google-my-business-mcp** | ~/google-my-business-mcp-server | OAuth | Unlimited |
| **jules-mcp-server** | ~/jules-mcp-server | Jules API Key | Limited beta |

---

## Optimization Recommendations

### Tier 1: Immediate (No Cost, High Value)

#### 1. Consolidate Gemini Access
**Current:** Using Zapier's Google AI Studio integration
**Recommendation:** Keep Zapier for simplicity, add direct gemini-mcp-server for advanced features

```json
// Add to ~/.claude/.mcp.json
"gemini": {
  "command": "node",
  "args": ["C:/Users/Jakeb/gemini-mcp-server/index.js"],
  "env": {
    "GEMINI_API_KEY": "YOUR_KEY"
  }
}
```

**Free Tier:** 60 requests/minute, 1M tokens/min input, 8K output
**Get API Key:** https://aistudio.google.com/app/apikey

#### 2. BigQuery for Analytics & ML
**Value:** Free 1TB queries/month, BigQuery ML included
**Use Cases:**
- Client analytics dashboards
- ML model training (no GPU cost)
- Data warehouse for client projects

```json
"bigquery": {
  "command": "node",
  "args": ["C:/Users/Jakeb/bigquery-mcp-server/index.js"]
}
```

#### 3. Google My Business for Client Reviews
**Value:** Manage client Google Business profiles
**Use Cases:**
- Automated review responses
- Post scheduling
- Analytics reporting

### Tier 2: Setup Required (Low/No Cost)

#### 4. Google Cloud Console Integration
**Value:** Manage infrastructure programmatically
**Prerequisites:**
```bash
gcloud auth application-default login
gcloud services enable cloudresourcemanager.googleapis.com compute.googleapis.com storage.googleapis.com logging.googleapis.com iam.googleapis.com
```

#### 5. Jules Coding Assistant
**Value:** Autonomous coding agent for GitHub repos
**Status:** Beta - requires Jules API access
```bash
# Add to ~/.jules/config.env
JULES_API_KEY=your_key
```

### Tier 3: Advanced (May Incur Costs)

#### 6. Vertex AI (Use Sparingly)
**Value:** Enterprise ML capabilities
**Warning:** Can incur costs quickly
**Free Tier:** Limited - check current pricing
**Recommendation:** Use only for client projects with budget

---

## Free Tier Limits Reference

### Google AI Studio / Gemini API
| Model | RPM | TPM (Input) | TPM (Output) | RPD |
|-------|-----|-------------|--------------|-----|
| Gemini 2.0 Flash | 10 | 4M | 400K | 1500 |
| Gemini 1.5 Flash | 15 | 1M | 100K | 1500 |
| Gemini 1.5 Pro | 2 | 32K | 8K | 50 |

### BigQuery
- **Free:** 1TB queries/month, 10GB storage
- **BigQuery ML:** Free for model training/prediction within query limits

### Google Cloud Platform (New Accounts)
- **$300 credit** for 90 days
- **Always Free:** f1-micro VM, 5GB Cloud Storage, 1GB Pub/Sub

### Zapier MCP
- **Free:** Uses your connected account quotas
- **No additional Zapier charges** for MCP usage

---

## Usage Monitoring Strategy

### 1. Google Cloud Console Dashboard
```bash
# View current usage
gcloud billing accounts list
gcloud projects list --filter="lifecycleState:ACTIVE"
```

### 2. Create Billing Alerts
```bash
# Set budget alert at $1
gcloud billing budgets create \
  --billing-account=BILLING_ACCOUNT_ID \
  --display-name="MCP Usage Alert" \
  --budget-amount=1.00 \
  --threshold-rules=percent=50 \
  --threshold-rules=percent=90 \
  --threshold-rules=percent=100
```

### 3. Automated Usage Tracking (n8n Workflow)
Create workflow to:
- Pull daily API usage from GCP
- Log to Google Sheets
- Alert if approaching limits

### 4. API Key Rotation Strategy
- Use separate API keys per service
- Track usage per key
- Rotate monthly for security

---

## Recommended MCP Configuration

### Updated ~/.claude/.mcp.json

```json
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.zapier.com/api/mcp/mcp"],
      "env": {}
    },
    "claude-skills": {
      "command": "uvx",
      "args": ["claude-skills-mcp"]
    },
    "canva": {
      "command": "npx",
      "args": ["-y", "@canva/cli@latest", "mcp"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-filesystem", "C:/Users/Jakeb"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-memory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_TOKEN"
      }
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-sequential-thinking"]
    },
    "gemini": {
      "command": "node",
      "args": ["C:/Users/Jakeb/gemini-mcp-server/index.js"],
      "env": {
        "GEMINI_API_KEY": "YOUR_GEMINI_KEY"
      }
    },
    "bigquery": {
      "command": "node",
      "args": ["C:/Users/Jakeb/bigquery-mcp-server/index.js"]
    },
    "gcloud": {
      "command": "node",
      "args": ["C:/Users/Jakeb/gcloud-mcp-server/index.js"]
    }
  }
}
```

---

## Service Priority Matrix

### For AI Consulting (support-forge.com)

| Priority | Service | Use Case | Cost Risk |
|----------|---------|----------|-----------|
| 1 | Zapier (Google Suite) | Client comms, scheduling, docs | None |
| 2 | Gemini API | AI features, content generation | Low |
| 3 | BigQuery ML | Client analytics, predictions | Low |
| 4 | GitHub (direct) | Code management | None |
| 5 | Google My Business | Client profile management | None |
| 6 | Jules | Autonomous coding | TBD |
| 7 | Vertex AI | Enterprise ML | High |
| 8 | GCloud Console | Infrastructure | Medium |

---

## Action Items

### Immediate (Today)
- [ ] Get Gemini API key from https://aistudio.google.com/app/apikey
- [ ] Run `gcloud auth application-default login`
- [ ] Add gemini and bigquery MCPs to config
- [ ] Set up $1 billing alert in GCP

### This Week
- [ ] Create n8n workflow for usage monitoring
- [ ] Test BigQuery ML with sample dataset
- [ ] Document client-facing AI capabilities

### This Month
- [ ] Evaluate Jules beta access
- [ ] Create client analytics dashboard template
- [ ] Develop AI consulting service offerings

---

## Notes

- **Zapier MCP is your best friend** - it handles auth and gives you Google Suite access without managing OAuth
- **Gemini 2.0 Flash** has the most generous free tier - use it as default
- **BigQuery ML** is underrated - train models with SQL, no infrastructure
- **Always set billing alerts** before enabling GCP APIs
- **Vertex AI** - only use for paying client projects

---

*Generated by Claude Code for Support Forge AI Consulting*
