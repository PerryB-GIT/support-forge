# AI Brand Manager

## Overview

**Problem Solved:** Maintaining brand consistency across multiple channels and assets is challenging. Marketing teams struggle with on-brand content creation, asset organization, and ensuring every touchpoint reflects the brand correctly. Off-brand materials slip through, assets get lost, and brand guidelines are ignored under deadline pressure.

**Solution:** An AI brand manager that creates on-brand graphics in Canva, organizes brand assets in Drive, manages social media consistency on LinkedIn, and enforces brand guidelines automatically - ensuring cohesive brand presentation everywhere.

## Tools Used

| Tool | Purpose |
|------|---------|
| Canva | Design creation, template management, brand kit |
| Google Drive | Asset library, brand guidelines, file organization |
| LinkedIn | Social media publishing, brand presence |
| Google Sheets | Content calendar, asset inventory, audit tracking |
| Gemini | Brand voice analysis, copy review |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                      AI BRAND MANAGER WORKFLOW                       │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │         ASSET CREATION                   │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Trigger: Design Request Submitted                │
              │ (Form or Sheet entry)                            │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Parse Request:                                   │
              │ - Asset type (social/print/digital)              │
              │ - Platform/dimensions                            │
              │ - Content/messaging                              │
              │ - Campaign/project                               │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Canva: Create Design                             │
              │ - Select brand template                          │
              │ - Apply brand colors & fonts                     │
              │ - Insert requested content                       │
              │ - Export in required formats                     │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ SAVE TO       │           │ UPDATE ASSET      │           │ NOTIFY        │
│ DRIVE         │           │ INVENTORY         │           │ REQUESTOR     │
│               │           │                   │           │               │
│ /Brand/       │           │ Log in sheet:     │           │ Email with:   │
│ Assets/       │           │ - Asset details   │           │ - Preview     │
│ [Category]/   │           │ - Location        │           │ - Download    │
│               │           │ - Usage rights    │           │ - Feedback    │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │         BRAND CONSISTENCY                │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ CONTENT       │           │ VISUAL CHECK      │           │ SOCIAL        │
│ REVIEW        │           │                   │           │ PUBLISHING    │
│               │           │ Review assets:    │           │               │
│ Gemini check: │           │ - Color accuracy  │           │ Scheduled:    │
│ - Brand voice │           │ - Logo usage      │           │ - LinkedIn    │
│ - Messaging   │           │ - Font compliance │           │ - On-brand    │
│ - Tone        │           │ - Template usage  │           │ - Consistent  │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │         ASSET MANAGEMENT                 │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Continuous:                                      │
              │ - Organize new assets                            │
              │ - Update asset inventory                         │
              │ - Archive outdated materials                     │
              │ - Maintain brand guidelines doc                  │
              │ - Track asset usage                              │
              └─────────────────────────────────────────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Brand Asset Management

**Sheet 1: Asset Inventory**
| Column | Description |
|--------|-------------|
| A: Asset ID | Unique identifier |
| B: Name | Asset name |
| C: Type | Logo/Image/Template/Icon/Video |
| D: Category | Social/Print/Digital/Internal |
| E: Platform | LinkedIn/Web/Email/All |
| F: Dimensions | Size specifications |
| G: File Format | PNG/JPG/PDF/SVG |
| H: Version | Current version |
| I: Created Date | When created |
| J: Last Updated | Last modification |
| K: Created By | Who created |
| L: Status | Active/Archived/Draft |
| M: Usage Rights | Unlimited/Campaign/Restricted |
| N: Drive Link | Location in Drive |
| O: Canva Link | Canva design link |
| P: Tags | Searchable keywords |

**Sheet 2: Design Requests**
| Column | Description |
|--------|-------------|
| A: Request ID | Unique identifier |
| B: Requestor | Who submitted |
| C: Date Submitted | Request date |
| D: Asset Type | Type needed |
| E: Platform | Target platform |
| F: Description | What's needed |
| G: Copy/Text | Text content |
| H: Due Date | Deadline |
| I: Status | Pending/In Progress/Complete/Rejected |
| J: Priority | High/Medium/Low |
| K: Assigned To | Designer assigned |
| L: Asset Link | Completed asset |
| M: Feedback | Comments/revisions |
| N: Completed Date | When delivered |

