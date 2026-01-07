# AI Real Estate Assistant

## Overview

**Problem Solved:** Real estate agents juggle dozens of listings, hundreds of leads, and constant communication demands. Leads go cold from slow follow-up, listing information is scattered, showing schedules are chaotic, and administrative tasks eat into selling time. The result: lost deals and burned-out agents.

**Solution:** An AI real estate assistant that manages listing information in Sheets, automates lead follow-up via Gmail, schedules showings through Calendar, and maintains client communication - allowing agents to focus on closing deals rather than administrative tasks.

## Tools Used

| Tool | Purpose |
|------|---------|
| Google Sheets | Listing database, lead tracking, transaction pipeline |
| Gmail | Lead follow-up, client communication, notifications |
| Google Calendar | Showing scheduling, open houses, client meetings |
| Google Drive | Property photos, contracts, client documents |
| Gemini | Lead qualification, response drafting, analysis |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                  AI REAL ESTATE ASSISTANT WORKFLOW                   │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │           LEAD MANAGEMENT                │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Trigger: New inquiry (email, form, referral)    │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Lead Processing:                                 │
              │ - Capture contact info                           │
              │ - Identify buyer/seller                          │
              │ - Extract property interests                     │
              │ - Assess urgency/timeline                        │
              │ - Score lead quality                             │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ HOT LEAD      │           │ WARM LEAD         │           │ NURTURE       │
│ Score: 80+    │           │ Score: 50-79      │           │ Score: <50    │
│               │           │                   │           │               │
│ - Immediate   │           │ - Same day        │           │ - Drip        │
│   response    │           │   response        │           │   campaign    │
│ - Priority    │           │ - Property        │           │ - Market      │
│   scheduling  │           │   matches         │           │   updates     │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │         LISTING MANAGEMENT               │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ NEW LISTING   │           │ ACTIVE LISTING    │           │ PENDING/SOLD  │
│               │           │                   │           │               │
│ - Create      │           │ - Match to leads  │           │ - Update      │
│   materials   │           │ - Schedule        │           │   status      │
│ - Notify      │           │   showings        │           │ - Notify      │
│   leads       │           │ - Track feedback  │           │   parties     │
│ - Marketing   │           │ - Price monitor   │           │ - Documents   │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │        SHOWING COORDINATION              │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Showing Request:                                 │
              │ - Check listing availability                     │
              │ - Check agent calendar                           │
              │ - Propose times                                  │
              │ - Confirm with all parties                       │
              │ - Send reminders                                 │
              │ - Collect feedback after                         │
              └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │        TRANSACTION TRACKING              │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Under Contract:                                  │
              │ - Track deadlines (inspection, appraisal, etc.) │
              │ - Send reminders                                 │
              │ - Document collection                            │
              │ - Milestone updates to all parties               │
              │ - Closing coordination                           │
              └─────────────────────────────────────────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Real Estate Database

**Sheet 1: Lead Database**
| Column | Description |
|--------|-------------|
| A: Lead ID | Unique identifier |
| B: Name | Full name |
| C: Email | Email address |
| D: Phone | Phone number |
| E: Type | Buyer/Seller/Both |
| F: Source | Website/Referral/Sign/Ad |
| G: Status | New/Active/Nurture/Client/Closed |
| H: Score | Lead quality score |
| I: Timeline | Immediate/3mo/6mo/1yr+ |
| J: Budget/Price | Price range |
| K: Areas | Target neighborhoods |
| L: Property Type | SFH/Condo/Multi/Land |
| M: Criteria | Key requirements |
| N: Last Contact | Date of last touch |
| O: Next Action | Scheduled next step |
| P: Assigned Agent | Agent responsible |
| Q: Notes | Conversation notes |

**Sheet 2: Listing Inventory**
| Column | Description |
|--------|-------------|
| A: MLS # | MLS listing number |
| B: Address | Property address |
| C: Status | Coming Soon/Active/Pending/Sold |
| D: List Price | Asking price |
| E: Beds | Bedrooms |
| F: Baths | Bathrooms |
| G: SqFt | Square footage |
| H: Property Type | SFH/Condo/etc. |
| I: List Date | When listed |
| J: Days on Market | DOM count |
| K: Seller | Seller name |
| L: Seller Contact | Seller email/phone |
| M: Showing Instructions | Access notes |
| N: Lockbox | Lockbox code/location |
| O: Open Houses | Scheduled OHs |
| P: Photos Link | Drive folder |
| Q: Notes | Listing notes |

