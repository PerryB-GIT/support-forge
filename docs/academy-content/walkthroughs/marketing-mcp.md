# Marketing MCP Integration Guide

> **Support Forge AI Launchpad Academy**
> LinkedIn and Google Ads integration through Claude

---

## Overview

Marketing automation is critical for modern businesses. With Zapier MCP, Claude can help you manage LinkedIn company updates, share content, create Google Ads campaigns, manage customer lists, and track conversions.

**What you'll learn:**
- Post updates to LinkedIn Company Pages
- Share content on LinkedIn profiles
- Manage Google Ads campaigns and customer lists
- Track offline conversions
- Create marketing reports

---

## Prerequisites

- [ ] Zapier MCP configured ([see setup guide](./zapier-mcp-setup.md))
- [ ] LinkedIn account with Company Page admin access
- [ ] Google Ads account with appropriate permissions
- [ ] Both accounts connected in Zapier

---

## LinkedIn Integration

### Available Tools

| Tool | Description |
|------|-------------|
| `linkedin_create_company_update` | Post to Company Page |
| `linkedin_create_share_update` | Share to personal profile |
| `linkedin_api_request_beta` | Advanced API requests |

### Example: Create a Company Page Update

```
Post an update to our company LinkedIn page announcing our new product launch
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__linkedin_create_company_update",
  "parameters": {
    "instructions": "Create company update about product launch",
    "company_id": "[your_company_id]",
    "comment": "Excited to announce the launch of our new product! After months of development, we're proud to introduce a solution that will transform how you work. Learn more at our website.\n\n#ProductLaunch #Innovation #Tech"
  }
}
```

### Example: Share with Image

```
Share a company update with our product image and link to the announcement page
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__linkedin_create_company_update",
  "parameters": {
    "instructions": "Create company update with image and link",
    "company_id": "[your_company_id]",
    "comment": "Check out our new product! Click below to learn more about how it can help your business.",
    "image": "https://example.com/product-image.png",
    "image_type": "image",
    "submitted_url": "https://example.com/product-launch",
    "title": "Introducing Our Revolutionary New Product",
    "description": "Transform your workflow with our latest innovation. See what all the buzz is about."
  }
}
```

### Example: Share to Personal Profile

```
Share a post to my personal LinkedIn about our company's industry insights
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__linkedin_create_share_update",
  "parameters": {
    "instructions": "Share industry insights post",
    "comment": "Great insights from our team on the future of AI in business. Proud to work with such forward-thinking colleagues!",
    "content__url": "https://example.com/blog/ai-insights",
    "content__title": "The Future of AI in Business: 5 Trends for 2026",
    "content__description": "Our research team shares predictions for how AI will transform business operations.",
    "visibility__code": "anyone"
  }
}
```

### Visibility Options

| Code | Description |
|------|-------------|
| `anyone` | Visible to everyone |
| `connections-only` | Only your connections |

### Example: Share with Image on Personal Profile

```
Share an article with a custom preview image
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__linkedin_create_share_update",
  "parameters": {
    "instructions": "Share article with image preview",
    "comment": "Just published my latest thoughts on marketing automation. Check it out!",
    "content__submitted_image_url": "https://example.com/article-thumbnail.jpg",
    "content__submitted_url": "https://example.com/marketing-automation-guide",
    "content__title": "The Complete Guide to Marketing Automation",
    "content__description": "Everything you need to know to get started with marketing automation.",
    "visibility__code": "anyone"
  }
}
```

---

## Google Ads Integration

### Available Tools

| Tool | Description |
|------|-------------|
| `google_ads_find_campaign_by_id` | Find campaign by ID |
| `google_ads_find_campaign_by_name` | Find campaign by name |
| `google_ads_set_campaign_status` | Enable/pause campaigns |
| `google_ads_find_customer_list` | Find audience lists |
| `google_ads_create_customer_list` | Create new audience |
| `google_ads_add_contact_to_customer_list` | Add to audience |
| `google_ads_add_contact_to_customer_list_with_email` | Add by email |
| `google_ads_remove_contact_from_customer_list` | Remove from audience |
| `google_ads_send_offline_conversion` | Track offline conversions |
| `google_ads_create_report` | Generate reports |

### Example: Find Campaign by Name

```
Find my Google Ads campaign called "Summer Sale 2026"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_find_campaign_by_name",
  "parameters": {
    "instructions": "Find campaign named Summer Sale 2026",
    "mainAccountId": "[your_account_id]"
  }
}
```

### Example: Pause a Campaign

```
Pause the "Summer Sale 2026" campaign
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_set_campaign_status",
  "parameters": {
    "instructions": "Pause Summer Sale 2026 campaign",
    "mainAccountId": "[your_account_id]",
    "status": "PAUSED"
  }
}
```

### Campaign Status Options

| Status | Description |
|--------|-------------|
| `ENABLED` | Campaign is active |
| `PAUSED` | Campaign is paused |
| `REMOVED` | Campaign is deleted |

### Example: Enable a Campaign

