# Client Report Generator

A Claude Code skill that generates professional client status reports by aggregating project data, metrics, and activities.

## Trigger

Invoke with: `/client-report` or `/report`

## Description

This skill creates comprehensive client reports by:
1. Fetching project metrics and KPIs
2. Compiling completed deliverables
3. Summarizing timeline progress
4. Highlighting upcoming milestones
5. Generating executive summary

## Input

Required:
- `client` - Client name or ID

Optional:
- `--period week|month|quarter` - Reporting period (default: month)
- `--format pdf|html|markdown` - Output format (default: markdown)
- `--include-metrics` - Include detailed metrics section
- `--executive-only` - Generate executive summary only
- `--send` - Send report via email to client

Example:
```
/client-report "Acme Corp" --period month --include-metrics
```

## Workflow

### Step 1: Load Client Context
```
1. Look up client in CRM/tracking sheet
2. Identify active projects
3. Fetch client preferences (report format, contacts)
4. Load previous report for comparison
```

### Step 2: Gather Project Data
```
For each active project:
- Fetch task completion status
- Calculate milestone progress
- Gather time tracking data
- Collect any blockers or risks
```

### Step 3: Compile Metrics
```
Aggregate key metrics:
- Tasks completed vs planned
- Hours utilized vs budgeted
- Sprint velocity (if applicable)
- SLA/KPI performance
- Trend vs previous period
```

### Step 4: Summarize Activities
```
Create activity log:
- Major deliverables completed
- Key decisions made
- Meetings and touchpoints
- Change requests processed
```

### Step 5: Analyze Status
```
Determine overall health:
- On track / At risk / Needs attention
- Budget status (green/yellow/red)
- Timeline status (green/yellow/red)
- Identify top 3 accomplishments
- Flag key concerns
```

### Step 6: Generate Report
```
Compile all sections into formatted report
Apply client-specific branding if configured
Generate export in requested format
```

## Output Format

### Markdown Report
```markdown
# Client Status Report

**Client:** Acme Corporation
**Period:** December 1-31, 2024
**Prepared by:** [Your Name]
**Date:** January 5, 2025

---

## Executive Summary

Overall project status is **ON TRACK**. This month we completed the user authentication module and began work on the reporting dashboard. Key metrics show 94% task completion rate and we remain within budget.

### Key Highlights
- Launched user authentication to production
- Completed 23 of 24 planned tasks
- Zero critical bugs in production
- On track for Q1 milestone

### Attention Items
- API documentation delayed by 3 days
- Additional scope requested for mobile views

---

## Project Status

### Website Redesign
| Metric | Status | Details |
|--------|--------|---------|
| Progress | 72% | On track |
| Budget | $18,500 / $25,000 | 74% utilized |
| Timeline | On schedule | Launch Feb 15 |

**Completed This Period:**
- Homepage design finalized
- 5 interior page templates
- Mobile responsive framework
- CMS integration

**In Progress:**
- Blog section development
- Contact form integration
- SEO implementation

**Next Period:**
- Complete blog section
- Client training sessions
- Launch preparation

---

## Deliverables

| Deliverable | Status | Date |
|-------------|--------|------|
| Homepage Design | Delivered | Dec 5 |
| Brand Guidelines | Delivered | Dec 12 |
| Content Migration | In Progress | Est. Jan 15 |
| Training Materials | Pending | Est. Jan 20 |

---

## Metrics & KPIs

### Task Completion
- Planned: 24 tasks
- Completed: 23 tasks
- Completion Rate: 96%
- Trend: +4% vs last month

### Time Utilization
- Budgeted: 80 hours
- Utilized: 74 hours
- Efficiency: 92%

### Quality Metrics
- Bugs Reported: 3
- Bugs Resolved: 3
- Average Resolution Time: 1.2 days

---

## Timeline

```
[============================>         ] 72%

Nov 1        Dec 31       Jan 31       Feb 15
Start        Current      Milestone    Launch
```

### Upcoming Milestones
| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Beta Launch | Jan 31 | On Track |
| Client Training | Feb 7 | Scheduled |
| Go Live | Feb 15 | On Track |

---

## Budget Summary

| Category | Budget | Spent | Remaining |
|----------|--------|-------|-----------|
| Design | $8,000 | $7,200 | $800 |
| Development | $12,000 | $8,500 | $3,500 |
| QA/Testing | $3,000 | $1,800 | $1,200 |
| PM/Admin | $2,000 | $1,000 | $1,000 |
| **Total** | **$25,000** | **$18,500** | **$6,500** |

---

## Risks & Concerns

| Risk | Severity | Mitigation |
|------|----------|------------|
| API delay | Medium | Parallel work streams |
| Scope creep | Low | Change request process |

---

## Next Period Goals

1. Complete blog section development
2. Finalize content migration
3. Begin QA testing cycle
4. Schedule client training

---

## Action Items

| Item | Owner | Due |
|------|-------|-----|
| Review blog design | Client | Jan 10 |
| Provide final content | Client | Jan 12 |
| Complete integration | [Your Team] | Jan 20 |

---

*Report generated automatically. For questions, contact [your-email@company.com]*
```

## Configuration

Create a `.client-report-config.json`:

```json
{
  "company_name": "Your Company",
  "company_logo": "https://...",
  "default_period": "month",
  "default_format": "markdown",
  "clients_sheet_id": "YOUR_SHEET_ID",
  "projects_sheet_id": "YOUR_SHEET_ID",
  "time_tracking_sheet_id": "YOUR_SHEET_ID",
  "include_budget": true,
  "include_timeline_visual": true,
  "send_email_on_generate": false,
  "email_template": "professional"
}
```

## Client Data Structure

Expected columns in Clients sheet:
```
Client ID | Company | Contact | Email | Active Projects | Report Frequency | Last Report
```

Expected columns in Projects sheet:
```
Project ID | Client ID | Name | Status | Budget | Spent | Start Date | End Date | Progress %
```

## Dependencies

### Required MCP Servers
- `zapier` - For Google Sheets access

### Optional
- Gmail MCP for sending reports
- Google Drive for file storage
- Time tracking integration

## Error Handling

| Error | Handling |
|-------|----------|
| Client not found | Prompt for client selection |
| No project data | Generate structure with placeholders |
| Missing metrics | Note "Data not available" |
| Send failed | Save locally, retry option |

## Examples

### Monthly Report
```
> /client-report "Acme Corp"

Loading client data...
Found 2 active projects
Gathering metrics for December...

Generated report saved to:
./reports/acme-corp-december-2024.md

Would you like to send this to the client?
```

### Quick Executive Summary
```
> /client-report "Acme Corp" --executive-only

## Executive Summary - Acme Corp

Status: ON TRACK
Progress: 72% complete
Budget: 74% utilized ($18,500 / $25,000)

Highlights:
- User auth launched successfully
- 96% task completion rate
- On track for Feb 15 launch

Concerns:
- API documentation delayed 3 days

Next milestone: Beta Launch (Jan 31)
```

## Related Skills

- `/invoice-summary` - Generate billing summary
- `/project-status` - Quick project status check
- `/weekly-update` - Weekly progress update
- `/client-dashboard` - Interactive client metrics
