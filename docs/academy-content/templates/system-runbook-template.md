# System Runbook: [System Name]

**Document Version:** 1.0
**Last Updated:** [Date]
**Owner:** [Name]
**Status:** [ ] Draft [ ] Active [ ] Archived

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Name] | Initial version |
| | | | |

---

## 1. System Overview

### Purpose
*What does this system do and why does it exist?*

[This system automates [process] to [achieve outcome]. It was implemented to [solve problem/improve efficiency/etc.].]

### System Type
- [ ] Workflow automation (Zapier/n8n/Make)
- [ ] Scheduled job
- [ ] Event-triggered automation
- [ ] AI assistant/chatbot
- [ ] Data pipeline
- [ ] Integration
- [ ] Other: ____________

### Business Context
| Field | Value |
|-------|-------|
| Business process | [What process this supports] |
| Department | [Owning department] |
| Business criticality | [ ] Critical [ ] High [ ] Medium [ ] Low |
| Users affected if down | [Number/description] |
| SLA requirements | [e.g., 99.9% uptime, 5-min response] |

---

## 2. Architecture

### System Diagram
```
[Create a simple ASCII or link to diagram]

┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Trigger   │───▶│  Processor  │───▶│   Output    │
│  (Webhook)  │    │   (n8n)     │    │  (Sheets)   │
└─────────────┘    └─────────────┘    └─────────────┘
                          │
                          ▼
                   ┌─────────────┐
                   │  AI Service │
                   │  (Claude)   │
                   └─────────────┘
```

### Components

| Component | Technology | Purpose | Location |
|-----------|------------|---------|----------|
| Trigger | Zapier webhook | Receives form data | Zapier cloud |
| Processor | n8n workflow | Data transformation | AWS EC2 |
| AI Service | Claude API | Content generation | Anthropic cloud |
| Data Store | Google Sheets | Store results | Google cloud |
| Notifications | Slack | Alert team | Slack cloud |

### Dependencies

| Dependency | Type | Failure Impact | Fallback |
|------------|------|----------------|----------|
| [Service 1] | External API | [Impact] | [Fallback plan] |
| [Service 2] | Database | [Impact] | [Fallback plan] |
| [Service 3] | Third-party | [Impact] | [Fallback plan] |

---

## 3. Access & Credentials

### Access Requirements

| Resource | Access Method | Who Has Access | Request Process |
|----------|---------------|----------------|-----------------|
| n8n dashboard | SSO | Automation team | Ticket to IT |
| AWS console | IAM | DevOps | Manager approval |
| API keys | Password vault | Lead only | Owner approval |
| Logs | CloudWatch | DevOps, Leads | Standard access |

### Credential Locations

| Credential | Purpose | Vault Path | Rotation Schedule |
|------------|---------|------------|-------------------|
| Claude API key | AI processing | Vault/AI/Claude | Quarterly |
| Google OAuth | Sheets access | Vault/Google/Sheets | Annually |
| Slack webhook | Notifications | Vault/Slack/Webhook | Annually |

**Note:** Never store actual credentials in this document.

---

## 4. Normal Operations

### Operational Schedule

| Operation | Schedule | Duration | Notes |
|-----------|----------|----------|-------|
| Primary workflow | Triggered by webhook | ~30 seconds | On-demand |
| Daily summary | 6:00 AM ET | ~2 minutes | Scheduled |
| Weekly cleanup | Sunday 2:00 AM | ~5 minutes | Scheduled |

### Expected Volumes

| Metric | Normal Range | Alert Threshold |
|--------|--------------|-----------------|
| Executions/day | 50-100 | >200 or <10 |
| Processing time | 5-30 seconds | >60 seconds |
| Error rate | <2% | >5% |
| API calls/day | 200-400 | >1000 |

### Monitoring

| What to Monitor | Tool | Dashboard/Location | Alert Recipients |
|-----------------|------|-------------------|------------------|
| Workflow executions | n8n | n8n > Executions | #automation-alerts |
| Error rate | n8n | n8n > Executions > Failed | [email/Slack] |
| API usage | Claude console | console.anthropic.com | [email] |
| Response time | Custom | [Dashboard URL] | [email/Slack] |

---

## 5. Troubleshooting

### Quick Diagnosis

**System not responding?**
1. Check n8n is running: [n8n dashboard URL]
2. Check AWS EC2 status: [AWS console link]
3. Check API status pages: [Links]

**Outputs incorrect?**
1. Check input data format
2. Review recent execution logs
3. Test with known good input
4. Check for API changes

### Common Issues

#### Issue: Workflow not triggering
**Symptoms:** No new executions despite expected triggers
**Possible Causes:**
1. Webhook URL changed
2. Trigger source not sending
3. n8n instance down

**Resolution Steps:**
1. Verify webhook URL matches trigger configuration
2. Check trigger source (form, app) is operational
3. Check n8n dashboard for instance status
4. Review n8n logs: `docker logs n8n`

---

#### Issue: API errors from Claude
**Symptoms:** Errors mentioning rate limit, authentication, or timeout
**Possible Causes:**
1. API key expired or revoked
2. Rate limit exceeded
3. API service issue

**Resolution Steps:**
1. Check API key is valid in console.anthropic.com
2. Check usage against limits
3. Check Anthropic status page
4. Rotate API key if needed (see Credential Rotation section)

---

#### Issue: Missing or incorrect outputs
**Symptoms:** Data not appearing in destination or wrong format
**Possible Causes:**
1. Mapping/transformation error
2. Schema change in source or destination
3. AI returning unexpected format

**Resolution Steps:**
1. Check execution logs for errors
2. Compare input/output with expected schema
3. Test transformation logic manually
4. Review and update prompts if AI-related

---

### Error Messages Reference

