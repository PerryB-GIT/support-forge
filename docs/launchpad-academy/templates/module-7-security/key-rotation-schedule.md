# Key Rotation Schedule

## Overview

This document tracks all API keys, credentials, and secrets requiring regular rotation. Keeping credentials fresh reduces the risk of unauthorized access from compromised or leaked keys.

---

## Rotation Schedule Summary

| Service | Key Type | Created | Rotation Frequency | Next Due | Owner | Status |
|---------|----------|---------|-------------------|----------|-------|--------|
| *Example: AWS* | *Access Key* | *2024-01-15* | *90 days* | *2024-04-15* | *John D.* | *Active* |

---

## Detailed Key Inventory

### Production Environment

#### Key #1: [Service Name]

| Field | Value |
|-------|-------|
| **Service/API** | |
| **Key Identifier** | *(Last 4 characters only: ...xxxx)* |
| **Purpose** | |
| **Created Date** | |
| **Rotation Frequency** | 90 days |
| **Next Rotation Due** | |
| **Responsible Person** | |
| **Backup Contact** | |
| **Where Key Is Stored** | |
| **Rotation Procedure** | *See procedure section below* |
| **Last Rotated** | |
| **Notes** | |

---

#### Key #2: [Service Name]

| Field | Value |
|-------|-------|
| **Service/API** | |
| **Key Identifier** | *(Last 4 characters only: ...xxxx)* |
| **Purpose** | |
| **Created Date** | |
| **Rotation Frequency** | 90 days |
| **Next Rotation Due** | |
| **Responsible Person** | |
| **Backup Contact** | |
| **Where Key Is Stored** | |
| **Rotation Procedure** | *See procedure section below* |
| **Last Rotated** | |
| **Notes** | |

---

#### Key #3: [Service Name]

| Field | Value |
|-------|-------|
| **Service/API** | |
| **Key Identifier** | *(Last 4 characters only: ...xxxx)* |
| **Purpose** | |
| **Created Date** | |
| **Rotation Frequency** | 90 days |
| **Next Rotation Due** | |
| **Responsible Person** | |
| **Backup Contact** | |
| **Where Key Is Stored** | |
| **Rotation Procedure** | *See procedure section below* |
| **Last Rotated** | |
| **Notes** | |

---

### Development/Staging Environment

#### Dev Key #1: [Service Name]

| Field | Value |
|-------|-------|
| **Service/API** | |
| **Key Identifier** | *(Last 4 characters only: ...xxxx)* |
| **Purpose** | |
| **Created Date** | |
| **Rotation Frequency** | 180 days |
| **Next Rotation Due** | |
| **Responsible Person** | |
| **Where Key Is Stored** | |
| **Notes** | |

---

## Rotation Procedures

### AWS Access Keys

1. Log into AWS Console as administrator
2. Navigate to IAM > Users > [Username] > Security credentials
3. Click "Create access key"
4. Store new key securely in secrets manager
5. Update all applications using the key
6. Verify applications work with new key
7. Deactivate old key (do not delete yet)
8. Monitor for 24-48 hours for issues
9. Delete old key after verification period
10. Update this document with new dates

### Database Passwords

1. Generate new secure password (min 20 characters)
2. Update password in database system
3. Update password in secrets manager
4. Update all application configurations
5. Restart affected services
6. Verify database connections work
7. Update this document with new dates

### Third-Party API Keys

1. Log into service provider dashboard
2. Generate new API key
3. Note any scope/permission requirements
4. Update key in secrets manager
5. Update all applications using the key
6. Test API connectivity
7. Revoke old key in provider dashboard
8. Update this document with new dates

### SSL/TLS Certificates

1. Generate new certificate signing request (CSR)
2. Submit to certificate authority
3. Receive and verify new certificate
4. Backup current certificate
5. Install new certificate on server
6. Test HTTPS connectivity
7. Update any pinned certificates in mobile apps
8. Update this document with new dates

---

## Rotation Frequency Guidelines

| Credential Type | Minimum Frequency | Recommended | Maximum |
|----------------|-------------------|-------------|---------|
| Production API Keys | 90 days | 60 days | 90 days |
| Database Passwords | 90 days | 90 days | 180 days |
| Service Accounts | 90 days | 90 days | 180 days |
| Personal Access Tokens | 30 days | 30 days | 90 days |
| Development Keys | 180 days | 90 days | 365 days |
| SSH Keys | 365 days | 180 days | 365 days |
| SSL Certificates | Before expiry | 30 days before | Before expiry |

---

## Calendar Integration

### Setting Up Reminders

For each credential, create calendar reminders:

1. **2 weeks before** - "Upcoming: Rotate [Service] API Key"
2. **1 week before** - "Reminder: [Service] API Key rotation due soon"
3. **On due date** - "ACTION REQUIRED: Rotate [Service] API Key today"

### Recommended Calendar Events

```
Title: Rotate [Service Name] API Key
When: [Due Date], 9:00 AM
Reminder: 2 weeks before, 1 week before, 1 day before
Description:
- Key location: [Where stored]
- Procedure: [Link to procedure]
- Owner: [Responsible person]
- Backup: [Backup contact]
```

---

## Rotation History Log

Track all credential rotations for audit purposes.

| Date | Service | Key Type | Rotated By | Verified By | Notes |
|------|---------|----------|------------|-------------|-------|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

---

## Emergency Rotation Triggers

Rotate credentials immediately if:

- [ ] Credential may have been exposed publicly
- [ ] Team member with access leaves the company
- [ ] Suspicious activity detected in audit logs
- [ ] Security breach at a third-party service
- [ ] Credential found in code repository
- [ ] Unauthorized access attempt detected
- [ ] Compliance audit requirement

---

## Compliance Notes

### Regulatory Requirements

| Regulation | Rotation Requirement | Our Policy |
|------------|---------------------|------------|
| PCI DSS | 90 days for system passwords | 90 days |
| HIPAA | "Regularly" - interpret as 90 days | 90 days |
| SOC 2 | Defined policy required | 90 days |
| GDPR | Best practice | 90 days |

---

## Contacts

### Primary Security Contact
- **Name**:
- **Email**:
- **Phone**:

### Backup Security Contact
- **Name**:
- **Email**:
- **Phone**:

### Third-Party Support Contacts

| Service | Support Contact | Account Number |
|---------|-----------------|----------------|
| | | |
| | | |
| | | |

---

*Last Updated: [DATE]*
*Next Full Review: [DATE]*
*Document Owner: [NAME]*
