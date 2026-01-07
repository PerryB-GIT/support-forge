# AI HR Coordinator

## Overview

**Problem Solved:** HR teams spend 40% of their time on administrative tasks - processing onboarding paperwork, scheduling interviews, sending policy reminders, and managing document requests. New hires wait days for access and materials, creating poor first impressions.

**Solution:** An AI HR coordinator that automates employee onboarding workflows, manages document collection and storage, schedules orientation sessions, and handles routine HR inquiries - ensuring consistent, timely experiences for all employees.

## Tools Used

| Tool | Purpose |
|------|---------|
| Google Drive | Document storage, template management, shared folders |
| Google Calendar | Interview scheduling, orientation sessions, review dates |
| Gmail | Onboarding communications, policy distribution |
| Google Sheets | Employee database, onboarding tracking, compliance |
| Gemini | Document generation, FAQ responses |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AI HR COORDINATOR WORKFLOW                        │
└─────────────────────────────────────────────────────────────────────┘

              ┌─────────────────────────────────────────┐
              │          NEW HIRE ONBOARDING            │
              └─────────────────────────────────────────┘
                               │
                               ▼
              ┌─────────────────────────────────────────┐
              │ Trigger: New row added to              │
              │ "Incoming Employees" sheet             │
              └─────────────────────────────────────────┘
                               │
        ┌──────────────────────┼──────────────────────────────────────┐
        ▼                      ▼                                      ▼
┌───────────────┐    ┌───────────────────────┐            ┌───────────────┐
│ Create Drive  │    │ Generate Welcome      │            │ Schedule      │
│ Folder:       │    │ Email + Paperwork     │            │ Calendar      │
│ /Employees/   │    │ Links                 │            │ Events        │
│ [Name]/       │    └───────────────────────┘            └───────────────┘
│  ├─ Onboard   │               │                                 │
│  ├─ Reviews   │               ▼                                 ▼
│  └─ Documents │    ┌───────────────────────┐         ┌─────────────────┐
└───────────────┘    │ Send Day 1 Email:     │         │ - Day 1 Orient  │
                     │ - Welcome message     │         │ - IT Setup      │
                     │ - Paperwork checklist │         │ - HR Onboard    │
                     │ - First day details   │         │ - 30/60/90 Day  │
                     │ - Contact info        │         │ - Benefits      │
                     └───────────────────────┘         └─────────────────┘
                               │
                               ▼
              ┌─────────────────────────────────────────┐
              │        DOCUMENT COLLECTION               │
              └─────────────────────────────────────────┘
                               │
        ┌──────────────────────┼──────────────────────────────────────┐
        ▼                      ▼                                      ▼
┌───────────────┐    ┌───────────────────────┐            ┌───────────────┐
│ Track Form    │    │ Send Reminders        │            │ Mark Complete │
│ Submissions   │    │ for Missing Docs      │            │ When All      │
│ - I-9         │    │ - Day 3 if missing    │            │ Received      │
│ - W-4         │    │ - Day 5 escalation    │            │               │
│ - Direct Dep  │    │ - Day 7 to manager    │            │               │
│ - Emergency   │    └───────────────────────┘            └───────────────┘
└───────────────┘

              ┌─────────────────────────────────────────┐
              │         ONGOING HR SUPPORT               │
              └─────────────────────────────────────────┘
                               │
        ┌──────────────────────┼──────────────────────────────────────┐
        ▼                      ▼                                      ▼
┌───────────────┐    ┌───────────────────────┐            ┌───────────────┐
│ Policy        │    │ Review Scheduling     │            │ FAQ           │
│ Distribution  │    │ - 30/60/90 day        │            │ Auto-Response │
│ - Handbook    │    │ - Annual reviews      │            │ - PTO policy  │
│ - Benefits    │    │ - Anniversary dates   │            │ - Benefits    │
│ - Updates     │    └───────────────────────┘            │ - Procedures  │
└───────────────┘                                         └───────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Employee Database

**Google Sheet: HR Master Database**

**Sheet 1: Employee Directory**
| Column | Description |
|--------|-------------|
| A: Employee ID | Unique identifier |
| B: Full Name | Employee name |
| C: Personal Email | Pre-hire contact |
| D: Work Email | Company email |
| E: Department | Team/department |
| F: Manager | Direct supervisor |
| G: Title | Job title |
| H: Start Date | First day |
| I: Salary | Compensation |
| J: Employment Type | Full-time/Part-time/Contract |
| K: Location | Office/Remote/Hybrid |
| L: Drive Folder | Link to employee folder |
| M: Status | Active/Onboarding/Offboarded |

**Sheet 2: Onboarding Tracker**
| Column | Description |
|--------|-------------|
| A: Employee ID | Reference to directory |
| B: Name | Employee name |
| C: Start Date | First day |
| D: Offer Letter | Received/Pending |
| E: I-9 | Complete/Pending |
| F: W-4 | Complete/Pending |
| G: Direct Deposit | Complete/Pending |
| H: Emergency Contact | Complete/Pending |
| I: Handbook Signed | Complete/Pending |
| J: IT Setup | Complete/Pending |
| K: Benefits Enrolled | Complete/Pending |
| L: Day 1 Orient | Complete/Pending |
| M: 30-Day Check | Scheduled/Complete |
| N: Onboarding Status | In Progress/Complete |
| O: Notes | Additional context |