**Sheet 3: Showings**
| Column | Description |
|--------|-------------|
| A: Showing ID | Unique identifier |
| B: Property | MLS # or address |
| C: Client | Lead/buyer name |
| D: Date | Showing date |
| E: Time | Showing time |
| F: Duration | Expected duration |
| G: Status | Requested/Confirmed/Completed/Cancelled |
| H: Agent | Showing agent |
| I: Feedback | Post-showing feedback |
| J: Interest Level | Hot/Warm/Pass |
| K: Follow-up | Next step |
| L: Calendar Event | Event link |

**Sheet 4: Transaction Pipeline**
| Column | Description |
|--------|-------------|
| A: Transaction ID | Unique identifier |
| B: Property | Address |
| C: Client | Buyer/Seller name |
| D: Side | Buyer/Seller/Both |
| E: Contract Price | Sale price |
| F: Commission | Expected commission |
| G: Status | Active/Pending/Closed/Fell Through |
| H: Contract Date | Acceptance date |
| I: Inspection Due | Inspection deadline |
| J: Appraisal Due | Appraisal deadline |
| K: Financing Due | Loan contingency |
| L: Closing Date | Expected close |
| M: Actual Close | Actual close date |
| N: Documents | Drive folder |
| O: Notes | Transaction notes |

### Step 2: Configure Lead Management

**Workflow: New Lead Processing**
```yaml
Trigger: New form submission OR Email inquiry
  │
  ├─ Node 1: Extract Lead Info
  │    - Name, email, phone
  │    - Buyer/seller interest
  │    - Property requirements
  │    - Timeline
  │
  ├─ Node 2: Gemini Lead Scoring
  │    - Analyze inquiry urgency
  │    - Assess timeline
  │    - Evaluate motivation signals
  │    - Calculate score (0-100)
  │
  ├─ Node 3: Add to Database
  │    - Create lead record
  │    - Set status: "New"
  │    - Assign to agent
  │
  ├─ Node 4: Route by Score
  │    │
  │    ├─ Hot (80+)
  │    │    - Immediate notification to agent
  │    │    - Draft personalized response
  │    │    - Suggest property matches
  │    │
  │    ├─ Warm (50-79)
  │    │    - Add to daily follow-up queue
  │    │    - Match to listings
  │    │    - Draft intro email
  │    │
  │    └─ Nurture (<50)
  │         - Add to drip campaign
  │         - Send welcome email
  │         - Schedule periodic check-ins
  │
  └─ Node 5: Send Initial Response
       - Personalized based on inquiry
       - Include relevant listings
       - Easy reply/callback option
```

**Workflow: Lead Follow-Up Sequence**
```yaml
Trigger: Lead status = "New" OR "Active", no contact in X days
  │
  ├─ Node 1: Determine Follow-Up Needed
  │    - Hot leads: 1 day without contact
  │    - Warm leads: 3 days without contact
  │    - Nurture: 14 days without contact
  │
  ├─ Node 2: Generate Follow-Up Content
  │    - New listings matching criteria
  │    - Market updates
  │    - Personal check-in
  │
  ├─ Node 3: Draft Email
  │    - Personalized subject
  │    - Reference their search
  │    - Include value (listings, insights)
  │    - Clear CTA
  │
  └─ Node 4: Send or Queue
       - Auto-send for nurture
       - Queue for agent review (hot/warm)
```

### Step 3: Listing-Lead Matching

**Workflow: Property Matching**
```yaml
Trigger: New listing added OR Listing price change
  │
  ├─ Node 1: Get Listing Details
  │    - Price, beds, baths, area
  │    - Property type
  │    - Key features
  │
  ├─ Node 2: Match Against Leads
  │    - Price within budget (+10%)
  │    - Beds/baths meet criteria
  │    - Area in target list
  │    - Property type match
  │
  ├─ Node 3: For Each Match
  │    - Score match quality
  │    - Add to notification queue
  │
  ├─ Node 4: Generate Notifications
  │    - "New listing matching your criteria"
  │    - Property highlights
  │    - Link to details/photos
  │    - CTA to schedule showing
  │
  └─ Node 5: Send/Queue Emails
       - Hot leads: Send immediately
       - Others: Batch daily digest
```