| Error Message | Meaning | Resolution |
|---------------|---------|------------|
| `401 Unauthorized` | Invalid/expired API key | Rotate API key |
| `429 Too Many Requests` | Rate limit hit | Reduce frequency, add delays |
| `500 Internal Server Error` | Provider issue | Check status page, retry |
| `Connection refused` | Service unreachable | Check service status, network |
| `Timeout` | Response too slow | Increase timeout, reduce payload |

---

## 6. Incident Response

### Severity Levels

| Severity | Definition | Response Time | Examples |
|----------|------------|---------------|----------|
| P1 - Critical | System completely down | 15 minutes | All workflows failing |
| P2 - High | Major feature impaired | 1 hour | Primary workflow broken |
| P3 - Medium | Minor feature impaired | 4 hours | Non-critical errors |
| P4 - Low | Cosmetic/minor issue | Next business day | Formatting issues |

### Escalation Path

| Level | Contact | When to Escalate |
|-------|---------|------------------|
| L1 | On-call: [Name/Phone] | First response |
| L2 | Team Lead: [Name/Phone] | After 30 min or P1/P2 |
| L3 | Engineering Manager: [Name/Phone] | After 2 hours or critical |
| L4 | Director: [Name/Phone] | Extended outage or data loss |

### Incident Procedure

1. **Acknowledge**
   - Acknowledge alert within SLA
   - Update status channel: #incidents

2. **Assess**
   - Determine severity
   - Identify affected components
   - Check for related issues

3. **Communicate**
   - Notify stakeholders per severity
   - Update status page if customer-facing

4. **Resolve**
   - Follow troubleshooting steps
   - Implement fix or workaround
   - Verify resolution

5. **Document**
   - Complete incident report
   - Update runbook if new issue
   - Schedule post-mortem if needed

---

## 7. Maintenance Procedures

### Routine Maintenance

#### Daily Checks
- [ ] Review overnight execution summary
- [ ] Check error count is within threshold
- [ ] Verify outputs are being generated
- [ ] Monitor API usage trending

#### Weekly Maintenance
- [ ] Review all failed executions
- [ ] Check log storage usage
- [ ] Verify backups completed
- [ ] Review and clean up test data

#### Monthly Maintenance
- [ ] Review and optimize slow workflows
- [ ] Update dependencies if needed
- [ ] Audit access permissions
- [ ] Review and update documentation

### Credential Rotation

**Schedule:** Quarterly (or when compromised)

**Steps:**
1. Generate new credential in provider console
2. Update in password vault
3. Update in n8n credentials
4. Test with single execution
5. Monitor for 24 hours
6. Revoke old credential
7. Document in change log

### Backup & Recovery

**What's Backed Up:**
| Component | Backup Method | Frequency | Retention |
|-----------|---------------|-----------|-----------|
| Workflow definitions | n8n export | Daily | 30 days |
| Credentials | Vault backup | Daily | 90 days |
| Logs | CloudWatch | Real-time | 14 days |
| Configuration | Git repo | On change | Unlimited |

**Recovery Procedure:**
1. [Steps to restore from backup]
2. [Steps to verify restoration]
3. [Steps to resume operations]

---

## 8. Change Management

### Change Types

| Type | Approval | Testing Required | Rollback Plan |
|------|----------|------------------|---------------|
| Config change | Peer review | Staging test | Restore previous config |
| Workflow update | Team lead | Full regression | Version rollback |
| Credential update | Owner approval | Single test | Immediate rotation |
| Infrastructure | CAB approval | Full test suite | Infrastructure rollback |

### Deployment Procedure

1. **Prepare**
   - Document changes
   - Notify stakeholders
   - Prepare rollback

2. **Deploy (off-peak)**
   - Export current version
   - Apply changes
   - Initial smoke test

3. **Verify**
   - Test all affected functions
   - Monitor metrics
   - Confirm with stakeholders

4. **Complete**
   - Update documentation
   - Close change ticket
   - Monitor for 24 hours

---

## 9. Contacts

### Primary Contacts

| Role | Name | Contact | Availability |
|------|------|---------|--------------|
| System Owner | [Name] | [Email/Phone] | Business hours |
| Technical Lead | [Name] | [Email/Phone] | Business hours |
| On-call | [Rotation] | [Phone/PagerDuty] | 24/7 |

### Vendor Contacts

| Vendor | Purpose | Support Contact | Account ID |
|--------|---------|-----------------|------------|
| Anthropic | Claude API | support@anthropic.com | [ID] |
| n8n | Workflow platform | [Support URL] | [ID] |
| AWS | Infrastructure | AWS Support | [Account] |

### Communication Channels

| Channel | Purpose | Link |
|---------|---------|------|
| #automation-team | Team discussion | [Slack link] |
| #automation-alerts | System alerts | [Slack link] |
| #incidents | Incident coordination | [Slack link] |

---

## 10. Appendix

### Related Documentation

| Document | Purpose | Location |
|----------|---------|----------|
| Architecture diagram | Visual system design | [Link] |
| API documentation | Integration details | [Link] |
| Training materials | User guides | [Link] |
| Change log | History of changes | [Link] |

### Useful Commands

```bash
# Check n8n status
docker ps | grep n8n

# View n8n logs
docker logs n8n --tail 100

# Restart n8n
docker-compose restart n8n

# Export workflows (backup)
docker exec n8n n8n export:workflow --all > backup.json

# Check API connectivity
curl -I https://api.anthropic.com/v1/messages
```

### Glossary

| Term | Definition |
|------|------------|
| MCP | Model Context Protocol - connects AI to tools |
| Workflow | Automated sequence of actions in n8n |
| Webhook | HTTP endpoint that triggers automation |
| Execution | Single run of a workflow |

---

*Template from AI Launchpad Academy - support-forge.com*
