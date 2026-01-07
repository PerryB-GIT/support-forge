# AI Project Manager

## Overview

**Problem Solved:** Development teams lose 20% of productivity to project coordination overhead - status update meetings, task tracking, deadline chasing, and stakeholder communication. Project managers spend more time reporting than actually managing.

**Solution:** An AI project manager that automatically tracks GitHub activity, updates project sheets, manages calendar events for milestones, and generates stakeholder reports - keeping everyone aligned without constant manual updates.

## Tools Used

| Tool | Purpose |
|------|---------|
| GitHub | Issue tracking, PR monitoring, code activity |
| Google Sheets | Project tracking, resource allocation, metrics |
| Google Calendar | Sprint events, milestones, deadline reminders |
| Gmail | Stakeholder updates, team notifications |
| Gemini | Status summarization, risk analysis |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AI PROJECT MANAGER WORKFLOW                       │
└─────────────────────────────────────────────────────────────────────┘

                         ┌─────────────────┐
                         │  GitHub Repo    │
                         └────────┬────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        ▼                         ▼                         ▼
┌───────────────┐         ┌───────────────┐         ┌───────────────┐
│ Issue Created │         │ PR Opened/    │         │ Issue Closed/ │
│ or Updated    │         │ Merged        │         │ Milestone Hit │
└───────┬───────┘         └───────┬───────┘         └───────┬───────┘
        │                         │                         │
        ▼                         ▼                         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    Update Project Tracker Sheet                      │
│  - Task status      - Assignee       - Time logged                  │
│  - Sprint progress  - Dependencies   - Blockers                     │
└─────────────────────────────────────────────────────────────────────┘
        │
        ├────────────────────────────────────────────┐
        ▼                                            ▼
┌─────────────────────┐                    ┌─────────────────────┐
│ Check Deadlines     │                    │ Calculate Metrics   │
│ - Overdue tasks     │                    │ - Velocity          │
│ - At-risk items     │                    │ - Burndown          │
│ - Upcoming due      │                    │ - Cycle time        │
└─────────┬───────────┘                    └─────────────────────┘
          │
          ▼
┌─────────────────────┐
│ Risk Detected?      │
└─────────┬───────────┘
     Yes  │
          ▼
┌─────────────────────┐         ┌─────────────────────┐
│ Send Alert Email    │────────▶│ Create Calendar     │
│ to Team/Stakeholder │         │ Reminder Event      │
└─────────────────────┘         └─────────────────────┘

                    SCHEDULED WORKFLOWS

┌─────────────────────────────────────────────────────────────────────┐
│ Daily (9 AM): Team standup summary email                            │
│ Weekly (Monday): Sprint planning prep + stakeholder report          │
│ Bi-weekly (Sprint end): Retrospective data + velocity report        │
└─────────────────────────────────────────────────────────────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Project Tracking Sheet

**Sheet 1: Sprint Backlog**
| Column | Description |
|--------|-------------|
| A: Issue # | GitHub issue number |
| B: Title | Task title |
| C: Type | Bug/Feature/Task/Spike |
| D: Status | To Do/In Progress/Review/Done |
| E: Assignee | Team member |
| F: Story Points | Effort estimate |
| G: Sprint | Sprint number |
| H: Priority | P0/P1/P2/P3 |
| I: Created | Date created |
| J: Started | Date work began |
| K: Completed | Date completed |
| L: Cycle Time | Days from start to complete |
| M: Blocked | Yes/No |
| N: Blocker Reason | Description of blocker |
| O: GitHub Link | Direct link to issue |

**Sheet 2: Sprint Metrics**
- Sprint burndown data
- Velocity by sprint
- Issue type distribution
- Team capacity utilization

**Sheet 3: Team Capacity**
- Team member availability
- Current workload
- Skills matrix

### Step 2: Configure GitHub Integration

**GitHub Webhook Events to Monitor:**
- `issues` - opened, closed, assigned, labeled
- `pull_request` - opened, closed, merged, review_requested
- `issue_comment` - created (for blockers/updates)
- `project_card` - moved (board column changes)

### Step 3: Create Automation Workflows

**Workflow 1: Issue Sync**
```yaml
Trigger: GitHub - New/Updated Issue
  │
  ├─ Node 1: Parse Issue Data
  │    - Extract: number, title, labels, assignee, milestone
  │
  ├─ Node 2: Map Status from Labels
  │    - "in-progress" → In Progress
  │    - "needs-review" → Review
  │    - "blocked" → Blocked flag = Yes
  │
  ├─ Node 3: Google Sheets - Lookup
  │    - Find row by Issue #
  │    - If not found, create new row
  │
  └─ Node 4: Google Sheets - Update
       - Update status, assignee, labels
       - Log timestamp for tracking
```

**Workflow 2: PR Activity Tracker**
```yaml
Trigger: GitHub - PR Event
  │
  ├─ Node 1: Get Linked Issues
  │    - Parse PR body for "Fixes #123" or "Closes #123"
  │
  ├─ Node 2: Update Issue Status
  │    - PR opened → "In Review"
  │    - PR merged → "Done"
  │
  └─ Node 3: Calculate Cycle Time
       - If status = Done, compute days since Started
```

**Workflow 3: Daily Standup Summary**
```yaml
Trigger: Schedule - Daily 9:00 AM
  │
  ├─ Node 1: Query Sheets
  │    - Get all "In Progress" items
  │    - Get items completed yesterday
  │    - Get blocked items
  │
  ├─ Node 2: Gemini - Generate Summary
  │    - Format as standup-style update
  │
  └─ Node 3: Gmail - Send to Team
       - Subject: "Daily Standup: [DATE]"
```

