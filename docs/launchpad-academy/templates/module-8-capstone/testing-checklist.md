# Testing Checklist: Client Onboarding Agent

Use this comprehensive checklist to verify your capstone project works correctly before considering it complete.

---

## Pre-Testing Setup

### Environment Verification
- [ ] n8n instance is running and accessible
- [ ] All credential connections are configured and tested
- [ ] Webhook URL is active and reachable
- [ ] Test Google Sheet exists with correct column headers
- [ ] Test Slack channel exists and bot has permissions
- [ ] Test calendar is accessible

### Test Data Preparation
- [ ] Create test payload file with valid data
- [ ] Create test payload with minimal data (only required fields)
- [ ] Create test payload with maximum data (all fields populated)
- [ ] Create test payloads for edge cases (see below)

---

## End-to-End Test Scenarios

### Scenario 1: Complete Happy Path

**Input:**
```json
{
  "client": {
    "name": "John Smith",
    "email": "john.smith@testcompany.com",
    "company": "Test Company LLC",
    "phone": "+1-555-123-4567",
    "website": "https://testcompany.com"
  },
  "project": {
    "type": "web-development",
    "name": "Website Redesign",
    "budget": "$10,000-$15,000",
    "timeline": "8 weeks",
    "startDate": "2024-02-15",
    "description": "Complete redesign of corporate website with CMS integration"
  },
  "preferences": {
    "communicationMethod": "email",
    "meetingPreference": "morning",
    "timezone": "America/New_York",
    "specialRequests": "Prefer weekly status updates"
  }
}
```

**Expected Results:**
- [ ] Webhook returns 200 status
- [ ] Response contains valid clientId
- [ ] Google Drive folder created with correct name
- [ ] All subfolders created (Contracts, Brief, Assets, Deliverables)
- [ ] Spreadsheet row added with all fields populated
- [ ] Calendar event created with correct date/time
- [ ] Welcome email received at test address
- [ ] Slack notification posted to channel

---

### Scenario 2: Minimal Data (Required Fields Only)

**Input:**
```json
{
  "client": {
    "name": "Jane Doe",
    "email": "jane@minimal.test",
    "company": "Minimal Corp"
  },
  "project": {
    "type": "consulting"
  }
}
```

**Expected Results:**
- [ ] Workflow completes without errors
- [ ] Default values used for missing optional fields
- [ ] Folder name correctly derived from company name
- [ ] Email sent with appropriate default content
- [ ] Meeting scheduled with default time preference

---

### Scenario 3: All Project Types

Test each project type produces appropriate content:

| Project Type | Test Status | Checklist Correct | Email Correct |
|--------------|-------------|-------------------|---------------|
| web-development | [ ] | [ ] | [ ] |
| consulting | [ ] | [ ] | [ ] |
| marketing | [ ] | [ ] | [ ] |
| support | [ ] | [ ] | [ ] |
| custom | [ ] | [ ] | [ ] |

---

### Scenario 4: Different Meeting Preferences

| Preference | Expected Time | Verified |
|------------|---------------|----------|
| morning | 10:00 AM | [ ] |
| afternoon | 2:00 PM | [ ] |
| evening | 5:00 PM | [ ] |
| (none/default) | 10:00 AM | [ ] |

---

## Edge Cases to Verify

### Special Characters in Names

**Test Case EC-1: Company with Special Characters**
```json
{
  "client": {
    "name": "Bob O'Brien",
    "email": "bob@test.com",
    "company": "Smith & Jones, LLC"
  },
  "project": { "type": "consulting" }
}
```
- [ ] Folder name sanitized correctly (removes special chars)
- [ ] Email displays name correctly with apostrophe
- [ ] Spreadsheet stores full company name

---

**Test Case EC-2: Unicode Characters**
```json
{
  "client": {
    "name": "Maria Garcia",
    "email": "maria@test.com",
    "company": "Cafe Espresso"
  },
  "project": { "type": "marketing" }
}
```
- [ ] Accented characters handled in all outputs

---

**Test Case EC-3: Very Long Company Name**
```json
{
  "client": {
    "name": "Test User",
    "email": "test@test.com",
    "company": "The Incredibly Long Company Name That Might Cause Issues With File Systems And Display Truncation In Various Places Throughout The Application"
  },
  "project": { "type": "web-development" }
}
```
- [ ] Folder created (may be truncated)
- [ ] Spreadsheet stores full name
- [ ] No workflow errors

---

### Email Format Variations

**Test Case EC-4: Email Formats**

| Email Format | Should Work |
|--------------|-------------|
| simple@test.com | [ ] |
| name.surname@company.co.uk | [ ] |
| user+tag@gmail.com | [ ] |
| "quoted"@test.com | [ ] |

---

### Empty/Null Optional Fields

**Test Case EC-5: Explicit Null Values**
```json
{
  "client": {
    "name": "Null Test",
    "email": "null@test.com",
    "company": "Null Company",
    "phone": null,
    "website": ""
  },
  "project": {
    "type": "support",
    "budget": null,
    "description": ""
  }
}
```
- [ ] No errors from null values
- [ ] Empty strings handled gracefully
- [ ] Default values applied where appropriate

