# AI Legal Assistant

## Overview

**Problem Solved:** Legal professionals drown in document management, deadline tracking, and client communication. Critical deadlines are missed, documents are misfiled, client communication is inconsistent, and billable time is lost to administrative tasks. The complexity of legal work demands precision that manual processes struggle to maintain.

**Solution:** An AI legal assistant that organizes legal documents in Drive, tracks critical deadlines with Calendar alerts, manages client communication via Gmail, and maintains matter tracking in Sheets - ensuring nothing falls through the cracks while maximizing billable time.

## Tools Used

| Tool | Purpose |
|------|---------|
| Google Drive | Document management, matter files, templates |
| Google Sheets | Matter tracking, deadline management, client database |
| Gmail | Client communication, deadline alerts, notifications |
| Google Calendar | Court dates, deadlines, client meetings |
| Gemini | Document analysis, communication drafting |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                     AI LEGAL ASSISTANT WORKFLOW                      │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │        DOCUMENT MANAGEMENT               │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Trigger: New document received/created           │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Document Processing:                             │
              │ - Identify document type                         │
              │ - Extract key dates (filing, deadlines)          │
              │ - Identify matter/client                         │
              │ - Classify and tag                               │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ FILE          │           │ EXTRACT           │           │ UPDATE        │
│               │           │ DEADLINES         │           │ TRACKING      │
│ Save to:      │           │                   │           │               │
│ /Matters/     │           │ - Court dates     │           │ - Log in      │
│ [Client]/     │           │ - Response due    │           │   matter      │
│ [Matter]/     │           │ - Filing limits   │           │ - Note type   │
│ [Type]/       │           │ - Statute dates   │           │ - Update      │
└───────────────┘           └───────────────────┘           │   status      │
                                    │                       └───────────────┘
                                    ▼
                          ┌───────────────────┐
                          │ Create Calendar   │
                          │ Events + Alerts   │
                          └───────────────────┘

                    ┌─────────────────────────────────────────┐
                    │         DEADLINE TRACKING                │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ ADVANCE       │           │ IMMEDIATE         │           │ CRITICAL      │
│ NOTICE        │           │ ALERT             │           │ ESCALATION    │
│               │           │                   │           │               │
│ 30/14/7 days  │           │ 3 days/1 day      │           │ Day of        │
│ before        │           │ before            │           │ deadline      │
│               │           │                   │           │               │
│ - Planning    │           │ - Action needed   │           │ - All hands   │
│   reminder    │           │ - Prep deadline   │           │ - Executive   │
└───────────────┘           └───────────────────┘           │   alert       │
                                                            └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │        CLIENT COMMUNICATION              │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ STATUS        │           │ DOCUMENT          │           │ BILLING       │
│ UPDATES       │           │ REQUESTS          │           │ COMMUNICATION │
│               │           │                   │           │               │
│ - Progress    │           │ - Missing docs    │           │ - Invoice     │
│   reports     │           │ - Signatures      │           │   delivery    │
│ - Next steps  │           │ - Information     │           │ - Payment     │
│ - Milestones  │           │   needed          │           │   reminders   │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │          MATTER MANAGEMENT               │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Track:                                           │
              │ - Matter status and phase                        │
              │ - All deadlines (court, internal)                │
              │ - Documents received/sent                        │
              │ - Time entries                                   │
              │ - Client communications                          │
              │ - Billing status                                 │
              └─────────────────────────────────────────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Legal Practice Management

**Sheet 1: Client Database**
| Column | Description |
|--------|-------------|
| A: Client ID | Unique identifier |
| B: Client Name | Individual or entity name |
| C: Client Type | Individual/Corporation/LLC |
| D: Primary Contact | Main contact person |
| E: Email | Primary email |
| F: Phone | Contact phone |
| G: Address | Mailing address |
| H: Intake Date | When became client |
| I: Conflict Check | Conflict cleared date |
| J: Engagement Letter | Signed (link) |
| K: Billing Type | Hourly/Flat/Contingency |
| L: Rate | Billing rate |
| M: Trust Balance | Retainer balance |
| N: Status | Active/Inactive/Closed |
| O: Notes | Client notes |

