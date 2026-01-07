# AI Ad Campaign Manager

## Overview

**Problem Solved:** Digital advertising requires constant monitoring, optimization, and reporting. Campaign managers spend hours checking performance, adjusting budgets, updating audiences, and compiling reports. Slow reactions to underperforming ads waste budget, while delayed reporting frustrates stakeholders.

**Solution:** An AI ad campaign manager that monitors Google Ads performance in real-time, automatically flags underperforming campaigns, manages audience lists, and generates comprehensive performance reports - ensuring maximum ROI from ad spend.

## Tools Used

| Tool | Purpose |
|------|---------|
| Google Ads | Campaign management, audience updates, reporting |
| Google Sheets | Performance tracking, benchmarks, analysis |
| Gmail | Alerts, reports, stakeholder updates |
| Google Drive | Report storage, historical data |
| Gemini | Performance analysis, recommendation generation |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                   AI AD CAMPAIGN MANAGER WORKFLOW                    │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │        PERFORMANCE MONITORING            │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Hourly: Pull Campaign Performance Data           │
              │ - Impressions, Clicks, CTR                       │
              │ - Conversions, CPA, ROAS                         │
              │ - Spend vs Budget                                │
              │ - Quality Score changes                          │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ PERFORMING    │           │ NEEDS ATTENTION   │           │ CRITICAL      │
│ Above KPIs    │           │ Slightly off      │           │ Major issue   │
│               │           │                   │           │               │
│ Action:       │           │ Action:           │           │ Action:       │
│ - Log data    │           │ - Flag for review │           │ - Pause/Alert │
│ - Continue    │           │ - Minor adjust    │           │ - Immediate   │
│               │           │                   │           │   notification│
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │         AUDIENCE MANAGEMENT              │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ NEW CUSTOMERS │           │ REMARKETING       │           │ EXCLUSIONS    │
│               │           │ LISTS             │           │               │
│ Add from CRM: │           │ Update from:      │           │ Add:          │
│ - Leads       │           │ - Site visitors   │           │ - Converters  │
│ - Purchases   │           │ - Email opens     │           │ - Bounces     │
│ - Sign-ups    │           │ - Engagers        │           │ - Complaints  │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │           REPORTING ENGINE               │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ DAILY BRIEF   │           │ WEEKLY REPORT     │           │ MONTHLY       │
│ - Spend       │           │ - Performance     │           │ ANALYSIS      │
│ - Conversions │           │   trends          │           │ - Deep dive   │
│ - Key issues  │           │ - Top campaigns   │           │ - Strategy    │
│               │           │ - Recommendations │           │ - Forecast    │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │         BUDGET OPTIMIZATION              │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Daily Analysis:                                  │
              │ - Identify over/under-spending campaigns         │
              │ - Calculate optimal budget distribution          │
              │ - Flag reallocation opportunities                │
              │ - Generate recommendations                       │
              └─────────────────────────────────────────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Performance Tracking Sheets

**Sheet 1: Campaign Tracker**
| Column | Description |
|--------|-------------|
| A: Date | Performance date |
| B: Campaign ID | Google Ads campaign ID |
| C: Campaign Name | Campaign name |
| D: Campaign Type | Search/Display/Shopping/Video |
| E: Status | Enabled/Paused |
| F: Budget | Daily budget |
| G: Spend | Actual spend |
| H: Impressions | Total impressions |
| I: Clicks | Total clicks |
| J: CTR | Click-through rate |
| K: CPC | Cost per click |
| L: Conversions | Total conversions |
| M: Conv Rate | Conversion rate |
| N: CPA | Cost per acquisition |
| O: Conv Value | Conversion value |
| P: ROAS | Return on ad spend |
| Q: Quality Score | Average QS |
| R: Performance | Good/Fair/Poor |