---

## Error Handling Tests

### Missing Required Fields

**Test Case ERR-1: No Client Name**
```json
{
  "client": {
    "email": "test@test.com",
    "company": "Test Co"
  },
  "project": { "type": "consulting" }
}
```
- [ ] Returns 400 status code
- [ ] Error message identifies missing field
- [ ] No partial data created (folder, spreadsheet row)

---

**Test Case ERR-2: No Email**
```json
{
  "client": {
    "name": "No Email Test",
    "company": "Test Co"
  },
  "project": { "type": "consulting" }
}
```
- [ ] Returns 400 status code
- [ ] Error message identifies missing email

---

**Test Case ERR-3: No Company**
```json
{
  "client": {
    "name": "No Company Test",
    "email": "test@test.com"
  },
  "project": { "type": "consulting" }
}
```
- [ ] Returns 400 status code
- [ ] Error message identifies missing company

---

**Test Case ERR-4: Empty Body**
```json
{}
```
- [ ] Returns 400 status code
- [ ] Meaningful error message returned

---

### Invalid Data Format

**Test Case ERR-5: Invalid Email Format**
```json
{
  "client": {
    "name": "Bad Email",
    "email": "not-an-email",
    "company": "Test Co"
  },
  "project": { "type": "consulting" }
}
```
- [ ] Handled gracefully (either rejected or flagged)

---

**Test Case ERR-6: Unknown Project Type**
```json
{
  "client": {
    "name": "Unknown Type",
    "email": "test@test.com",
    "company": "Test Co"
  },
  "project": { "type": "unknown-type-xyz" }
}
```
- [ ] Defaults to 'custom' type
- [ ] Workflow completes successfully

---

## Performance Checks

### Timing Tests

| Metric | Target | Actual | Pass |
|--------|--------|--------|------|
| Total execution time | < 30 seconds | _____ | [ ] |
| Webhook response time | < 5 seconds | _____ | [ ] |
| Folder creation | < 10 seconds | _____ | [ ] |
| Email delivery | < 60 seconds | _____ | [ ] |

---

### Load Testing (Optional)

- [ ] Submit 5 requests in quick succession
- [ ] Verify all 5 complete without errors
- [ ] Check for duplicate entries
- [ ] Verify unique client IDs generated

---

## Security Verification

### Data Protection

- [ ] Webhook requires HTTPS (in production)
- [ ] No sensitive data in URL parameters
- [ ] Credentials not exposed in logs
- [ ] Error messages don't leak internal details

---

### Access Control

- [ ] Google Drive folders have correct sharing settings
- [ ] Spreadsheet not publicly accessible
- [ ] Slack channel is appropriate (not public if contains PII)
- [ ] Calendar events don't expose sensitive details publicly

---

### Input Validation

- [ ] SQL injection attempts handled (N/A for most, but verify)
- [ ] XSS in description doesn't execute in email
- [ ] Large payloads don't crash workflow
- [ ] Malformed JSON returns proper error

---

## Integration Verification

### Google Drive
- [ ] Correct Google account used
- [ ] Folder created in expected location
- [ ] Folder permissions set correctly
- [ ] WebViewLink returned and valid

### Google Sheets
- [ ] Correct spreadsheet targeted
- [ ] Correct worksheet/tab used
- [ ] All columns populated
- [ ] Data types correct (dates formatted properly)

### Google Calendar
- [ ] Correct calendar targeted
- [ ] Event appears at correct time
- [ ] Attendee receives invitation
- [ ] Google Meet link generated (if configured)
- [ ] Description contains all relevant info

### Gmail
- [ ] Email sent from correct account
- [ ] Subject line correct
- [ ] HTML renders properly
- [ ] Links in email work
- [ ] No spam folder issues

### Slack
- [ ] Message appears in correct channel
- [ ] Formatting displays correctly
- [ ] Links work
- [ ] Attachment fields visible

---

## Cleanup Checklist

After testing, clean up test data:

- [ ] Delete test folders from Google Drive
- [ ] Remove test rows from spreadsheet
- [ ] Delete test calendar events
- [ ] Clear test emails from sent folder
- [ ] Delete test messages from Slack (if needed)

---

## Final Verification

### Documentation
- [ ] All node descriptions are filled in
- [ ] Workflow notes explain key logic
- [ ] Environment variables documented
- [ ] README updated with setup instructions

### Workflow Health
- [ ] No disabled nodes that should be active
- [ ] No orphaned nodes (not connected)
- [ ] Error handling configured
- [ ] Workflow is active/enabled

### Sign-Off

| Reviewer | Date | Status |
|----------|------|--------|
| Self-review | __________ | [ ] Pass |
| Peer review | __________ | [ ] Pass |
| Instructor | __________ | [ ] Pass |

---

## Test Results Summary

**Total Tests: ____**
**Passed: ____**
**Failed: ____**
**Skipped: ____**

**Notes:**
```
[Document any issues found and how they were resolved]
```

---

*Congratulations on completing the testing checklist! If all tests pass, you're ready to complete your capstone certificate.*
