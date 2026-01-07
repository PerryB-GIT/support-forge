# Email Marketing Automation with Claude MCP

> Build sophisticated email marketing systems using Gmail, Google Sheets, and Claude's intelligent automation capabilities.

## Business Value

Email marketing remains the highest ROI channel for most businesses:

| Metric | Industry Average | With Automation |
|--------|------------------|-----------------|
| ROI | $36 per $1 spent | $42+ per $1 spent |
| Open rates | 15-25% | 25-35% (with optimization) |
| Click rates | 2-5% | 5-10% (with personalization) |
| Time per campaign | 4-8 hours | 1-2 hours |

**The challenge**: Managing email marketing requires constant attention - list management, content creation, sending, and analysis.

**The solution**: Build an integrated system using Gmail for sending, Sheets for subscriber management, and Claude for content and automation.

---

## System Architecture

```
[Subscriber Sources] → [Google Sheets CRM] → [Claude Processing] → [Gmail/Email Platform]
                              ↓                       ↓
                    [Segmentation]           [Content Generation]
                              ↓                       ↓
                    [Automation Triggers]    [Performance Analysis]
```

---

## Part 1: Subscriber Management System

### Step 1: Create the Subscriber Database

**Setup request:**
```
Create a Google Sheet called "Email Marketing HQ" with these worksheets:

1. "Subscribers" - columns:
   Email, First Name, Last Name, Signup Date, Source, Status (Active/Unsubscribed/Bounced),
   Segment, Last Email Date, Total Opens, Total Clicks, Engagement Score, Notes

2. "Email Log" - columns:
   Date Sent, Subject Line, Recipient Count, Opens, Open Rate, Clicks, Click Rate,
   Unsubscribes, Campaign Type, Notes

3. "Templates" - columns:
   Template Name, Subject Line Template, Body Template, Use Case, Last Used, Performance Score

4. "Segments" - columns:
   Segment Name, Criteria, Subscriber Count, Last Updated, Average Open Rate

5. "Sequences" - columns:
   Sequence Name, Email Number, Days After Trigger, Subject, Status, Sent Count

6. "Campaign Calendar" - columns:
   Scheduled Date, Campaign Name, Segment, Status, Subject Line, Content Notes
```

### Step 2: Import Existing Subscribers

**Import workflow:**
```
I have a list of subscribers to import. Here's the data:
[Paste CSV or spreadsheet data]

Process this data and:
1. Add to my Subscribers worksheet
2. Set Status to "Active" for all
3. Set Signup Date to today if not provided
4. Identify any duplicate emails
5. Flag any potentially invalid email formats
6. Report: Total imported, duplicates found, invalid emails
```

### Step 3: Subscriber Segmentation

**Create segments:**
```
Create email segments based on my subscriber data:

Segment definitions:
1. "New Subscribers" - Signed up within last 30 days
2. "Engaged" - Opened 3+ emails in last 60 days
3. "At Risk" - No opens in last 90 days
4. "VIP" - Total clicks > 10
5. "Re-engage" - Previously active, no activity in 60-90 days

Update my Segments worksheet and tag each subscriber in the main list.
```

---

## Part 2: Email Content Creation

### Template Library

**Create reusable templates:**
```
Create email templates for these common use cases:

1. Welcome Email
   - Warm greeting
   - What to expect
   - Quick win/value
   - Call to action

2. Newsletter
   - Main headline
   - 3 content sections
   - Featured product/service
   - Social links

3. Promotional
   - Attention-grabbing headline
   - Offer details
   - Urgency element
   - Clear CTA button

4. Re-engagement
   - "We miss you" hook
   - What they're missing
   - Special offer to return
   - Easy unsubscribe option

For each, provide subject line templates and body structure in HTML format.
Save to my Templates worksheet.
```

### Generating Email Content

**Newsletter creation:**
```
Generate a newsletter for Sweet Meadow Bakery:

Topic: February specials and Valentine's Day
Segments: All active subscribers
Tone: Warm, community-focused, appetizing

Include:
- Compelling subject line (under 50 characters)
- Preview text (under 100 characters)
- Introduction paragraph
- 3 featured items with descriptions
- Valentine's Day special offer
- Call-to-action
- Footer with unsubscribe

Format: HTML email with inline styles
```

**Promotional email:**
```
Create a promotional email for:

Business: HomeBase Veterinary
Offer: 20% off wellness exams this month
Target: Pet owners who haven't visited in 6+ months
Urgency: Offer expires end of month

Include:
- Subject line with urgency
- Personalization (pet name if available)
- Clear offer presentation
- Benefits of wellness exams
- Easy booking CTA
- P.S. line with reminder
```

### A/B Test Subject Lines

