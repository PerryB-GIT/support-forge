# Credential Vault Documentation Template

**SECURITY WARNING:** This template is for DOCUMENTATION purposes only. Never store actual passwords or API keys in plain text files. Use a secure password manager or secrets management system.

**Organization:** [Your Organization]
**Last Updated:** [Date]
**Document Owner:** [Name]

---

## Instructions

This template helps you document WHERE credentials are stored and WHO has access, without storing the actual secrets. Use this alongside a proper password manager (1Password, Bitwarden, HashiCorp Vault, AWS Secrets Manager, etc.).

---

## Part 1: Password Manager Reference

### Primary Vault

| Field | Value |
|-------|-------|
| Service | [1Password / Bitwarden / LastPass / Other] |
| Team/Business Account | [Account name] |
| Vault Name | [Vault name for AI/automation credentials] |
| Admin Contact | [Who manages the vault] |
| Access Request Process | [How to request access] |

### Vault Organization

| Folder/Category | Contents | Access Level |
|-----------------|----------|--------------|
| AI Services | OpenAI, Anthropic, Google AI | Developers |
| Automation | Zapier, n8n, Make | Automation Team |
| Cloud Infrastructure | AWS, GCP, Azure | DevOps |
| Business Tools | CRM, Email, Calendar | All Team |
| API Keys - Production | Live API keys | Senior Dev Only |
| API Keys - Development | Test/sandbox keys | All Developers |

---

## Part 2: Service Credential Index

### AI & LLM Services

| Service | Account Email | Vault Location | Access Holders | Rotation Schedule |
|---------|---------------|----------------|----------------|-------------------|
| OpenAI | billing@company.com | AI Services/OpenAI | John, Sarah | Quarterly |
| Anthropic | api@company.com | AI Services/Anthropic | John, Sarah | Quarterly |
| Google AI Studio | gcp@company.com | AI Services/Google | John, Mike | Quarterly |
| Hugging Face | dev@company.com | AI Services/HuggingFace | Dev Team | As needed |

### Automation Platforms

| Service | Account Email | Vault Location | Access Holders | Rotation Schedule |
|---------|---------------|----------------|----------------|-------------------|
| Zapier | automation@company.com | Automation/Zapier | Sarah, Lisa | Annually |
| n8n Cloud | n8n@company.com | Automation/n8n | John, Sarah | Annually |
| Make (Integromat) | make@company.com | Automation/Make | Sarah | Annually |

### Cloud Infrastructure

| Service | Account Email | Vault Location | Access Holders | Rotation Schedule |
|---------|---------------|----------------|----------------|-------------------|
| AWS Root | aws-root@company.com | Cloud/AWS-Root | CEO, CTO Only | Never (MFA) |
| AWS IAM Admin | aws-admin@company.com | Cloud/AWS-Admin | DevOps Team | Quarterly |
| Vercel | deploy@company.com | Cloud/Vercel | Dev Team | Annually |
| Cloudflare | dns@company.com | Cloud/Cloudflare | DevOps | Annually |

### Business Applications

| Service | Account Email | Vault Location | Access Holders | Rotation Schedule |
|---------|---------------|----------------|----------------|-------------------|
| Google Workspace | admin@company.com | Business/Google | IT Admin | MFA Only |
| HubSpot | crm@company.com | Business/HubSpot | Sales Team | Annually |
| Slack | admin@company.com | Business/Slack | IT Admin | MFA Only |
| GitHub | github@company.com | Dev/GitHub | Dev Team | Annually |

---

## Part 3: API Key Inventory

### Production API Keys

| Service | Key Name/ID | Purpose | Created | Last Rotated | Owner |
|---------|-------------|---------|---------|--------------|-------|
| OpenAI | sk-prod-...xxx | Production API calls | 2024-01 | 2024-06 | John |
| Stripe | sk_live_...xxx | Payment processing | 2023-06 | 2024-01 | Finance |
| SendGrid | SG...xxx | Email sending | 2024-02 | 2024-08 | Sarah |
| Twilio | AC...xxx | SMS notifications | 2024-03 | N/A | Sarah |

### Development API Keys

| Service | Key Name/ID | Purpose | Environment | Owner |
|---------|-------------|---------|-------------|-------|
| OpenAI | sk-dev-...xxx | Development/testing | Development | Dev Team |
| Stripe | sk_test_...xxx | Test payments | Staging | Dev Team |
| SendGrid | SG-test...xxx | Email testing | Development | Dev Team |

### Webhook Secrets

| Service | Webhook Purpose | Vault Location | Owner |
|---------|----------------|----------------|-------|
| Stripe | Payment events | Webhooks/Stripe | Finance |
| GitHub | CI/CD triggers | Webhooks/GitHub | DevOps |
| Zapier | n8n integration | Webhooks/Zapier | Sarah |

---

## Part 4: Access Control Matrix

### Role-Based Access