**Sheet 3: Brand Guidelines Reference**
| Column | Description |
|--------|-------------|
| A: Element | Brand element |
| B: Primary | Primary value |
| C: Secondary | Secondary value |
| D: Usage Notes | How to use |
| E: Don'ts | What to avoid |
| F: Example Link | Visual example |

**Sheet 4: Content Calendar**
| Column | Description |
|--------|-------------|
| A: Date | Publish date |
| B: Platform | LinkedIn/Other |
| C: Content Type | Image/Video/Text |
| D: Topic | Post topic |
| E: Copy | Post text |
| F: Asset Link | Visual asset |
| G: Status | Draft/Approved/Published |
| H: Engagement | Post metrics |

### Step 2: Configure Asset Creation Workflow

**Workflow: Design Request Processing**
```yaml
Trigger: New row in Design Requests OR Form Submission
  │
  ├─ Node 1: Validate Request
  │    - Check required fields
  │    - Verify requestor
  │    - Assess feasibility
  │
  ├─ Node 2: Prioritize & Assign
  │    - Based on due date and priority
  │    - Assign to available designer
  │    - Set status to "In Progress"
  │
  ├─ Node 3: Get Brand Assets
  │    - Pull relevant templates from Canva
  │    - Get brand colors, fonts, logos
  │
  ├─ Node 4: Create in Canva
  │    - Select appropriate template
  │    - Apply brand elements
  │    - Insert requested content
  │
  ├─ Node 5: Brand Check
  │    - Verify color accuracy
  │    - Check logo placement
  │    - Validate font usage
  │
  ├─ Node 6: Export & Save
  │    - Export in required formats
  │    - Save to Drive structure
  │    - Update Asset Inventory
  │
  └─ Node 7: Deliver
       - Update request status
       - Email requestor with links
       - Request feedback
```

**Workflow: Quick Social Graphics**
```yaml
Trigger: Content calendar entry status = "Needs Asset"
  │
  ├─ Node 1: Get Post Details
  │    - Topic
  │    - Key message
  │    - Platform requirements
  │
  ├─ Node 2: Select Template
  │    - Match topic to template category
  │    - Get platform-specific template
  │
  ├─ Node 3: Canva Create
  │    - Use brand template
  │    - Add headline/message
  │    - Export for platform
  │
  ├─ Node 4: Save & Link
  │    - Save to /Brand/Social/[Month]/
  │    - Update calendar with asset link
  │
  └─ Node 5: Mark Ready
       - Update status to "Ready for Review"
       - Notify for approval
```

### Step 3: Brand Consistency Checks

**Workflow: Content Voice Review**
```yaml
Trigger: New content submitted for review
  │
  ├─ Node 1: Get Brand Guidelines
  │    - Voice attributes
  │    - Messaging pillars
  │    - Tone requirements
  │
  ├─ Node 2: Gemini Analysis
  │    - Analyze submitted content
  │    - Check brand voice alignment
  │    - Evaluate messaging consistency
  │    - Flag potential issues
  │
  ├─ Node 3: Generate Feedback
  │    │
  │    ├─ If On-Brand
  │    │    - Approve with notes
  │    │    - Mark ready for use
  │    │
  │    └─ If Issues Found
  │         - Specific feedback
  │         - Suggested revisions
  │         - Examples of correct usage
  │
  └─ Node 4: Update Status
       - Log review results
       - Notify submitter
```

**Workflow: Asset Audit**
```yaml
Trigger: Monthly (1st of month)
  │
  ├─ Node 1: Scan Active Assets
  │    - Get all "Active" status assets
  │    - Check last updated dates
  │
  ├─ Node 2: Identify Issues
  │    - Assets > 6 months old without review
  │    - Missing required fields
  │    - Deprecated templates used
  │
  ├─ Node 3: Check Usage
  │    - Which assets are being used
  │    - Which are never accessed
  │
  ├─ Node 4: Generate Audit Report
  │    - Assets needing refresh
  │    - Unused assets for archival
  │    - Brand consistency issues
  │
  └─ Node 5: Distribute
       - Email to brand team
       - Create action items
```