**Generate test variations:**
```
Generate 5 subject line variations for this email:

Campaign: Spring cleaning special
Offer: 15% off house cleaning services
Business: Witch's Broom Cleaning

Variations should test:
1. Question format
2. Number/statistic
3. Urgency
4. Personalization
5. Curiosity gap

Keep all under 50 characters. Include predicted open rate factor (1-10).
```

---

## Part 3: Gmail Integration for Sending

### Sending Individual Emails

**Single email send:**
```
Send this email via Gmail:

To: customer@example.com
Subject: Your February Sweet Meadow Update
Body: [HTML content from template]

From name: Sweet Meadow Bakery
```

**Claude executes:**
```
mcp__zapier__gmail_send_email
Instructions: Send newsletter email to customer@example.com
to: ["customer@example.com"]
subject: Your February Sweet Meadow Update
body: [HTML content]
body_type: html
from_name: Sweet Meadow Bakery
```

### Creating Draft Campaigns

**Batch draft creation:**
```
Create Gmail drafts for my newsletter to these subscribers:

[List 10 email addresses]

Subject: Sweet Meadow February Newsletter
Body: [Generated newsletter content]

Create as drafts so I can review before sending.
```

**Claude executes (for each):**
```
mcp__zapier__gmail_create_draft
Instructions: Create newsletter draft for [email]
to: ["email@example.com"]
subject: Sweet Meadow February Newsletter
body: [HTML content]
body_type: html
```

### Personalized Sending

**Merge-style sending:**
```
Send personalized emails to these subscribers:

Subscriber data:
1. Email: john@example.com, First Name: John, Last Visit: January 5
2. Email: sarah@example.com, First Name: Sarah, Last Visit: December 12
3. Email: mike@example.com, First Name: Mike, Last Visit: February 1

Template:
Subject: {First Name}, we've got something special for you
Body: Include greeting with name and mention their last visit date

Send each email with personalized details.
```

---

## Part 4: Automated Email Sequences

### Welcome Sequence Setup

**Create welcome series:**
```
Design a 5-email welcome sequence for new subscribers:

Business: Vineyard Valais (wine shop)
Goal: Educate and convert to first purchase

Email 1 (Immediate):
- Subject focus: Welcome
- Content: Introduction, what to expect, immediate 10% discount

Email 2 (Day 3):
- Subject focus: Our story
- Content: Brand history, wine selection philosophy

Email 3 (Day 7):
- Subject focus: Best sellers
- Content: Top 5 wines with descriptions

Email 4 (Day 14):
- Subject focus: Educational
- Content: Wine pairing guide, showcase expertise

Email 5 (Day 21):
- Subject focus: Special offer
- Content: Extended welcome offer, urgency

For each, provide full content and save to my Sequences worksheet.
```

### Sequence Management Workflow

**Track sequence progress:**
```
Add a "Sequence Tracking" worksheet to my Email Marketing HQ:

Columns:
- Subscriber Email
- Sequence Name
- Current Email Number
- Last Email Sent Date
- Next Email Due Date
- Status (Active/Completed/Paused)

This tracks where each subscriber is in automated sequences.
```

### Daily Sequence Processing

**Daily sequence check:**
```
Check my sequence tracking for emails due today:

Look for subscribers where:
- Status = Active
- Next Email Due Date = today

For each, provide:
- Subscriber email
- Sequence name
- Email number to send
- Subject line (from sequence definition)

I'll confirm before sending.
```

---

## Part 5: Subscriber Analytics

### Engagement Scoring

**Calculate engagement scores:**
```
Update engagement scores for all subscribers in my list:

Scoring formula:
- Open in last 30 days: +3 points
- Open in last 31-60 days: +2 points
- Open in last 61-90 days: +1 point
- Click ever: +2 points per click (max 10)
- Recent signup (last 30 days): +5 points (new subscriber boost)
- No activity 90+ days: -5 points

Score ranges:
- 15+: Highly Engaged
- 10-14: Engaged
- 5-9: Moderate
- 1-4: Low
- 0 or below: At Risk

Update each subscriber's Engagement Score and update my Segments based on scores.
```

### Campaign Performance Analysis

**Post-send analysis:**
```
Analyze this email campaign's performance:

Campaign: February Newsletter
Sent to: 500 subscribers
Opens: 125 (25%)
Unique clicks: 35 (7% of opens)
Unsubscribes: 3

Benchmarks:
- Our average open rate: 22%
- Our average click rate: 5%
- Industry average open rate: 20%
- Industry average click rate: 3%

Provide:
1. Performance assessment
2. What worked well
3. Areas for improvement
4. Recommendations for next campaign
5. Update my Email Log worksheet
```

### List Health Report

