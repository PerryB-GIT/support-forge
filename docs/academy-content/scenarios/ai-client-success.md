# AI Client Success Manager

## Overview

**Problem Solved:** Client success teams juggle dozens of accounts, making it impossible to maintain consistent check-ins, track health metrics, and spot at-risk clients before it's too late. The result: reactive fire-fighting instead of proactive relationship building, leading to preventable churn.

**Solution:** An AI client success manager that automates health scoring based on engagement data, schedules regular check-in calls, sends personalized outreach, and generates account intelligence reports - ensuring every client feels valued and issues are caught early.

## Tools Used

| Tool | Purpose |
|------|---------|
| Google Sheets | Client database, health scoring, activity tracking |
| Google Calendar | Check-in scheduling, QBR planning |
| Gmail | Outreach, check-ins, milestone communications |
| Google Drive | Account plans, meeting notes, shared resources |
| Gemini | Health analysis, communication drafting |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                  AI CLIENT SUCCESS MANAGER WORKFLOW                  │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │         CLIENT HEALTH MONITORING         │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Daily: Calculate Client Health Scores            │
              │ - Product usage metrics                          │
              │ - Support ticket volume/sentiment                │
              │ - Engagement (emails opened, calls attended)     │
              │ - Payment status                                 │
              │ - Time since last contact                        │
              │ - NPS/CSAT feedback                              │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ HEALTHY       │           │ AT RISK           │           │ CRITICAL      │
│ Score: 80-100 │           │ Score: 50-79      │           │ Score: <50    │
│               │           │                   │           │               │
│ Action:       │           │ Action:           │           │ Action:       │
│ - Maintain    │           │ - Increase touch  │           │ - Immediate   │
│   cadence     │           │ - Investigate     │           │   outreach    │
│ - Growth      │           │ - Create plan     │           │ - Escalate    │
│   opportunity │           │                   │           │ - Save plan   │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │        PROACTIVE OUTREACH                │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ MILESTONE     │           │ CHECK-IN          │           │ VALUE-ADD     │
│ OUTREACH      │           │ SCHEDULING        │           │ COMMUNICATION │
│               │           │                   │           │               │
│ - Onboarding  │           │ - Monthly touch   │           │ - New feature │
│   complete    │           │ - Quarterly QBR   │           │   announcement│
│ - 30/60/90 day│           │ - Annual review   │           │ - Best practice│
│ - Anniversary │           │ - Renewal prep    │           │ - Industry news│
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │         REPORTING & INSIGHTS             │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ ACCOUNT       │           │ PORTFOLIO         │           │ RENEWAL       │
│ INTELLIGENCE  │           │ OVERVIEW          │           │ FORECAST      │
│               │           │                   │           │               │
│ Per-account   │           │ Weekly summary:   │           │ Upcoming:     │
│ insights for  │           │ - Health trends   │           │ - Renewals    │
│ CSM prep      │           │ - At-risk list    │           │ - Expansion   │
│               │           │ - Wins/losses     │           │ - Risk        │
└───────────────┘           └───────────────────┘           └───────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Client Database

**Sheet 1: Client Master**
| Column | Description |
|--------|-------------|
| A: Client ID | Unique identifier |
| B: Company Name | Client company |
| C: Primary Contact | Main contact name |
| D: Contact Email | Primary email |
| E: Contact Phone | Phone number |
| F: CSM Assigned | Customer Success Manager |
| G: Contract Start | Start date |
| H: Contract End | Renewal date |
| I: MRR/ARR | Monthly/Annual revenue |
| J: Plan Tier | Plan level |
| K: Industry | Client industry |
| L: Use Case | Primary use case |
| M: Health Score | Current score (0-100) |
| N: Health Status | Healthy/At-Risk/Critical |
| O: Last Contact | Date of last meaningful touch |
| P: Next Scheduled | Next planned touchpoint |
| Q: NPS Score | Latest NPS |
| R: Notes | Account notes |

**Sheet 2: Health Score Inputs**
| Column | Description |
|--------|-------------|
| A: Client ID | Reference |
| B: Company | Company name |
| C: Usage Score | Product usage (0-100) |
| D: Support Score | Support health (0-100) |
| E: Engagement Score | Communication engagement (0-100) |
| F: Payment Score | Payment health (0-100) |
| G: Sentiment Score | Feedback sentiment (0-100) |
| H: Recency Score | Time since last contact (0-100) |
| I: Composite Score | Weighted average |
| J: Last Updated | Calculation timestamp |

