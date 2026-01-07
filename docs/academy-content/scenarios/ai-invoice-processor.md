# AI Invoice Processor

## Overview

**Problem Solved:** Accounts payable teams spend countless hours manually entering invoice data, chasing down approvals, and tracking payment status. Invoices get lost in inboxes, data entry errors cause payment issues, and vendors follow up about unpaid invoices. This manual process is slow, error-prone, and frustrating for everyone.

**Solution:** An AI invoice processor that automatically captures invoices from email, extracts key data using Gemini, logs everything to Google Sheets, organizes documents in Drive, and tracks payment status - transforming AP from a bottleneck into a streamlined operation.

## Tools Used

| Tool | Purpose |
|------|---------|
| Gmail | Invoice intake, vendor communication |
| Google Sheets | Invoice tracking, payment scheduling, vendor database |
| Google Drive | Invoice archive, document storage |
| Gemini | Data extraction, invoice analysis |
| n8n | Workflow orchestration |
| Code by Zapier | Custom processing, calculations |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AI INVOICE PROCESSOR WORKFLOW                     │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │           INVOICE INTAKE                 │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Trigger: Email with invoice attachment           │
              │ - Subject contains: invoice, bill, statement     │
              │ - Attachment type: PDF, PNG, JPG                 │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Gemini Vision: Extract Invoice Data              │
              │ - Invoice number                                 │
              │ - Vendor name & address                          │
              │ - Invoice date                                   │
              │ - Due date                                       │
              │ - Line items                                     │
              │ - Subtotal, tax, total                           │
              │ - Payment terms                                  │
              │ - Bank/payment details                           │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ VALIDATE      │           │ CATEGORIZE        │           │ SAVE & LOG    │
│               │           │                   │           │               │
│ - Check for   │           │ - Match vendor    │           │ - Archive to  │
│   duplicates  │           │ - Apply GL code   │           │   Drive       │
│ - Verify      │           │ - Assign cost     │           │ - Log to      │
│   amounts     │           │   center          │           │   tracking    │
│ - Flag issues │           │ - Set approval    │           │   sheet       │
│               │           │   workflow        │           │               │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │          APPROVAL WORKFLOW               │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ AUTO-APPROVE  │           │ SINGLE APPROVAL   │           │ MULTI-LEVEL   │
│               │           │                   │           │               │
│ Criteria:     │           │ For amounts:      │           │ For amounts:  │
│ - Under $100  │           │ - $100 - $1,000   │           │ - Over $5,000 │
│ - Known vendor│           │ - Known vendor    │           │ - New vendor  │
│ - Recurring   │           │                   │           │ - Unusual     │
└───────────────┘           └───────────────────┘           └───────────────┘
        │                             │                             │
        └─────────────────────────────┼─────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Approval Request:                                │
              │ - Email to approver with invoice summary         │
              │ - Quick approve/reject buttons                   │
              │ - Link to full invoice                           │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │          PAYMENT TRACKING                │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ SCHEDULE      │           │ PAYMENT DUE       │           │ OVERDUE       │
│ PAYMENT       │           │ REMINDER          │           │ ALERT         │
│               │           │                   │           │               │
│ Add to        │           │ 5 days before:    │           │ Escalate:     │
│ payment batch │           │ Reminder email    │           │ - Alert AP    │
│               │           │ to AP             │           │ - Email vendor│
└───────────────┘           └───────────────────┘           └───────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Invoice Tracking System

**Sheet 1: Invoice Log**
| Column | Description |
|--------|-------------|
| A: Invoice ID | System-generated ID |
| B: Invoice # | Vendor's invoice number |
| C: Vendor Name | Supplier name |
| D: Vendor ID | Reference to vendor database |
| E: Invoice Date | Date on invoice |
| F: Due Date | Payment due date |
| G: Amount | Invoice total |
| H: Currency | USD/EUR/etc. |
| I: Category | Expense category |
| J: GL Code | General ledger code |
| K: Cost Center | Department/project |
| L: Status | Pending/Approved/Paid/Disputed |
| M: Approval Status | Awaiting/Approved/Rejected |
| N: Approver | Who needs to approve |
| O: Approved Date | When approved |
| P: Payment Date | When paid |
| Q: Payment Method | Check/ACH/Wire/Card |
| R: Drive Link | Invoice document link |
| S: Email Link | Original email |
| T: Notes | Additional notes |