**Monthly list health check:**
```
Generate a list health report from my subscriber data:

Analyze:
- Total subscribers
- Active rate (engaged in last 90 days)
- Bounce rate
- Unsubscribe rate (last 30 days)
- Growth rate (new signups - unsubscribes)
- Segment distribution
- Average engagement score

Recommendations:
- Subscribers to re-engage
- Subscribers to consider removing
- Segments to nurture
- List growth strategies
```

---

## Part 6: Integration Patterns

### Pattern 1: Website Signup to Welcome Sequence

**Full signup flow:**
```
New subscriber signed up:
- Email: newcustomer@example.com
- Name: Alex Johnson
- Source: Website popup
- Interest: Wine recommendations

Actions needed:
1. Add to my Subscribers worksheet
2. Add to "New Subscribers" segment
3. Start Welcome Sequence (set Next Email Due = today)
4. Send Email 1 immediately
5. Log the action
```

### Pattern 2: Purchase to Thank You Email

**Post-purchase email:**
```
Customer just made a purchase:
- Email: buyer@example.com
- Product: Assorted Croissant Box
- Order total: $45
- First-time buyer: Yes

Generate and send a thank you email that:
- Thanks them by name
- Confirms their order details
- Offers a 15% discount on next order (code: THANKS15)
- Invites them to follow on social media

Also update their subscriber record with:
- Tag: "Customer"
- Note: "First purchase: $45 - Croissant Box"
```

### Pattern 3: Cart Abandonment Recovery

**Recovery sequence:**
```
Set up a cart abandonment recovery system:

When I tell you about an abandoned cart:
- Capture: Email, items in cart, cart value

Trigger sequence:
Email 1 (1 hour later): "Did you forget something?"
Email 2 (24 hours later): "Your cart is waiting"
Email 3 (72 hours later): "10% off to complete your order"

For abandoned cart: alex@example.com, 2 bottles wine, $85 value
Create Email 1 draft now, schedule reminders for Emails 2 and 3.
```

### Pattern 4: Re-engagement Campaign

**Win-back workflow:**
```
Identify subscribers who haven't opened an email in 60-90 days and create a re-engagement campaign:

1. Query my Subscribers list for: No opens in 60-90 days, Status = Active
2. Generate a re-engagement email with:
   - Subject line testing "We miss you" vs "Is this goodbye?"
   - Special offer to return
   - Clear unsubscribe option
3. Create drafts for first 10 subscribers as a test
4. Track in Email Log as "Re-engagement Campaign"
```

### Pattern 5: Birthday/Anniversary Emails

**Automated celebration emails:**
```
Set up birthday email automation:

1. Add "Birthday" column to my Subscribers worksheet
2. Create a birthday email template with:
   - Personalized greeting
   - Special birthday offer
   - Warm wishes

Daily check: Which subscribers have birthdays today?
Auto-generate and draft birthday emails for review.
```

---

## Part 7: Advanced Email Strategies

### Segmented Campaigns

**Multi-segment campaign:**
```
Create a segmented promotional campaign:

Segment 1: VIP Customers
- Offer: Exclusive 25% off
- Messaging: Thank them for loyalty, early access

Segment 2: Regular Customers
- Offer: 15% off
- Messaging: Valued customer appreciation

Segment 3: New Subscribers
- Offer: First purchase 20% off
- Messaging: Welcome, incentive to try

Segment 4: At-Risk
- Offer: 30% off comeback special
- Messaging: We miss you, limited time

Generate all four email versions. I'll send to appropriate segments.
```

### Behavioral Triggers

**Setup behavioral emails:**
```
Define behavioral email triggers:

Trigger 1: "Browse Abandonment"
- When: Visited website but didn't purchase
- Email: "See something you liked?"
- Timing: 24 hours later

Trigger 2: "Repeat Purchase Reminder"
- When: 30 days since last purchase (consumable products)
- Email: "Time to restock?"
- Timing: Automatic

Trigger 3: "Review Request"
- When: 7 days after purchase
- Email: "How did we do?"
- Timing: Automatic

Create email templates for each trigger.
```

### Content Personalization

**Dynamic content blocks:**
```
Create a newsletter with dynamic content blocks:

Base template: Monthly newsletter
Dynamic sections based on segment:

For "Wine Enthusiasts":
- Featured wines with tasting notes
- Wine education content
- Vineyard updates

For "Gift Buyers":
- Gift sets and bundles
- Corporate gift options
- Shipping cutoff reminders

For "New Subscribers":
- Brand story
- Bestsellers introduction
- First purchase incentive

Generate the base template with placeholder markers for each segment.
```

---

## Part 8: Compliance and Best Practices

### GDPR/CAN-SPAM Compliance

