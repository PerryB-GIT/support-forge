# AI Sales Assistant

## Overview

**Problem Solved:** Sales reps spend only 35% of their time actually selling. The rest goes to data entry, lead research, follow-up scheduling, and CRM updates. Hot leads go cold, follow-ups are missed, and valuable selling time is lost to administrative tasks.

**Solution:** An AI sales assistant that automatically tracks leads in Google Sheets, sends personalized follow-up sequences via Gmail, schedules meetings via Calendar, and provides daily pipeline intelligence - ensuring no opportunity falls through the cracks.

## Tools Used

| Tool | Purpose |
|------|---------|
| Google Sheets | CRM/lead database, pipeline tracking, reports |
| Gmail | Follow-up sequences, outreach, notifications |
| Google Calendar | Meeting scheduling, follow-up reminders |
| Google Drive | Proposals, contracts, sales materials |
| Gemini | Email personalization, lead research, analysis |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                      AI SALES ASSISTANT WORKFLOW                     │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │            LEAD MANAGEMENT               │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ New Lead      │           │ Lead Status       │           │ Lead Activity │
│ Added         │           │ Changed           │           │ Detected      │
│ (Form/Manual) │           │                   │           │ (Email Reply) │
└───────┬───────┘           └─────────┬─────────┘           └───────┬───────┘
        │                             │                             │
        ▼                             ▼                             ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                          UPDATE LEAD DATABASE                              │
│  - Contact info      - Lead score        - Activity log                   │
│  - Company details   - Next action       - Communication history          │
└───────────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    AUTOMATED FOLLOW-UP ENGINE                        │
└─────────────────────────────────────────────────────────────────────┘
        │
        ├─────────────────────────────────────────────────────────────┐
        ▼                                                             ▼
┌─────────────────────┐                                    ┌─────────────────┐
│ SEQUENCE AUTOMATION │                                    │ MEETING BOOKING │
│                     │                                    │                 │
│ Day 0: Initial      │                                    │ When: Lead says │
│        outreach     │                                    │ "let's talk"    │
│ Day 3: Follow-up #1 │                                    │                 │
│ Day 7: Value add    │                                    │ Action:         │
│ Day 14: Check-in    │                                    │ - Parse request │
│ Day 21: Break-up    │                                    │ - Check calendar│
│                     │                                    │ - Propose times │
└─────────────────────┘                                    │ - Create event  │
                                                           └─────────────────┘

                    ┌─────────────────────────────────────────┐
                    │          PIPELINE INTELLIGENCE           │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ Daily         │           │ Weekly Pipeline   │           │ At-Risk       │
│ Task List     │           │ Report            │           │ Deal Alerts   │
│ - Follow-ups  │           │ - By stage        │           │ - Stale leads │
│ - Meetings    │           │ - Forecast        │           │ - No activity │
│ - Proposals   │           │ - Win rate        │           │ - Due dates   │
└───────────────┘           └───────────────────┘           └───────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Sales CRM Sheet

**Sheet 1: Lead Database**
| Column | Description |
|--------|-------------|
| A: Lead ID | Unique identifier |
| B: Company | Company name |
| C: Contact Name | Primary contact |
| D: Email | Contact email |
| E: Phone | Contact phone |
| F: Title | Contact's role |
| G: Source | How they found us |
| H: Status | New/Contacted/Qualified/Proposal/Negotiation/Won/Lost |
| I: Deal Value | Estimated deal size |
| J: Lead Score | 1-100 based on fit and engagement |
| K: Created Date | When lead was added |
| L: Last Contact | Most recent interaction |
| M: Next Action | Scheduled next step |
| N: Next Action Date | When to take action |
| O: Assigned To | Sales rep |
| P: Notes | Context and history |
| Q: Sequence Stage | Current email sequence step |
| R: Meeting Scheduled | Yes/No |

**Sheet 2: Activity Log**
| Column | Description |
|--------|-------------|
| A: Timestamp | When activity occurred |
| B: Lead ID | Reference to lead |
| C: Type | Email/Call/Meeting/Note |
| D: Direction | Inbound/Outbound |
| E: Subject | Email subject or call topic |
| F: Summary | Brief description |
| G: Outcome | Result of activity |
| H: Rep | Who performed action |

**Sheet 3: Pipeline Dashboard**
- Leads by stage
- Revenue by stage
- Conversion rates
- Rep performance
- Monthly trends

### Step 2: Configure Lead Intake