### Step 4: Social Media Management

**Workflow: LinkedIn Publishing**
```yaml
Trigger: Content calendar entry approved + scheduled time
  │
  ├─ Node 1: Get Post Content
  │    - Text copy
  │    - Image/video asset
  │    - Hashtags
  │
  ├─ Node 2: Final Brand Check
  │    - Image on-brand
  │    - Copy matches voice
  │    - Hashtags appropriate
  │
  ├─ Node 3: Publish to LinkedIn
  │    - Create company update
  │    - Attach media
  │
  ├─ Node 4: Update Calendar
  │    - Status: Published
  │    - Add post URL
  │
  └─ Node 5: Schedule Engagement Check
       - 24hr later: Capture metrics
       - Update engagement data
```

### Step 5: Asset Organization

**Drive Structure:**
```
/Brand/
├── Guidelines/
│   ├── Brand_Guidelines_Master.pdf
│   ├── Voice_and_Tone_Guide.pdf
│   ├── Visual_Identity_Guide.pdf
│   └── Quick_Reference_Card.pdf
├── Logos/
│   ├── Primary/
│   ├── Secondary/
│   ├── Icons/
│   └── Variations/
├── Templates/
│   ├── Social_Media/
│   ├── Presentations/
│   ├── Documents/
│   └── Email/
├── Assets/
│   ├── Photography/
│   ├── Illustrations/
│   ├── Icons/
│   └── Backgrounds/
├── Social/
│   ├── 2024/
│   │   ├── 01-January/
│   │   ├── 02-February/
│   │   └── .../
│   └── 2025/
├── Campaigns/
│   ├── [Campaign_Name]/
│   └── .../
└── Archive/
    └── Deprecated/
```

## Example Prompts/Commands

### Brand Voice Check
```
Analyze this content for brand voice compliance:

Content: "[CONTENT_TO_REVIEW]"
Platform: [PLATFORM]
Content Type: [TYPE]

Our brand voice is:
- Primary Attributes: [LIST - e.g., Professional, Approachable, Innovative]
- Tone: [DESCRIPTION - e.g., Confident but not arrogant]
- Language: [GUIDELINES - e.g., Avoid jargon, use active voice]
- Personality: [DESCRIPTION - e.g., Friendly expert]

Messaging Pillars:
- [PILLAR_1]
- [PILLAR_2]
- [PILLAR_3]

Evaluate:
1. Voice Alignment (1-10): How well does it match our voice?
2. Tone Appropriateness: Is the tone right for this platform/content type?
3. Message Clarity: Is the core message clear?
4. Pillar Connection: Which messaging pillar does this support?

If score < 8, provide:
- Specific issues found
- Suggested revisions
- Examples of how to improve

If score >= 8:
- Confirmation of approval
- Any minor enhancement suggestions
```

### Social Post Creation
```
Create a LinkedIn post for our brand:

Topic: [TOPIC]
Key Message: [CORE_MESSAGE]
Goal: [AWARENESS/ENGAGEMENT/TRAFFIC/LEADS]
Campaign: [CAMPAIGN_NAME if applicable]

Brand Guidelines:
- Voice: [VOICE_ATTRIBUTES]
- Audience: [TARGET_AUDIENCE]
- Style: [STYLE_NOTES]

Create:
1. Post text (under 1300 characters for optimal engagement)
   - Hook (first line to grab attention)
   - Body (value and context)
   - CTA (clear call to action)

2. Suggested hashtags (3-5 relevant)

3. Image direction (for designer):
   - Key visual concept
   - Text overlay suggestion
   - Template recommendation

Make it authentic, not salesy. Prioritize value.
```