**Sheet 3: Activity Log**
| Column | Description |
|--------|-------------|
| A: Timestamp | Activity date/time |
| B: Client ID | Reference |
| C: Activity Type | Call/Email/Meeting/Note |
| D: Direction | Inbound/Outbound |
| E: Subject | Topic of activity |
| F: Summary | Brief description |
| G: Outcome | Result |
| H: Next Action | Follow-up needed |
| I: CSM | Who performed |

**Sheet 4: Renewal Tracker**
| Column | Description |
|--------|-------------|
| A: Client ID | Reference |
| B: Company | Company name |
| C: Current ARR | Current annual value |
| D: Renewal Date | Contract end |
| E: Days Until | Days to renewal |
| F: Renewal Status | On Track/At Risk/Lost |
| G: Expansion Opportunity | Upsell potential |
| H: Prep Started | Date started renewal prep |
| I: Last Renewal Touch | Most recent renewal discussion |
| J: Notes | Renewal notes |

### Step 2: Configure Health Scoring

**Workflow: Daily Health Score Calculation**
```yaml
Trigger: Daily 6:00 AM
  │
  ├─ Node 1: Gather Usage Data
  │    - API call to product analytics
  │    - Or manual sheet with usage metrics
  │    - Calculate usage trend (up/down/flat)
  │
  ├─ Node 2: Gather Support Data
  │    - Count open tickets
  │    - Average resolution time
  │    - Sentiment from tickets
  │
  ├─ Node 3: Gather Engagement Data
  │    - Email open rates
  │    - Call attendance
  │    - Meeting participation
  │
  ├─ Node 4: Gather Payment Data
  │    - Payment status (current/late)
  │    - Invoice history
  │
  ├─ Node 5: Calculate Component Scores
  │    - Each factor: 0-100
  │    - Apply weights:
  │      - Usage: 30%
  │      - Support: 20%
  │      - Engagement: 20%
  │      - Payment: 15%
  │      - Sentiment: 15%
  │
  ├─ Node 6: Update Health Scores
  │    - Write to Health Score Inputs
  │    - Update Client Master health status
  │
  └─ Node 7: Trigger Alerts
       - Critical (< 50): Immediate alert to CSM + manager
       - At Risk (50-79): Add to daily at-risk review
       - Healthy (80+): No alert
```

### Step 3: Automated Outreach Scheduling

**Workflow: Check-in Scheduler**
```yaml
Trigger: Weekly Monday 7:00 AM
  │
  ├─ Node 1: Get Clients Needing Attention
  │    - No contact in 30+ days (healthy)
  │    - No contact in 14+ days (at-risk)
  │    - No contact in 7+ days (critical)
  │    - Approaching milestones
  │
  ├─ Node 2: For Each Client
  │    │
  │    ├─ Check CSM Calendar
  │    │    - Find available slots
  │    │    - Consider client timezone
  │    │
  │    └─ Draft Check-in Request
  │         - Personalize based on health
  │         - Reference recent activity
  │         - Include meeting purpose
  │
  ├─ Node 3: Create Calendar Holds
  │    - Tentative events for scheduling
  │    - Include meeting prep time
  │
  └─ Node 4: Notify CSM
       - List of outreach to send
       - Draft emails ready for review
       - Priority ranking
```

**Workflow: Milestone Outreach**
```yaml
Trigger: Daily 8:00 AM
  │
  ├─ Node 1: Check for Milestones
  │    - 30-day anniversary
  │    - 60-day anniversary
  │    - 90-day anniversary
  │    - 1-year anniversary
  │    - Contract anniversary
  │
  ├─ Node 2: Generate Personalized Message
  │    - Acknowledge milestone
  │    - Reference achievements/progress
  │    - Offer value (review, optimization)
  │
  └─ Node 3: Send or Queue
       - High-health: Auto-send
       - Lower-health: Queue for CSM review
```

### Step 4: At-Risk Intervention

**Workflow: At-Risk Response**
```yaml
Trigger: Client health drops to At-Risk or Critical
  │
  ├─ Node 1: Immediate Alert
  │    - Email to assigned CSM
  │    - Include: Current score, trend, factors
  │
  ├─ Node 2: Generate Save Plan Suggestions
  │    - Gemini: Analyze risk factors
  │    - Suggest intervention steps
  │    - Identify quick wins
  │
  ├─ Node 3: Create Intervention Tasks
  │    - Immediate check-in call
  │    - Executive outreach (if critical)
  │    - Product review session
  │
  └─ Node 4: Update Tracking
       - Log intervention start
       - Set review dates
       - Track improvement
```

