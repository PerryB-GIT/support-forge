# Credential Security Checklist

## Overview

This checklist helps ensure your API keys, passwords, and other sensitive credentials are stored and managed securely. Following these practices protects your business from data breaches, unauthorized access, and costly security incidents.

---

## API Key Storage Best Practices

### Secure Storage Methods

- [ ] **Use a secrets manager** - Store keys in dedicated services like:
  - AWS Secrets Manager
  - Azure Key Vault
  - HashiCorp Vault
  - 1Password/Bitwarden for team sharing

- [ ] **Never hardcode credentials** - Keys should never appear directly in your code

- [ ] **Use encrypted storage** - If storing locally, ensure encryption at rest

- [ ] **Implement access controls** - Only authorized team members can access credentials

- [ ] **Create service-specific keys** - Each application gets its own API key

- [ ] **Use minimum permissions** - Keys should only have access they absolutely need

---

## Environment Variable Usage

### Setting Up Environment Variables

- [ ] **Create a `.env` file** for local development
  ```
  # Example .env file structure
  DATABASE_URL=your_database_connection_string
  API_KEY=your_api_key_here
  SECRET_KEY=your_secret_key_here
  ```

- [ ] **Use `.env.example`** as a template (with placeholder values only)
  ```
  # Example .env.example file (safe to commit)
  DATABASE_URL=your_database_url_here
  API_KEY=your_api_key_here
  SECRET_KEY=generate_a_secret_key
  ```

- [ ] **Load variables securely** in your application
  - Node.js: Use `dotenv` package
  - Python: Use `python-dotenv` package
  - Production: Set in hosting platform's environment settings

- [ ] **Separate environments** - Different credentials for development, staging, production

- [ ] **Document required variables** - List all needed env vars in README

---

## .gitignore Essentials

### Files That Must Be Ignored

Add these to your `.gitignore` file:

```gitignore
# Environment files
.env
.env.local
.env.development
.env.staging
.env.production
*.env

# IDE and system files
.idea/
.vscode/
.DS_Store
Thumbs.db

# Credential files
*.pem
*.key
*.p12
*.pfx
credentials.json
serviceAccountKey.json
*-credentials.json
secrets.yaml
secrets.json

# AWS specific
.aws/credentials
aws-exports.js

# Log files (may contain sensitive data)
*.log
logs/

# Database files
*.sqlite
*.db

# Backup files
*.bak
*.backup
```

### Verification Steps

- [ ] **Check `.gitignore` exists** in project root
- [ ] **Verify patterns are correct** - Test with `git status`
- [ ] **Include in all repositories** - Don't skip any project
- [ ] **Update regularly** - Add new patterns as needed

---

## Secret Scanning Setup

### Enable Automated Scanning

- [ ] **GitHub Secret Scanning**
  - Enable in repository Settings > Security > Secret scanning
  - Covers common API key patterns automatically

- [ ] **Pre-commit hooks** - Scan before code is committed
  ```bash
  # Install git-secrets
  git secrets --install
  git secrets --register-aws  # For AWS credentials
  ```

- [ ] **CI/CD integration** - Add scanning to your deployment pipeline
  - Tools: GitLeaks, TruffleHog, detect-secrets

- [ ] **Regular repository audits** - Scan existing codebase periodically

### Response Plan for Detected Secrets

- [ ] **Immediate revocation** - Rotate compromised credentials instantly
- [ ] **Audit access logs** - Check for unauthorized usage
- [ ] **Remove from git history** - Use BFG Repo-Cleaner or git filter-branch
- [ ] **Post-incident review** - Document and learn from the incident

---

## Key Rotation Schedule

### Rotation Frequency Guidelines

| Credential Type | Recommended Frequency |
|----------------|----------------------|
| Production API keys | 90 days |
| Database passwords | 90 days |
| Service account keys | 90 days |
| Development API keys | 180 days |
| Personal access tokens | 90 days |
| SSH keys | Annually |
| SSL/TLS certificates | Before expiration |

### Rotation Process

- [ ] **Document rotation procedures** for each credential type
- [ ] **Set calendar reminders** for upcoming rotations
- [ ] **Test new credentials** before retiring old ones
- [ ] **Update all environments** - Don't forget staging/testing
- [ ] **Verify application functionality** after rotation
- [ ] **Retire old credentials** - Revoke after confirming new ones work
- [ ] **Log the rotation** - Maintain audit trail

---

## What NOT to Do

### Common Mistakes to Avoid

#### 1. Hardcoding Credentials in Source Code

```javascript
// NEVER DO THIS
const apiKey = "sk-abc123xyz789realkey";
const dbPassword = "MyS3cretP@ssword!";

// ALWAYS DO THIS
const apiKey = process.env.API_KEY;
const dbPassword = process.env.DB_PASSWORD;
```

#### 2. Committing .env Files

```bash
# WRONG - This commits your secrets
git add .
git commit -m "Added all files"

# RIGHT - Check what you're committing
git status  # Review files first
git add src/  # Add specific directories
git add -p  # Review each change
```

#### 3. Sharing Credentials Insecurely

```
WRONG methods:
- Slack/Teams messages
- Email
- Shared documents
- Screenshots
- Sticky notes

RIGHT methods:
- Password manager sharing features
- Encrypted file transfer
- Secrets manager with access controls
```

#### 4. Using the Same Key Everywhere

```
WRONG: One API key for all environments and applications

RIGHT:
- Development: dev_api_key_xxx
- Staging: staging_api_key_xxx
- Production: prod_api_key_xxx
- Service A: service_a_api_key_xxx
- Service B: service_b_api_key_xxx
```

#### 5. Ignoring Key Expiration

```
WRONG: "This key has worked for 3 years, why change it?"

RIGHT: Regular rotation prevents long-term exposure risks
```

#### 6. Overly Permissive Keys

```
WRONG: Admin-level API key used by frontend application

RIGHT: Create keys with minimum required permissions
- Read-only where possible
- Scoped to specific resources
- Time-limited when available
```

---

## Quick Security Audit

### Run This Checklist Monthly

1. [ ] Review who has access to production credentials
2. [ ] Check for any credentials approaching rotation date
3. [ ] Verify .gitignore is properly configured
4. [ ] Run secret scanning on repositories
5. [ ] Review and remove unused credentials
6. [ ] Check for any third-party apps with excessive permissions
7. [ ] Verify MFA is enabled for all credential management accounts
8. [ ] Review audit logs for suspicious access patterns

---

## Emergency Response

### If Credentials Are Exposed

1. **Immediately rotate** the exposed credential
2. **Check access logs** for unauthorized usage
3. **Assess impact** - What data/systems could have been accessed?
4. **Remove from public** - Delete from repository, message, etc.
5. **Clean git history** if committed to repository
6. **Notify stakeholders** if required by compliance/contracts
7. **Document incident** for future prevention
8. **Update procedures** to prevent recurrence

---

## Resources

- [GitHub Secret Scanning Documentation](https://docs.github.com/en/code-security/secret-scanning)
- [AWS Secrets Manager Best Practices](https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

---

*Last Updated: [DATE]*
*Review Frequency: Monthly*
*Owner: [YOUR NAME/ROLE]*
