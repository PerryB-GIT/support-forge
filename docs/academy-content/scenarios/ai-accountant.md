# AI Accountant

## Overview

**Problem Solved:** Small businesses spend 5-10 hours weekly on manual expense tracking, invoice processing, and financial report generation. This leads to delayed insights, missed deductions, and cash flow blind spots.

**Solution:** An AI-powered accounting assistant that automatically processes invoices from email, categorizes expenses in Google Sheets, and generates financial reports on demand.

## Tools Used

| Tool | Purpose |
|------|---------|
| Gmail | Invoice intake, vendor communication |
| Google Sheets | Expense tracking, financial data storage |
| Google Drive | Invoice archive, report storage |
| Gemini | Invoice data extraction, categorization |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                      AI ACCOUNTANT WORKFLOW                         │
└─────────────────────────────────────────────────────────────────────┘

[Gmail Inbox]
      │
      ▼
┌─────────────┐    No     ┌─────────────┐
│ New Email   │──────────▶│ Skip        │
│ Received?   │           └─────────────┘
└─────────────┘
      │ Yes
      ▼
┌─────────────────────┐
│ Check for Invoice   │
│ Attachments (PDF,   │
│ PNG, etc.)          │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│ Gemini: Extract     │
│ - Vendor name       │
│ - Amount            │
│ - Date              │
│ - Category          │
│ - Line items        │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│ Save to Google      │
│ Sheets "Expenses"   │
└─────────────────────┘
      │
      ├───────────────────────────┐
      ▼                           ▼
┌─────────────────────┐    ┌─────────────────────┐
│ Archive Invoice     │    │ Update Category     │
│ to Drive Folder     │    │ Totals & Monthly    │
│ /Invoices/YYYY/MM   │    │ Summary             │
└─────────────────────┘    └─────────────────────┘
      │                           │
      └───────────────────────────┘
                  │
                  ▼
         ┌─────────────────────┐
         │ Weekly: Generate    │
         │ Financial Summary   │
         │ Report              │
         └─────────────────────┘
                  │
                  ▼
         ┌─────────────────────┐
         │ Email Report to     │
         │ Owner/Stakeholders  │
         └─────────────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up the Expense Tracking Sheet

Create a Google Sheet with the following structure:

**Sheet 1: Raw Expenses**
| Column | Description |
|--------|-------------|
| A: Date | Transaction date |
| B: Vendor | Vendor/supplier name |
| C: Category | Expense category |
| D: Amount | Transaction amount |
| E: Tax Deductible | Yes/No |
| F: Invoice Link | Drive link to original |
| G: Payment Status | Paid/Pending/Overdue |
| H: Due Date | Payment due date |
| I: Notes | Additional context |

**Sheet 2: Category Summary**
- Monthly totals by category
- Year-to-date comparisons
- Budget vs. actual

**Sheet 3: Vendor Summary**
- Spending by vendor
- Payment history
- Outstanding balances

### Step 2: Create Gmail Filter

Set up a label for invoice-related emails:
- Create label: "Invoices/Pending"
- Filter criteria: `has:attachment (invoice OR receipt OR bill OR statement)`

### Step 3: Configure Invoice Processing Workflow

**n8n Workflow Configuration:**

```yaml
Trigger: Gmail - New Email with Label "Invoices/Pending"
  │
  ├─ Node 1: Get Attachments
  │    - Download PDF/image attachments
  │
  ├─ Node 2: Gemini Vision
  │    - Extract invoice data
  │    - Prompt: "Extract vendor, amount, date, line items, due date"
  │
  ├─ Node 3: Categorize
  │    - Map vendor to expense category
  │    - Flag tax-deductible items
  │
  ├─ Node 4: Google Sheets
  │    - Append row to expenses sheet
  │
  ├─ Node 5: Google Drive
  │    - Upload original to /Invoices/YYYY/MM/
  │    - Update sheet with file link
  │
  └─ Node 6: Gmail
       - Move to "Invoices/Processed" label
       - Remove "Invoices/Pending" label
```

### Step 4: Set Up Weekly Reporting

**Report Generation Workflow (Scheduled: Every Friday 4PM):**

1. Pull data from Sheets for current week
2. Calculate key metrics:
   - Total expenses
   - Top categories
   - Pending payments
   - Upcoming due dates
