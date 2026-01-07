# Access Control Review Checklist

## Overview

Regular access control reviews ensure that only authorized individuals have access to your systems and data. This checklist guides you through a comprehensive review of user accounts, service accounts, API keys, and third-party integrations.

**Review Frequency**: Quarterly (minimum) or after any significant team changes

---

## Pre-Review Preparation

- [ ] Schedule review with all stakeholders
- [ ] Gather list of all systems/services to review
- [ ] Export current user lists from each system
- [ ] Obtain current employee/contractor roster from HR
- [ ] Review previous audit findings and action items
- [ ] Set aside dedicated time (estimate 2-4 hours)

---

## Section 1: IAM User Audit

### Cloud Provider Accounts (AWS/Azure/GCP)

#### User Inventory

| Username | Real Name | Role | Last Active | MFA Enabled | Access Level | Action Needed |
|----------|-----------|------|-------------|-------------|--------------|---------------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

#### Review Checklist

- [ ] **List all IAM users** - Export from cloud console
- [ ] **Verify each user is current employee/contractor**
- [ ] **Remove accounts for departed users**
  - Departure date: ___________
  - Account disabled date: ___________
  - Account deleted date: ___________
- [ ] **Review admin/root access** - Limit to essential personnel only
- [ ] **Check access key age** - Flag any over 90 days
- [ ] **Verify MFA is enabled** for all users
- [ ] **Review groups and policies** - Users should have minimum necessary access
- [ ] **Check for unused accounts** - No login in 90+ days
- [ ] **Review cross-account access** - Document and verify necessity

#### Questions to Ask

1. Does this user still need access?
2. Does their access level match their current role?
3. Are they using their access regularly?
4. Could their permissions be reduced?

---

## Section 2: Service Account Review

### Service Account Inventory

| Account Name | Purpose | Owner | Created Date | Last Used | Permissions | Status |
|--------------|---------|-------|--------------|-----------|-------------|--------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

#### Review Checklist

- [ ] **List all service accounts** across all systems
- [ ] **Document purpose** of each service account
- [ ] **Assign an owner** to each service account
- [ ] **Verify accounts are still needed**
- [ ] **Check for overly broad permissions**
- [ ] **Review authentication methods** (key vs. role-based)
- [ ] **Check for shared credentials** - Each service should have unique account
- [ ] **Verify logging is enabled** for service account actions
- [ ] **Flag dormant accounts** - No activity in 30+ days
- [ ] **Document service dependencies**

#### Service Account Best Practices Verification

- [ ] Service accounts do NOT have console/UI access
- [ ] Service accounts use role-based authentication where possible
- [ ] Service accounts have minimum required permissions
- [ ] Service account keys are rotated on schedule
- [ ] Service accounts are not shared between services

---

## Section 3: API Key Scope Verification

### API Key Inventory

| Key Name | Service | Scope/Permissions | Created | Last Used | Owner | Compliant |
|----------|---------|-------------------|---------|-----------|-------|-----------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

#### Review Checklist

- [ ] **Inventory all API keys** in use
- [ ] **Verify each key has defined purpose**
- [ ] **Check permission scopes** - Should be minimum necessary
  - [ ] Read-only where appropriate
  - [ ] Scoped to specific resources
  - [ ] Time-limited if possible
- [ ] **Identify keys with excessive permissions**
- [ ] **Check for duplicate/redundant keys**
- [ ] **Verify keys are stored securely** (not in code)
- [ ] **Confirm rotation schedule is followed**
- [ ] **Review rate limits** - Appropriate for use case
- [ ] **Check IP restrictions** - Enabled where possible

#### Common Scope Issues

| Issue | Risk | Action |
|-------|------|--------|
| Full admin access when read-only needed | High | Reduce scope |
| Access to all resources when one needed | Medium | Scope to specific resource |
| No IP restrictions | Medium | Add allowlist |
| No expiration | Low | Set expiration if available |

---

## Section 4: Third-Party App Access Audit

### Connected Applications Inventory

| App Name | Purpose | Access Level | Data Accessed | Last Used | Approved | Action |
|----------|---------|--------------|---------------|-----------|----------|--------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

#### Platform-Specific Reviews

##### Google Workspace
- [ ] Review at: Security > API controls > Third-party app access
- [ ] List all connected applications
- [ ] Verify each app is still needed
- [ ] Check data access permissions
- [ ] Remove unauthorized/unused apps