**Sheet 2: Matter Tracker**
| Column | Description |
|--------|-------------|
| A: Matter ID | Unique matter number |
| B: Client ID | Reference to client |
| C: Client Name | Client name |
| D: Matter Name | Case/matter description |
| E: Practice Area | Litigation/Corporate/Family/etc. |
| F: Status | Active/On Hold/Closed |
| G: Open Date | When opened |
| H: Close Date | When closed |
| I: Attorney | Lead attorney |
| J: Paralegal | Assigned paralegal |
| K: Court/Venue | If litigation |
| L: Case Number | Court case number |
| M: Opposing Party | Opposing party name |
| N: Opposing Counsel | Opposing attorney |
| O: Next Deadline | Soonest deadline |
| P: Drive Folder | Matter folder link |
| Q: Notes | Matter notes |

**Sheet 3: Deadline Calendar**
| Column | Description |
|--------|-------------|
| A: Deadline ID | Unique identifier |
| B: Matter ID | Reference to matter |
| C: Matter Name | Matter description |
| D: Deadline Type | Court/Filing/Internal/Client |
| E: Description | What's due |
| F: Due Date | Deadline date |
| G: Due Time | If time-specific |
| H: Priority | Critical/High/Medium/Low |
| I: Status | Pending/Complete/Extended |
| J: Responsible | Who's responsible |
| K: Reminder Sent | Tracking column |
| L: Calendar Link | Event link |
| M: Notes | Deadline notes |

**Sheet 4: Document Log**
| Column | Description |
|--------|-------------|
| A: Doc ID | Unique identifier |
| B: Matter ID | Reference to matter |
| C: Document Name | Document title |
| D: Document Type | Pleading/Contract/Correspondence/etc. |
| E: Direction | Incoming/Outgoing |
| F: Date | Document date |
| G: From/To | Sender/recipient |
| H: Filed | If court-filed |
| I: Drive Link | Document location |
| J: Summary | Brief description |
| K: Status | Draft/Final/Signed |

### Step 2: Configure Document Management

**Drive Structure:**
```
/Legal/
├── Clients/
│   └── [Client_Name]/
│       └── [Matter_Name]/
│           ├── 01_Engagement/
│           │   ├── Engagement_Letter.pdf
│           │   └── Conflict_Check.pdf
│           ├── 02_Pleadings/
│           ├── 03_Correspondence/
│           ├── 04_Discovery/
│           ├── 05_Research/
│           ├── 06_Contracts/
│           ├── 07_Client_Documents/
│           └── 08_Billing/
├── Templates/
│   ├── Engagement_Letters/
│   ├── Pleadings/
│   ├── Contracts/
│   └── Correspondence/
└── Admin/
    ├── Calendaring_Rules/
    └── Practice_Guides/
```

**Workflow: Document Intake**
```yaml
Trigger: Email with attachment to legal@ OR File upload to inbox
  │
  ├─ Node 1: Identify Document Type
  │    - Gemini: Analyze content
  │    - Classify: Pleading/Contract/Letter/etc.
  │    - Extract key information
  │
  ├─ Node 2: Match to Matter
  │    - Check client/case references
  │    - Match to existing matters
  │    - If new: Flag for review
  │
  ├─ Node 3: Extract Deadlines
  │    - Court dates
  │    - Response requirements
  │    - Filing deadlines
  │    - Statute of limitations
  │
  ├─ Node 4: File Document
  │    - Move to proper folder
  │    - Standardize filename
  │    - Log in Document Log
  │
  ├─ Node 5: Create Deadline Entries
  │    - Add to Deadline Calendar
  │    - Create calendar events
  │    - Set reminder sequences
  │
  └─ Node 6: Notify Team
       - Email to responsible attorney
       - Include deadline summary
       - Link to document
```

### Step 3: Deadline Management System