3. Generate summary using Gemini
4. Email report to stakeholders

## Example Prompts/Commands

### Invoice Data Extraction Prompt
```
Analyze this invoice image and extract the following in JSON format:
{
  "vendor_name": "",
  "invoice_number": "",
  "invoice_date": "",
  "due_date": "",
  "subtotal": 0,
  "tax": 0,
  "total": 0,
  "line_items": [
    {"description": "", "quantity": 0, "unit_price": 0, "total": 0}
  ],
  "payment_terms": "",
  "vendor_address": ""
}
```

### Expense Categorization Prompt
```
Categorize this expense into one of the following categories:
- Software & Subscriptions
- Office Supplies
- Professional Services
- Marketing & Advertising
- Travel & Entertainment
- Utilities
- Equipment
- Payroll & Contractors
- Insurance
- Other

Vendor: [VENDOR_NAME]
Description: [DESCRIPTION]
Amount: [AMOUNT]

Respond with just the category name and whether it's typically tax-deductible (Yes/No).
```

### Weekly Summary Generation Prompt
```
Generate a financial summary for the week of [DATE_RANGE]:

Total Expenses: $[TOTAL]
Top Categories:
1. [CATEGORY]: $[AMOUNT]
2. [CATEGORY]: $[AMOUNT]
3. [CATEGORY]: $[AMOUNT]

Pending Invoices: [COUNT] totaling $[AMOUNT]
Overdue Payments: [COUNT] totaling $[AMOUNT]

Provide:
1. A 2-sentence executive summary
2. Any cash flow concerns
3. Recommended actions for next week
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| New email with invoice attachment | Process and log expense | Real-time |
| Invoice due date approaching (3 days) | Send payment reminder email | Daily check |
| Invoice overdue | Escalation email + flag in sheet | Daily check |
| Friday 4:00 PM | Generate weekly financial summary | Weekly |
| 1st of month | Generate monthly P&L report | Monthly |
| End of quarter | Generate quarterly tax prep report | Quarterly |

## Expected Outcomes

### Quantitative Results
- **Time saved:** 6-8 hours per week on manual data entry
- **Processing speed:** Invoices logged within 5 minutes of receipt
- **Accuracy:** 95%+ categorization accuracy after training
- **Visibility:** Real-time expense tracking vs. monthly reconciliation

### Qualitative Benefits
- Instant visibility into cash flow
- Automated audit trail for all expenses
- Consistent categorization for tax purposes
- Early warning on payment issues
- Better vendor relationship through timely payments

## ROI Estimate

### Assumptions
- Average salary: $60,000/year ($30/hour)
- Current time on expense management: 8 hours/week
- AI solution time: 1 hour/week (review + exceptions)

### Calculation
| Metric | Value |
|--------|-------|
| Weekly time saved | 7 hours |
| Monthly time saved | 28 hours |
| Monthly labor savings | $840 |
| Annual labor savings | $10,080 |
| Tool costs (estimated) | $50/month |
| **Net annual ROI** | **$9,480** |

### Additional Value
- Reduced late payment fees: ~$500/year
- Better tax categorization (deduction capture): ~$1,000/year
- Reduced accountant prep time: ~$500/year
- **Total annual value: ~$11,480**

## Advanced Extensions

1. **Bank Statement Reconciliation:** Match invoices to bank transactions
2. **Vendor Payment Automation:** Generate payment batches for approval
3. **Budget Alerts:** Real-time notifications when category spending exceeds threshold
4. **Forecast Generation:** AI-powered cash flow predictions
5. **Tax Prep Package:** Quarterly export for accountant review

## Sample Sheet Templates

### Monthly Summary Formula
```
=SUMIFS(Expenses!D:D, Expenses!A:A, ">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1), Expenses!A:A, "<"&DATE(YEAR(TODAY()),MONTH(TODAY())+1,1))
```

### Category Pivot Query
```
=QUERY(Expenses!A:I, "SELECT C, SUM(D) WHERE A >= date '"&TEXT(EOMONTH(TODAY(),-1)+1,"yyyy-mm-dd")&"' GROUP BY C ORDER BY SUM(D) DESC LABEL SUM(D) 'Total'")
```