**Sheet 2: KPI Benchmarks**
| Column | Description |
|--------|-------------|
| A: Campaign Type | Campaign category |
| B: Target CTR | Minimum CTR |
| C: Target CPA | Maximum CPA |
| D: Target ROAS | Minimum ROAS |
| E: Target Conv Rate | Minimum conversion rate |
| F: Budget Threshold | Daily spend alert |
| G: Quality Score Min | Minimum QS acceptable |

**Sheet 3: Audience Lists**
| Column | Description |
|--------|-------------|
| A: List ID | Google Ads list ID |
| B: List Name | Audience name |
| C: List Type | Remarketing/Customer Match/Similar |
| D: Size | Current list size |
| E: Last Updated | Update timestamp |
| F: Status | Active/Paused |
| G: Source | Where data comes from |

**Sheet 4: Alert Log**
| Column | Description |
|--------|-------------|
| A: Timestamp | When alert triggered |
| B: Campaign | Affected campaign |
| C: Alert Type | Spend/Performance/Quality |
| D: Severity | Critical/Warning/Info |
| E: Description | What happened |
| F: Action Taken | What was done |
| G: Resolved | Yes/No |

### Step 2: Configure Performance Monitoring

**Workflow: Hourly Performance Check**
```yaml
Trigger: Hourly during business hours
  │
  ├─ Node 1: Pull Campaign Data
  │    - Google Ads: Get all enabled campaigns
  │    - Get today's performance metrics
  │    - Get yesterday's comparison
  │
  ├─ Node 2: Compare Against Benchmarks
  │    - For each campaign:
  │    - Check CTR vs target
  │    - Check CPA vs target
  │    - Check ROAS vs target
  │    - Check spend vs budget
  │
  ├─ Node 3: Classify Performance
  │    - Good: All KPIs met
  │    - Fair: 1-2 KPIs off
  │    - Poor: 3+ KPIs off
  │
  ├─ Node 4: Log to Tracker Sheet
  │    - Update daily row
  │    - Add performance classification
  │
  └─ Node 5: Trigger Alerts (if needed)
       - Poor performance: Email alert
       - Overspend: Immediate notification
       - Quality Score drop: Flag for review
```

**Workflow: Critical Alert Handler**
```yaml
Trigger: Performance check identifies critical issue
  │
  ├─ Node 1: Assess Severity
  │    - CPA > 2x target: Critical
  │    - ROAS < 50% target: Critical
  │    - Spend > 120% budget: Critical
  │    - 0 conversions (spend > $50): Warning
  │
  ├─ Node 2: Log Alert
  │    - Add to Alert Log sheet
  │    - Include all relevant metrics
  │
  ├─ Node 3: Send Notification
  │    - Email to campaign manager
  │    - Include: Issue, metrics, recommendation
  │
  └─ Node 4: Optional Auto-Action
       - If enabled: Pause campaign
       - Log action taken
```

### Step 3: Audience Management Automation

**Workflow: Customer List Sync**
```yaml
Trigger: Daily 2:00 AM
  │
  ├─ Node 1: Get New Customers
  │    - Query CRM/Sheet for new customers
  │    - Get email addresses (hashed)
  │    - Filter for marketing consent
  │
  ├─ Node 2: Add to Customer Match
  │    - Google Ads: Add to customer list
  │    - Handle duplicates
  │    - Track additions
  │
  ├─ Node 3: Update Exclusion List
  │    - Add recent converters
  │    - Add unsubscribes
  │    - Add bounced emails
  │
  └─ Node 4: Log Updates
       - Update Audience Lists sheet
       - Note list sizes
       - Track sync status
```

### Step 4: Reporting Automation

**Workflow: Daily Brief**
```yaml
Trigger: Daily 8:00 AM
  │
  ├─ Node 1: Compile Yesterday's Data
  │    - Total spend
  │    - Total conversions
  │    - Top 3 campaigns
  │    - Bottom 3 campaigns
  │    - Any alerts triggered
  │
  ├─ Node 2: Compare to Previous Day
  │    - Spend change %
  │    - Conversion change %
  │    - CPA trend
  │
  ├─ Node 3: Gemini Summary
  │    - Key highlights
  │    - Issues to address
  │    - Recommendations
  │
  └─ Node 4: Send Brief
       - Email to stakeholders
       - Clean, scannable format
```

