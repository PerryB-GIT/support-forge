# Automation Launch Readiness Checklist

**Project/Automation Name:** [Name]
**Target Launch Date:** [Date]
**Project Lead:** [Name]
**Checklist Version:** 1.0

---

## Instructions

Complete this checklist before launching any automation to production. All "Critical" items must pass. Address any failures before proceeding with launch.

---

## Part 1: Development Complete

### Code/Configuration Complete

| Item | Status | Owner | Notes |
|------|--------|-------|-------|
| [ ] All workflows built and configured | | | |
| [ ] All integrations connected | | | |
| [ ] All templates finalized | | | |
| [ ] All triggers configured | | | |
| [ ] Error handling implemented | | | |
| [ ] Logging configured | | | |
| [ ] No hardcoded test values | | | |
| [ ] Code reviewed by second person | | | |

### Environment Configuration

| Item | Status | Owner | Notes |
|------|--------|-------|-------|
| [ ] Production credentials in place | | | |
| [ ] Development/test credentials removed | | | |
| [ ] Environment variables set | | | |
| [ ] API keys are production keys | | | |
| [ ] Webhook URLs are production | | | |
| [ ] Database points to production | | | |

---

## Part 2: Testing Complete

### Functional Testing

| Test Type | Status | Pass/Fail | Notes |
|-----------|--------|-----------|-------|
| [ ] Happy path tested | | [ ] Pass [ ] Fail | Main use case works |
| [ ] Edge cases tested | | [ ] Pass [ ] Fail | Unusual inputs |
| [ ] Error scenarios tested | | [ ] Pass [ ] Fail | What happens when things fail |
| [ ] Empty/null inputs tested | | [ ] Pass [ ] Fail | Missing data handling |
| [ ] Large data volumes tested | | [ ] Pass [ ] Fail | Performance at scale |
| [ ] Duplicate handling tested | | [ ] Pass [ ] Fail | Same input twice |

### Integration Testing

| Integration | Status | Pass/Fail | Notes |
|-------------|--------|-----------|-------|
| [ ] [Integration 1] | | [ ] Pass [ ] Fail | |
| [ ] [Integration 2] | | [ ] Pass [ ] Fail | |
| [ ] [Integration 3] | | [ ] Pass [ ] Fail | |
| [ ] End-to-end flow verified | | [ ] Pass [ ] Fail | |
| [ ] Data flows correctly between systems | | [ ] Pass [ ] Fail | |

### User Acceptance Testing

| Item | Status | Tester | Notes |
|------|--------|--------|-------|
| [ ] Business owner approved output | | | |
| [ ] Sample outputs reviewed | | | |
| [ ] Format/content correct | | | |
| [ ] Timing/triggers correct | | | |
| [ ] Stakeholder sign-off received | | | |

---

## Part 3: Security Verified

### Credential Security

| Item | Status | Critical? |
|------|--------|-----------|
| [ ] No secrets in code or configs | | CRITICAL |
| [ ] API keys from password manager | | CRITICAL |
| [ ] Production keys different from dev | | CRITICAL |
| [ ] Minimum necessary permissions | | High |
| [ ] No test/dummy data in production | | High |

### Data Security

| Item | Status | Critical? |
|------|--------|-----------|
| [ ] Sensitive data encrypted | | CRITICAL |
| [ ] HTTPS used for all connections | | CRITICAL |
| [ ] PII handled appropriately | | CRITICAL |
| [ ] Logging doesn't expose secrets | | High |
| [ ] Data retention policy followed | | Medium |

### Access Control

| Item | Status | Critical? |
|------|--------|-----------|
| [ ] Only authorized users have access | | CRITICAL |
| [ ] Admin access limited | | High |
| [ ] Audit trail enabled | | Medium |

---

## Part 4: Monitoring & Alerting

### Monitoring Setup

| Item | Status | Owner | Notes |
|------|--------|-------|-------|
| [ ] Error notifications configured | | | Who gets alerted? |
| [ ] Success confirmations if needed | | | |
| [ ] Performance monitoring in place | | | |
| [ ] Usage/volume tracking | | | |
| [ ] Cost monitoring if applicable | | | |

### Alert Configuration

| Alert Type | Recipient | Method | Tested? |
|------------|-----------|--------|---------|
| Errors | [Name/Team] | [Slack/Email] | [ ] Yes [ ] No |
| Failures | [Name/Team] | [Slack/Email] | [ ] Yes [ ] No |
| Unusual activity | [Name/Team] | [Slack/Email] | [ ] Yes [ ] No |

---

## Part 5: Documentation Complete

### Technical Documentation

| Document | Status | Location | Owner |
|----------|--------|----------|-------|
| [ ] System architecture diagram | | [Link] | |
| [ ] Workflow documentation | | [Link] | |
| [ ] Integration details | | [Link] | |
| [ ] Troubleshooting guide | | [Link] | |
| [ ] Runbook for operations | | [Link] | |

### User Documentation