### Step 4: Showing Management

**Workflow: Showing Request Handler**
```yaml
Trigger: Showing request email OR Form submission
  │
  ├─ Node 1: Parse Request
  │    - Property requested
  │    - Preferred times
  │    - Client info
  │
  ├─ Node 2: Check Availability
  │    - Listing availability
  │    - Agent calendar
  │    - Seller preferences
  │
  ├─ Node 3: Propose Times
  │    - 2-3 available slots
  │    - Buffer for travel
  │
  ├─ Node 4: Confirm Showing
  │    - Create calendar event
  │    - Add to Showings sheet
  │    - Notify all parties
  │
  ├─ Node 5: Pre-Showing Reminders
  │    - 24 hours: Confirmation
  │    - 2 hours: Address and details
  │
  └─ Node 6: Post-Showing Follow-Up
       - Send feedback request
       - Log results
       - Determine next steps
```

**Workflow: Showing Feedback Collection**
```yaml
Trigger: 2 hours after scheduled showing time
  │
  ├─ Node 1: Send Feedback Request
  │    - Quick rating (1-5)
  │    - Interest level
  │    - Likes/dislikes
  │    - Make offer interest
  │
  ├─ Node 2: Log Feedback
  │    - Update Showings sheet
  │    - Update lead record
  │
  ├─ Node 3: Trigger Follow-Up
  │    │
  │    ├─ If Hot Interest
  │    │    - Alert agent immediately
  │    │    - Draft offer discussion email
  │    │
  │    ├─ If Warm
  │    │    - Suggest similar properties
  │    │    - Schedule follow-up call
  │    │
  │    └─ If Pass
  │         - Note feedback
  │         - Adjust criteria
  │         - Continue search
  │
  └─ Node 4: Notify Seller (if applicable)
       - Summary of showing
       - General feedback
       - Market positioning advice
```

### Step 5: Transaction Management

**Workflow: Contract to Close Tracking**
```yaml
Trigger: Transaction status = "Pending"
  │
  ├─ Node 1: Create Transaction Record
  │    - All key dates
  │    - Parties involved
  │    - Document folder
  │
  ├─ Node 2: Set Up Deadline Reminders
  │    - Inspection: -3 days, -1 day
  │    - Appraisal: -5 days, -2 days
  │    - Financing: -7 days, -3 days
  │    - Closing: -7 days, -3 days, -1 day
  │
  ├─ Node 3: Schedule Milestone Updates
  │    - Weekly status to all parties
  │    - Immediate updates on issues
  │
  └─ Node 4: Document Tracking
       - Track received documents
       - Request missing items
       - Organize in Drive
```

## Example Prompts/Commands

### Lead Scoring and Qualification
```
Score and qualify this real estate lead:

Lead Information:
Name: [NAME]
Contact: [EMAIL/PHONE]
Source: [SOURCE]
Initial Inquiry: "[INQUIRY_TEXT]"

Assess:
1. Lead Score (0-100) based on:
   - Urgency signals (timeline, motivation)
   - Financial readiness (pre-approval, budget mention)
   - Specificity (clear criteria vs. vague)
   - Engagement level (detail in inquiry)

2. Lead Type:
   - Buyer / Seller / Investor / Both

3. Timeline Assessment:
   - Immediate (0-3 months)
   - Near-term (3-6 months)
   - Future (6-12 months)
   - Long-term (12+ months)

4. Key Criteria Extracted:
   - Price range
   - Bedrooms/bathrooms
   - Areas/neighborhoods
   - Must-haves
   - Deal-breakers

5. Recommended Next Action:
   - Immediate call
   - Same-day email with listings
   - Nurture sequence
   - Request more information

6. Suggested Response Approach:
   - Key points to address
   - Questions to ask
   - Listings to recommend
```

