# AI Support Agent

## Overview

**Problem Solved:** Customer support teams are overwhelmed with repetitive inquiries, leading to slow response times, inconsistent answers, and frustrated customers. Support agents spend 60% of their time on routine questions that could be automated, leaving complex issues backlogged.

**Solution:** An AI support agent that automatically triages incoming tickets via Gmail, drafts responses to common questions, escalates complex issues appropriately, and maintains a knowledge base in Sheets - delivering faster, more consistent customer support.

## Tools Used

| Tool | Purpose |
|------|---------|
| Gmail | Ticket intake, response sending, threading |
| Google Sheets | Ticket tracking, knowledge base, response templates |
| Google Drive | Documentation, macros, policies |
| Gemini | Intent classification, response drafting, sentiment analysis |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                      AI SUPPORT AGENT WORKFLOW                       │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │           TICKET INTAKE                  │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Trigger: New email to support@company.com        │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Gemini Analysis:                                 │
              │ - Classify intent (billing, technical, general)  │
              │ - Assess urgency (low, medium, high, critical)   │
              │ - Detect sentiment (positive, neutral, negative) │
              │ - Identify customer type (new, existing, VIP)    │
              │ - Extract key details                            │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ TIER 1        │           │ TIER 2            │           │ TIER 3        │
│ Auto-Response │           │ Draft + Review    │           │ Escalation    │
│               │           │                   │           │               │
│ Common FAQs:  │           │ Complex issues:   │           │ Critical:     │
│ - Password    │           │ - Multi-step      │           │ - VIP account │
│ - Billing Q   │           │ - Unusual case    │           │ - Legal       │
│ - How-to      │           │ - Needs research  │           │ - Security    │
│ - Status      │           │                   │           │ - Angry (high)│
└───────┬───────┘           └─────────┬─────────┘           └───────┬───────┘
        │                             │                             │
        ▼                             ▼                             ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ Send response │           │ Draft response    │           │ Create urgent │
│ immediately   │           │ for agent review  │           │ ticket, alert │
│ + log ticket  │           │ + flag for action │           │ senior team   │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │          TICKET MANAGEMENT               │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ For All Tickets:                                 │
              │ - Log to Ticket Tracker sheet                    │
              │ - Assign ticket ID                               │
              │ - Set SLA deadline                               │
              │ - Track response time                            │
              │ - Update status through lifecycle                │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ SLA Monitoring:                                  │
              │ - Approaching deadline: Alert agent              │
              │ - Exceeded deadline: Escalate to manager         │
              │ - Follow-up needed: Auto-reminder                │
              └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │        FOLLOW-UP & RESOLUTION            │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ Customer      │           │ No Response       │           │ Issue         │
│ Responds      │           │ (24-48 hrs)       │           │ Resolved      │
│               │           │                   │           │               │
│ - Re-analyze  │           │ - Send follow-up  │           │ - Close ticket│
│ - Continue    │           │ - Check if solved │           │ - Send CSAT   │
│   thread      │           │ - Final close     │           │ - Log metrics │
└───────────────┘           └───────────────────┘           └───────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Ticket Tracking System

**Sheet 1: Ticket Tracker**
| Column | Description |
|--------|-------------|
| A: Ticket ID | Unique identifier (auto-generated) |
| B: Created | Timestamp received |
| C: Customer Email | Sender email |
| D: Customer Name | Extracted or looked up |
| E: Customer Type | New/Existing/VIP |
| F: Subject | Email subject |
| G: Category | Billing/Technical/General/Sales |
| H: Urgency | Low/Medium/High/Critical |
| I: Sentiment | Positive/Neutral/Negative |
| J: Status | Open/Pending/Resolved/Closed |
| K: Assigned To | Support agent |
| L: SLA Deadline | Response due by |
| M: First Response | Time of first response |
| N: Resolution Time | Time to resolve |
| O: Response Type | Auto/Draft/Manual |
| P: CSAT Score | Customer satisfaction (1-5) |
| Q: Thread Link | Gmail thread link |
| R: Notes | Agent notes |