| Document | Status | Location | Owner |
|----------|--------|----------|-------|
| [ ] User guide created | | [Link] | |
| [ ] FAQ documented | | [Link] | |
| [ ] Known issues listed | | [Link] | |
| [ ] Contact info for support | | [Link] | |

---

## Part 6: Rollback Plan

### Rollback Preparation

| Item | Status | Notes |
|------|--------|-------|
| [ ] Rollback procedure documented | | |
| [ ] Previous version available | | |
| [ ] Rollback tested | | |
| [ ] Data backup taken before launch | | |
| [ ] Rollback decision criteria defined | | |

### Rollback Triggers

| Condition | Action |
|-----------|--------|
| Error rate > [X]% | Rollback |
| [X] users report issues | Investigate, possible rollback |
| Critical data corruption | Immediate rollback |
| Security vulnerability discovered | Immediate rollback |

### Rollback Steps

1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Notify stakeholders]
5. [Investigate root cause]

---

## Part 7: Communication Plan

### Stakeholder Notification

| Stakeholder | Method | Timing | Owner |
|-------------|--------|--------|-------|
| Executives | Email | 1 day before | |
| Users/Team | Slack + Email | Launch day | |
| Customers (if applicable) | Email | As appropriate | |
| Support team | Meeting | 2 days before | |

### Launch Announcement Draft

```
Subject: [Automation Name] Now Live

Hi team,

[Automation Name] is now live! Here's what you need to know:

**What's New:**
- [Feature 1]
- [Feature 2]

**How to Use:**
[Brief instructions]

**What to Expect:**
[Set expectations]

**Questions?**
Contact [Name] via [channel]

Best,
[Your name]
```

---

## Part 8: Training Complete

### Training Status

| Audience | Training Type | Status | Date |
|----------|---------------|--------|------|
| Primary users | Live session | [ ] Complete | |
| Support team | Documentation + Q&A | [ ] Complete | |
| Stakeholders | Overview briefing | [ ] Complete | |

### Training Materials

| Material | Status | Location |
|----------|--------|----------|
| [ ] User guide distributed | | |
| [ ] Video walkthrough (if applicable) | | |
| [ ] FAQs shared | | |
| [ ] Support contacts provided | | |

---

## Part 9: Go-Live Execution

### Pre-Launch (1 hour before)

| Task | Status | Time | Owner |
|------|--------|------|-------|
| [ ] Final system check | | | |
| [ ] All team members available | | | |
| [ ] Monitoring dashboards open | | | |
| [ ] Communication channels ready | | | |
| [ ] Rollback plan accessible | | | |

### Launch Steps

| Step | Status | Time | Owner | Notes |
|------|--------|------|-------|-------|
| 1. [ ] Activate workflow/automation | | | | |
| 2. [ ] Verify trigger works | | | | |
| 3. [ ] Check first execution | | | | |
| 4. [ ] Verify output correct | | | | |
| 5. [ ] Monitor for errors (15 min) | | | | |
| 6. [ ] Confirm stable operation | | | | |
| 7. [ ] Send launch notification | | | | |

### Post-Launch (First Hour)

| Task | Status | Notes |
|------|--------|-------|
| [ ] Monitor error rates | | |
| [ ] Check performance metrics | | |
| [ ] Verify integrations working | | |
| [ ] Respond to any issues | | |
| [ ] Document any anomalies | | |

---

## Part 10: Post-Launch Review

### 24-Hour Check

| Item | Status | Notes |
|------|--------|-------|
| [ ] Automation running successfully | | |
| [ ] No critical errors | | |
| [ ] Performance acceptable | | |
| [ ] User feedback collected | | |
| [ ] Any issues documented | | |

### 1-Week Review

| Item | Status | Notes |
|------|--------|-------|
| [ ] Metrics tracking as expected | | |
| [ ] No ongoing issues | | |
| [ ] User adoption successful | | |
| [ ] Documentation updated | | |
| [ ] Lessons learned captured | | |

### Success Metrics Check

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| [Metric 1] | [Target] | [Actual] | [ ] Met [ ] Not met |
| [Metric 2] | [Target] | [Actual] | [ ] Met [ ] Not met |
| [Metric 3] | [Target] | [Actual] | [ ] Met [ ] Not met |

---

## Launch Approval Sign-Off

### Readiness Confirmation

| Area | Status | Approver |
|------|--------|----------|
| Development | [ ] Ready | [Name] |
| Testing | [ ] Ready | [Name] |
| Security | [ ] Ready | [Name] |
| Documentation | [ ] Ready | [Name] |
| Training | [ ] Ready | [Name] |

### Final Approval

- [ ] All critical items passed
- [ ] All high-priority items passed or have mitigation
- [ ] Rollback plan in place
- [ ] Team ready for launch

**Approved for Launch:**

Project Lead: _____________________ Date: _________

Sponsor: _____________________ Date: _________

**Actual Launch Date/Time:** ___________________

---

*Template from AI Launchpad Academy - support-forge.com*