### Step 5: Reporting Automation

**Workflow: Weekly Portfolio Report**
```yaml
Trigger: Weekly Friday 4:00 PM
  │
  ├─ Node 1: Compile Health Metrics
  │    - Total clients by health status
  │    - Week-over-week changes
  │    - At-risk movements
  │
  ├─ Node 2: Activity Metrics
  │    - Touchpoints this week
  │    - Meetings held
  │    - Outstanding follow-ups
  │
  ├─ Node 3: Renewal Pipeline
  │    - Upcoming renewals (30/60/90 days)
  │    - Renewal risk assessment
  │    - Expansion opportunities
  │
  ├─ Node 4: Gemini Analysis
  │    - Summarize key insights
  │    - Identify patterns
  │    - Recommend focus areas
  │
  └─ Node 5: Distribute Report
       - Email to CS team + leadership
       - Save to Drive
```

## Example Prompts/Commands

### Health Score Analysis
```
Analyze this client's health signals:

Client: [COMPANY_NAME]
Industry: [INDUSTRY]
Plan: [PLAN_TIER]
Contract Value: $[ARR]
Account Age: [MONTHS] months

Health Metrics:
- Product Usage: [METRIC] (trend: [UP/DOWN/FLAT])
- Support Tickets This Month: [COUNT]
- Avg Ticket Sentiment: [POSITIVE/NEUTRAL/NEGATIVE]
- Email Open Rate: [RATE]%
- Last Check-in Call: [DATE]
- NPS Score: [SCORE]
- Payment Status: [CURRENT/LATE]

Provide:
1. Overall health assessment (Healthy/At-Risk/Critical)
2. Key risk factors (top 3)
3. Key strengths (top 3)
4. Recommended immediate actions
5. 30-day improvement plan
6. Talking points for next check-in

Be specific and actionable.
```

### Check-in Email Drafting
```
Draft a check-in email for this client:

Client: [COMPANY_NAME]
Contact: [NAME], [TITLE]
Last Contact: [DATE]
Health Status: [STATUS]
Recent Activity:
- [ACTIVITY_1]
- [ACTIVITY_2]
Account Notes: [NOTES]

Purpose: [ROUTINE CHECK-IN / CONCERN FOLLOW-UP / MILESTONE]

The email should:
1. Be warm but professional
2. Reference something specific about their account
3. Provide value (tip, resource, or offer)
4. Have a clear, easy ask (scheduling call or quick reply)
5. Not sound like a template

Tone: [BASED ON RELATIONSHIP LENGTH AND HEALTH]
Length: 100-150 words
```

### Quarterly Business Review Prep
```
Generate a QBR preparation brief for this client:

Client: [COMPANY_NAME]
Contact: [NAME], [TITLE]
Contract: $[ARR], renews [DATE]
Account Age: [MONTHS] months

Quarter Performance:
- Usage: [SUMMARY]
- ROI/Value Delivered: [IF KNOWN]
- Support Tickets: [COUNT], resolved in [AVG_TIME]
- Key Achievements: [LIST]
- Challenges Faced: [LIST]

Health Trend: [IMPROVING/STABLE/DECLINING]
Current Health Score: [SCORE]

Create a QBR agenda including:
1. Opening (relationship reinforcement)
2. Quarter recap - wins and achievements
3. Usage and adoption insights
4. Challenges and how we addressed them
5. Roadmap preview - what's coming
6. Success planning - next quarter goals
7. Expansion discussion (if appropriate)
8. Open discussion and feedback

For each section, provide:
- Talking points
- Data to reference
- Questions to ask
- Potential concerns to address proactively
```