```
Reactivate the "Summer Sale 2026" campaign
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_set_campaign_status",
  "parameters": {
    "instructions": "Enable Summer Sale 2026 campaign",
    "mainAccountId": "[your_account_id]",
    "status": "ENABLED"
  }
}
```

---

## Customer List Management

### Example: Create Customer List

```
Create a new customer list called "Newsletter Subscribers Q1 2026"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_create_customer_list",
  "parameters": {
    "instructions": "Create newsletter subscribers list",
    "mainAccountId": "[your_account_id]",
    "name": "Newsletter Subscribers Q1 2026",
    "description": "Subscribers who signed up for our newsletter in Q1 2026"
  }
}
```

### Example: Find Customer List

```
Find my customer list named "VIP Customers"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_find_customer_list",
  "parameters": {
    "instructions": "Find VIP Customers list",
    "mainAccountId": "[your_account_id]",
    "name": "VIP Customers"
  }
}
```

### Example: Add Contact by Email

```
Add john@example.com to the "VIP Customers" list
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_add_contact_to_customer_list_with_email",
  "parameters": {
    "instructions": "Add john@example.com to VIP Customers",
    "mainAccountId": "[your_account_id]",
    "customer_list_id": "[list_id]",
    "emailAddress": "john@example.com",
    "adUserData": "GRANTED",
    "adPersonalization": "GRANTED"
  }
}
```

### Consent Options

When adding contacts, you must specify consent:

| Field | Options | Description |
|-------|---------|-------------|
| `adUserData` | `GRANTED`, `DENIED`, `UNSPECIFIED` | Consent for using data |
| `adPersonalization` | `GRANTED`, `DENIED`, `UNSPECIFIED` | Consent for personalization |

### Example: Add Contact with Full Details

```
Add a customer with their hashed identifiers to my remarketing list
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_add_contact_to_customer_list",
  "parameters": {
    "instructions": "Add customer with identifier to list",
    "mainAccountId": "[your_account_id]",
    "customer_list_id": "[list_id]",
    "customer_identifier": "hashed_email_or_phone",
    "adUserData": "GRANTED",
    "adPersonalization": "GRANTED"
  }
}
```

### Example: Remove Contact

```
Remove john@example.com from the "VIP Customers" list
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_remove_contact_from_customer_list",
  "parameters": {
    "instructions": "Remove john@example.com from VIP Customers",
    "mainAccountId": "[your_account_id]",
    "customer_list_id": "[list_id]",
    "customer_identifier": "john@example.com",
    "adUserData": "GRANTED",
    "adPersonalization": "GRANTED"
  }
}
```

---

## Conversion Tracking

### Example: Send Offline Conversion

```
Track a store purchase as an offline conversion for the "Store Visits" conversion action
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_send_offline_conversion",
  "parameters": {
    "instructions": "Track store purchase conversion",
    "mainAccountId": "[your_account_id]",
    "name": "Store Visits",
    "value": "150.00",
    "currency": "USD",
    "time": "2026-01-04T14:30:00Z",
    "identifier_source": ["email"],
    "adUserData": "GRANTED",
    "adPersonalization": "GRANTED"
  }
}
```

### Identifier Source Options

| Source | Description |
|--------|-------------|
| `email` | Match by email address |
| `phone` | Match by phone number |
| `address` | Match by physical address |
| `gclid` | Match by Google Click ID |

### Example: Track CRM Conversion

```
Send a conversion for a closed deal worth $5,000 from our CRM
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_send_offline_conversion",
  "parameters": {
    "instructions": "Track CRM deal closure conversion",
    "mainAccountId": "[your_account_id]",
    "name": "CRM Deal Closure",
    "value": "5000.00",
    "currency": "USD",
    "time": "2026-01-04T10:00:00Z",
    "identifier_source": ["gclid", "email"],
    "adUserData": "GRANTED",
    "adPersonalization": "GRANTED"
  }
}
```

---

## Reporting

### Example: Create Campaign Report

```
Create a report showing campaign performance for the last 30 days
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_create_report",
  "parameters": {
    "instructions": "Create campaign performance report for last 30 days",
    "mainAccountId": "[your_account_id]",
    "resource": "campaign",
    "datePreset": "LAST_30_DAYS",
    "limit": "100"
  }
}
```

### Date Preset Options

| Preset | Description |
|--------|-------------|
| `TODAY` | Today only |
| `YESTERDAY` | Yesterday only |
| `LAST_7_DAYS` | Past 7 days |
| `LAST_14_DAYS` | Past 14 days |
| `LAST_30_DAYS` | Past 30 days |
| `LAST_MONTH` | Previous calendar month |
| `THIS_MONTH` | Current month to date |

### Resource Types

| Resource | Description |
|----------|-------------|
| `campaign` | Campaign-level metrics |
| `ad_group` | Ad group metrics |
| `ad` | Individual ad metrics |
| `keyword` | Keyword performance |
| `search_term` | Search term report |

### Example: Create Ad Group Report

