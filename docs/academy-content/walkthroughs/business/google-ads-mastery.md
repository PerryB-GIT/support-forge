# Google Ads Mastery with Claude MCP

> Transform your Google Ads management with AI-powered automation. This guide shows you how to manage campaigns, audiences, and conversions directly through Claude.

## Business Value

Google Ads typically requires:
- **30-60 minutes daily** for campaign monitoring
- **2-4 hours weekly** for reporting
- **Constant vigilance** for budget optimization
- **Technical expertise** for conversion tracking

With Claude MCP integration, you can:
- **Reduce management time by 70%** through conversational commands
- **Get instant campaign insights** without logging into the dashboard
- **Automate audience management** based on CRM data
- **Track offline conversions** automatically
- **Generate reports** in seconds, not hours

**Expected ROI**: Businesses typically see 15-25% improvement in ROAS within 60 days due to faster response times and better optimization cycles.

---

## Prerequisites

Before starting, ensure you have:

1. **Google Ads Account** with active campaigns
2. **Zapier MCP Connection** configured in Claude
3. **Google Sheets** (for reporting integration)
4. **Manager Account Access** (if managing multiple accounts)

---

## Part 1: Understanding the Google Ads MCP Tools

### Available Tools Overview

| Tool | Purpose | Common Use Case |
|------|---------|-----------------|
| `find_campaign_by_id` | Retrieve specific campaign | Get performance data |
| `find_campaign_by_name` | Search campaigns | Find campaigns matching criteria |
| `find_customer_list` | Locate audiences | Verify audience existence |
| `create_customer_list` | Build new audiences | Remarketing lists |
| `add_contact_to_customer_list` | Add emails to audiences | CRM sync |
| `remove_contact_from_customer_list` | Remove from audiences | Unsubscribe handling |
| `create_report` | Generate performance data | Weekly reporting |
| `send_offline_conversion` | Track offline sales | Attribution |
| `set_campaign_status` | Enable/Disable campaigns | Budget management |

---

## Part 2: Initial Setup and Configuration

### Step 1: Connect Google Ads to Zapier

1. Log into your Zapier account
2. Navigate to **Connected Accounts**
3. Search for **Google Ads**
4. Click **Connect** and authorize with your Google account
5. Select the appropriate account (Manager or individual)

### Step 2: Verify Connection in Claude

Ask Claude to verify the connection:

```
Check my Google Ads connection status and list available accounts.
```

Expected response confirms your connected account and available actions.

### Step 3: Identify Your Account Structure

For manager accounts with multiple clients:

```
List all managed accounts in my Google Ads manager account.
```

---

## Part 3: Campaign Management

### Finding Campaigns

**By Name (Partial Match):**
```
Find my Google Ads campaigns containing "Brand" in the name.
```

This triggers:
```
mcp__zapier__google_ads_find_campaign_by_name
Instructions: Find campaigns with "Brand" in the name
```

**By ID (Exact Match):**
```
Get details for Google Ads campaign ID 12345678901.
```

### Real Example: Campaign Discovery

**Your request:**
```
Show me all active campaigns for my main Google Ads account and their current status.
```

**Claude executes:**
```
mcp__zapier__google_ads_find_campaign_by_name
Instructions: Find all campaigns and return their names, IDs, and status
mainAccountId: [Your connected account]
```

**Response includes:**
- Campaign names
- Campaign IDs
- Status (ENABLED, PAUSED, REMOVED)
- Budget information

### Managing Campaign Status

**Pause a Campaign:**
```
Pause my "Summer Sale 2024" campaign in Google Ads.
```

**Claude executes:**
```
mcp__zapier__google_ads_set_campaign_status
Instructions: Pause the campaign named "Summer Sale 2024"
status: PAUSED
mainAccountId: [Your account]
```

**Enable a Campaign:**
```
Enable the Google Ads campaign with ID 98765432101.
```