### Asset Request Processing
```
Process this design request:

Request: "[REQUEST_DESCRIPTION]"
Requestor: [NAME]
Due Date: [DATE]
Platform: [PLATFORM]
Dimensions: [DIMENSIONS if specified]

Based on our brand templates and guidelines:

1. Template Recommendation:
   - Which Canva template to use
   - Why it's appropriate

2. Design Specifications:
   - Exact dimensions needed
   - File formats to deliver
   - Color requirements

3. Content Placement:
   - Where text should go
   - Image/logo positioning
   - Visual hierarchy

4. Quality Checklist:
   - [ ] Brand colors used correctly
   - [ ] Logo placed per guidelines
   - [ ] Fonts match brand fonts
   - [ ] Adequate white space
   - [ ] Text readable at size
   - [ ] Platform requirements met

5. Delivery Notes:
   - What files to deliver
   - Where to save in Drive
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| Design request submitted | Process and assign | Real-time |
| Content needs asset | Create quick social graphic | Real-time |
| Content submitted for review | Brand voice check | Real-time |
| Asset created | Update inventory, organize | Real-time |
| Scheduled publish time | Post to LinkedIn | Per schedule |
| 24 hrs post-publish | Capture engagement metrics | Daily |
| Monthly (1st) | Brand asset audit | Monthly |
| Quarterly (1st) | Brand guidelines review | Quarterly |

## Expected Outcomes

### Quantitative Results
- **Asset creation time:** 60% faster with templates
- **Brand consistency:** 95%+ on-brand content
- **Response time:** Design requests fulfilled in 24-48 hrs
- **Asset findability:** 100% organized and searchable
- **Social posting:** 100% consistency on schedule

### Qualitative Benefits
- Cohesive brand presence across all channels
- Empowered team to create on-brand materials
- Protected brand integrity
- Reduced design bottlenecks
- Professional, consistent customer experience

## ROI Estimate

### Assumptions
- Brand/Marketing Manager salary: $75,000/year ($37.50/hour)
- Designer salary: $65,000/year ($32.50/hour)
- Time on brand management: 15 hours/week
- Post-automation time: 6 hours/week
- Off-brand materials fixed: 5/month at 2 hrs each

### Calculation
| Metric | Value |
|--------|-------|
| Weekly time saved | 9 hours |
| Monthly time saved | 36 hours |
| Monthly labor savings (blended) | $1,260 |
| Off-brand fixes avoided | 10 hours/month |
| Fix avoidance value | $350/month |
| Monthly savings | $1,610 |
| Annual savings | $19,320 |
| Tool costs (Canva Pro + others) | $30/month |
| **Net annual ROI** | **$18,960** |

### Additional Value
- Stronger brand recognition
- More professional market presence
- Faster campaign launches
- Better design resource utilization

## Advanced Extensions

1. **Multi-Platform Publishing:** Extend to all social channels
2. **Brand Sentiment Monitoring:** Track brand mentions
3. **Competitive Analysis:** Monitor competitor branding
4. **Template Auto-Generation:** Create templates from winners
5. **Partner/Franchise Brand Control:** Ensure partner compliance

## Sample Brand Guidelines Quick Reference

```yaml
Brand Colors:
  Primary:
    - Name: Brand Blue
    - Hex: #0066CC
    - RGB: 0, 102, 204
    - Usage: Headlines, buttons, accents

  Secondary:
    - Name: Warm Gray
    - Hex: #6B7280
    - RGB: 107, 114, 128
    - Usage: Body text, secondary elements

  Accent:
    - Name: Success Green
    - Hex: #10B981
    - Usage: CTAs, positive indicators

Typography:
  Headlines: Inter Bold
  Subheads: Inter Semi-Bold
  Body: Inter Regular
  Minimum sizes: 16px body, 24px headlines

Logo Usage:
  Minimum size: 32px height
  Clear space: 1x logo height around
  Backgrounds: White, Brand Blue only
  Never: Stretch, rotate, add effects

Voice Attributes:
  - Professional but approachable
  - Confident not arrogant
  - Clear not complex
  - Helpful not pushy

Messaging Don'ts:
  - Don't use "synergy" or buzzwords
  - Don't make unsupported claims
  - Don't use ALL CAPS
  - Don't be negative about competitors
```