**Sheet 2: Knowledge Base**
| Column | Description |
|--------|-------------|
| A: KB ID | Knowledge base article ID |
| B: Category | Article category |
| C: Question/Topic | The question or topic covered |
| D: Keywords | Search keywords |
| E: Answer | Full response |
| F: Short Answer | Brief version for quick replies |
| G: Links | Related documentation |
| H: Last Updated | When last reviewed |
| I: Usage Count | Times used |
| J: Effectiveness | Resolution rate |

**Sheet 3: Response Templates**
| Column | Description |
|--------|-------------|
| A: Template ID | Unique identifier |
| B: Name | Template name |
| C: Category | When to use |
| D: Subject Line | Email subject template |
| E: Body | Email body template |
| F: Variables | Placeholders used |
| G: Tone | Formal/Friendly/Apologetic |

**Sheet 4: Team Performance**
| Column | Description |
|--------|-------------|
| A: Agent | Agent name |
| B: Tickets Handled | Total tickets |
| C: Avg Response Time | Average first response |
| D: Avg Resolution Time | Average close time |
| E: CSAT Average | Customer satisfaction |
| F: Auto-Response Rate | % handled by AI |
| G: Escalation Rate | % escalated |

### Step 2: Configure Email Intake

**Workflow: Ticket Triage**
```yaml
Trigger: Gmail - New email to support@company.com
  │
  ├─ Node 1: Check for Thread
  │    - If reply to existing thread:
  │    - Find existing ticket
  │    - Update status to "Pending"
  │    - Skip to analysis
  │
  ├─ Node 2: Extract Details
  │    - Sender email
  │    - Subject line
  │    - Body content
  │    - Attachments (note if present)
  │
  ├─ Node 3: Lookup Customer
  │    - Check customer database
  │    - Determine: New/Existing/VIP
  │    - Get purchase history if exists
  │
  ├─ Node 4: Gemini Analysis
  │    - Classify intent/category
  │    - Assess urgency
  │    - Analyze sentiment
  │    - Extract key details
  │    - Match to knowledge base
  │
  ├─ Node 5: Create Ticket
  │    - Generate ticket ID
  │    - Log to Tracker sheet
  │    - Set SLA based on urgency
  │
  └─ Node 6: Route Ticket
       - Tier 1 (FAQ): Auto-respond
       - Tier 2 (Complex): Draft for review
       - Tier 3 (Critical): Escalate immediately
```

### Step 3: Auto-Response System

**Workflow: Tier 1 Auto-Response**
```yaml
Trigger: Ticket routed to Tier 1
  │
  ├─ Node 1: Match to Knowledge Base
  │    - Find best matching KB article
  │    - Confidence threshold: 85%
  │
  ├─ Node 2: Personalize Response
  │    - Get customer name
  │    - Insert KB answer
  │    - Add relevant links
  │    - Include ticket reference
  │
  ├─ Node 3: Generate Final Email
  │    - Apply appropriate template
  │    - Set professional tone
  │    - Add signature
  │
  ├─ Node 4: Send Response
  │    - Reply to original email
  │    - Maintain thread
  │
  └─ Node 5: Update Ticket
       - Status: "Pending Customer"
       - First Response Time: [timestamp]
       - Response Type: "Auto"
       - Schedule follow-up check
```

**Workflow: Tier 2 Draft + Review**
```yaml
Trigger: Ticket routed to Tier 2
  │
  ├─ Node 1: Research Issue
  │    - Search knowledge base
  │    - Check for similar past tickets
  │    - Gather relevant context
  │
  ├─ Node 2: Draft Response
  │    - Gemini: Create response based on:
  │    - Issue details
  │    - KB articles
  │    - Customer context
  │    - Company policies
  │
  ├─ Node 3: Create Draft in Gmail
  │    - Save as draft reply
  │    - Add [REVIEW NEEDED] prefix
  │
  ├─ Node 4: Notify Agent
  │    - Email alert with ticket details
  │    - Include draft preview
  │    - Link to Gmail draft
  │
  └─ Node 5: Update Ticket
       - Status: "Awaiting Review"
       - Assigned To: [agent]
       - Add review deadline
```