### Automation Pattern: Budget-Based Pausing

**Scenario**: Pause campaigns when monthly budget reaches 90%

```
Check my Google Ads campaign "Lead Gen - Main" and if spend is over $4,500
(90% of $5,000 budget), pause it and notify me.
```

**Workflow:**
1. Claude checks campaign spend via report
2. Compares against threshold
3. Pauses if needed
4. Reports action taken

---

## Part 4: Customer List (Audience) Management

### Why Customer Lists Matter

Customer lists enable:
- **Remarketing** to existing customers
- **Lookalike audiences** for expansion
- **Exclusion lists** to prevent wasted spend
- **Customer match** for personalized ads

### Creating a New Customer List

**Basic Creation:**
```
Create a new customer list in Google Ads called "Q1 2024 Purchasers"
with description "Customers who purchased in Q1 2024".
```

**Claude executes:**
```
mcp__zapier__google_ads_create_customer_list
Instructions: Create a customer list named "Q1 2024 Purchasers" with the given description
name: Q1 2024 Purchasers
description: Customers who purchased in Q1 2024
mainAccountId: [Your account]
```

### Finding Existing Lists

```
Find my Google Ads customer list named "Newsletter Subscribers".
```

**Claude executes:**
```
mcp__zapier__google_ads_find_customer_list
Instructions: Find customer list named "Newsletter Subscribers"
name: Newsletter Subscribers
mainAccountId: [Your account]
```

### Adding Contacts to Lists

**Single Contact:**
```
Add the email john.smith@example.com to my "High Value Customers"
customer list in Google Ads.
```

**Claude executes:**
```
mcp__zapier__google_ads_add_contact_to_customer_list_with_email
Instructions: Add john.smith@example.com to "High Value Customers" list
emailAddress: john.smith@example.com
customer_list_id: [Retrieved list ID]
adUserData: GRANTED
adPersonalization: GRANTED
mainAccountId: [Your account]
```

### Bulk Import from Google Sheets

**Scenario**: Import 500 customer emails from a spreadsheet

**Step 1 - Read the spreadsheet:**
```
Read all emails from column A in my "Customer Emails" Google Sheet,
starting from row 2.
```

**Step 2 - Add to customer list:**
```
Add all those emails to my "Remarketing - All Customers" list in Google Ads.
```

**Complete workflow request:**
```
Import all email addresses from my "CRM Export" Google Sheet (column B, rows 2-500)
and add them to my Google Ads customer list called "CRM Sync - January 2024".
```

### Removing Contacts

**Handle unsubscribes or data deletion requests:**
```
Remove john.smith@example.com from all my Google Ads customer lists.
```

**Claude executes:**
```
mcp__zapier__google_ads_remove_contact_from_customer_list
Instructions: Remove john.smith@example.com from customer lists
customer_identifier: john.smith@example.com
customer_list_id: [Each list ID]
adUserData: GRANTED
adPersonalization: GRANTED
mainAccountId: [Your account]
```

---

## Part 5: Offline Conversion Tracking

### Why Offline Conversions Matter

Most businesses have conversions that happen offline:
- Phone calls leading to sales
- In-store purchases from online ads
- B2B deals closed weeks after ad click
- Service appointments booked

Without offline conversion tracking, your Google Ads attribution is incomplete, leading to poor optimization decisions.

### Setting Up Offline Conversions

**Prerequisite**: Create a conversion action in Google Ads first:
1. Go to Google Ads > Tools > Conversions
2. Create a new conversion action
3. Select "Import" > "Other data sources"
4. Note the conversion action name

### Sending Offline Conversions

**Single Conversion:**
```
Send an offline conversion to Google Ads:
- Conversion action: "Phone Sale"
- Email: customer@example.com
- Value: $500
- Currency: USD
- Timestamp: 2024-01-15 14:30:00
```

