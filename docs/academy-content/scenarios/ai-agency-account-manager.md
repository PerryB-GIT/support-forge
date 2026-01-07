# AI Agency Account Manager

## Overview

**Problem Solved:** Agency account managers juggle multiple clients, each with different deliverables, timelines, and communication preferences. Reports are compiled manually, client updates are inconsistent, deliverable tracking is scattered, and too much time goes to administrative tasks instead of strategic client work.

**Solution:** An AI agency account manager that generates automated client reports, tracks deliverables in Sheets, manages client communication via Gmail, and maintains project documentation in Drive - ensuring consistent, professional client management at scale.

## Tools Used

| Tool | Purpose |
|------|---------|
| Google Sheets | Client tracking, deliverable management, metrics |
| Gmail | Client communication, updates, reports |
| Google Drive | Deliverables, client folders, reports |
| Google Calendar | Client meetings, deadline tracking |
| Gemini | Report generation, communication drafting |
| n8n | Workflow orchestration |
| Canva | Report graphics, client presentations |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                 AI AGENCY ACCOUNT MANAGER WORKFLOW                   │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │         CLIENT REPORTING                 │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Automated Report Generation:                     │
              │ - Pull performance data                          │
              │ - Calculate key metrics                          │
              │ - Generate insights                              │
              │ - Create visual report                           │
              │ - Deliver to client                              │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ WEEKLY        │           │ MONTHLY           │           │ QUARTERLY     │
│ UPDATES       │           │ REPORT            │           │ REVIEW        │
│               │           │                   │           │               │
│ - Activity    │           │ - Full metrics    │           │ - Strategy    │
│   summary     │           │ - Performance     │           │   review      │
│ - Quick wins  │           │ - Insights        │           │ - Planning    │
│ - Next week   │           │ - Recommendations │           │ - Roadmap     │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │       DELIVERABLE TRACKING               │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ For Each Client:                                 │
              │ - Track all deliverables                         │
              │ - Monitor deadlines                              │
              │ - Update status                                  │
              │ - Alert on at-risk items                         │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ ON TRACK      │           │ AT RISK           │           │ OVERDUE       │
│               │           │                   │           │               │
│ - Log         │           │ - Alert AM        │           │ - Escalate    │
│ - Continue    │           │ - Reassess        │           │ - Client      │
│               │           │ - Intervene       │           │   communication│
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │       CLIENT COMMUNICATION               │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ PROACTIVE     │           │ REACTIVE          │           │ SCHEDULED     │
│               │           │                   │           │               │
│ - Updates     │           │ - Client          │           │ - Meetings    │
│ - Wins        │           │   inquiries       │           │ - Reports     │
│ - Insights    │           │ - Issues          │           │ - Reviews     │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │        ACCOUNT HEALTH                    │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Monitor:                                         │
              │ - Deliverable completion rate                    │
              │ - Client satisfaction signals                    │
              │ - Communication frequency                        │
              │ - Upsell/expansion opportunities                 │
              │ - Risk indicators                                │
              └─────────────────────────────────────────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Agency Management System

**Sheet 1: Client Master**
| Column | Description |
|--------|-------------|
| A: Client ID | Unique identifier |
| B: Client Name | Company name |
| C: Industry | Client industry |
| D: Primary Contact | Main contact name |
| E: Contact Email | Primary email |
| F: Account Manager | Assigned AM |
| G: Contract Start | Agreement start |
| H: Contract End | Renewal date |
| I: Monthly Retainer | Monthly fee |
| J: Services | Services provided |
| K: Reporting Day | Weekly report day |
| L: Meeting Day | Regular meeting day |
| M: Health Score | Account health (0-100) |
| N: Status | Active/Paused/Churned |
| O: Drive Folder | Client folder link |
| P: Notes | Account notes |

**Sheet 2: Deliverables Tracker**
| Column | Description |
|--------|-------------|
| A: Deliverable ID | Unique identifier |
| B: Client ID | Reference to client |
| C: Client Name | Client name |
| D: Deliverable | What's being delivered |
| E: Type | Blog/Design/Campaign/Report/etc. |
| F: Status | Not Started/In Progress/Review/Complete/Delivered |
| G: Assigned To | Team member responsible |
| H: Due Date | Client deadline |
| I: Internal Due | Internal deadline |
| J: Priority | High/Medium/Low |
| K: Dependencies | Waiting on |
| L: Delivery Link | Link to deliverable |
| M: Client Approved | Approval status |
| N: Notes | Deliverable notes |

