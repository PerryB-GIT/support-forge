# Zapier Templates Collection

A curated list of useful Zapier templates to jumpstart your automation journey. Each template can be customized to fit your specific needs.

---

## Lead Generation & Sales

### 1. New Form Submission to CRM
**Template:** [Google Forms to HubSpot CRM](https://zapier.com/shared/google-forms-to-hubspot-crm/e8c1c3c8e0f9e8a7b6c5d4e3f2a1b0c9)

**What it does:**
- Captures Google Form responses
- Creates or updates contact in HubSpot
- Triggers follow-up workflow

**Customization Tips:**
- Add field mapping for custom form fields
- Include a filter step to qualify leads before adding to CRM
- Add a Slack notification for high-value leads
- Connect to your email marketing for immediate follow-up

---

### 2. Lead Capture to Spreadsheet + Email
**Template:** [Typeform to Google Sheets + Gmail](https://zapier.com/shared/typeform-google-sheets-gmail-notification/a1b2c3d4e5f6g7h8i9j0)

**What it does:**
- Saves Typeform responses to Google Sheets
- Sends email notification to your team
- Can trigger auto-responder

**Customization Tips:**
- Add conditional logic based on form answers
- Include lead scoring calculation
- Route to different team members based on inquiry type
- Add calendar booking link in the auto-response

---

## Email & Communication

### 3. Email Attachment Saver
**Template:** [Gmail Attachments to Google Drive](https://zapier.com/shared/gmail-attachments-to-google-drive/b2c3d4e5f6g7h8i9j0k1)

**What it does:**
- Monitors Gmail for emails with attachments
- Saves attachments to organized Google Drive folders
- Maintains file naming convention

**Customization Tips:**
- Filter by sender or subject line
- Create date-based folder structure
- Add notification when large files are saved
- Connect to Dropbox or OneDrive instead

---

### 4. Missed Call Follow-up
**Template:** [Missed Call to SMS + Email](https://zapier.com/shared/missed-call-sms-email-followup/c3d4e5f6g7h8i9j0k1l2)

**What it does:**
- Detects missed calls from your phone system
- Sends SMS to caller apologizing
- Emails you with caller details

**Customization Tips:**
- Add business hours filter (no SMS at 2am)
- Include callback scheduling link
- Route urgent calls to backup number
- Log all missed calls to a CRM

---

## Project Management

### 5. New Client Project Setup
**Template:** [Stripe Payment to Trello + Slack](https://zapier.com/shared/stripe-trello-slack-project-setup/d4e5f6g7h8i9j0k1l2m3)

**What it does:**
- Triggers on successful Stripe payment
- Creates Trello board from template
- Notifies team in Slack
- Adds client to project list

**Customization Tips:**
- Add Google Drive folder creation
- Include welcome email sequence
- Create recurring calendar events
- Set up automated check-in reminders

---

### 6. Task Due Date Reminders
**Template:** [Asana Task Reminders to Slack](https://zapier.com/shared/asana-task-due-slack-reminder/e5f6g7h8i9j0k1l2m3n4)

**What it does:**
- Checks for tasks due today/tomorrow
- Sends Slack reminders to assignees
- Daily summary of overdue tasks

**Customization Tips:**
- Customize reminder timing (2 days before, etc.)
- Add SMS for critical tasks
- Create escalation for overdue items
- Include task links in notifications

---

## Content & Social Media

### 7. Blog Post Social Distribution
**Template:** [RSS Feed to Social Media](https://zapier.com/shared/rss-to-twitter-linkedin-facebook/f6g7h8i9j0k1l2m3n4o5)

**What it does:**
- Monitors your blog RSS feed
- Posts to Twitter, LinkedIn, Facebook
- Customizes message for each platform

**Customization Tips:**
- Add delay between posts (not all at once)
- Include relevant hashtags by category
- Schedule for optimal posting times
- Add to Buffer for review before posting

---

### 8. Content Calendar Automation
**Template:** [Google Calendar to Social Posts](https://zapier.com/shared/google-calendar-scheduled-social-posts/g7h8i9j0k1l2m3n4o5p6)

**What it does:**
- Reads content from Google Calendar events
- Posts to social media at scheduled time
- Supports multiple platforms

**Customization Tips:**
- Use calendar event description for post content
- Add approval step before posting
- Include image attachments from Drive
- Track performance with UTM parameters

---

## Customer Support

### 9. Support Ticket Routing
**Template:** [Email to Zendesk + Slack Alert](https://zapier.com/shared/email-zendesk-slack-support-routing/h8i9j0k1l2m3n4o5p6q7)

**What it does:**
- Creates Zendesk ticket from email
- Alerts support team in Slack
- Assigns based on keywords

**Customization Tips:**
- Add priority detection from subject/body
- Route VIP customers to senior support
- Include customer history lookup
- Set SLA timers based on priority

---

### 10. Customer Feedback Collection
**Template:** [NPS Survey to Spreadsheet + Follow-up](https://zapier.com/shared/nps-survey-spreadsheet-followup/i9j0k1l2m3n4o5p6q7r8)

**What it does:**
- Collects NPS survey responses
- Logs to Google Sheets for analysis
- Triggers appropriate follow-up

**Customization Tips:**
- Segment by score (promoter/passive/detractor)
- Alert team lead for low scores immediately
- Request reviews from promoters (score 9-10)
- Schedule callback for detractors (score 0-6)

---

## Quick Reference: Template Categories

| Category | Best For | Key Integrations |
|----------|----------|------------------|
| Lead Gen | Sales teams | Forms, CRM, Email |
| Email | All teams | Gmail, Sheets, Slack |
| Projects | Project managers | Trello, Asana, Slack |
| Content | Marketing | RSS, Social, Calendar |
| Support | Customer success | Help desk, Email, Slack |

---

## How to Use These Templates

### Step 1: Click the Template Link
Each link opens Zapier with the template pre-loaded.

### Step 2: Connect Your Accounts
- Link your Google, Slack, CRM accounts
- Authorize Zapier to access your data
- Test each connection

### Step 3: Customize the Workflow
- Map your specific fields
- Add filters and conditions
- Adjust timing and triggers

### Step 4: Test Thoroughly
- Run manual tests first
- Check all edge cases
- Verify data flows correctly

### Step 5: Turn On and Monitor
- Enable the Zap
- Monitor first few runs
- Adjust as needed

---

## Building Your Own Templates

### Template Creation Tips:

1. **Start Simple**
   - Begin with 2-3 step Zaps
   - Add complexity after testing

2. **Use Filters Wisely**
   - Prevent unnecessary task usage
   - Only trigger when needed

3. **Add Error Handling**
   - Include fallback actions
   - Set up error notifications

4. **Document Your Zaps**
   - Use clear naming conventions
   - Add descriptions to each step

### Naming Convention Suggestion:
```
[Trigger App] > [Action] > [Destination]

Examples:
- Form > NewLead > HubSpot
- Gmail > Attachment > Drive
- Calendar > Reminder > Slack
```

---

## Cost Optimization Tips

1. **Combine Steps**
   - Use Paths to handle multiple outcomes in one Zap
   - Reduces task count

2. **Use Filters**
   - Stop Zaps early when conditions aren't met
   - Filtered actions don't count as tasks

3. **Batch Operations**
   - Use Digest to collect items before acting
   - One notification vs many

4. **Schedule Triggers**
   - Use schedule triggers vs instant when real-time isn't needed
   - More control over task usage

---

## Additional Resources

- [Zapier Template Gallery](https://zapier.com/templates)
- [Zapier University](https://zapier.com/university)
- [Zapier Community](https://community.zapier.com)
- [Zapier Blog - Automation Ideas](https://zapier.com/blog/category/automation/)

---

*Template by Launchpad Academy - Module 5: Automation Engines*
