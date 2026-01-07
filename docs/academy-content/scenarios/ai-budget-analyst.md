# AI Budget Analyst

## Overview

**Problem Solved:** Finance teams spend excessive time manually categorizing expenses, tracking budget variances, and creating reports. Spreadsheet-based budgets quickly become outdated, variance analysis happens too late to take action, and stakeholders lack real-time visibility into financial health.

**Solution:** An AI budget analyst that automatically categorizes expenses in Google Sheets, tracks budget versus actual in real-time, identifies variances and trends, and generates variance reports with actionable insights - enabling proactive financial management.

## Tools Used

| Tool | Purpose |
|------|---------|
| Google Sheets | Budget tracking, expense categorization, reports |
| Gmail | Alerts, budget notifications, stakeholder reports |
| Google Drive | Report storage, documentation |
| Gemini | Expense analysis, trend identification, recommendations |
| n8n | Workflow orchestration |
| Code by Zapier | Calculations, data transformations |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                      AI BUDGET ANALYST WORKFLOW                      │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │       EXPENSE CATEGORIZATION             │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Trigger: New expense entry added                 │
              │ (Manual or imported from bank/card)              │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Gemini Analysis:                                 │
              │ - Analyze description                            │
              │ - Match to budget category                       │
              │ - Assign GL code                                 │
              │ - Identify cost center                           │
              │ - Flag unusual amounts                           │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Update Budget Tracker:                           │
              │ - Categorize expense                             │
              │ - Update category totals                         │
              │ - Recalculate remaining budget                   │
              │ - Check for threshold breaches                   │
              └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │        BUDGET MONITORING                 │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ THRESHOLD     │           │ TREND             │           │ ANOMALY       │
│ MONITORING    │           │ ANALYSIS          │           │ DETECTION     │
│               │           │                   │           │               │
│ Alert when:   │           │ Track:            │           │ Flag:         │
│ - 50% spent   │           │ - Month over      │           │ - Unusual     │
│ - 75% spent   │           │   month           │           │   amounts     │
│ - 90% spent   │           │ - Year over year  │           │ - Duplicate   │
│ - Over budget │           │ - Seasonality     │           │ - Wrong cat   │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │         VARIANCE ANALYSIS                │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Calculate Variances:                             │
              │ - Budget vs Actual                               │
              │ - $ Variance                                     │
              │ - % Variance                                     │
              │ - YTD performance                                │
              │ - Forecast based on trend                        │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Gemini Insights:                                 │
              │ - Identify root causes                           │
              │ - Suggest corrective actions                     │
              │ - Forecast year-end position                     │
              │ - Recommend reallocations                        │
              └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │            REPORTING                     │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ DAILY         │           │ WEEKLY            │           │ MONTHLY       │
│ SUMMARY       │           │ REPORT            │           │ ANALYSIS      │
│               │           │                   │           │               │
│ - Expenses    │           │ - Category roll-  │           │ - Full        │
│   logged      │           │   up              │           │   variance    │
│ - Alerts      │           │ - Variance        │           │ - Trend       │
│ - Quick stats │           │   summary         │           │   analysis    │
└───────────────┘           │ - Action items    │           │ - Forecast    │
                            └───────────────────┘           └───────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Budget Tracking System

**Sheet 1: Annual Budget**
| Column | Description |
|--------|-------------|
| A: Category ID | Unique identifier |
| B: Category | Expense category name |
| C: Department | Owning department |
| D: Annual Budget | Total annual budget |
| E: Jan Budget | January allocation |
| F: Feb Budget | February allocation |
| G-P: Mar-Dec | Remaining months |
| Q: YTD Budget | Year-to-date budget |
| R: YTD Actual | Year-to-date actual |
| S: YTD Variance | $ Variance |
| T: Variance % | Percentage variance |
| U: Remaining | Budget remaining |
| V: Status | On Track/Warning/Over |