##### Microsoft 365
- [ ] Review at: Azure AD > Enterprise applications
- [ ] Audit user consent grants
- [ ] Review admin consent grants
- [ ] Check application permissions
- [ ] Remove unnecessary applications

##### GitHub/GitLab
- [ ] Review at: Settings > Applications > Authorized OAuth Apps
- [ ] Check organization-level integrations
- [ ] Review webhook configurations
- [ ] Audit deploy keys
- [ ] Remove unused integrations

##### Social Media Accounts
- [ ] Review connected apps on each platform
- [ ] Check posting permissions
- [ ] Verify analytics access
- [ ] Remove old marketing tools

#### Third-Party Risk Questions

1. Is this application still being used?
2. Is the vendor still in business/supported?
3. Does the access level match current needs?
4. When was the app's security last reviewed?
5. Does the app have its own security certifications?

---

## Section 5: MFA Status Check

### MFA Enrollment Status

| System | Total Users | MFA Enabled | MFA Disabled | Compliance % |
|--------|-------------|-------------|--------------|--------------|
| | | | | |
| | | | | |
| | | | | |

#### MFA Requirements Checklist

- [ ] **All admin accounts** have MFA enabled
- [ ] **All regular user accounts** have MFA enabled
- [ ] **Recovery methods** are documented and secure
- [ ] **MFA methods** meet security standards
  - Preferred: Hardware keys (YubiKey), Authenticator apps
  - Acceptable: SMS (if no alternative)
  - Not recommended: Email-based codes
- [ ] **Backup codes** are generated and stored securely
- [ ] **Lost device procedures** are documented

#### Users Without MFA - Action Required

| Username | System | Reason | Action | Due Date | Status |
|----------|--------|--------|--------|----------|--------|
| | | | | | |
| | | | | | |

---

## Section 6: Unused Credential Cleanup

### Credentials Marked for Removal

| Credential Type | Identifier | Last Used | Owner | Removal Date | Removed By |
|-----------------|------------|-----------|-------|--------------|------------|
| | | | | | |
| | | | | | |
| | | | | | |

#### Cleanup Checklist

- [ ] **Identify all unused credentials** (no activity 90+ days)
- [ ] **Contact credential owners** to verify no longer needed
- [ ] **Disable before deleting** - Allow 30-day grace period
- [ ] **Document removal** in audit log
- [ ] **Update application configurations** if needed
- [ ] **Verify no service disruption** after removal

#### Cleanup Criteria

| Credential Type | "Unused" Threshold | Disable Period | Delete After |
|-----------------|-------------------|----------------|--------------|
| User accounts | 90 days inactive | Immediate | 30 days |
| API keys | 90 days no calls | Immediate | 14 days |
| Service accounts | 60 days inactive | After verification | 30 days |
| SSH keys | 180 days | Immediate | 30 days |

---

## Review Summary

### Statistics

| Category | Total Reviewed | Issues Found | Actions Required |
|----------|---------------|--------------|------------------|
| IAM Users | | | |
| Service Accounts | | | |
| API Keys | | | |
| Third-Party Apps | | | |
| MFA Status | | | |
| Unused Credentials | | | |
| **TOTAL** | | | |

### Critical Findings

List any high-priority issues requiring immediate action:

1.
2.
3.

### Action Items

| Priority | Finding | Action Required | Owner | Due Date | Status |
|----------|---------|-----------------|-------|----------|--------|
| High | | | | | |
| High | | | | | |
| Medium | | | | | |
| Medium | | | | | |
| Low | | | | | |

---

## Sign-Off

### Review Completed By

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Reviewer | | | |
| Security Lead | | | |
| Management Approval | | | |

### Next Review Scheduled

**Date**: _______________

**Reviewer Assigned**: _______________

---

## Appendix: Access Control Policy Summary

### Access Levels Defined

| Level | Description | Example Roles |
|-------|-------------|---------------|
| Admin | Full system access | System administrators, Security team |
| Power User | Extended capabilities | Team leads, Senior developers |
| Standard | Normal business functions | Regular employees |
| Limited | Restricted access | Contractors, Temporary staff |
| Read-Only | View only | Auditors, Reporting users |

### Access Request Process

1. User submits access request through [SYSTEM]
2. Manager approval required
3. Security team reviews and provisions
4. Access reviewed quarterly

### Access Revocation Triggers

- Employment termination
- Role change
- Project completion
- Extended leave (90+ days)
- Security incident
- Compliance requirement

---

*Review Date: [DATE]*
*Next Review: [DATE]*
*Document Owner: [NAME]*
