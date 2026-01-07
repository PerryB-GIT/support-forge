# AI Content Creator

## Overview

**Problem Solved:** Content creation is time-consuming and inconsistent. Marketing teams struggle to maintain regular posting schedules across multiple platforms while creating engaging graphics and copy. The result: sporadic posting, mismatched branding, and missed engagement opportunities.

**Solution:** An AI content creator that generates social media posts, creates on-brand graphics in Canva, manages a content calendar in Sheets, and publishes to LinkedIn - maintaining consistent presence with minimal manual effort.

## Tools Used

| Tool | Purpose |
|------|---------|
| Google Sheets | Content calendar, idea bank, performance tracking |
| Canva | Graphic creation, brand templates |
| LinkedIn | Social publishing, engagement |
| Google Drive | Asset storage, content library |
| Gemini | Copy generation, content ideas |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                      AI CONTENT CREATOR WORKFLOW                     │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │          CONTENT PLANNING                │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Weekly: Generate Content Ideas                   │
              │ - Industry trends                                │
              │ - Evergreen topics                               │
              │ - Company updates                                │
              │ - Engagement hooks                               │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Add to Content Calendar Sheet                    │
              │ - Date/time    - Platform                       │
              │ - Topic        - Status                         │
              │ - Content type - Assigned                       │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │          CONTENT CREATION                │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ COPY          │           │ GRAPHICS          │           │ SCHEDULING    │
│               │           │                   │           │               │
│ Gemini:       │           │ Canva:            │           │ When approved:│
│ - Hook        │           │ - Create design   │           │ - LinkedIn    │
│ - Body        │           │ - Brand template  │           │   API post    │
│ - CTA         │           │ - Export image    │           │ - Track in    │
│ - Hashtags    │           │ - Save to Drive   │           │   calendar    │
└───────────────┘           └───────────────────┘           └───────────────┘
        │                             │                                 │
        └─────────────────────────────┼─────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Human Review & Approval                          │
              │ - Review copy and graphics                       │
              │ - Approve or request changes                     │
              │ - Mark as "Ready to Publish"                     │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │          AUTO-PUBLISH                    │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ At scheduled time:                               │
              │ - Post to LinkedIn                               │
              │ - Update status to "Published"                   │
              │ - Start engagement tracking                      │
              └─────────────────────────────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │          PERFORMANCE TRACKING            │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ 24-48 hours post-publish:                        │
              │ - Capture engagement metrics                     │
              │ - Update performance sheet                       │
              │ - Identify top performers                        │
              │ - Inform future content strategy                 │
              └─────────────────────────────────────────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Content Calendar Sheet

**Sheet 1: Content Calendar**
| Column | Description |
|--------|-------------|
| A: Content ID | Unique identifier |
| B: Scheduled Date | Publish date |
| C: Scheduled Time | Publish time |
| D: Platform | LinkedIn/Twitter/Facebook |
| E: Content Type | Image/Video/Text/Carousel |
| F: Topic | Content topic/theme |
| G: Hook | Opening line |
| H: Body | Main content |
| I: CTA | Call to action |
| J: Hashtags | Relevant hashtags |
| K: Image Link | Canva/Drive link |
| L: Status | Idea/Draft/Review/Approved/Published |
| M: Assigned To | Who's responsible |
| N: Post URL | Published post link |
| O: Notes | Additional context |

**Sheet 2: Idea Bank**
| Column | Description |
|--------|-------------|
| A: Idea ID | Unique identifier |
| B: Topic | Topic idea |
| C: Category | Educational/Promotional/Engagement/News |
| D: Source | Where idea came from |
| E: Target Audience | Who this is for |
| F: Content Format | Suggested format |
| G: Priority | High/Medium/Low |
| H: Used | Yes/No |
| I: Date Added | When added |

**Sheet 3: Performance Tracker**
| Column | Description |
|--------|-------------|
| A: Content ID | Reference to calendar |
| B: Platform | Where posted |
| C: Published Date | Actual publish date |
| D: Impressions | View count |
| E: Likes | Like count |
| F: Comments | Comment count |
| G: Shares | Share count |
| H: Clicks | Link clicks |
| I: Engagement Rate | Calculated rate |
| J: Top Performer | Yes/No flag |

### Step 2: Configure Content Ideation