**Workflow 4: Risk Detection**
```yaml
Trigger: Schedule - Every 2 hours
  │
  ├─ Node 1: Check Deadline Risks
  │    - Tasks due within 2 days with status != Done
  │    - Tasks in "In Progress" > 5 days
  │    - Blockers unresolved > 1 day
  │
  ├─ Node 2: If Risks Found
  │    - Compile risk report
  │
  ├─ Node 3: Gmail - Alert Notification
  │    - Send to PM and relevant assignee
  │
  └─ Node 4: Calendar - Create Reminder
       - 15-min sync event for next morning
```

### Step 4: Weekly Stakeholder Reports

**Automated Monday Report:**
1. Pull sprint progress from Sheets
2. Query GitHub for key metrics
3. Generate executive summary with Gemini
4. Email to stakeholder distribution list

## Example Prompts/Commands

### Daily Standup Generation
```
Generate a team standup summary from this data:

**Completed Yesterday:**
[LIST OF COMPLETED ITEMS]

**In Progress Today:**
[LIST OF CURRENT WORK]

**Blocked:**
[LIST OF BLOCKERS]

Format as a brief, scannable email. Highlight any risks or items needing attention.
Keep it under 200 words. Use bullet points. Include issue numbers as links.
```

### Sprint Report Generation
```
Create a sprint summary report:

Sprint: [NUMBER]
Sprint Goal: [GOAL]
Duration: [START_DATE] to [END_DATE]

Metrics:
- Planned: [X] story points
- Completed: [Y] story points
- Velocity: [Z]%
- Bugs found: [N]
- PRs merged: [M]

Completed Items:
[LIST]

Rolled Over:
[LIST]

Generate:
1. Executive summary (3 sentences)
2. Key achievements
3. Challenges faced
4. Recommendations for next sprint
5. Team recognition (who delivered exceptional work)
```

### Risk Analysis Prompt
```
Analyze this project data for risks:

Current Sprint Progress: [X]%
Days Remaining: [N]
Velocity Trend: [UP/DOWN/STABLE]
Current Blockers: [LIST]
Overdue Items: [LIST]

Identify:
1. Delivery risks (will we hit the deadline?)
2. Resource risks (team capacity issues?)
3. Technical risks (complex items still pending?)
4. Dependency risks (waiting on external factors?)

For each risk, provide:
- Severity (High/Medium/Low)
- Mitigation recommendation
- Escalation suggestion if needed
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| GitHub issue created | Add to sprint backlog sheet | Real-time |
| GitHub issue closed | Mark complete, calculate cycle time | Real-time |
| GitHub PR merged | Update linked issues to Done | Real-time |
| Issue labeled "blocked" | Alert PM, create followup event | Real-time |
| Daily 9:00 AM | Generate standup summary email | Daily |
| Monday 8:00 AM | Sprint kickoff report | Weekly |
| Friday 4:00 PM | End of week status report | Weekly |
| Sprint end date | Retrospective data package | Bi-weekly |
| Task overdue | Escalation notification | Daily check |

## Expected Outcomes

### Quantitative Results
- **Meeting time reduced:** 3-5 hours/week saved on status updates
- **Reporting time saved:** 4 hours/week on manual report creation
- **Issue tracking accuracy:** 100% sync between GitHub and sheets
- **Risk detection:** Issues flagged 2-3 days earlier on average

### Qualitative Benefits
- Real-time visibility into project health
- Consistent, professional stakeholder communication
- Early warning system for blockers and delays
- Data-driven sprint planning
- Reduced "where are we on X?" questions

## ROI Estimate

### Assumptions
- PM salary: $80,000/year ($40/hour)
- Developer salary: $100,000/year ($50/hour)
- Team size: 5 developers + 1 PM
- Current weekly overhead: PM 10hrs, each dev 2hrs

### Calculation
| Metric | Value |
|--------|-------|
| PM time saved | 7 hours/week |
| Dev time saved (5 x 1.5hr) | 7.5 hours/week |
| PM weekly savings | $280 |
| Dev weekly savings | $375 |
| Monthly savings | $2,620 |
| Annual savings | $31,440 |
| Tool costs (estimated) | $100/month |
| **Net annual ROI** | **$30,240** |

### Additional Value
- Faster delivery from reduced blockers: ~$5,000/year
- Better stakeholder satisfaction: retained business value
- Improved sprint predictability: better planning = less crunch

## Advanced Extensions

1. **Slack Integration:** Post updates to team channels
2. **Resource Forecasting:** AI predicts capacity needs based on velocity
3. **Dependency Mapping:** Visualize and track cross-team dependencies
4. **Retro Insights:** AI analyzes patterns across sprints for improvement areas
5. **Client Portal:** Auto-generated progress dashboard for client access

## Sample Sheet Formulas

### Velocity Calculation
```
=SUMIFS('Sprint Backlog'!F:F, 'Sprint Backlog'!G:G, [Sprint#], 'Sprint Backlog'!D:D, "Done")
```

### Cycle Time Average
```
=AVERAGEIFS('Sprint Backlog'!L:L, 'Sprint Backlog'!G:G, [Sprint#], 'Sprint Backlog'!L:L, ">0")
```

### Burndown Chart Data
```
=SUMIFS('Sprint Backlog'!F:F, 'Sprint Backlog'!G:G, [Sprint#]) - SUMIFS('Sprint Backlog'!F:F, 'Sprint Backlog'!G:G, [Sprint#], 'Sprint Backlog'!K:K, "<="&[DATE])
```