**Sheet 3: Key Dates**
| Column | Description |
|--------|-------------|
| A: Employee ID | Reference |
| B: Name | Employee name |
| C: Start Date | Anniversary date |
| D: Next Review | Scheduled review date |
| E: Benefits Renewal | Annual benefits date |
| F: Birthday | Optional celebration |

### Step 2: Create Drive Structure

```
/HR/
├── Templates/
│   ├── Offer_Letter_Template.docx
│   ├── Onboarding_Checklist.pdf
│   ├── I-9_Form.pdf
│   ├── W-4_Form.pdf
│   ├── Direct_Deposit_Form.pdf
│   ├── Emergency_Contact_Form.pdf
│   ├── Employee_Handbook.pdf
│   ├── Benefits_Guide.pdf
│   └── Welcome_Packet/
├── Policies/
│   ├── PTO_Policy.pdf
│   ├── Remote_Work_Policy.pdf
│   ├── Code_of_Conduct.pdf
│   └── Expense_Policy.pdf
├── Employees/
│   └── [Employee_Name]/
│       ├── Onboarding/
│       ├── Performance/
│       └── Documents/
└── Reports/
    ├── Monthly_Headcount/
    └── Compliance/
```

### Step 3: Configure Onboarding Workflow

**Workflow 1: New Hire Initialization**
```yaml
Trigger: Google Sheets - New row in "Incoming Employees"
  │
  ├─ Node 1: Create Employee Folder
  │    - Create folder structure in Drive
  │    - Copy template documents
  │    - Set sharing permissions
  │
  ├─ Node 2: Add to Onboarding Tracker
  │    - Create row with all pending items
  │    - Link to Drive folder
  │
  ├─ Node 3: Generate Welcome Email
  │    - Personalize from template
  │    - Include paperwork links
  │    - Include first day details
  │
  ├─ Node 4: Schedule Calendar Events
  │    - Day 1 orientation
  │    - IT setup session
  │    - HR paperwork review
  │    - Manager 1:1
  │    - 30-day check-in
  │    - 60-day check-in
  │    - 90-day review
  │
  └─ Node 5: Notify Stakeholders
       - Email to manager
       - Email to IT for setup
       - Add to HR calendar
```

**Workflow 2: Document Tracking**
```yaml
Trigger: Daily 9:00 AM
  │
  ├─ Node 1: Query Onboarding Tracker
  │    - Find employees with pending documents
  │    - Calculate days since start
  │
  ├─ Node 2: For Each Incomplete Item
  │    - Day 3: First reminder to employee
  │    - Day 5: Second reminder + CC HR
  │    - Day 7: Escalation to manager
  │
  └─ Node 3: Send Appropriate Email
       - Personalized reminder
       - Specific missing items listed
       - Direct links to forms
```

**Workflow 3: Policy Distribution**
```yaml
Trigger: Drive - New file in /HR/Policies/
  │
  ├─ Node 1: Identify Policy Type
  │    - Parse filename and content
  │    - Determine affected employees
  │
  ├─ Node 2: Generate Announcement
  │    - Summarize key changes
  │    - Include effective date
  │
  └─ Node 3: Distribute
       - Email to all employees
       - Update acknowledgment tracker
       - Schedule reminder for unacknowledged
```

### Step 4: HR Inquiry Response System

**Workflow: FAQ Auto-Response**
```yaml
Trigger: Gmail - Email to hr@company.com
  │
  ├─ Node 1: Analyze Query
  │    - Gemini: Classify question type
  │    - Match to FAQ database
  │
  ├─ Node 2: Check Confidence
  │    - High confidence: Auto-respond
  │    - Medium: Draft for HR review
  │    - Low: Forward to HR team
  │
  ├─ Node 3: Generate Response
  │    - Pull relevant policy excerpts
  │    - Personalize for employee
  │    - Include links to resources
  │
  └─ Node 4: Log Interaction
       - Record in HR inquiry sheet
       - Track common questions
```

## Example Prompts/Commands

### Welcome Email Generation
```
Generate a warm, professional welcome email for a new employee:

Employee Name: [NAME]
Start Date: [DATE]
Department: [DEPARTMENT]
Manager: [MANAGER_NAME]
Position: [TITLE]
Office Location: [LOCATION/REMOTE]

Include:
1. Enthusiastic welcome
2. Confirmation of start date and time
3. First day logistics (where to go, who to ask for)
4. Paperwork checklist with deadlines
5. Links to required forms
6. Contact information for questions
7. Expression of excitement about having them join

Tone: Warm but professional. Make them feel valued.
Length: 300-400 words.
```