**Workflow: Weekly Content Ideas**
```yaml
Trigger: Weekly (Sunday 6:00 PM)
  │
  ├─ Node 1: Gather Inputs
  │    - Pull industry news
  │    - Check trending topics
  │    - Review company updates
  │    - Check content performance (what worked)
  │
  ├─ Node 2: Gemini - Generate Ideas
  │    - 5-7 content ideas for the week
  │    - Mix of formats and topics
  │    - Include hooks and angles
  │
  ├─ Node 3: Add to Idea Bank
  │    - Log each idea
  │    - Set priority
  │    - Note source/inspiration
  │
  └─ Node 4: Add to Calendar
       - Schedule ideas across week
       - Assign optimal times
       - Set status to "Idea"
```

### Step 3: Content Generation Workflow

**Workflow: Content Creation**
```yaml
Trigger: New calendar entry status = "Idea"
  │
  ├─ Node 1: Get Topic Details
  │    - Topic, audience, format
  │    - Any specific requirements
  │
  ├─ Node 2: Gemini - Generate Copy
  │    │
  │    ├─ Hook (first line)
  │    │    - Attention-grabbing
  │    │    - Platform-appropriate
  │    │
  │    ├─ Body (main content)
  │    │    - Value-driven
  │    │    - Brand voice
  │    │
  │    ├─ CTA (call to action)
  │    │    - Clear next step
  │    │
  │    └─ Hashtags
  │         - 3-5 relevant tags
  │
  ├─ Node 3: Canva - Create Graphic
  │    - Select brand template
  │    - Add headline/key text
  │    - Export to Drive
  │
  ├─ Node 4: Update Calendar
  │    - Add generated copy
  │    - Link to graphic
  │    - Status = "Draft"
  │
  └─ Node 5: Notify for Review
       - Email to content approver
       - Include preview of content
```

### Step 4: Publishing Workflow

**Workflow: Auto-Publish**
```yaml
Trigger: Every 15 minutes during business hours
  │
  ├─ Node 1: Check Calendar
  │    - Status = "Approved"
  │    - Scheduled Time <= Now
  │    - Platform = LinkedIn
  │
  ├─ Node 2: For Each Ready Post
  │    │
  │    ├─ Format Content
  │    │    - Compile hook + body + CTA + hashtags
  │    │    - Format for platform character limits
  │    │
  │    └─ Get Image
  │         - Download from Drive link
  │
  ├─ Node 3: Publish to LinkedIn
  │    - Create company update
  │    - Attach image if present
  │    - Get post URL
  │
  └─ Node 4: Update Calendar
       - Status = "Published"
       - Add Post URL
       - Timestamp actual publish time
```

### Step 5: Performance Tracking

**Workflow: Engagement Metrics**
```yaml
Trigger: Daily 6:00 AM
  │
  ├─ Node 1: Get Published Posts (24-48 hrs ago)
  │    - Query calendar for recent posts
  │    - Get post URLs
  │
  ├─ Node 2: For Each Post
  │    - Fetch engagement metrics from LinkedIn
  │    - Calculate engagement rate
  │
  ├─ Node 3: Update Performance Sheet
  │    - Log all metrics
  │    - Flag top performers
  │
  └─ Node 4: Weekly Analysis (if Sunday)
       - Gemini: Analyze week's performance
       - Identify patterns
       - Suggest adjustments
       - Email report to team
```

## Example Prompts/Commands

### Content Idea Generation
```
Generate 7 LinkedIn content ideas for next week for a [COMPANY_TYPE] company.

Our audience: [TARGET_AUDIENCE]
Our tone: [BRAND_VOICE - e.g., professional but approachable]
Our goals: [AWARENESS/ENGAGEMENT/LEADS]

Recent top-performing topics:
[LIST_OF_RECENT_WINNERS]

Provide for each idea:
1. Topic/theme
2. Content angle (unique take)
3. Format recommendation (text, image, carousel)
4. Hook concept (first line idea)
5. Best day/time to post

Mix should include:
- 2 educational/how-to posts
- 2 thought leadership/opinion pieces
- 1 company culture/behind-the-scenes
- 1 engagement post (question/poll concept)
- 1 promotional/product-related (soft sell)
```

### LinkedIn Post Generation
```
Write a LinkedIn post about: [TOPIC]

Target audience: [AUDIENCE]
Goal: [EDUCATE/ENGAGE/PROMOTE]
Our brand voice: [DESCRIPTION]
Length: [SHORT (under 100 words) / MEDIUM (100-200) / LONG (200-300)]

Structure:
1. Hook (first line) - must stop the scroll
2. Body - deliver value, use line breaks for readability
3. CTA - what should reader do next?
4. Hashtags - 3-5 relevant, mix of popular and niche

Additional requirements:
- [Any specific points to include]
- [Any tone adjustments]

Format for LinkedIn - use emojis sparingly if at all, focus on clear formatting.
```