**Compliance checklist:**
```
Audit my email marketing for compliance:

Check my setup for:
1. Clear unsubscribe link in every email
2. Physical address in footer
3. Accurate "From" name and email
4. No deceptive subject lines
5. Consent tracking for each subscriber
6. Unsubscribe processing within 10 days
7. No purchased lists

Add a "Consent" column to my Subscribers worksheet:
- Consent Date
- Consent Source
- Consent Type (Explicit/Implicit)
```

### Unsubscribe Handling

**Process unsubscribes:**
```
Process these unsubscribe requests:

Unsubscribed emails:
- user1@example.com
- user2@example.com
- user3@example.com

Actions:
1. Update Status to "Unsubscribed" in Subscribers worksheet
2. Add Unsubscribe Date
3. Remove from any active sequences
4. Add to "Suppression List" worksheet
5. Never email these addresses again
6. Log in Email Log as unsubscribe action
```

### Deliverability Best Practices

**Deliverability audit:**
```
Review my email practices for deliverability:

Current practices:
- Sending frequency: [describe]
- List cleaning: [describe]
- Authentication: [describe]

Provide recommendations for:
1. Optimal sending frequency
2. List hygiene schedule
3. Subject line best practices
4. HTML email best practices
5. Image-to-text ratio
6. Spam trigger words to avoid
```

---

## Part 9: Reporting and Analytics

### Weekly Email Report

**Generate weekly report:**
```
Generate my weekly email marketing report:

Campaigns sent this week:
[Paste from Email Log]

Report should include:
1. Total emails sent
2. Average open rate
3. Average click rate
4. Unsubscribes
5. Best performing subject line
6. Worst performing subject line
7. List growth (new signups - unsubscribes)
8. Revenue attributed (if available)
9. Recommendations for next week
```

### Monthly Performance Dashboard

**Monthly analysis:**
```
Update my email marketing dashboard for [Month]:

Data needed:
- All campaigns from Email Log
- Subscriber list changes
- Segment performance

Create a summary:
1. Month-over-month comparison
2. Best campaigns by open rate
3. Best campaigns by click rate
4. Segment engagement trends
5. List health metrics
6. Goals achieved vs. set
7. Goals for next month
```

### ROI Calculation

**Calculate email ROI:**
```
Calculate email marketing ROI for last month:

Inputs:
- Total emails sent: 2,000
- Revenue from email (tracked): $3,500
- Time spent on email marketing: 8 hours
- Tools cost: $50

Calculate:
- Revenue per email sent
- Revenue per subscriber
- Cost per email (time + tools)
- Net profit from email
- ROI percentage
- Compare to industry benchmarks
```

---

## Part 10: Workflow Automation Summary

### Daily Tasks (10 minutes)

```
Run my daily email marketing tasks:

1. Check for new subscribers to welcome
2. Process any unsubscribe requests
3. Check sequence triggers due today
4. Review any campaign performance from yesterday
5. Update engagement scores for active subscribers
```

### Weekly Tasks (30 minutes)

```
Run my weekly email marketing tasks:

1. Plan next week's campaigns
2. Generate newsletter content
3. Update segment assignments
4. Review list health metrics
5. Create A/B test for next campaign
6. Archive completed sequences
```

### Monthly Tasks (1 hour)

```
Run my monthly email marketing review:

1. Generate full performance report
2. Clean list (remove bounces, long-term inactive)
3. Review and update segments
4. Refresh email templates
5. Plan next month's campaign calendar
6. Calculate and report ROI
7. Set goals for next month
```

---

## Quick Reference Card

### Subscriber Management
```
Add subscriber: Add to Subscribers sheet, set segment, start welcome sequence
Remove subscriber: Set Status to Unsubscribed, add to suppression list
Update subscriber: Modify record, recalculate engagement score
```

### Email Creation
```
Newsletter: Use template, personalize, add dynamic content
Promotional: Clear offer, urgency, strong CTA
Sequence: Follow timing, track progress, measure completion
```

### Sending
```
Single: Gmail send_email with HTML body
Batch: Create drafts, review, send manually
Sequence: Track in worksheet, send on schedule
```

### Analysis
```
Campaign: Opens, clicks, unsubscribes, revenue
Subscriber: Engagement score, segment membership
List: Health metrics, growth rate, churn
```

---

## Next Steps

1. **Build foundation**: Create Email Marketing HQ spreadsheet
2. **Import list**: Add existing subscribers with proper fields
3. **Create templates**: Build your core email templates
4. **Setup welcome**: Create and activate welcome sequence
5. **Start sending**: Send your first campaign through the system
6. **Measure**: Track performance and optimize

---

*This guide is part of the Support Forge Academy MCP Mastery series. Email marketing success comes from consistency, personalization, and continuous optimization.*