### Step 4: Escalation Handling

**Workflow: Tier 3 Escalation**
```yaml
Trigger: Ticket identified as Critical
  │
  ├─ Node 1: Immediate Logging
  │    - Flag as CRITICAL in sheet
  │    - Record escalation reason
  │
  ├─ Node 2: Alert Senior Team
  │    - Email to support manager
  │    - Include: Customer info, issue, urgency
  │    - CC: Account manager (if VIP)
  │
  ├─ Node 3: Send Acknowledgment
  │    - Quick reply to customer
  │    - Confirm receipt
  │    - Set expectation for response
  │
  └─ Node 4: Create Task
       - High-priority task for team
       - Add to manager's action items
       - Schedule check-in reminder
```

### Step 5: SLA Monitoring

**Workflow: SLA Tracker**
```yaml
Trigger: Every 30 minutes
  │
  ├─ Node 1: Check Open Tickets
  │    - Get all tickets with Status != Closed
  │    - Calculate time since creation
  │
  ├─ Node 2: Compare to SLA
  │    - Critical: 1 hour
  │    - High: 4 hours
  │    - Medium: 8 hours
  │    - Low: 24 hours
  │
  ├─ Node 3: For Approaching SLA
  │    - 30 mins before: Alert assigned agent
  │
  └─ Node 4: For Exceeded SLA
       - Alert agent + manager
       - Flag in tracker
       - Update escalation status
```

## Example Prompts/Commands

### Ticket Classification
```
Analyze this customer support email:

From: [EMAIL]
Subject: [SUBJECT]
Body: [BODY]

Customer context:
- Account status: [ACTIVE/INACTIVE]
- Customer since: [DATE]
- Past tickets: [COUNT]
- VIP status: [YES/NO]

Classify this ticket:

1. Category (choose one):
   - Billing (payments, invoices, refunds)
   - Technical (product issues, bugs, errors)
   - Account (login, settings, access)
   - Sales (pricing, upgrades, features)
   - General (other questions)

2. Urgency (choose one):
   - Critical (service down, security, VIP angry)
   - High (blocking issue, important deadline)
   - Medium (significant inconvenience)
   - Low (general question, minor issue)

3. Sentiment:
   - Positive / Neutral / Negative / Angry

4. Key Details:
   - Main issue (1 sentence)
   - Specific request (if any)
   - Missing information needed

5. Suggested Routing:
   - Tier 1 (FAQ/Auto): If common question with KB match
   - Tier 2 (Draft): If needs research or nuance
   - Tier 3 (Escalate): If critical or sensitive

6. Recommended KB Articles:
   - [List matching articles if any]

Format as JSON.
```

### Response Drafting
```
Draft a support response for this ticket:

Customer Issue:
[ISSUE_DESCRIPTION]

Category: [CATEGORY]
Sentiment: [SENTIMENT]
Customer Type: [NEW/EXISTING/VIP]

Relevant KB Article:
[KB_CONTENT]

Additional Context:
[ANY_RELEVANT_INFO]

Requirements:
1. Match the customer's communication style
2. Be [empathetic/direct] based on sentiment
3. Provide clear, actionable steps
4. Include any relevant links
5. Offer additional help if needed
6. Professional but warm tone

If information is missing, note what to ask for.
If escalation is needed, note why.

Length: Appropriate to issue complexity (typically 100-200 words)
```