| Role | AI Services | Automation | Cloud Admin | Production Keys |
|------|-------------|------------|-------------|-----------------|
| CEO | Read | Read | Full | Emergency |
| CTO | Full | Full | Full | Full |
| Developer | Full | Read | Limited | None |
| DevOps | Read | Full | Full | Limited |
| Sales | None | Read | None | None |
| Marketing | Limited | Limited | None | None |

### Individual Access Log

| Person | Email | Role | Access Granted | Last Review |
|--------|-------|------|----------------|-------------|
| John Smith | john@company.com | CTO | Full | 2024-12 |
| Sarah Jones | sarah@company.com | Lead Dev | AI, Automation, Cloud | 2024-12 |
| Mike Wilson | mike@company.com | Developer | AI, Development Keys | 2024-12 |
| Lisa Chen | lisa@company.com | Marketing | Automation (limited) | 2024-12 |

---

## Part 5: Environment Variables Reference

### Production Environment

| Variable Name | Service | Storage Location | Notes |
|---------------|---------|------------------|-------|
| OPENAI_API_KEY | OpenAI | Vercel Env Vars | Production key |
| DATABASE_URL | PostgreSQL | Vercel Env Vars | Connection string |
| STRIPE_SECRET_KEY | Stripe | Vercel Env Vars | Live key |
| SENDGRID_API_KEY | SendGrid | Vercel Env Vars | Production |
| NEXT_PUBLIC_* | Various | Git repo | Public, non-secret |

### Staging Environment

| Variable Name | Service | Storage Location | Notes |
|---------------|---------|------------------|-------|
| OPENAI_API_KEY | OpenAI | Vercel Env Vars | Separate staging key |
| DATABASE_URL | PostgreSQL | Vercel Env Vars | Staging database |
| STRIPE_SECRET_KEY | Stripe | Vercel Env Vars | Test mode key |

### Local Development

| Variable Name | Source | Notes |
|---------------|--------|-------|
| All dev keys | .env.local (git-ignored) | Copy from vault |
| Template | .env.example | Committed, no secrets |

---

## Part 6: Security Policies

### Credential Rotation Schedule

| Frequency | Services | Process |
|-----------|----------|---------|
| Monthly | None currently | - |
| Quarterly | OpenAI, Anthropic, AI APIs | Rotate and update all deployments |
| Annually | Zapier, Make, Business tools | Review and rotate during audit |
| On incident | All affected | Immediate rotation, access review |
| On offboarding | All user had access to | Same day as departure |

### Rotation Checklist

When rotating a credential:
- [ ] Generate new credential in service dashboard
- [ ] Update in password manager vault
- [ ] Update in all production environments
- [ ] Update in staging environments
- [ ] Update local .env.example with new format (if changed)
- [ ] Notify team members who need to update local env
- [ ] Revoke old credential after 24-hour overlap
- [ ] Document rotation in this file
- [ ] Update "Last Rotated" date

### Emergency Procedures

**If credential compromise suspected:**
1. Immediately rotate the affected credential
2. Review access logs for unauthorized usage
3. Check for any created resources/charges
4. Notify affected team members
5. Document incident
6. Review access controls

---

## Part 7: Onboarding & Offboarding

### New Team Member Onboarding

| Step | Action | Responsible | Timeline |
|------|--------|-------------|----------|
| 1 | Add to password manager | IT Admin | Day 1 |
| 2 | Grant role-based vault access | Manager | Day 1 |
| 3 | Create individual service accounts where needed | IT Admin | Day 1-3 |
| 4 | Security training | HR/IT | Week 1 |
| 5 | Document access granted | IT Admin | Day 3 |

### Team Member Offboarding

| Step | Action | Responsible | Timeline |
|------|--------|-------------|----------|
| 1 | Revoke password manager access | IT Admin | Same day |
| 2 | Rotate any individually-known credentials | IT Admin | Same day |
| 3 | Remove from service accounts | IT Admin | Same day |
| 4 | Review shared credentials for rotation | IT Admin | Within 24h |
| 5 | Update this document | IT Admin | Within 24h |

---

## Part 8: Audit Log

### Recent Changes

| Date | Change | Performed By | Reason |
|------|--------|--------------|--------|
| 2024-12-15 | Rotated OpenAI production key | John | Quarterly rotation |
| 2024-12-10 | Added Lisa to Automation vault | Sarah | Role expansion |
| 2024-12-01 | Offboarded Tom - all access revoked | IT Admin | Resignation |
| 2024-11-15 | Added Anthropic credentials | John | New service |

### Scheduled Reviews

| Review Type | Frequency | Next Scheduled | Responsible |
|-------------|-----------|----------------|-------------|
| Access audit | Quarterly | 2025-01-15 | IT Admin |
| Rotation compliance | Monthly | 2025-01-01 | DevOps |
| Full security review | Annually | 2025-06-01 | CTO |

---

## Notes

*Additional security considerations, exceptions, or pending actions:*

[Add notes here]

---

*Template from AI Launchpad Academy - support-forge.com*

**REMINDER:** This document should be stored securely and access-controlled. Consider encrypting this file or storing it in your password manager as a secure note.