**Claude executes:**
```
mcp__zapier__google_ads_send_offline_conversion
Instructions: Record offline conversion for Phone Sale
name: Phone Sale
identifier_source: ["EMAIL"]
value: 500
currency: USD
time: 2024-01-15T14:30:00
adUserData: GRANTED
adPersonalization: GRANTED
mainAccountId: [Your account]
managedAccountId: [If applicable]
```

### Automation Pattern: CRM-to-Ads Sync

**Scenario**: Automatically send conversions when deals close in your CRM

**Workflow request:**
```
Every time I tell you about a closed deal, send an offline conversion to Google Ads with:
- The customer's email
- The deal value
- Conversion action "CRM - Closed Won"
- Current timestamp

Deal: john@company.com closed for $2,500 today.
```

### Batch Conversion Import

**From Google Sheets:**
```
Import offline conversions from my "January Sales" Google Sheet:
- Column A: Email
- Column B: Sale Amount
- Column C: Sale Date
Send each row as an offline conversion to Google Ads using "Store Sale" conversion action.
```

---

## Part 6: Reporting and Analytics

### Creating Campaign Reports

**Basic Performance Report:**
```
Create a Google Ads report showing all campaigns with impressions, clicks,
cost, and conversions for the last 30 days.
```

**Claude executes:**
```
mcp__zapier__google_ads_create_report
Instructions: Generate campaign performance report for last 30 days with impressions, clicks, cost, conversions
resource: campaign
datePreset: LAST_30_DAYS
mainAccountId: [Your account]
managedAccountId: [If applicable]
```

### Report Types Available

| Resource | What It Shows |
|----------|---------------|
| `campaign` | Campaign-level performance |
| `ad_group` | Ad group performance |
| `ad` | Individual ad performance |
| `keyword` | Keyword performance |
| `search_term` | Actual search queries |

### Saving Reports to Google Sheets

**Complete reporting workflow:**
```
Create a Google Ads campaign performance report for last 7 days and save it
to a new worksheet called "Weekly Report - Jan 15" in my "Google Ads Reports" spreadsheet.
```

**Workflow steps:**
1. Generate report via Google Ads MCP
2. Create new worksheet in Sheets
3. Format and insert data
4. Apply formatting for readability

### Automated Weekly Reporting

**Setup request:**
```
Every Monday, I want you to:
1. Pull my Google Ads campaign report for the previous week
2. Add it to my "Weekly Performance" Google Sheet as a new tab
3. Include: Campaign name, impressions, clicks, CTR, cost, conversions, CPA
4. Summarize the top 3 and bottom 3 performing campaigns
```

---

## Part 7: Integration Patterns

### Pattern 1: Sheets-Based Campaign Dashboard

**Create a live dashboard:**

```
Set up a campaign monitoring system:
1. Create a Google Sheet called "Google Ads Dashboard"
2. Add worksheets: "Daily Metrics", "Campaign Status", "Audiences"
3. Right now, populate "Campaign Status" with all my active campaigns
```

**Daily update request:**
```
Update my Google Ads Dashboard with today's performance data.
```

### Pattern 2: Customer Journey Automation

**New customer flow:**
```
When I say "New customer: [email]", do the following:
1. Add them to my "All Customers" list in Google Ads
2. Remove them from "Prospects" list
3. Log the action in my "Customer Actions" Google Sheet
```

**Usage:**
```
New customer: sarah@techcompany.com
```

### Pattern 3: Budget Alert System

**Setup:**
```
I want to track campaign budgets. My campaigns and monthly budgets are:
- "Brand Search": $3,000
- "Competitor Terms": $2,000
- "Display Remarketing": $1,500

Check current spend and alert me if any are over 80%.
```

### Pattern 4: Conversion Funnel Tracking

**Multi-stage tracking:**
```
Track this customer journey through Google Ads conversions:
- Email: lead@business.com
- Stage 1: "Demo Scheduled" - $0 value - January 10
- Stage 2: "Proposal Sent" - $0 value - January 15
- Stage 3: "Deal Closed" - $10,000 value - January 22
```