### Canva Design Instructions
```
Create a LinkedIn post image with these specifications:

Template: [BRAND_TEMPLATE_NAME]
Dimensions: 1200 x 1200 px (square) OR 1200 x 627 px (landscape)

Content:
Headline: "[HEADLINE_TEXT]"
Subtext (optional): "[SUBTEXT]"

Style:
- Use brand colors: [HEX_CODES]
- Use brand fonts: [FONT_NAMES]
- Include logo in bottom corner
- [Any specific imagery notes]

Export as PNG for upload.
```

### Performance Analysis
```
Analyze this week's LinkedIn content performance:

Posts published: [COUNT]
Total impressions: [NUMBER]
Total engagement: [NUMBER]
Average engagement rate: [PERCENTAGE]

Individual post performance:
[TABLE OF POSTS WITH METRICS]

Best performer: [POST_DETAILS]
Worst performer: [POST_DETAILS]

Provide:
1. Key insights (what worked, what didn't)
2. Content type performance comparison
3. Optimal posting time analysis
4. Recommendations for next week
5. Ideas for repurposing top performer
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| Sunday 6:00 PM | Generate weekly content ideas | Weekly |
| New calendar entry created | Generate draft copy + graphics | Real-time |
| Status changed to "Approved" | Queue for publishing | Real-time |
| Scheduled publish time reached | Publish to LinkedIn | Every 15 min |
| 48 hours post-publish | Capture engagement metrics | Daily |
| Sunday 7:00 AM | Weekly performance report | Weekly |
| Monthly (1st) | Monthly content recap | Monthly |

## Expected Outcomes

### Quantitative Results
- **Content volume:** 5-7 posts per week (vs. 1-2 inconsistent)
- **Creation time:** 30 minutes per post (vs. 2+ hours)
- **Consistency:** 100% posting schedule adherence
- **Engagement:** 40% increase within first month
- **Reach:** 3x impressions from consistent posting

### Qualitative Benefits
- Consistent brand presence
- On-brand visuals every time
- Data-driven content strategy
- Freed creative time for strategic work
- Professional, polished content

## ROI Estimate

### Assumptions
- Marketing coordinator salary: $55,000/year ($27.50/hour)
- Current content creation: 10 hours/week
- Post-automation time: 3 hours/week
- Agency alternative cost: $2,000/month for similar output

### Calculation
| Metric | Value |
|--------|-------|
| Weekly time saved | 7 hours |
| Monthly time saved | 28 hours |
| Monthly labor savings | $770 |
| Agency cost avoidance | $2,000/month |
| Monthly value | $2,770 |
| Annual value | $33,240 |
| Tool costs (Canva Pro + others) | $50/month |
| **Net annual ROI** | **$32,640** |

### Additional Value
- Increased brand awareness: leads generation
- Employee time for strategic initiatives
- Consistent employer branding for recruiting

## Advanced Extensions

1. **Multi-Platform Publishing:** Extend to Twitter, Facebook, Instagram
2. **Content Repurposing:** Automatically create variations for different platforms
3. **Trend Monitoring:** Auto-generate content around trending topics
4. **A/B Testing:** Create multiple versions and track performance
5. **Employee Advocacy:** Queue content for team members to share

## Content Strategy Templates

### Weekly Content Mix
```
Monday: Educational/How-to content
Tuesday: Industry insight/Opinion
Wednesday: Company culture/Team spotlight
Thursday: Case study/Success story
Friday: Engagement post (question/tip)
Weekend: (Optional) Inspirational quote or personal story
```

### Post Format Templates

**Educational Post:**
```
[Hook: Surprising stat or question]

Here's what [topic] really means for [audience]:

1. [Point 1]
2. [Point 2]
3. [Point 3]

The key takeaway? [Main insight]

[CTA: Question or action]

#hashtag1 #hashtag2 #hashtag3
```

**Engagement Post:**
```
[Provocative question or hot take]

I've been thinking about this a lot lately.

[2-3 sentences of context]

What's your take?

[A or B options, or open question]

#hashtag1 #hashtag2
```

**Company Culture:**
```
Behind the scenes at [Company]:

[Story or moment]

[Why this matters to us]

[What it says about our values]

Grateful to work with a team that [attribute].

#CompanyLife #hashtag
```