**Sheet 2: Vendor Database**
| Column | Description |
|--------|-------------|
| A: Vendor ID | Unique identifier |
| B: Vendor Name | Company name |
| C: Contact Name | Primary contact |
| D: Email | Contact email |
| E: Phone | Contact phone |
| F: Address | Billing address |
| G: Default GL | Default GL code |
| H: Default Category | Default expense category |
| I: Payment Terms | Net 30, etc. |
| J: Preferred Payment | ACH/Check/Wire |
| K: Bank Details | Payment information |
| L: Tax ID | W-9 on file reference |
| M: Status | Active/Inactive |
| N: Total YTD | Year-to-date spend |
| O: Notes | Vendor notes |

**Sheet 3: Payment Schedule**
| Column | Description |
|--------|-------------|
| A: Payment ID | Unique identifier |
| B: Invoice ID | Reference to invoice |
| C: Vendor | Vendor name |
| D: Amount | Payment amount |
| E: Due Date | Original due date |
| F: Scheduled Date | Planned payment date |
| G: Payment Method | How paying |
| H: Status | Scheduled/Processing/Completed |
| I: Batch ID | Payment batch reference |
| J: Confirmation | Payment confirmation |

**Sheet 4: GL Codes**
| Column | Description |
|--------|-------------|
| A: GL Code | General ledger code |
| B: Description | What it's for |
| C: Category | Expense category |
| D: Default Approver | Who typically approves |
| E: Budget | Annual budget |
| F: YTD Actual | Year-to-date spend |
| G: Remaining | Budget remaining |

### Step 2: Configure Email Intake

**Workflow: Invoice Detection**
```yaml
Trigger: Gmail - New email matching:
  - has:attachment
  - (invoice OR bill OR statement OR receipt)
  - NOT (already labeled "Processed")
  │
  ├─ Node 1: Get Attachments
  │    - Download PDF/image files
  │    - Store temporarily for processing
  │
  ├─ Node 2: Gemini Vision - Extract Data
  │    - Analyze each attachment
  │    - Extract structured invoice data
  │    - Return JSON format
  │
  ├─ Node 3: Validate Extraction
  │    - Verify required fields present
  │    - Check for reasonable values
  │    - Flag if confidence low
  │
  ├─ Node 4: Duplicate Check
  │    - Search existing invoices
  │    - Match on vendor + invoice # + amount
  │    - If duplicate: Flag and stop
  │
  ├─ Node 5: Vendor Lookup
  │    - Find or create vendor
  │    - Apply defaults (GL, category)
  │
  ├─ Node 6: Save to Drive
  │    - Upload to /Invoices/[Year]/[Month]/
  │    - Standardize filename: [Date]_[Vendor]_[Amount].pdf
  │
  ├─ Node 7: Log to Sheet
  │    - Add row to Invoice Log
  │    - Set status: "Pending Approval"
  │
  ├─ Node 8: Label Email
  │    - Apply "Invoices/Processed" label
  │
  └─ Node 9: Trigger Approval
       - Based on amount and vendor
       - Route to appropriate workflow
```

### Step 3: Approval Workflow

**Workflow: Approval Routing**
```yaml
Trigger: New invoice logged OR Status = "Pending Approval"
  │
  ├─ Node 1: Determine Approval Level
  │    │
  │    ├─ Auto-Approve (no action needed)
  │    │    - Amount < $100
  │    │    - Vendor status = "Trusted"
  │    │    - Recurring expected invoice
  │    │
  │    ├─ Single Approval
  │    │    - Amount $100 - $5,000
  │    │    - Standard vendor
  │    │
  │    └─ Multi-Level Approval
  │         - Amount > $5,000
  │         - New vendor
  │         - Unusual category
  │
  ├─ Node 2: If Auto-Approve
  │    - Set status: "Approved"
  │    - Move to payment scheduling
  │
  ├─ Node 3: If Approval Needed
  │    │
  │    ├─ Get Approver
  │    │    - From GL code default
  │    │    - Or cost center manager
  │    │
  │    ├─ Send Approval Request
  │    │    - Email with invoice summary
  │    │    - Embedded image preview
  │    │    - Approve/Reject/Question buttons
  │    │    - Link to full document
  │    │
  │    └─ Set Reminder
  │         - If no response in 2 days
  │         - Send follow-up
  │
  └─ Node 4: Track Approval Status
       - Monitor for response
       - Update sheet on action
```