### Renewal Risk Assessment
```
Assess renewal risk for this client:

Client: [COMPANY_NAME]
Current ARR: $[VALUE]
Renewal Date: [DATE] ([DAYS] days away)
Contract Length: [MONTHS] months

Historical Context:
- Original Sale: [HOW THEY CAME ON]
- Previous Renewals: [SUCCESS/ISSUES]
- Account Growth: [EXPANDED/FLAT/CONTRACTED]

Current State:
- Health Score: [SCORE]
- Usage Trend: [UP/DOWN/FLAT]
- Champion Status: [ACTIVE/QUIET/DEPARTED]
- Decision Maker: [ENGAGED/DISENGAGED]
- Competitive Mentions: [YES/NO]
- Budget Discussions: [ANY_NOTES]

Recent Sentiment:
- Last NPS: [SCORE]
- Recent Feedback: [SUMMARY]
- Support Experience: [GOOD/MIXED/POOR]

Assess:
1. Renewal Probability (High/Medium/Low/At-Risk)
2. Key Risk Factors
3. Mitigating Strengths
4. Recommended Save Actions (if needed)
5. Expansion Opportunity Assessment
6. Competitor Threat Level
7. Decision Timeline Recommendation

Be realistic and specific.
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| Daily 6:00 AM | Calculate health scores | Daily |
| Health score drops 20+ points | Immediate CSM alert | Real-time |
| Client reaches "Critical" status | Alert CSM + manager, create save plan | Real-time |
| No contact in 30 days (healthy) | Prompt CSM for check-in | Daily check |
| No contact in 14 days (at-risk) | Urgent check-in prompt | Daily check |
| Milestone date reached | Send milestone email | Daily |
| 90 days before renewal | Start renewal prep workflow | Daily check |
| 30 days before renewal | Escalate if not engaged | Daily check |
| Weekly Friday 4:00 PM | Portfolio health report | Weekly |
| Monthly (1st) | Account review summaries | Monthly |

## Expected Outcomes

### Quantitative Results
- **Churn reduction:** 25-40% decrease in churn rate
- **CSM efficiency:** 30% more accounts per CSM
- **Response time:** At-risk identified 2-3 weeks earlier
- **Renewal rate:** 10-15% improvement
- **NPS improvement:** +10-20 points

### Qualitative Benefits
- Proactive relationship management
- Consistent client experience
- Data-driven prioritization
- Early warning on at-risk accounts
- Better expansion timing

## ROI Estimate

### Assumptions
- CSM salary: $70,000/year ($35/hour)
- Average ARR per client: $25,000
- Current churn rate: 12%
- Total clients: 100
- Current at-risk identified late: 60%

### Calculation
| Metric | Value |
|--------|-------|
| CSM time saved per week | 8 hours |
| Monthly time savings | 32 hours |
| Monthly labor savings | $1,120 |
| Annual labor savings | $13,440 |
| Churn reduction (12% to 9%) | 3 clients saved |
| ARR saved from reduced churn | $75,000 |
| Tool costs (estimated) | $100/month |
| **Net annual ROI** | **$87,240** |

### Additional Value
- Earlier expansion conversations: +$50,000 revenue
- Higher NPS = more referrals
- Scalability: handle more clients without hiring

## Advanced Extensions

1. **Product Usage Integration:** Direct analytics connection
2. **Executive Business Reviews:** Auto-generated EBR decks
3. **Champion Tracking:** Monitor stakeholder changes
4. **Competitive Intelligence:** Track competitor mentions
5. **Predictive Churn Model:** ML-based risk scoring

## Sample Health Score Formula

```yaml
Health Score Calculation:

Usage Score (30%):
  - Daily Active Users trend
  - Feature adoption breadth
  - Usage depth (time/engagement)
  - Scoring: Above target = 100, At target = 80, Below = 60, Declining = 40

Support Score (20%):
  - Ticket volume vs average
  - Ticket sentiment
  - Resolution satisfaction
  - Scoring: Low volume + positive = 100, Average = 70, High volume + negative = 40

Engagement Score (20%):
  - Email open rate
  - Call attendance
  - Meeting participation
  - Event attendance
  - Scoring: Highly engaged = 100, Moderate = 70, Low = 40

Payment Score (15%):
  - Payment timeliness
  - Invoice disputes
  - Budget discussions
  - Scoring: Always on time = 100, Sometimes late = 70, Frequent issues = 40

Sentiment Score (15%):
  - NPS score
  - Survey responses
  - Qualitative feedback
  - Scoring: Promoter = 100, Passive = 70, Detractor = 40

Composite Score:
  = (Usage * 0.30) + (Support * 0.20) + (Engagement * 0.20) + (Payment * 0.15) + (Sentiment * 0.15)

Health Status:
  - 80-100: Healthy (green)
  - 50-79: At Risk (yellow)
  - 0-49: Critical (red)
```