**Sheet 3: Client Activity Log**
| Column | Description |
|--------|-------------|
| A: Log ID | Unique identifier |
| B: Client ID | Reference to client |
| C: Date | Activity date |
| D: Type | Meeting/Email/Call/Deliverable/Note |
| E: Summary | Brief description |
| F: Participants | Who was involved |
| G: Outcome | Result/next steps |
| H: Follow-Up | Follow-up needed |
| I: Logged By | Who logged |

**Sheet 4: Performance Metrics**
| Column | Description |
|--------|-------------|
| A: Client ID | Reference to client |
| B: Month | Reporting month |
| C: Metric 1 | Campaign-specific metric |
| D: Metric 2 | Campaign-specific metric |
| E: Metric 3 | Campaign-specific metric |
| F: Goal | Monthly goal |
| G: Actual | Actual performance |
| H: Variance | Performance variance |
| I: Trend | Up/Down/Stable |
| J: Insights | Key observations |

### Step 2: Configure Reporting Automation

**Workflow: Weekly Client Update**
```yaml
Trigger: Weekly (client-specific reporting day)
  │
  ├─ Node 1: Gather Week's Data
  │    - Deliverables completed
  │    - Work in progress
  │    - Key metrics (if applicable)
  │    - Team activity
  │
  ├─ Node 2: Compile Update Content
  │    │
  │    ├─ Completed This Week
  │    │    - Deliverables delivered
  │    │    - Milestones hit
  │    │
  │    ├─ In Progress
  │    │    - Current work status
  │    │    - Expected completions
  │    │
  │    └─ Next Week
  │         - Planned activities
  │         - Any client needs
  │
  ├─ Node 3: Gemini - Generate Summary
  │    - Professional, concise format
  │    - Highlight wins
  │    - Clear next steps
  │
  ├─ Node 4: AM Review
  │    - Draft to AM for quick review
  │    - AM approves or edits
  │
  └─ Node 5: Send to Client
       - Email update
       - CC relevant team
       - Log in Activity Log
```

**Workflow: Monthly Performance Report**
```yaml
Trigger: Monthly (1st business day)
  │
  ├─ Node 1: Collect All Metrics
  │    - Pull from tracking sources
  │    - Calculate month-over-month
  │    - Compare to goals
  │
  ├─ Node 2: Compile Report Data
  │    │
  │    ├─ Executive Summary
  │    │    - Key highlights
  │    │    - Overall performance
  │    │
  │    ├─ Metrics Dashboard
  │    │    - KPI performance
  │    │    - Trends visualization
  │    │
  │    ├─ Deliverables Summary
  │    │    - Completed work
  │    │    - Quality metrics
  │    │
  │    └─ Recommendations
  │         - Insights from data
  │         - Next month priorities
  │
  ├─ Node 3: Gemini - Generate Insights
  │    - Analyze performance patterns
  │    - Identify opportunities
  │    - Draft recommendations
  │
  ├─ Node 4: Create Visual Report
  │    - Canva: Generate report PDF
  │    - Brand-consistent design
  │
  ├─ Node 5: Save to Drive
  │    - Client folder
  │    - Reports subfolder
  │
  └─ Node 6: Deliver Report
       - Email to client
       - Schedule review meeting
       - Log delivery
```

### Step 3: Deliverable Management

**Workflow: Deliverable Tracking**
```yaml
Trigger: Daily 8:00 AM
  │
  ├─ Node 1: Check All Deliverables
  │    - Get all non-complete items
  │    - Calculate days to deadline
  │
  ├─ Node 2: Categorize Status
  │    │
  │    ├─ On Track
  │    │    - Sufficient time remaining
  │    │    - In expected status
  │    │
  │    ├─ At Risk (3 days out, not in final stages)
  │    │    - Alert assigned team member
  │    │    - Alert account manager
  │    │    - Create action plan
  │    │
  │    └─ Overdue
  │         - Immediate escalation
  │         - Client communication needed
  │         - Resolution plan required
  │
  ├─ Node 3: Send AM Summary
  │    - All accounts overview
  │    - At-risk items highlighted
  │    - Action items
  │
  └─ Node 4: Update Tracking
       - Log status checks
       - Note any interventions
```

**Workflow: Deliverable Completion**
```yaml
Trigger: Deliverable status = "Complete" or "Delivered"
  │
  ├─ Node 1: Update Tracking
  │    - Mark as delivered
  │    - Log delivery date
  │
  ├─ Node 2: File Deliverable
  │    - Save to client Drive folder
  │    - Organize by type/date
  │
  ├─ Node 3: If Approval Required
  │    - Email to client for review
  │    - Request approval
  │    - Track response
  │
  └─ Node 4: Log Activity
       - Add to Activity Log
       - Note in weekly update
```