**Workflow: New Lead Processing**
```yaml
Trigger: Google Sheets - New row OR Form submission
  │
  ├─ Node 1: Validate Data
  │    - Check for required fields
  │    - Dedupe against existing leads
  │
  ├─ Node 2: Enrich Lead Data
  │    - Gemini: Research company
  │    - Find company size, industry
  │    - Identify potential use case
  │
  ├─ Node 3: Calculate Lead Score
  │    - Company size: +10-30 points
  │    - Industry fit: +10-20 points
  │    - Role seniority: +10-20 points
  │    - Source quality: +10-20 points
  │
  ├─ Node 4: Update Sheet
  │    - Add enriched data
  │    - Set initial status
  │    - Set lead score
  │
  ├─ Node 5: Assign Rep
  │    - Round-robin or territory-based
  │
  └─ Node 6: Start Sequence
       - Add to email sequence
       - Schedule first touchpoint
```

### Step 3: Email Sequence Automation

**Workflow: Follow-Up Sequence**
```yaml
Trigger: Schedule - Every 2 hours during business hours
  │
  ├─ Node 1: Query Leads
  │    - Status = New OR Contacted
  │    - Next Action Date <= Today
  │    - Sequence Stage < 5 (not completed)
  │
  ├─ Node 2: For Each Lead
  │    │
  │    ├─ Check for Replies
  │    │    - If replied, pause sequence
  │    │    - Move to "Engaged" status
  │    │
  │    └─ Generate Personalized Email
  │         - Gemini: Create email based on:
  │         - Sequence stage (1-5)
  │         - Company info
  │         - Previous interactions
  │
  ├─ Node 3: Send Email
  │    - Via Gmail
  │    - Track in Activity Log
  │
  └─ Node 4: Update Lead
       - Increment Sequence Stage
       - Set Next Action Date
       - Update Last Contact
```

### Step 4: Meeting Booking Automation

**Workflow: Meeting Request Handler**
```yaml
Trigger: Gmail - Reply from lead
  │
  ├─ Node 1: Analyze Reply
  │    - Gemini: Determine intent
  │    - Meeting request?
  │    - Question?
  │    - Objection?
  │    - Not interested?
  │
  ├─ Node 2: If Meeting Request
  │    │
  │    ├─ Check Calendar Availability
  │    │    - Next 5 business days
  │    │    - Preferred meeting slots
  │    │
  │    ├─ Generate Response
  │    │    - Propose 3 time options
  │    │    - Include calendar booking link
  │    │
  │    └─ Update Lead
  │         - Status = "Meeting Scheduled"
  │         - Pause sequence
  │
  └─ Node 3: If Other Intent
       - Flag for sales rep review
       - Draft suggested response
```

### Step 5: Pipeline Intelligence

**Workflow: Daily Sales Brief**
```yaml
Trigger: Daily 7:00 AM
  │
  ├─ Node 1: Gather Data
  │    - Today's scheduled follow-ups
  │    - Today's meetings
  │    - Hot leads (score > 80)
  │    - Stale leads (no contact > 7 days)
  │    - Deals closing this week
  │
  ├─ Node 2: Gemini Analysis
  │    - Summarize pipeline health
  │    - Identify top priorities
  │    - Flag at-risk deals
  │
  └─ Node 3: Send Brief
       - Personalized email per rep
       - Action items highlighted
```

## Example Prompts/Commands

### Initial Outreach Email
```
Write a cold outreach email for a sales lead:

Company: [COMPANY_NAME]
Industry: [INDUSTRY]
Contact: [NAME], [TITLE]
Company Size: [SIZE]
Our Product: [BRIEF_DESCRIPTION]
Value Proposition: [KEY_BENEFIT]

The email should:
1. Reference something specific about their company (no generic flattery)
2. Identify a pain point relevant to their role
3. Connect our solution to their likely challenge
4. Include a clear, low-commitment CTA
5. Be under 150 words
6. Sound human, not salesy

Tone: Professional but conversational. No buzzwords.
```

### Follow-Up Email Sequence
```
Generate follow-up email #[NUMBER] of 5 for this lead:

Previous emails sent:
[SUMMARY_OF_PREVIOUS_EMAILS]

Lead info:
- Company: [COMPANY]
- Contact: [NAME]
- Industry: [INDUSTRY]
- Time since first email: [DAYS] days
- No response yet

Email sequence strategy:
1. Initial outreach (Day 0)
2. Value-add follow-up (Day 3)
3. Social proof/case study (Day 7)
4. Different angle/new insight (Day 14)
5. Friendly break-up email (Day 21)

Generate email #[NUMBER] following this strategy.
Keep it short (under 100 words). Include a specific question to drive response.
```