**Workflow: Weekly Report**
```yaml
Trigger: Weekly Monday 9:00 AM
  │
  ├─ Node 1: Compile Weekly Metrics
  │    - All campaigns performance
  │    - Week-over-week trends
  │    - Budget utilization
  │    - Top performers analysis
  │
  ├─ Node 2: Create Visualization Data
  │    - Spend trend chart data
  │    - Conversion trend chart data
  │    - Campaign comparison table
  │
  ├─ Node 3: Gemini Analysis
  │    - Executive summary
  │    - Key insights
  │    - Optimization recommendations
  │    - Budget reallocation suggestions
  │
  ├─ Node 4: Generate Report Document
  │    - Create Google Doc
  │    - Save to Drive
  │
  └─ Node 5: Distribute
       - Email report link
       - Key highlights in email body
```

### Step 5: Budget Optimization Workflow

**Workflow: Budget Analysis**
```yaml
Trigger: Daily 6:00 AM
  │
  ├─ Node 1: Analyze Spend Distribution
  │    - Campaign spend vs performance
  │    - Calculate efficiency (Conv/$)
  │    - Identify high/low performers
  │
  ├─ Node 2: Calculate Optimal Distribution
  │    - If high performer is limited by budget
  │    - If low performer is overspending
  │    - Calculate reallocation opportunity
  │
  ├─ Node 3: Generate Recommendations
  │    - Specific budget changes
  │    - Expected impact
  │    - Risk assessment
  │
  └─ Node 4: Send Recommendation
       - Email to campaign manager
       - Include data and rationale
       - Link to full analysis
```

## Example Prompts/Commands

### Daily Performance Analysis
```
Analyze yesterday's Google Ads performance:

Total Spend: $[SPEND]
Total Conversions: [COUNT]
Average CPA: $[CPA]
Average ROAS: [ROAS]x

Campaign Performance:
[TABLE: Campaign, Spend, Conv, CPA, ROAS, CTR]

Benchmarks:
- Target CPA: $[TARGET_CPA]
- Target ROAS: [TARGET_ROAS]x
- Target CTR: [TARGET_CTR]%

Provide:
1. Performance summary (3 sentences)
2. Top 2 performing campaigns and why
3. Bottom 2 performing campaigns and issues
4. Immediate actions needed (if any)
5. Budget reallocation opportunity (if any)

Keep it concise - this is for morning briefing.
```

### Weekly Report Generation
```
Generate a comprehensive weekly Google Ads report:

Reporting Period: [DATE_RANGE]
Total Budget: $[BUDGET]
Total Spend: $[SPEND]

Weekly Performance:
[DETAILED METRICS TABLE]

Week-over-Week Comparison:
- Spend: [CHANGE]%
- Conversions: [CHANGE]%
- CPA: [CHANGE]%
- ROAS: [CHANGE]%

Campaign Breakdown:
[CAMPAIGN BY CAMPAIGN DATA]

Alerts Triggered This Week:
[LIST OF ALERTS]

Create a report with:
1. Executive Summary (5 sentences max)
2. Key Performance Table with trends
3. Top 3 Wins this week
4. Top 3 Challenges this week
5. Specific Optimization Recommendations (3-5)
6. Budget Reallocation Suggestions
7. Forecast for Next Week

Format for executive readability.
```