### HR FAQ Response
```
An employee has asked the following question:
"[EMPLOYEE_QUESTION]"

Employee context:
- Department: [DEPARTMENT]
- Tenure: [YEARS_WITH_COMPANY]
- Employment Type: [TYPE]

Using our policy documents and guidelines, provide:
1. A clear, helpful answer
2. Reference to specific policy if applicable
3. Any relevant deadlines or steps they need to take
4. Contact information for follow-up if needed

Tone: Friendly, helpful, professional.
If this requires HR decision-making or contains sensitive information,
indicate that this should be escalated to HR team.
```

### Performance Review Reminder
```
Generate a reminder email for an upcoming performance review:

Manager: [MANAGER_NAME]
Employee: [EMPLOYEE_NAME]
Review Type: [30-day/60-day/90-day/Annual]
Scheduled Date: [DATE]
Time: [TIME]

Include:
1. Reminder of the scheduled review
2. Preparation suggestions for manager
3. Link to review template/form
4. Key areas to cover for this review type
5. Deadline for completing documentation

Tone: Supportive, encouraging thorough preparation.
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| New hire added to sheet | Full onboarding workflow | Real-time |
| Start date = Today | Day 1 welcome and checklist | Daily check |
| Document pending > 3 days | First reminder email | Daily check |
| Document pending > 5 days | Second reminder + HR CC | Daily check |
| Document pending > 7 days | Manager escalation | Daily check |
| 30 days before review | Schedule review meeting | Daily check |
| 7 days before review | Send prep materials | Daily check |
| New policy uploaded | Distribution email | Real-time |
| Email to HR inbox | FAQ auto-response attempt | Real-time |
| Monthly (1st) | Headcount report generation | Monthly |
| Employee anniversary | Recognition email + review reminder | Daily check |

## Expected Outcomes

### Quantitative Results
- **Onboarding time:** Reduced from 2 weeks to 3 days (paperwork complete)
- **HR admin time:** Reduced by 60% (15 hours/week saved)
- **Document collection rate:** 95% complete within first week
- **Policy acknowledgment:** 100% within 48 hours
- **Response time to HR queries:** Under 1 hour vs. 24+ hours

### Qualitative Benefits
- Consistent onboarding experience for all new hires
- New employees feel welcomed and prepared
- Managers receive timely notifications and reminders
- Compliance documentation automatically organized
- HR team focuses on strategic initiatives vs. admin

## ROI Estimate

### Assumptions
- HR Coordinator salary: $55,000/year ($27.50/hour)
- Current time on onboarding admin: 15 hours/week
- Post-automation admin time: 5 hours/week
- Average 2 new hires per month

### Calculation
| Metric | Value |
|--------|-------|
| Weekly time saved | 10 hours |
| Monthly time saved | 40 hours |
| Monthly labor savings | $1,100 |
| Annual labor savings | $13,200 |
| Tool costs (estimated) | $50/month |
| **Net annual ROI** | **$12,600** |

### Additional Value
- Faster time-to-productivity for new hires: ~$2,000/hire
- Reduced compliance risk: avoided penalties
- Improved employee retention from better onboarding: ~$5,000/year
- **Total annual value with 24 hires: ~$60,000+**

## Advanced Extensions

1. **Background Check Integration:** Track status and receive results
2. **Benefits Enrollment Assistant:** Guide employees through options
3. **Exit Interview Automation:** Offboarding workflow mirror
4. **Training Tracking:** Monitor required training completion
5. **Employee Self-Service Portal:** FAQ chatbot for common questions

## Sample Email Templates

### Day 1 Welcome Email
```
Subject: Welcome to [Company]! Everything You Need for Day 1 ????

Hi [First Name],

We're thrilled to officially welcome you to [Company]! Your first day is
coming up on [Start Date], and we want to make sure you have everything
you need.

?? FIRST DAY DETAILS
- Date: [Date]
- Time: [Time]
- Location: [Address/Link for remote]
- Ask for: [Greeter Name]
- What to bring: [Items]

???? PAPERWORK CHECKLIST
Please complete these before your first day:
[ ] I-9 Form - [Link] (Deadline: Day 1)
[ ] W-4 Form - [Link] (Deadline: Day 1)
[ ] Direct Deposit - [Link] (Deadline: Week 1)
[ ] Emergency Contact - [Link] (Deadline: Week 1)

???? YOUR FIRST WEEK
We've scheduled the following to help you get started:
- Day 1: Orientation with HR (9am)
- Day 1: IT Setup (10am)
- Day 1: Team Lunch (12pm)
- Day 2: [Manager] 1:1 (10am)

???? RESOURCES
- Employee Handbook: [Link]
- Benefits Guide: [Link]
- Company Directory: [Link]

Questions? Reply to this email or reach out to [HR Contact].

We can't wait to have you on the team!

Best,
[HR Name]
[Company] HR Team
```

### Missing Document Reminder
```
Subject: Friendly Reminder: Outstanding Onboarding Documents

Hi [First Name],

Hope your first few days at [Company] are going well!

I noticed we're still missing a few items from your onboarding paperwork:

??? Still needed:
[List of missing items with links]

Could you please complete these by [Deadline]? They're required for
[payroll processing/compliance/benefits enrollment].

If you're having trouble with any of the forms or have questions,
just reply to this email - I'm happy to help!

Thanks,
[HR Name]
```