### Property Matching
```
Find matching leads for this listing:

Property Details:
- Address: [ADDRESS]
- Price: $[PRICE]
- Beds: [BEDS] / Baths: [BATHS]
- SqFt: [SQFT]
- Property Type: [TYPE]
- Key Features: [FEATURES]
- Neighborhood: [AREA]

Active Leads:
[LIST_OF_LEADS_WITH_CRITERIA]

Identify:
1. Perfect Matches (90%+ match):
   - Meets all criteria
   - Within budget
   - Priority notification

2. Strong Matches (70-89%):
   - Meets most criteria
   - Slight stretch (price, size, location)
   - Worth presenting

3. Possible Matches (50-69%):
   - Meets some criteria
   - May need discussion
   - Include in digest

For each match, provide:
- Match score
- What matches well
- Potential concerns
- Recommended pitch angle
```

### Showing Follow-Up Email
```
Draft a post-showing follow-up email:

Showing Details:
- Property: [ADDRESS]
- Client: [NAME]
- Date: [DATE]
- Agent Observations: [NOTES]

Their Feedback (if received):
[FEEDBACK]

Their Overall Interest: [HOT/WARM/COLD]

Generate an email that:
1. Thanks them for their time
2. References specific observations (what they liked)
3. Addresses any concerns mentioned
4. Provides next steps based on interest level:
   - If Hot: Offer discussion, comparable sales
   - If Warm: Similar properties, keep searching
   - If Cold: Refine criteria, different options
5. Clear call to action

Tone: [AGENT'S TYPICAL TONE]
Length: Keep concise (under 200 words)
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| New lead inquiry | Process, score, respond | Real-time |
| Lead no contact (varies by score) | Follow-up sequence | Daily check |
| New listing added | Match to leads, notify | Real-time |
| Listing price change | Re-match, notify | Real-time |
| Showing requested | Schedule, confirm | Real-time |
| 24 hrs before showing | Send reminder | Event-based |
| 2 hrs after showing | Request feedback | Event-based |
| Transaction milestone approaching | Send reminders | Daily check |
| Weekly Friday | Weekly activity summary | Weekly |

## Expected Outcomes

### Quantitative Results
- **Lead response time:** Under 5 minutes (vs. hours)
- **Follow-up compliance:** 100% (vs. 40%)
- **Showings scheduled:** 2x increase
- **Administrative time:** 60% reduction
- **Lead-to-client conversion:** 30% improvement

### Qualitative Benefits
- No leads fall through cracks
- Consistent, professional communication
- Better client experience
- More time for high-value activities
- Organized transaction management

## ROI Estimate

### Assumptions
- Agent income: $100,000/year
- Average commission: $10,000/transaction
- Current transactions: 15/year
- Time on admin: 25 hours/week
- Post-automation: 10 hours/week

### Calculation
| Metric | Value |
|--------|-------|
| Weekly time saved | 15 hours |
| Additional selling time | 60 hours/month |
| Additional transactions (est.) | 3/year |
| Additional revenue | $30,000 |
| Tool costs (estimated) | $100/month |
| **Net annual ROI** | **$28,800** |

### Additional Value
- Better client retention and referrals
- Reduced stress and burnout
- Competitive advantage in responsiveness

## Advanced Extensions

1. **MLS Integration:** Auto-sync listings and status
2. **Showing Feedback Analysis:** Pattern recognition across showings
3. **Market Analytics:** AI-powered pricing recommendations
4. **Client Portal:** Self-service showing scheduling
5. **Transaction Coordinator:** Full closing management

## Sample Lead Scoring Matrix

```yaml
Lead Score Components (0-100 total):

Timeline (0-30 points):
  - Immediate (30)
  - 3 months (25)
  - 6 months (15)
  - 12 months (5)
  - Just looking (0)

Financial Readiness (0-25 points):
  - Pre-approved + proof (25)
  - Pre-approved (20)
  - Spoken to lender (15)
  - Stated budget (10)
  - No mention (0)

Specificity (0-20 points):
  - Exact criteria known (20)
  - General requirements (15)
  - Basic parameters (10)
  - Vague interest (5)

Engagement (0-15 points):
  - Multiple properties viewed (15)
  - Detailed questions asked (10)
  - Basic inquiry (5)

Source Quality (0-10 points):
  - Referral (10)
  - Direct contact (8)
  - Website signup (5)
  - Third-party lead (3)

Score Interpretation:
  - 80-100: Hot - Immediate personal attention
  - 50-79: Warm - Same-day response, regular follow-up
  - 30-49: Nurture - Drip campaign, monthly check-in
  - 0-29: Long-term - Quarterly updates, market info
```