---

## Part 8: Advanced Automation Workflows

### Workflow 1: Competitor Campaign Automation

**Scenario**: Automatically manage competitor bidding based on your capacity

```
If I say "Capacity: LOW", pause my "Competitor - [Brand]" campaigns.
If I say "Capacity: HIGH", enable them.
Always log the change to my "Campaign Changes" Google Sheet.
```

### Workflow 2: Seasonal Campaign Management

**Setup seasonal rules:**
```
Create a seasonal campaign checklist:
- Summer campaigns: Enable May 1, Pause September 15
- Holiday campaigns: Enable November 1, Pause January 15
- Q1 promotion: Enable January 2, Pause March 31

When I ask "Prepare for [season]", enable/pause the appropriate campaigns.
```

### Workflow 3: Lead Quality Feedback Loop

**Improve targeting with conversion data:**
```
Process my lead quality report:
1. Read "Lead Quality" sheet with columns: Email, Source Campaign, Quality Score (1-5)
2. For leads scored 4-5, send $100 offline conversion to original campaign
3. For leads scored 1-2, add to "Low Quality Leads" exclusion list
4. Summarize actions taken
```

---

## Part 9: Troubleshooting

### Common Issues and Solutions

**Issue: "Campaign not found"**
- Verify campaign name spelling
- Check if campaign is in the correct account
- Use `find_campaign_by_name` with partial name

**Issue: "Customer list upload failed"**
- Ensure email format is valid
- Verify consent flags are set to GRANTED
- Check if list exists and you have access

**Issue: "Conversion not tracking"**
- Verify conversion action name matches exactly
- Check timestamp format (ISO 8601)
- Ensure user data consent is granted

### API Limitations

| Limitation | Workaround |
|------------|------------|
| 500 contacts per batch | Split into multiple requests |
| 90-day conversion window | Cannot import older conversions |
| Manager account required for some features | Use direct account access |

---

## Part 10: ROI Measurement

### Tracking Your Time Savings

Create a tracking system:
```
Create a "Claude Ads Management" Google Sheet with columns:
- Date
- Task Performed
- Estimated Manual Time (minutes)
- Actual Claude Time (minutes)
- Time Saved

Log each task we do together for ROI tracking.
```

### Key Metrics to Monitor

| Metric | Before Claude | Target After |
|--------|---------------|--------------|
| Daily management time | 45 min | 15 min |
| Weekly reporting time | 3 hours | 30 min |
| Audience update frequency | Monthly | Weekly |
| Conversion tracking delay | 3+ days | Same day |

### Calculating ROI

```
Calculate my Google Ads management ROI:
- My hourly rate: $75
- Hours saved per week: 4
- Weeks using Claude: 12
- Additional ROAS improvement: 15%
- Monthly ad spend: $10,000
```

---

## Quick Reference Card

### Campaign Management
```
Find campaigns named "[name]"
Pause campaign "[name]"
Enable campaign ID [id]
Get status of all campaigns
```

### Audience Management
```
Create customer list "[name]"
Add [email] to "[list name]"
Remove [email] from "[list name]"
Find customer list "[name]"
```

### Reporting
```
Create report for last [7/30/90] days
Show [campaign/ad_group/keyword] performance
Save report to Google Sheets
```

### Conversions
```
Send offline conversion: [email], [value], [conversion action]
Import conversions from [Sheet name]
```

---

## Next Steps

1. **Start simple**: Find and review your campaign performance
2. **Build audiences**: Create your first customer list from Sheets
3. **Track conversions**: Set up one offline conversion action
4. **Automate reporting**: Create your weekly report workflow
5. **Expand**: Add budget alerts and automated rules

---

*This guide is part of the Support Forge Academy MCP Mastery series. For questions or advanced use cases, refer to the complete documentation or ask Claude directly.*