**Workflow: Deadline Alert Sequence**
```yaml
Trigger: Daily 7:00 AM
  │
  ├─ Node 1: Get Upcoming Deadlines
  │    - 30 days out
  │    - 14 days out
  │    - 7 days out
  │    - 3 days out
  │    - 1 day out
  │    - Today
  │
  ├─ Node 2: For Each Deadline
  │    │
  │    ├─ Check Alert Status
  │    │    - Has this interval been sent?
  │    │    - Is it still pending?
  │    │
  │    └─ Determine Alert Level
  │         - 30 days: Planning notice
  │         - 14 days: Preparation reminder
  │         - 7 days: Action required
  │         - 3 days: Priority alert
  │         - 1 day: Critical warning
  │         - Today: Urgent escalation
  │
  ├─ Node 3: Send Appropriate Alerts
  │    │
  │    ├─ 30/14/7 days
  │    │    - Email to responsible party
  │    │    - Include matter details
  │    │
  │    ├─ 3/1 days
  │    │    - Email + escalate to attorney
  │    │    - Calendar reminder
  │    │
  │    └─ Today
  │         - Email to all (attorney, paralegal, admin)
  │         - Executive alert if critical
  │
  └─ Node 4: Log Alerts Sent
       - Update tracking
       - Note in matter file
```

**Workflow: Deadline Calculation (Litigation)**
```yaml
Trigger: New court document filed/received
  │
  ├─ Node 1: Identify Response Requirements
  │    - Type of document
  │    - Applicable rules
  │    - Standard response period
  │
  ├─ Node 2: Calculate Deadlines
  │    - Apply court rules
  │    - Add/subtract for:
  │      - Service method
  │      - Holidays
  │      - Weekends
  │      - Extensions
  │
  ├─ Node 3: Add Internal Buffers
  │    - Draft due: 7 days before
  │    - Review due: 3 days before
  │    - Final due: 1 day before
  │
  └─ Node 4: Create Full Timeline
       - Filing deadline
       - All internal milestones
       - Calendar everything
```

### Step 4: Client Communication

**Workflow: Status Update Automation**
```yaml
Trigger: Weekly OR Matter milestone reached
  │
  ├─ Node 1: Gather Matter Status
  │    - Recent activity
  │    - Upcoming deadlines
  │    - Documents received/sent
  │    - Current phase
  │
  ├─ Node 2: Generate Update
  │    - Gemini: Create client-friendly summary
  │    - Explain recent developments
  │    - Note next steps
  │    - Flag any client action needed
  │
  ├─ Node 3: Review Queue
  │    - Draft for attorney review
  │    - Attorney approves/edits
  │
  └─ Node 4: Send Update
       - Email to client
       - Log communication
       - Schedule next update
```

**Workflow: Document Request**
```yaml
Trigger: Missing document identified OR Manual request
  │
  ├─ Node 1: Identify Missing Items
  │    - What's needed
  │    - Why it's needed
  │    - Deadline for receipt
  │
  ├─ Node 2: Generate Request Email
  │    - Clear list of items
  │    - Specific instructions
  │    - Deadline emphasized
  │    - Upload link/instructions
  │
  ├─ Node 3: Send and Track
  │    - Email to client
  │    - Log request
  │    - Set follow-up reminder
  │
  └─ Node 4: Follow-Up Sequence
       - 3 days: Reminder if not received
       - 7 days: Second reminder
       - 10 days: Call required
```

## Example Prompts/Commands

### Document Classification
```
Analyze this legal document and classify it:

Document Text:
[DOCUMENT_CONTENT or summary]

Determine:
1. Document Type:
   - Pleading (Motion, Brief, Complaint, Answer, etc.)
   - Contract (Agreement, Amendment, etc.)
   - Correspondence (Letter, Email, etc.)
   - Court Order
   - Discovery (Interrogatories, Document Request, etc.)
   - Client Document
   - Other

2. Matter Information:
   - Parties mentioned
   - Case number (if any)
   - Court/venue (if any)

3. Key Dates Extracted:
   - Document date
   - Response deadlines
   - Hearing dates
   - Filing requirements

4. Summary (2-3 sentences):
   - What is this document
   - Key content/purpose
   - Action required

5. Suggested Filing Location:
   - Client folder
   - Document subfolder
   - Filename suggestion

Format as structured data for automation.
```