**Sheet 2: Expense Log**
| Column | Description |
|--------|-------------|
| A: Entry ID | Unique identifier |
| B: Date | Transaction date |
| C: Description | Expense description |
| D: Vendor | Who was paid |
| E: Amount | Transaction amount |
| F: Category | Budget category |
| G: GL Code | General ledger code |
| H: Department | Cost center |
| I: Source | Bank/Card/Invoice/Manual |
| J: Reference | Transaction reference |
| K: Auto-Cat | AI categorized? Yes/No |
| L: Confidence | Categorization confidence |
| M: Notes | Additional notes |
| N: Logged By | Who entered |
| O: Logged Date | Entry timestamp |

**Sheet 3: Monthly Summary**
| Column | Description |
|--------|-------------|
| A: Month | Month name |
| B: Budget | Monthly budget |
| C: Actual | Monthly actual |
| D: Variance $ | Dollar variance |
| E: Variance % | Percentage variance |
| F: Cumulative Budget | YTD budget |
| G: Cumulative Actual | YTD actual |
| H: Status | Performance indicator |
| I: Key Drivers | Main variance drivers |

**Sheet 4: Alert Thresholds**
| Column | Description |
|--------|-------------|
| A: Category | Budget category |
| B: 50% Threshold | Amount at 50% |
| C: 75% Threshold | Amount at 75% |
| D: 90% Threshold | Amount at 90% |
| E: Current % | Current % used |
| F: Alert Level | None/Yellow/Orange/Red |
| G: Last Alert | When last alerted |
| H: Owner | Who to notify |

### Step 2: Configure Expense Processing

**Workflow: Expense Categorization**
```yaml
Trigger: New row added to Expense Log OR Category = blank
  │
  ├─ Node 1: Get Expense Details
  │    - Description
  │    - Vendor
  │    - Amount
  │    - Date
  │
  ├─ Node 2: Lookup Vendor History
  │    - Find previous expenses from vendor
  │    - Get typical category
  │    - Check for patterns
  │
  ├─ Node 3: Gemini Analysis
  │    - Analyze description
  │    - Consider vendor history
  │    - Match to budget categories
  │    - Assess confidence
  │
  ├─ Node 4: Apply Categorization
  │    │
  │    ├─ If High Confidence (>90%)
  │    │    - Auto-apply category
  │    │    - Mark Auto-Cat = Yes
  │    │
  │    └─ If Lower Confidence
  │         - Apply suggested category
  │         - Flag for review
  │         - Add to review queue
  │
  ├─ Node 5: Update Budget Tracker
  │    - Add to category total
  │    - Recalculate remaining
  │    - Update YTD figures
  │
  └─ Node 6: Check Thresholds
       - If threshold crossed
       - Trigger appropriate alert
```

**Workflow: Bulk Import Processing**
```yaml
Trigger: Bank/Card statement import
  │
  ├─ Node 1: Parse Import
  │    - Standardize format
  │    - Extract transactions
  │    - Identify duplicates
  │
  ├─ Node 2: For Each Transaction
  │    - Run categorization
  │    - Log to Expense Log
  │    - Update budgets
  │
  └─ Node 3: Generate Import Summary
       - Total imported
       - Categories assigned
       - Items needing review
       - Email to finance team
```

### Step 3: Threshold Monitoring

**Workflow: Budget Alert System**
```yaml
Trigger: Every hour during business hours OR expense logged
  │
  ├─ Node 1: Calculate Current Percentages
  │    - For each category
  │    - YTD Actual / YTD Budget
  │
  ├─ Node 2: Check Against Thresholds
  │    - 50% level: Yellow
  │    - 75% level: Orange
  │    - 90% level: Red
  │    - Over 100%: Critical
  │
  ├─ Node 3: Identify New Breaches
  │    - Compare to last alert
  │    - Only alert on new levels
  │
  ├─ Node 4: For Each New Alert
  │    │
  │    ├─ Update Alert Sheet
  │    │    - Current level
  │    │    - Last alert timestamp
  │    │
  │    └─ Send Notification
  │         - Email to category owner
  │         - Include current stats
  │         - Recommendations
  │
  └─ Node 5: Log Alert History
       - Track all alerts sent
       - Monitor response
```

### Step 4: Variance Analysis