### Knowledge Base Search
```
Find the best matching knowledge base answer for this query:

Customer Question: "[CUSTOMER_QUESTION]"

Available KB Topics:
[LIST_OF_KB_ARTICLES_WITH_KEYWORDS]

Return:
1. Best matching article (with confidence %)
2. Second best match (if applicable)
3. If no good match: Indicate this needs manual response
4. Suggested response based on match

If match confidence > 85%, this can be auto-responded.
If 60-85%, draft for review.
If < 60%, route to human.
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| New email to support@ | Triage and route ticket | Real-time |
| Reply from customer | Update ticket, re-analyze | Real-time |
| 30 min before SLA | Alert assigned agent | Every 30 min |
| SLA exceeded | Escalate to manager | Every 30 min |
| Ticket idle 24 hrs | Send follow-up | Daily check |
| Ticket idle 48 hrs | Auto-close check | Daily check |
| Ticket resolved | Send CSAT survey | Real-time |
| Daily 8:00 AM | Daily ticket summary | Daily |
| Weekly Monday | Team performance report | Weekly |

## Expected Outcomes

### Quantitative Results
- **First response time:** Under 5 minutes for Tier 1 (vs. 4+ hours)
- **Auto-resolution rate:** 40-50% of tickets
- **Agent productivity:** 3x more tickets per agent
- **SLA compliance:** 95%+ (vs. 70%)
- **CSAT improvement:** +15% from faster responses

### Qualitative Benefits
- Consistent response quality
- 24/7 initial response coverage
- Reduced agent burnout on repetitive queries
- Better escalation handling
- Knowledge base continuously improving

## ROI Estimate

### Assumptions
- Support agent salary: $45,000/year ($22.50/hour)
- Team size: 3 agents
- Current ticket volume: 500/month
- Current time per ticket: 15 minutes average
- Post-automation time: 5 minutes (for non-auto tickets)
- Auto-resolution rate: 45%

### Calculation
| Metric | Value |
|--------|-------|
| Tickets auto-resolved | 225/month |
| Time saved (225 x 15 min) | 56 hours/month |
| Remaining tickets faster | 37 hours saved |
| Total monthly time saved | 93 hours |
| Monthly labor savings | $2,092 |
| Annual labor savings | $25,104 |
| Capacity increase | 200+ more tickets/month |
| Tool costs (estimated) | $75/month |
| **Net annual ROI** | **$24,204** |

### Additional Value
- Faster response = higher customer retention
- Reduced churn from support delays: ~$10,000/year
- Scalability without hiring: ~$45,000/year (1 FTE)
- **Total potential value: $79,000+/year**

## Advanced Extensions

1. **Sentiment Trend Analysis:** Track customer mood patterns
2. **Proactive Support:** Detect issues before tickets come in
3. **Multi-Channel:** Add chat, social media intake
4. **Self-Service Enhancement:** Auto-update FAQ from tickets
5. **Agent Coaching:** AI suggestions for improvement

## Sample Knowledge Base Structure

```yaml
Categories:
  Billing:
    - Payment Methods
    - Invoice Questions
    - Refund Policy
    - Subscription Management
    - Pricing Changes

  Technical:
    - Getting Started
    - Common Errors
    - Integration Issues
    - Performance Problems
    - Feature How-Tos

  Account:
    - Password Reset
    - Login Issues
    - Account Settings
    - Team Management
    - Permissions

  General:
    - Contact Information
    - Company Policies
    - Feature Requests
    - Partnership Inquiries

Article Template:
  Title: [Question/Topic]
  Keywords: [search, terms, here]
  Short Answer: [1-2 sentences for quick reply]
  Full Answer: [Complete explanation with steps]
  Related Links: [Documentation, videos, etc.]
  Last Updated: [Date]
  Owner: [Team member responsible]
```

## Sample SLA Configuration

```yaml
SLA Levels:
  Critical:
    - First Response: 1 hour
    - Resolution Target: 4 hours
    - Escalation: Immediate to manager
    - Examples: Service outage, security issue, VIP complaint

  High:
    - First Response: 4 hours
    - Resolution Target: 24 hours
    - Escalation: 2 hours before deadline
    - Examples: Blocking issue, important customer

  Medium:
    - First Response: 8 hours
    - Resolution Target: 48 hours
    - Escalation: 4 hours before deadline
    - Examples: Significant issue, normal customers

  Low:
    - First Response: 24 hours
    - Resolution Target: 72 hours
    - Escalation: 8 hours before deadline
    - Examples: General questions, non-urgent inquiries
```