### Client Status Update
```
Generate a client status update for this matter:

Matter: [MATTER_NAME]
Client: [CLIENT_NAME]
Practice Area: [AREA]
Current Phase: [PHASE]

Recent Activity (last 30 days):
[LIST_OF_ACTIVITIES]

Upcoming Deadlines:
[LIST_OF_DEADLINES]

Recent Documents:
[LIST_OF_DOCUMENTS]

Generate an update email that:
1. Is written for a non-lawyer client
2. Avoids unnecessary legal jargon
3. Clearly explains recent developments
4. Notes what we've done on their behalf
5. Explains next steps and timeline
6. Identifies any action needed from client
7. Maintains professional, reassuring tone

Length: 200-300 words
Include: Subject line suggestion
```

### Deadline Extraction
```
Extract all deadlines from this legal document:

Document Type: [TYPE]
Document Text: [CONTENT]

Filed/Served Date: [DATE]
Jurisdiction: [JURISDICTION]

Extract and calculate:
1. Explicit Deadlines:
   - Any dates mentioned
   - Any "within X days" requirements

2. Implied Deadlines (based on rules):
   - Response periods
   - Motion deadlines
   - Discovery obligations

3. For Each Deadline:
   - Description
   - Due Date (calculated)
   - Applicable Rule
   - Priority (Critical/High/Medium)
   - Internal prep dates

4. Holiday/Weekend Adjustments:
   - Note if calculation affected by court closures

Format for import to tracking system.
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| Document received | Classify, file, extract deadlines | Real-time |
| New deadline created | Set up reminder sequence | Real-time |
| 30/14/7/3/1 days before deadline | Send appropriate alert | Daily |
| Deadline today | Urgent escalation | Daily |
| Weekly (Monday) | Client status updates (per matter) | Weekly |
| Document request outstanding | Follow-up reminder | Daily check |
| New matter opened | Create folder structure | Real-time |
| Matter closed | Archive and final report | Real-time |

## Expected Outcomes

### Quantitative Results
- **Missed deadlines:** Zero (from deadline tracking)
- **Document filing time:** 80% reduction
- **Client communication consistency:** 100%
- **Administrative time:** 50% reduction
- **Deadline visibility:** Real-time vs. manual checking

### Qualitative Benefits
- Complete audit trail for all matters
- Consistent client experience
- Reduced malpractice risk
- Better work-life balance for staff
- Professional, organized practice

## ROI Estimate

### Assumptions
- Legal Assistant salary: $55,000/year ($27.50/hour)
- Attorney billing rate: $300/hour
- Time on admin (legal assistant): 25 hours/week
- Post-automation admin: 12 hours/week
- Attorney time on admin: 5 hours/week
- Post-automation attorney admin: 2 hours/week

### Calculation
| Metric | Value |
|--------|-------|
| Legal Assistant time saved | 13 hours/week |
| Attorney time saved | 3 hours/week |
| Monthly LA savings | $1,430 |
| Monthly attorney time recovered | $3,600 (billable) |
| Monthly value | $5,030 |
| Annual value | $60,360 |
| Tool costs (estimated) | $100/month |
| **Net annual ROI** | **$59,160** |

### Additional Value
- Malpractice prevention: priceless
- Client satisfaction improvement
- Competitive advantage in responsiveness

## Advanced Extensions

1. **Conflict Checking:** Automated conflict of interest checks
2. **Time Entry Assistance:** AI-suggested time entries
3. **Court Filing Integration:** E-filing automation
4. **Research Assistance:** Legal research summaries
5. **Template Generation:** Auto-populate legal documents

## Sample Deadline Rules

```yaml
Federal Civil Procedure (Examples):

Answer to Complaint:
  - Base: 21 days from service
  - If served outside US: 60 days
  - Extensions: Common, usually to 30 days

Motion Response:
  - Opposition: 14 days from motion
  - Reply: 7 days from opposition

Discovery:
  - Initial Disclosures: 14 days after Rule 26(f) conference
  - Interrogatory Response: 30 days from service
  - Document Request Response: 30 days from service
  - Deposition Notice: Reasonable time (typically 14+ days)

Appeals:
  - Notice of Appeal: 30 days from judgment (civil)
  - Notice of Appeal: 14 days from judgment (criminal)

Internal Buffers:
  - Draft Due: Filing deadline - 7 days
  - Attorney Review: Filing deadline - 3 days
  - Final/Filing: Filing deadline - 1 day

Service Method Additions:
  - Mail: +3 days
  - Electronic: +0 days (typically)
```