### Step 4: Client Communication Management

**Workflow: Client Email Response Draft**
```yaml
Trigger: Email from client to AM
  │
  ├─ Node 1: Analyze Email
  │    - Identify request/question type
  │    - Extract key points
  │    - Check urgency
  │
  ├─ Node 2: Gather Context
  │    - Recent deliverables
  │    - Current work status
  │    - Past communications
  │
  ├─ Node 3: Gemini - Draft Response
  │    - Address all points raised
  │    - Include relevant updates
  │    - Professional, helpful tone
  │
  ├─ Node 4: Save Draft
  │    - Create Gmail draft
  │    - Alert AM to review
  │
  └─ Node 5: Log Inquiry
       - Add to Activity Log
       - Note for weekly update
```

**Workflow: Proactive Client Outreach**
```yaml
Trigger: No client contact in 7+ days (active clients)
  │
  ├─ Node 1: Gather Update Content
  │    - Recent work completed
  │    - Current progress
  │    - Any wins to share
  │
  ├─ Node 2: Generate Check-In
  │    - Personalized message
  │    - Share progress
  │    - Ask if anything needed
  │
  └─ Node 3: Queue for AM
       - Draft for review
       - AM sends or modifies
```

### Step 5: Account Health Monitoring

**Workflow: Health Score Calculation**
```yaml
Trigger: Weekly Sunday
  │
  ├─ Node 1: Calculate Health Factors
  │    │
  │    ├─ Deliverable Performance (25%)
  │    │    - On-time delivery rate
  │    │    - Revision rate
  │    │
  │    ├─ Communication Health (25%)
  │    │    - Response time
  │    │    - Proactive updates
  │    │    - Meeting attendance
  │    │
  │    ├─ Results Performance (30%)
  │    │    - Goal achievement
  │    │    - Metric trends
  │    │
  │    └─ Relationship Signals (20%)
  │         - Expansion discussions
  │         - Referrals given
  │         - Feedback sentiment
  │
  ├─ Node 2: Calculate Score
  │    - Weighted average
  │    - Trend vs. last period
  │
  ├─ Node 3: Categorize Health
  │    - Healthy (80-100): Maintain/grow
  │    - Watch (60-79): Address issues
  │    - At Risk (<60): Intervention needed
  │
  └─ Node 4: Alert on Changes
       - Notify if score drops 10+
       - Recommend actions
```

## Example Prompts/Commands

### Weekly Update Generation
```
Generate a weekly client update:

Client: [CLIENT_NAME]
Account Manager: [AM_NAME]
Week Ending: [DATE]

Completed This Week:
[LIST_OF_COMPLETED_ITEMS]

In Progress:
[LIST_OF_CURRENT_WORK_WITH_STATUS]

Metrics (if applicable):
[RELEVANT_METRICS]

Next Week Planned:
[UPCOMING_WORK]

Any Issues/Blockers:
[ISSUES_IF_ANY]

Create an update email that:
1. Opens with a quick win or positive highlight
2. Summarizes completed work concisely
3. Shows progress on ongoing items
4. Previews next week's focus
5. Notes any items needing client input
6. Ends with clear next steps or call to action

Tone: [CLIENT_PREFERRED_TONE: Professional/Casual/Technical]
Length: Keep under 300 words
Format: Easy to scan with bullets
```

### Monthly Report Executive Summary
```
Generate an executive summary for a monthly report:

Client: [CLIENT_NAME]
Month: [MONTH]
Services: [SERVICES_PROVIDED]

Performance Metrics:
[TABLE_OF_METRICS_WITH_GOALS_AND_ACTUALS]

Deliverables Completed:
[LIST_OF_DELIVERABLES]

Key Wins:
[NOTABLE_ACHIEVEMENTS]

Challenges:
[ANY_ISSUES_ENCOUNTERED]

Create an executive summary that:
1. Opens with the bottom-line performance assessment
2. Highlights 2-3 key wins in business terms
3. Addresses any underperformance honestly
4. Shows trend direction (improving/stable/declining)
5. Provides 2-3 actionable recommendations
6. Sets expectations for next month

Length: 200-250 words
Tone: Strategic, results-focused
Include: One clear call-to-action for next steps
```

