# AI Automation Security Audit Checklist

**Organization:** [Organization Name]
**Audit Date:** [Date]
**Auditor:** [Name]
**Review Period:** [Start Date] to [End Date]

---

## Instructions

Use this checklist quarterly (minimum) to audit the security of your AI automation systems. Complete each section and document findings. Address any "Failed" items immediately.

---

## Part 1: Account Security

### Two-Factor Authentication (2FA)

| Service | 2FA Enabled | Method | Last Verified |
|---------|-------------|--------|---------------|
| Claude.ai | [ ] Pass [ ] Fail | [Authenticator/SMS/Key] | [Date] |
| OpenAI | [ ] Pass [ ] Fail | | |
| Zapier | [ ] Pass [ ] Fail | | |
| n8n | [ ] Pass [ ] Fail | | |
| AWS | [ ] Pass [ ] Fail | | |
| Google Workspace | [ ] Pass [ ] Fail | | |
| GitHub | [ ] Pass [ ] Fail | | |
| Password Manager | [ ] Pass [ ] Fail | | |

**Findings:**
- [ ] All critical accounts have 2FA enabled
- [ ] Authenticator app preferred over SMS
- [ ] Hardware keys used for highest-value accounts (AWS root, etc.)

### Password Security

| Check | Status | Notes |
|-------|--------|-------|
| [ ] All passwords unique (not reused) | | |
| [ ] Passwords 16+ characters | | |
| [ ] No passwords in plain text files | | |
| [ ] Password manager used consistently | | |
| [ ] Master password is strong and unique | | |
| [ ] Password manager has 2FA | | |

---

## Part 2: API Key & Credential Security

### API Key Inventory

| Service | Key Purpose | Last Rotated | Rotation Due | Location Stored |
|---------|-------------|--------------|--------------|-----------------|
| OpenAI | Production API | [Date] | [Date] | [Vault name] |
| Anthropic | Claude API | [Date] | [Date] | |
| SendGrid | Email sending | [Date] | [Date] | |
| Stripe | Payments | [Date] | [Date] | |
| [Add more] | | | | |

### Credential Storage Audit

| Check | Status | Notes |
|-------|--------|-------|
| [ ] No API keys in code repositories | | Run `git secrets` scan |
| [ ] No credentials in .env files committed to git | | Check .gitignore |
| [ ] All secrets in password manager or secrets service | | |
| [ ] Environment variables used for runtime secrets | | |
| [ ] Secrets rotated on schedule | | |
| [ ] Old/unused credentials revoked | | |
| [ ] Service accounts use minimum permissions | | |

### Git Repository Scan

```bash
# Run these to check for exposed secrets

# Check for common secret patterns
git log -p | grep -i "password\|secret\|api_key\|token" | head -50

# Use git-secrets or gitleaks
gitleaks detect --source . -v

# Check .env files aren't committed
git ls-files | grep -E "^\.env"
```

| Scan Result | Status | Action Required |
|-------------|--------|-----------------|
| [ ] No secrets in commit history | | |
| [ ] No .env files committed | | |
| [ ] No hardcoded credentials | | |

---

## Part 3: Access Control

### User Access Review

| User | Role | Services With Access | Access Level | Last Active | Status |
|------|------|---------------------|--------------|-------------|--------|
| [Name] | Admin | All | Full | [Date] | [ ] Appropriate |
| [Name] | Developer | GitHub, Claude | Standard | [Date] | [ ] Appropriate |
| [Name] | Marketing | Zapier (limited) | Read-only | [Date] | [ ] Appropriate |

### Access Control Checks

| Check | Status | Notes |
|-------|--------|-------|
| [ ] All users have appropriate access level | | |
| [ ] No shared accounts in use | | |
| [ ] Former employees/contractors removed | | |
| [ ] Guest/external access reviewed | | |
| [ ] Admin accounts minimized | | |
| [ ] Service accounts documented | | |
| [ ] Access requests require approval | | |

### Privileged Access

| High-Privilege Account | Owner | Last Used | Review Status |
|-----------------------|-------|-----------|---------------|
| AWS Root | [Name] | [Date] | [ ] Reviewed |
| GitHub Org Owner | [Name] | [Date] | [ ] Reviewed |
| Zapier Admin | [Name] | [Date] | [ ] Reviewed |
| [Add more] | | | |

---

## Part 4: Automation Security

### Workflow Security Review

| Workflow/Automation | Contains Sensitive Data? | Last Reviewed | Security Rating |
|--------------------|-------------------------|---------------|-----------------|
| Lead capture | Yes - PII | [Date] | [ ] Secure [ ] Needs work |
| Email automation | Yes - Email content | [Date] | [ ] Secure [ ] Needs work |
| Invoice processor | Yes - Financial | [Date] | [ ] Secure [ ] Needs work |
| [Add more] | | | |

### Automation Security Checks

| Check | Status | Notes |
|-------|--------|-------|
| [ ] Workflows use HTTPS for all connections | | |
| [ ] Sensitive data encrypted in transit | | |
| [ ] Webhook endpoints use authentication | | |
| [ ] No sensitive data logged in plain text | | |
| [ ] Error handling doesn't expose secrets | | |
| [ ] Rate limiting implemented where needed | | |
| [ ] Input validation on all user inputs | | |
| [ ] Output sanitized before display/storage | | |

### AI-Specific Security

| Check | Status | Notes |
|-------|--------|-------|
| [ ] Prompts don't expose internal data | | |
| [ ] AI outputs validated before use | | |
| [ ] No PII sent to AI without consent | | |
| [ ] AI API calls logged for audit | | |
| [ ] Token limits set to prevent abuse | | |
| [ ] AI-generated content reviewed before publication | | |