```
Create a report for ad group performance this month
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ads_create_report",
  "parameters": {
    "instructions": "Create ad group report for this month",
    "mainAccountId": "[your_account_id]",
    "resource": "ad_group",
    "datePreset": "THIS_MONTH",
    "limit": "50"
  }
}
```

---

## Common Errors and Fixes

### LinkedIn Errors

#### Error: "Company page not found"

**Cause:** Invalid company ID or no admin access

**Fix:**
- Find your company ID in LinkedIn Admin settings
- Verify your account has admin access
- Reconnect LinkedIn in Zapier

#### Error: "Rate limit exceeded"

**Cause:** Too many API requests

**Fix:**
- Wait before making more requests
- LinkedIn allows ~100 API calls per day for some endpoints
- Spread requests throughout the day

#### Error: "Invalid image URL"

**Cause:** Image URL is not accessible or wrong format

**Fix:**
- Use publicly accessible URLs
- Supported formats: PNG, JPG, GIF
- Ensure URL uses HTTPS

### Google Ads Errors

#### Error: "Customer not found"

**Cause:** Invalid account ID or no access

**Fix:**
- Use the correct customer ID (format: XXX-XXX-XXXX)
- For managed accounts, specify `managedAccountId`
- Verify connected account has access

#### Error: "Campaign not found"

**Cause:** Campaign name doesn't match or was deleted

**Fix:**
- Check exact campaign name spelling
- Verify campaign hasn't been removed
- Try finding by ID instead

#### Error: "Customer match upload failed"

**Cause:** Invalid data format or consent issues

**Fix:**
- Ensure proper consent values
- Hash emails/phone numbers if required
- Check that list exists and is active

#### Error: "Conversion action not found"

**Cause:** Conversion action name doesn't match

**Fix:**
- Check exact conversion action name
- Verify action is active in Google Ads
- Create the conversion action if it doesn't exist

---

## Pro Tips

### LinkedIn Tips

#### 1. Optimal Posting Times

Research shows best engagement at:
- Tuesday-Thursday mornings (8-10 AM)
- Lunch hours (12-1 PM)
- Avoid weekends for B2B content

#### 2. Hashtag Strategy

Use 3-5 relevant hashtags:
```
#IndustryTopic #CompanyName #Trending
```

#### 3. Image Specifications

For best display:
- Company updates: 1200x627 pixels
- Personal shares: 1200x1200 pixels
- Max file size: 8MB

#### 4. Content Length

LinkedIn recommends:
- 150-300 characters for maximum engagement
- Use line breaks for readability
- Include clear call-to-action

### Google Ads Tips

#### 1. Customer List Best Practices

- Minimum 1,000 users for most targeting
- Refresh lists regularly
- Segment by customer value

#### 2. Conversion Timing

Send conversions within 24 hours:
```
Conversion timestamp should be when the action occurred,
not when you're uploading it
```

#### 3. Report Scheduling

Create regular reports:
- Daily: Campaign spend monitoring
- Weekly: Performance trends
- Monthly: Comprehensive analysis

#### 4. Campaign Organization

Use consistent naming:
```
[Channel] - [Objective] - [Audience] - [Date]
Search - Leads - B2B - Q1-2026
```

---

## Workflow Examples

### Content Publishing Workflow

```
1. Find design in Canva for social post
2. Export design as PNG
3. Create LinkedIn company update with image
4. Create personal share with commentary
5. Log posting to Google Sheet for tracking
```

### Lead Nurture Workflow

```
1. When new lead added to CRM
2. Add email to "New Leads" customer list
3. Enable "New Lead Nurture" campaign
4. Track conversions as leads progress
```

### Campaign Performance Workflow

```
1. Create campaign report for last 7 days
2. Find underperforming campaigns
3. Pause campaigns with high cost, low conversions
4. Send report summary via email
```

### Customer Lifecycle Workflow

```
1. When customer makes purchase
2. Send offline conversion to Google Ads
3. Add to "Repeat Customers" list
4. Remove from "Prospect" list
5. Share success story on LinkedIn
```

---

## Integration Scenarios

### LinkedIn + Google Sheets

```
1. Track all LinkedIn posts in spreadsheet
2. Record engagement metrics
3. Analyze best performing content
```

### Google Ads + Gmail

```
1. Create campaign performance report
2. Format report summary
3. Email to stakeholders
```

### LinkedIn + Canva

```
1. Create design in Canva
2. Export as PNG
3. Use image in LinkedIn update
```

### Google Ads + Google Sheets

```
1. Export customer list from Sheets
2. Add contacts to Google Ads list
3. Create targeted campaign
```

---

## Next Steps

- [Google Workspace MCP Guide](./google-workspace-mcp.md) - Track campaigns in Sheets
- [Design Tools MCP Guide](./design-tools-mcp.md) - Create ad visuals
- [AI Studio MCP Guide](./ai-studio-mcp.md) - Generate ad copy

---

*Support Forge AI Launchpad Academy - Building the Future of AI Integration*