**Workflow: Monthly Variance Report**
```yaml
Trigger: Monthly (1st business day) OR On demand
  │
  ├─ Node 1: Calculate Variances
  │    - For each category
  │    - Budget vs Actual (month)
  │    - Budget vs Actual (YTD)
  │    - Prior year comparison
  │
  ├─ Node 2: Identify Significant Variances
  │    - Over/under by >10%
  │    - Dollar impact >$1,000
  │    - Trending negatively
  │
  ├─ Node 3: Gemini Analysis
  │    - Analyze variance patterns
  │    - Identify root causes
  │    - Suggest actions
  │    - Forecast year-end
  │
  ├─ Node 4: Generate Report
  │    │
  │    ├─ Executive Summary
  │    │    - Key highlights
  │    │    - Major variances
  │    │    - Actions needed
  │    │
  │    ├─ Category Detail
  │    │    - Each category breakdown
  │    │    - Variance explanation
  │    │
  │    └─ Recommendations
  │         - Reallocations
  │         - Savings opportunities
  │         - Risk areas
  │
  ├─ Node 5: Save Report
  │    - To Drive /Finance/Reports/
  │
  └─ Node 6: Distribute
       - Email to stakeholders
       - Calendar invite for review
```

### Step 5: Forecasting

**Workflow: Rolling Forecast**
```yaml
Trigger: Weekly Monday 6:00 AM
  │
  ├─ Node 1: Analyze Spending Trends
  │    - Monthly run rate
  │    - Seasonal patterns
  │    - Known upcoming expenses
  │
  ├─ Node 2: Project Year-End
  │    - Based on current trends
  │    - Adjusted for seasonality
  │    - Include known commitments
  │
  ├─ Node 3: Compare to Budget
  │    - Projected vs budgeted
  │    - Identify over/under categories
  │    - Calculate total variance
  │
  ├─ Node 4: Gemini Recommendations
  │    - Actions to get on track
  │    - Reallocation opportunities
  │    - Risk mitigation
  │
  └─ Node 5: Update Forecast Sheet
       - Latest projections
       - Confidence level
       - Key assumptions
```

## Example Prompts/Commands

### Expense Categorization
```
Categorize this expense:

Description: [EXPENSE_DESCRIPTION]
Vendor: [VENDOR_NAME]
Amount: $[AMOUNT]
Date: [DATE]

Historical vendor categorization (if any):
[PREVIOUS_CATEGORIES]

Available Budget Categories:
1. Personnel - Salaries, benefits, contractors
2. Office & Facilities - Rent, utilities, supplies
3. Technology - Software, hardware, IT services
4. Marketing - Advertising, events, materials
5. Travel & Entertainment - Trips, meals, events
6. Professional Services - Legal, accounting, consulting
7. Operations - Logistics, fulfillment, materials
8. Other - Miscellaneous

Determine:
1. Best Category (from list above)
2. GL Code suggestion
3. Confidence level (0-100%)
4. Reasoning (brief explanation)
5. Alternative category (if applicable)

If this appears unusual (amount, timing, or type), flag it.
```

### Variance Analysis
```
Analyze budget variance for this category:

Category: [CATEGORY_NAME]
Period: [MONTH/QUARTER]

Budget Data:
- Period Budget: $[BUDGET]
- Period Actual: $[ACTUAL]
- Variance: $[VARIANCE] ([%])
- YTD Budget: $[YTD_BUDGET]
- YTD Actual: $[YTD_ACTUAL]
- Prior Year Same Period: $[PRIOR]

Largest Expenses This Period:
[TOP_5_EXPENSES_WITH_AMOUNTS]

Provide:
1. Variance Summary (2-3 sentences)
2. Root Cause Analysis
   - What drove the variance?
   - One-time vs recurring factors
3. Trend Assessment
   - Is this improving or worsening?
   - Expected trajectory
4. Impact Assessment
   - Year-end projection if trend continues
   - Risk level (High/Medium/Low)
5. Recommended Actions
   - Specific steps to address
   - Timeline for action
   - Expected result

Be specific and actionable. Avoid generic advice.
```