**Workflow: Approval Response Handler**
```yaml
Trigger: Approval email replied/clicked
  │
  ├─ Node 1: Parse Response
  │    - Approved
  │    - Rejected (with reason)
  │    - Question (need more info)
  │
  ├─ Node 2: Update Invoice
  │    │
  │    ├─ If Approved
  │    │    - Status: "Approved"
  │    │    - Log approver and date
  │    │    - Move to payment scheduling
  │    │
  │    ├─ If Rejected
  │    │    - Status: "Rejected"
  │    │    - Log reason
  │    │    - Notify submitter
  │    │
  │    └─ If Question
  │         - Status: "On Hold"
  │         - Create follow-up task
  │         - Notify AP team
  │
  └─ Node 3: If Multi-Level
       - Check if all approvals received
       - Route to next approver if needed
```

### Step 4: Payment Management

**Workflow: Payment Scheduling**
```yaml
Trigger: Invoice approved OR Daily 8:00 AM check
  │
  ├─ Node 1: Get Approved Invoices
  │    - Status = "Approved"
  │    - Not yet scheduled
  │
  ├─ Node 2: Calculate Payment Date
  │    - Based on due date
  │    - Apply payment terms
  │    - Optimize for cash flow (pay on due date)
  │
  ├─ Node 3: Create Payment Entry
  │    - Add to Payment Schedule
  │    - Group by payment date for batching
  │
  └─ Node 4: Update Invoice
       - Status: "Scheduled"
       - Add payment reference
```

**Workflow: Payment Reminders**
```yaml
Trigger: Daily 9:00 AM
  │
  ├─ Node 1: Check Upcoming Payments
  │    - Due within 5 days
  │    - Status: "Scheduled"
  │
  ├─ Node 2: Send Reminders
  │    - Email to AP team
  │    - List of payments due
  │    - Total amount
  │
  ├─ Node 3: Check Overdue
  │    - Due date passed
  │    - Status: "Scheduled" (not paid)
  │
  └─ Node 4: Escalate Overdue
       - Alert AP manager
       - Consider vendor notification
       - Flag in system
```

**Workflow: Payment Confirmation**
```yaml
Trigger: Manual mark as paid OR Bank integration
  │
  ├─ Node 1: Update Invoice
  │    - Status: "Paid"
  │    - Payment date
  │    - Confirmation number
  │
  ├─ Node 2: Update Payment Schedule
  │    - Status: "Completed"
  │    - Add confirmation
  │
  ├─ Node 3: Update Vendor
  │    - Increment YTD spend
  │
  └─ Node 4: Archive
       - Move invoice to paid folder
       - Update year-to-date reports
```

## Example Prompts/Commands

### Invoice Data Extraction
```
Analyze this invoice image and extract all relevant data:

Return a JSON object with:
{
  "vendor": {
    "name": "",
    "address": "",
    "phone": "",
    "email": ""
  },
  "invoice": {
    "number": "",
    "date": "YYYY-MM-DD",
    "due_date": "YYYY-MM-DD",
    "po_number": "",
    "currency": "USD"
  },
  "line_items": [
    {
      "description": "",
      "quantity": 0,
      "unit_price": 0.00,
      "total": 0.00
    }
  ],
  "totals": {
    "subtotal": 0.00,
    "tax": 0.00,
    "shipping": 0.00,
    "discount": 0.00,
    "total": 0.00
  },
  "payment": {
    "terms": "",
    "bank_name": "",
    "account_number": "",
    "routing_number": "",
    "notes": ""
  },
  "confidence": {
    "overall": 0.95,
    "fields_uncertain": []
  }
}

If any field is unclear, note it in fields_uncertain.
Ensure dates are in ISO format.
Convert all amounts to numbers (no currency symbols).
```