### Optimization Recommendations
```
Based on this campaign performance data, recommend optimizations:

Campaign: [CAMPAIGN_NAME]
Type: [SEARCH/DISPLAY/SHOPPING]
Current Performance:
- Daily Budget: $[BUDGET]
- Avg Daily Spend: $[SPEND]
- CTR: [CTR]%
- CPC: $[CPC]
- Conversions: [COUNT]
- CPA: $[CPA]
- ROAS: [ROAS]x
- Quality Score: [QS]

Targets:
- CPA Goal: $[TARGET_CPA]
- ROAS Goal: [TARGET_ROAS]x

Top Keywords:
[TOP 5 KEYWORDS WITH METRICS]

Worst Keywords:
[BOTTOM 5 KEYWORDS WITH METRICS]

Provide specific recommendations for:
1. Keywords to pause (with justification)
2. Keywords to increase bids (with suggested %)
3. Keywords to decrease bids (with suggested %)
4. New negative keywords to add
5. Ad copy improvements (if applicable)
6. Budget adjustment recommendation
7. Audience targeting adjustments

Be specific and actionable.
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| Hourly during business hours | Performance check | Hourly |
| CPA exceeds 2x target | Critical alert + pause option | Real-time |
| ROAS drops below 50% target | Warning alert | Real-time |
| Daily spend exceeds budget | Overspend alert | Real-time |
| Quality Score drops 2+ points | QS alert | Daily check |
| Daily 2:00 AM | Audience list sync | Daily |
| Daily 8:00 AM | Daily performance brief | Daily |
| Weekly Monday 9:00 AM | Weekly performance report | Weekly |
| Monthly (1st) | Monthly deep-dive analysis | Monthly |
| Campaign status changes | Log and notify | Real-time |

## Expected Outcomes

### Quantitative Results
- **Monitoring frequency:** Hourly (vs. daily manual)
- **Alert response time:** Under 1 hour (vs. next day)
- **Reporting time saved:** 5+ hours/week
- **Wasted spend reduction:** 15-25% improvement
- **ROAS improvement:** 10-20% from faster optimization

### Qualitative Benefits
- Never miss critical performance issues
- Consistent, professional reporting
- Data-driven optimization decisions
- Better stakeholder confidence
- More time for strategy vs. admin

## ROI Estimate

### Assumptions
- Campaign Manager salary: $65,000/year ($32.50/hour)
- Monthly ad spend: $50,000
- Current waste from slow optimization: 10% of spend
- Post-automation waste reduction: to 3%
- Time on monitoring/reporting: 15 hours/week
- Post-automation time: 5 hours/week

### Calculation
| Metric | Value |
|--------|-------|
| Weekly time saved | 10 hours |
| Monthly time saved | 40 hours |
| Monthly labor savings | $1,300 |
| Monthly ad waste reduction (7%) | $3,500 |
| Monthly total savings | $4,800 |
| Annual savings | $57,600 |
| Tool costs (estimated) | $150/month |
| **Net annual ROI** | **$55,800** |

### Additional Value
- Better ROAS from faster optimization
- Improved client/stakeholder relationships
- Reduced stress from manual monitoring
- Competitive advantage from real-time response

## Advanced Extensions

1. **Automated Bidding Adjustments:** Programmatic bid changes based on rules
2. **A/B Test Automation:** Automatic winner selection and scaling
3. **Cross-Platform Integration:** Include Meta Ads, LinkedIn Ads
4. **Attribution Analysis:** Multi-touch attribution reporting
5. **Competitor Monitoring:** Auction insights tracking and alerts

## Sample Alert Thresholds

```yaml
Critical Alerts (Immediate Action):
  - CPA > 200% of target
  - ROAS < 50% of target
  - Daily spend > 120% of budget before noon
  - 0 conversions with > $100 spend
  - Quality Score drops to < 5

Warning Alerts (Review Within 24hrs):
  - CPA > 130% of target
  - ROAS < 80% of target
  - CTR drops > 30% vs previous week
  - Quality Score drops 2+ points
  - Conversion rate drops > 25%

Info Alerts (Include in Daily Brief):
  - Budget nearly exhausted (> 90%)
  - New keyword entered top 3
  - Campaign hit conversion goal
  - Audience list size milestone
```