### Monthly Report Generation
```
Generate a monthly budget report:

Period: [MONTH] [YEAR]
Report Type: [EXECUTIVE/DETAILED]

Summary Data:
- Total Budget: $[TOTAL_BUDGET]
- Total Actual: $[TOTAL_ACTUAL]
- Overall Variance: $[VARIANCE] ([%])

Category Performance:
[TABLE: Category, Budget, Actual, Variance $, Variance %]

Significant Variances (>10%):
[LIST_OF_CATEGORIES_WITH_LARGE_VARIANCES]

Create a report with:

1. Executive Summary
   - Overall financial health (1 paragraph)
   - Key wins and concerns
   - Bottom line assessment

2. Performance Highlights
   - Categories performing well
   - Positive trends

3. Areas of Concern
   - Categories over budget
   - Negative trends
   - Action items

4. Recommendations
   - Specific actions for next month
   - Reallocation suggestions
   - Savings opportunities

5. Forecast Update
   - Year-end projection
   - Confidence level
   - Key assumptions

Format for executive readability. Use bullet points and bold for emphasis.
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| New expense logged | Categorize and update budget | Real-time |
| Bank statement imported | Bulk process transactions | On import |
| 50% threshold crossed | Yellow alert to owner | Real-time |
| 75% threshold crossed | Orange alert + manager | Real-time |
| 90% threshold crossed | Red alert + executive | Real-time |
| Over budget | Critical alert to all | Real-time |
| Daily 9:00 AM | Daily expense summary | Daily |
| Weekly Monday | Forecast update | Weekly |
| Monthly (1st) | Full variance report | Monthly |
| Quarterly | Deep-dive analysis | Quarterly |

## Expected Outcomes

### Quantitative Results
- **Categorization time:** 95% reduction (automatic)
- **Categorization accuracy:** 92%+ with AI
- **Variance detection:** Real-time vs. monthly
- **Reporting time:** 80% reduction
- **Budget overruns:** 60% reduction (early alerts)

### Qualitative Benefits
- Proactive budget management
- Consistent expense categorization
- Real-time financial visibility
- Data-driven decision making
- Reduced month-end scramble

## ROI Estimate

### Assumptions
- Financial Analyst salary: $75,000/year ($37.50/hour)
- Monthly expenses processed: 500
- Manual categorization: 3 min/expense
- Post-automation: 0.5 min/expense (review only)
- Budget overruns avoided: $2,000/month

### Calculation
| Metric | Value |
|--------|-------|
| Time saved per expense | 2.5 minutes |
| Monthly time saved | 21 hours |
| Monthly labor savings | $787 |
| Overruns avoided | $2,000/month |
| Monthly savings | $2,787 |
| Annual savings | $33,444 |
| Tool costs (estimated) | $75/month |
| **Net annual ROI** | **$32,544** |

### Additional Value
- Better cash flow management
- Improved stakeholder confidence
- Audit-ready categorization
- Strategic planning support

## Advanced Extensions

1. **Bank Integration:** Direct bank feed for transactions
2. **Approval Workflows:** Expense approval automation
3. **Department Dashboards:** Real-time budget views
4. **Predictive Analytics:** ML-based spend forecasting
5. **Policy Compliance:** Auto-flag policy violations

## Sample Budget Structure

```yaml
Budget Categories:

Personnel (40% of budget):
  - Salaries & Wages
  - Benefits
  - Contractors
  - Payroll Taxes
  - Training & Development

Operations (25% of budget):
  - Office Rent
  - Utilities
  - Office Supplies
  - Equipment
  - Maintenance

Technology (15% of budget):
  - Software Subscriptions
  - Hardware
  - IT Services
  - Cloud Infrastructure
  - Security

Marketing (10% of budget):
  - Advertising
  - Events
  - Content & Creative
  - Tools & Platforms

Professional Services (5% of budget):
  - Legal
  - Accounting
  - Consulting
  - Insurance

Other (5% of budget):
  - Travel
  - Entertainment
  - Miscellaneous

Alert Thresholds:
  - Green: Under 50% of period budget
  - Yellow: 50-74% of period budget
  - Orange: 75-89% of period budget
  - Red: 90-99% of period budget
  - Critical: At or over budget
```