### Invoice Categorization
```
Categorize this invoice for accounting:

Vendor: [VENDOR_NAME]
Description: [INVOICE_DESCRIPTION]
Line Items:
[LIST_OF_LINE_ITEMS]
Amount: $[AMOUNT]

Available Categories:
- Office Supplies
- Software & Subscriptions
- Professional Services
- Marketing & Advertising
- Travel & Entertainment
- Equipment
- Utilities
- Rent & Facilities
- Insurance
- Other

Available GL Codes:
[LIST_OF_GL_CODES_WITH_DESCRIPTIONS]

Available Cost Centers:
[LIST_OF_COST_CENTERS]

Determine:
1. Primary Category
2. GL Code (best match)
3. Cost Center (if determinable)
4. Is this likely recurring? (Yes/No)
5. Any concerns or flags

If multiple line items span categories, suggest split allocation.
```

### Approval Request Email
```
Generate an approval request email for this invoice:

Invoice Details:
- Vendor: [VENDOR_NAME]
- Invoice #: [INVOICE_NUMBER]
- Amount: $[AMOUNT]
- Due Date: [DUE_DATE]
- Category: [CATEGORY]
- Description: [DESCRIPTION]

Approver: [APPROVER_NAME]
Urgency: [STANDARD/URGENT]

Create an email that:
1. Is clear and scannable
2. Shows key details immediately
3. Explains what they need to do
4. Provides quick action options
5. Links to full invoice
6. Notes any concerns or context

Include approval buttons/links:
- [APPROVE] - One-click approval
- [REJECT] - Reject with reason prompt
- [QUESTION] - Request more information

Keep under 200 words.
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| Invoice email received | Extract, validate, log | Real-time |
| Invoice logged | Route for approval | Real-time |
| Approval response received | Update status, proceed | Real-time |
| Invoice approved | Schedule payment | Real-time |
| Daily 9:00 AM | Payment reminders | Daily |
| Daily 9:00 AM | Overdue alerts | Daily |
| Payment confirmed | Update records, archive | Real-time |
| Weekly Monday | AP summary report | Weekly |
| Monthly (1st) | Month-end reconciliation | Monthly |

## Expected Outcomes

### Quantitative Results
- **Processing time:** 90% reduction (minutes vs. hours)
- **Data accuracy:** 98%+ (vs. manual entry errors)
- **Late payments:** 80% reduction
- **Duplicate payments:** Eliminated
- **Approval turnaround:** 24 hours (vs. days)

### Qualitative Benefits
- No lost invoices
- Consistent categorization
- Complete audit trail
- Better vendor relationships
- Visibility into cash flow

## ROI Estimate

### Assumptions
- AP Clerk salary: $45,000/year ($22.50/hour)
- Invoices processed: 200/month
- Manual time per invoice: 15 minutes
- Post-automation time: 2 minutes
- Late payment fees avoided: $50/month average

### Calculation
| Metric | Value |
|--------|-------|
| Time saved per invoice | 13 minutes |
| Monthly time saved | 43 hours |
| Monthly labor savings | $968 |
| Late fees avoided | $50/month |
| Monthly savings | $1,018 |
| Annual savings | $12,216 |
| Tool costs (estimated) | $75/month |
| **Net annual ROI** | **$11,316** |

### Additional Value
- Early payment discounts captured: ~$500/year
- Reduced vendor complaints
- Better budget visibility
- Audit-ready documentation

## Advanced Extensions

1. **Bank Integration:** Auto-reconcile with bank statements
2. **Budget Alerts:** Flag when category exceeds budget
3. **Vendor Portal:** Self-service for vendors to check status
4. **Purchase Order Matching:** 3-way match automation
5. **Expense Policy Enforcement:** Auto-flag policy violations

## Sample Invoice Folder Structure

```
/Finance/
└── Invoices/
    ├── 2024/
    │   ├── 01-January/
    │   │   ├── PAID/
    │   │   └── PENDING/
    │   ├── 02-February/
    │   └── .../
    ├── 2025/
    │   └── .../
    ├── Vendors/
    │   ├── [Vendor_Name]/
    │   │   ├── W9.pdf
    │   │   ├── Contract.pdf
    │   │   └── Invoices/
    │   └── .../
    └── Reports/
        ├── Monthly/
        └── Annual/

File Naming Convention:
[YYYY-MM-DD]_[VendorName]_[InvoiceNumber]_$[Amount].pdf
Example: 2024-03-15_Acme_INV-1234_$1500.00.pdf
```