### Client Response Draft
```
Draft a response to this client email:

Client: [CLIENT_NAME]
Their Email: "[CLIENT_EMAIL_CONTENT]"

Account Context:
- Current project status: [STATUS]
- Recent deliverables: [LIST]
- Any known issues: [ISSUES]
- Relationship history: [CONTEXT]

Draft a response that:
1. Addresses each point/question raised
2. Provides specific, helpful information
3. Sets clear expectations (timelines, next steps)
4. Maintains our service standards
5. Opens door for follow-up if needed

Tone: Match client's style, default to [PROFESSIONAL/FRIENDLY]
Include: Any relevant attachments or links to reference
Flag: Any items requiring AM decision before sending
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| Client-specific reporting day | Send weekly update | Weekly |
| 1st business day of month | Generate monthly report | Monthly |
| Deliverable due in 3 days | At-risk alert | Daily |
| Deliverable overdue | Escalation | Real-time |
| Client email received | Draft response | Real-time |
| No contact in 7 days | Proactive outreach | Daily check |
| Sunday evening | Calculate health scores | Weekly |
| Health score drops 10+ | Alert AM | Real-time |
| Contract renewal 60 days out | Renewal prep reminder | Daily check |

## Expected Outcomes

### Quantitative Results
- **Reporting time:** 80% reduction
- **Update consistency:** 100% (never miss an update)
- **Client response time:** 50% faster
- **Deliverable tracking:** Real-time visibility
- **Account manager capacity:** Handle 30% more accounts

### Qualitative Benefits
- Consistent, professional client experience
- Proactive account management
- Early warning on account issues
- Better client retention
- More time for strategic work

## ROI Estimate

### Assumptions
- Account Manager salary: $65,000/year ($32.50/hour)
- Time on reporting/admin: 15 hours/week per AM
- Post-automation admin: 6 hours/week
- Average accounts per AM: 10
- Client retention improvement: 10%
- Average client value: $5,000/month

### Calculation
| Metric | Value |
|--------|-------|
| Weekly time saved per AM | 9 hours |
| Monthly time saved | 36 hours |
| Monthly labor savings | $1,170 |
| Clients retained from better service (1) | $5,000/month |
| Monthly value per AM | $6,170 |
| Annual value per AM | $74,040 |
| Tool costs (estimated) | $100/month |
| **Net annual ROI per AM** | **$72,840** |

### Additional Value
- Capacity to take on more clients
- Better client referrals
- Reduced churn costs
- Improved team satisfaction

## Advanced Extensions

1. **Client Portal:** Self-service deliverable viewing
2. **Multi-Channel Reporting:** Aggregate from ads, analytics, etc.
3. **Upsell Identification:** AI-spotted expansion opportunities
4. **Team Workload Balancing:** Optimize across AMs
5. **Competitive Intelligence:** Track client industry news

## Sample Drive Structure

```
/Clients/
└── [Client_Name]/
    ├── 00_Account_Info/
    │   ├── Contract.pdf
    │   ├── Brand_Guidelines.pdf
    │   └── Kickoff_Notes.docx
    ├── 01_Strategy/
    │   ├── Initial_Strategy.pdf
    │   └── Quarterly_Plans/
    ├── 02_Deliverables/
    │   ├── [Year]/
    │   │   ├── [Month]/
    │   │   │   ├── Blog_Posts/
    │   │   │   ├── Designs/
    │   │   │   ├── Campaigns/
    │   │   │   └── Other/
    ├── 03_Reports/
    │   ├── Weekly_Updates/
    │   ├── Monthly_Reports/
    │   └── Quarterly_Reviews/
    ├── 04_Communications/
    │   └── Key_Emails/
    └── 05_Assets/
        ├── Logos/
        ├── Images/
        └── Templates/
```

## Sample Health Score Calculation

```yaml
Account Health Score (0-100):

Deliverable Performance (25 points):
  On-time rate:
    - 100%: 25 points
    - 90-99%: 20 points
    - 80-89%: 15 points
    - 70-79%: 10 points
    - <70%: 5 points

Communication Health (25 points):
  Response time (avg):
    - <2 hours: 10 points
    - <4 hours: 8 points
    - <24 hours: 5 points
    - >24 hours: 2 points

  Update consistency:
    - Never missed: 10 points
    - Rarely missed: 7 points
    - Sometimes missed: 3 points

  Meeting attendance (client):
    - Always attends: 5 points
    - Usually attends: 3 points
    - Often reschedules: 1 point

Results Performance (30 points):
  Goal achievement:
    - Exceeding goals: 30 points
    - Meeting goals: 25 points
    - Slightly under: 15 points
    - Significantly under: 5 points

Relationship Signals (20 points):
  Expansion conversations: 0-5 points
  Referrals given: 0-5 points
  Feedback sentiment: 0-10 points

Total: Sum of all categories

Interpretation:
  - 80-100: Healthy (expand, upsell)
  - 60-79: Watch (monitor, address issues)
  - 40-59: At Risk (intervention needed)
  - <40: Critical (leadership involvement)
```