### Meeting Request Response
```
A lead has replied to schedule a meeting:

Their message: "[REPLY_TEXT]"

Lead context:
- Company: [COMPANY]
- Role: [TITLE]
- Deal value: $[VALUE]
- What they're interested in: [INTEREST]

My availability for the next week:
[AVAILABLE_SLOTS]

Generate a response that:
1. Thanks them for their interest
2. Confirms what we'll cover in the meeting
3. Proposes 3 specific times
4. Includes my calendar booking link: [LINK]
5. Is warm and professional

Keep it under 100 words.
```

### Daily Brief Generation
```
Generate a daily sales brief from this data:

Today's Date: [DATE]
Rep: [NAME]

Pipeline Summary:
- Total leads: [COUNT]
- By stage: [BREAKDOWN]
- Total pipeline value: $[VALUE]

Today's Tasks:
- Follow-ups due: [LIST]
- Meetings scheduled: [LIST]
- Proposals to send: [LIST]

Alerts:
- Stale leads (>7 days no contact): [LIST]
- High-value deals at risk: [LIST]
- Deals closing this week: [LIST]

Create a brief, actionable email that:
1. Starts with one key priority for the day
2. Lists top 3 actions with expected outcomes
3. Highlights any urgent items
4. Includes a motivational one-liner

Keep it scannable - use bullets and bold for key items.
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| New lead added to sheet | Enrich, score, and assign | Real-time |
| Lead replies to email | Analyze intent, pause/adjust sequence | Real-time |
| Sequence step due | Send personalized follow-up | Every 2 hours |
| Meeting request detected | Check availability, propose times | Real-time |
| Deal stage changed | Update pipeline metrics, notify team | Real-time |
| Daily 7:00 AM | Send rep daily brief | Daily |
| Weekly Monday 8:00 AM | Pipeline review report | Weekly |
| Lead no contact > 7 days | Stale lead alert | Daily check |
| Deal close date approaching | Reminder notification | Daily check |
| Meeting completed | Request meeting notes entry | Event-based |

## Expected Outcomes

### Quantitative Results
- **Selling time increased:** From 35% to 60% of day
- **Follow-up compliance:** 100% (vs. 40% manual)
- **Lead response time:** Under 5 minutes (vs. 6+ hours)
- **Meetings booked:** 2x increase
- **Pipeline visibility:** Real-time (vs. weekly manual updates)

### Qualitative Benefits
- No leads fall through the cracks
- Consistent, professional communication
- Personalized outreach at scale
- Data-driven prioritization
- Reduced administrative burden on reps

## ROI Estimate

### Assumptions
- Sales rep salary: $75,000/year ($37.50/hour)
- 5 reps on team
- Current admin time: 4 hours/day each
- Post-automation admin: 1 hour/day each
- Average deal value: $10,000
- Current close rate: 15%

### Calculation
| Metric | Value |
|--------|-------|
| Time saved per rep per day | 3 hours |
| Weekly time saved (team) | 75 hours |
| Monthly time savings | 300 hours |
| Monthly labor value saved | $11,250 |
| Annual labor savings | $135,000 |
| Additional deals from faster follow-up (est. 10%) | 12 deals/year |
| Revenue from additional deals | $120,000 |
| Tool costs (estimated) | $200/month |
| **Net annual ROI** | **$252,600** |

## Advanced Extensions

1. **LinkedIn Integration:** Enrich leads with LinkedIn data
2. **Call Recording Analysis:** Summarize and extract action items
3. **Proposal Generation:** Auto-create proposals from templates
4. **Win/Loss Analysis:** AI analysis of closed deals for insights
5. **Territory Optimization:** Suggest optimal lead distribution

## Sample Lead Scoring Matrix

```yaml
Company Size:
  - Enterprise (1000+): +30 points
  - Mid-market (100-999): +20 points
  - SMB (10-99): +10 points
  - Startup (<10): +5 points

Industry Fit:
  - Target industry: +20 points
  - Adjacent industry: +10 points
  - Other: +0 points

Role Seniority:
  - C-level: +25 points
  - VP/Director: +20 points
  - Manager: +15 points
  - Individual contributor: +5 points

Engagement Signals:
  - Requested demo: +20 points
  - Downloaded content: +10 points
  - Visited pricing page: +15 points
  - Email opened: +5 points
  - Email clicked: +10 points
  - Replied to email: +25 points

Source Quality:
  - Referral: +25 points
  - Inbound demo request: +20 points
  - Content download: +10 points
  - Purchased list: +5 points

Score Interpretation:
  - 80-100: Hot lead - prioritize immediately
  - 60-79: Warm lead - active outreach
  - 40-59: Nurture - stay in touch
  - <40: Low priority - minimal effort
```