---

## Part 5: Data Security

### Data Classification

| Data Type | Classification | Where Stored | Encryption | Access Control |
|-----------|---------------|--------------|------------|----------------|
| Customer PII | Confidential | CRM, Sheets | [ ] Yes [ ] No | [ ] Restricted |
| API Keys | Secret | Vault | [ ] Yes [ ] No | [ ] Restricted |
| Financial Data | Confidential | QuickBooks | [ ] Yes [ ] No | [ ] Restricted |
| Business Docs | Internal | Drive | [ ] Yes [ ] No | [ ] Limited |
| Public Content | Public | Website | N/A | Public |

### Data Protection Checks

| Check | Status | Notes |
|-------|--------|-------|
| [ ] Sensitive data identified and classified | | |
| [ ] Data encrypted at rest | | |
| [ ] Data encrypted in transit (HTTPS) | | |
| [ ] Backups encrypted | | |
| [ ] Data retention policies defined | | |
| [ ] Data deletion procedures documented | | |
| [ ] Cross-border data transfers compliant | | |

---

## Part 6: Infrastructure Security

### Cloud Security (AWS/GCP/Azure)

| Check | Status | Notes |
|-------|--------|-------|
| [ ] Root account secured with MFA | | |
| [ ] IAM policies follow least privilege | | |
| [ ] Security groups restrictive | | |
| [ ] Public access blocked where not needed | | |
| [ ] CloudTrail/logging enabled | | |
| [ ] Billing alerts configured | | |
| [ ] Resources tagged for tracking | | |

### Server Security (if self-hosting)

| Check | Status | Notes |
|-------|--------|-------|
| [ ] OS and software updated | | |
| [ ] Firewall configured | | |
| [ ] SSH key auth (no password) | | |
| [ ] Root login disabled | | |
| [ ] Fail2ban or similar enabled | | |
| [ ] Security patches automated | | |

---

## Part 7: Compliance

### Applicable Regulations

| Regulation | Applicable? | Compliance Status | Last Review |
|------------|-------------|-------------------|-------------|
| GDPR | [ ] Yes [ ] No | [ ] Compliant [ ] Partial [ ] Non-compliant | |
| CCPA | [ ] Yes [ ] No | [ ] Compliant [ ] Partial [ ] Non-compliant | |
| HIPAA | [ ] Yes [ ] No | [ ] Compliant [ ] Partial [ ] Non-compliant | |
| SOC 2 | [ ] Yes [ ] No | [ ] Compliant [ ] Partial [ ] Non-compliant | |
| PCI DSS | [ ] Yes [ ] No | [ ] Compliant [ ] Partial [ ] Non-compliant | |

### Compliance Checks

| Check | Status | Notes |
|-------|--------|-------|
| [ ] Privacy policy updated | | |
| [ ] Data processing agreements in place | | |
| [ ] User consent mechanisms working | | |
| [ ] Data subject requests process defined | | |
| [ ] Breach notification process defined | | |
| [ ] Vendor security reviewed | | |

---

## Part 8: Incident Response

### Incident Response Readiness

| Check | Status | Notes |
|-------|--------|-------|
| [ ] Incident response plan documented | | |
| [ ] Contact list for emergencies current | | |
| [ ] Escalation path defined | | |
| [ ] Backup access procedures tested | | |
| [ ] Recovery procedures documented | | |

### Recent Incidents (Last 12 Months)

| Date | Type | Severity | Resolution | Lessons Learned |
|------|------|----------|------------|-----------------|
| [Date] | [Type] | [Low/Med/High] | [Summary] | [Changes made] |
| | | | | |

---

## Part 9: Audit Summary

### Overall Security Score

| Category | Score (1-5) | Weight | Weighted Score |
|----------|-------------|--------|----------------|
| Account Security | [X] | 20% | [X] |
| Credential Management | [X] | 20% | [X] |
| Access Control | [X] | 15% | [X] |
| Automation Security | [X] | 15% | [X] |
| Data Security | [X] | 15% | [X] |
| Infrastructure | [X] | 10% | [X] |
| Compliance | [X] | 5% | [X] |
| **TOTAL** | | **100%** | **[X]/5** |

### Scoring Guide
- 5: Excellent - Best practices implemented
- 4: Good - Minor improvements needed
- 3: Adequate - Some gaps to address
- 2: Needs Improvement - Significant issues
- 1: Critical - Immediate action required

### Critical Findings (Immediate Action)

| Finding | Risk Level | Remediation | Owner | Due Date |
|---------|------------|-------------|-------|----------|
| | | | | |

### High Priority Findings (30 Days)

| Finding | Risk Level | Remediation | Owner | Due Date |
|---------|------------|-------------|-------|----------|
| | | | | |

### Medium Priority Findings (90 Days)

| Finding | Risk Level | Remediation | Owner | Due Date |
|---------|------------|-------------|-------|----------|
| | | | | |

---

## Part 10: Sign-Off

### Audit Completion

| Field | Value |
|-------|-------|
| Audit Completed By | [Name] |
| Date Completed | [Date] |
| Next Audit Due | [Date - typically 90 days] |
| Executive Sponsor | [Name] |
| Sponsor Sign-Off Date | [Date] |

### Acknowledgment

By signing below, I confirm this security audit was completed thoroughly and findings are accurate to the best of my knowledge.

**Auditor Signature:** ______________________ **Date:** ________

**Reviewer Signature:** ______________________ **Date:** ________

---

*Template from AI Launchpad Academy - support-forge.com*
