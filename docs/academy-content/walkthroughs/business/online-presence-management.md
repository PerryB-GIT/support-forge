# Complete Online Presence Management with Claude MCP

> Build a unified system to manage your entire digital footprint from a single command center.

## The Big Picture

Modern businesses exist across dozens of digital touchpoints:

| Channel | Purpose | Time Required |
|---------|---------|---------------|
| Website | Core conversion point | 2-5 hours/week |
| Google Business Profile | Local discovery | 1-2 hours/week |
| Social Media | Engagement & awareness | 5-10 hours/week |
| Email Marketing | Direct communication | 3-5 hours/week |
| Review Platforms | Reputation management | 2-4 hours/week |
| Advertising | Paid acquisition | 3-5 hours/week |
| SEO | Organic discovery | 2-4 hours/week |

**Total: 18-35 hours per week** just to maintain a basic presence.

**The solution**: A unified management system that consolidates monitoring, content creation, and reporting into efficient workflows powered by Claude MCP.

---

## System Architecture

```
                        ┌─────────────────────────┐
                        │   COMMAND CENTER        │
                        │   (Google Sheets Hub)   │
                        └───────────┬─────────────┘
                                    │
        ┌───────────────┬───────────┼───────────┬───────────────┐
        │               │           │           │               │
        ▼               ▼           ▼           ▼               ▼
┌───────────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐
│  Website/SEO  │ │    GBP    │ │  Social   │ │   Email   │ │   Ads     │
│   Analytics   │ │  Reviews  │ │  Media    │ │ Marketing │ │  Campaigns│
└───────────────┘ └───────────┘ └───────────┘ └───────────┘ └───────────┘
        │               │           │           │               │
        └───────────────┴───────────┼───────────┴───────────────┘
                                    │
                        ┌───────────▼─────────────┐
                        │   CLAUDE PROCESSING     │
                        │   Content & Automation  │
                        └─────────────────────────┘
```

---

## Part 1: Building the Command Center

### Step 1: Create the Master Dashboard

**Setup request:**
```
Create a comprehensive Google Sheet called "Business Command Center" with these worksheets:

1. "Dashboard" - Executive overview
2. "Content Calendar" - Cross-platform scheduling
3. "Brand Assets" - Voice, messaging, links
4. "Review Tracker" - All platform reviews
5. "Social Metrics" - Platform performance
6. "Website Analytics" - Traffic and conversions
7. "Email Performance" - Campaign metrics
8. "Ad Performance" - Paid campaign data
9. "Competitor Watch" - Competitive intelligence
10. "Action Items" - Tasks and priorities
11. "Monthly Report" - Stakeholder summary
```

### Step 2: Dashboard Overview Setup

**Configure dashboard:**
```
Set up my Dashboard worksheet as an executive overview:

Section 1: Quick Stats (This Week)
- Website visits
- New leads/customers
- Review count and average
- Social engagement
- Email performance
- Ad spend and ROAS

Section 2: Health Indicators
- Website: Up/Down, Speed score
- GBP: Rating, response rate
- Social: Engagement rate trend
- Email: List health, deliverability
- Ads: Budget pacing

Section 3: Priority Actions
- Top 3 items needing attention
- Upcoming deadlines
- Opportunities flagged

Section 4: This Month's Goals
- Target metrics
- Progress bars
- Days remaining

Create the structure with placeholder values I'll update weekly.
```

### Step 3: Brand Assets Repository

**Setup brand guide:**
```
Create my Brand Assets worksheet:

Section: Brand Voice
- Primary tone: [Define]
- Words we use: [List]
- Words we avoid: [List]
- Sample phrases: [Examples]

Section: Key Messages
- Primary value proposition
- Secondary benefits (3-5)
- Tagline variations
- Elevator pitch (30 sec, 60 sec)

Section: Boilerplate Copy
- Company description (short: 25 words)
- Company description (medium: 50 words)
- Company description (long: 100 words)
- Founder/owner bio

Section: Links and Handles
- Website URL
- Social media links (all platforms)
- Review site links
- Contact information

Section: Visual Assets
- Logo file locations
- Brand colors (hex codes)
- Font names
- Image style guidelines
```

---

## Part 2: Content Calendar System

### Unified Content Calendar

**Setup content calendar:**
```
Configure my Content Calendar worksheet:

Columns:
- Date
- Day of Week
- Platform (GBP/LinkedIn/Email/Blog/Other)
- Content Type (Post/Story/Newsletter/Article)
- Topic/Theme
- Status (Idea/Draft/Ready/Published)
- Assigned To
- Content/Copy
- Media Needed
- Link
- Performance Notes

Default views to create:
- Weekly view (next 7 days)
- Monthly view (full month)
- By platform (filtered)
- By status (filtered)

Pre-populate with a month of placeholder entries at recommended frequencies:
- GBP: 3 posts/week
- LinkedIn: 2 posts/week
- Email: 1 newsletter/week
- Blog: 1 article/2 weeks
```

### Content Batching Workflow

**Monthly content planning:**
```
Plan next month's content across all platforms:

Business: [Your business name]
Month: [Target month]
Key dates/events: [List any relevant dates]
Promotions planned: [List any offers]
Business priorities: [What to emphasize]

Generate:
1. 12 GBP posts (3/week)
2. 8 LinkedIn posts (2/week)
3. 4 email newsletter topics
4. 2 blog article ideas

For each piece:
- Platform
- Suggested date
- Topic/headline
- Key points to cover
- Call-to-action
- Content pillar (educational/promotional/engagement/brand)

Balance the content mix: 60% value/educational, 20% engagement, 20% promotional
```

### Cross-Platform Repurposing

**Maximize content efficiency:**
```
I have this piece of content. Help me repurpose it across platforms:

Original: [Blog post about X / Email about Y / etc.]

Adapt for:
1. GBP post (under 300 characters)
2. LinkedIn post (professional tone, storytelling)
3. Email highlight (for newsletter)
4. Social media quote graphics (3 key quotes)

Maintain consistent messaging while optimizing for each platform's best practices.
```

---

## Part 3: Social Media Management

### LinkedIn Company Updates

**Post to LinkedIn:**
```
Create and post a LinkedIn company update:

Topic: [Subject]
Tone: Professional but approachable
Goal: [Awareness/Engagement/Traffic/Leads]
Include: [Any specific elements]

Generate the post, then publish using LinkedIn MCP.
```

**Claude executes:**
```
mcp__zapier__linkedin_create_company_update
Instructions: Post company update about [topic]
company_id: [Your company page ID]
comment: [Generated post content]
title: [Preview title if linking]
description: [Preview description if linking]
submitted_url: [Link if applicable]
```

### Social Monitoring Setup

**Track social engagement:**
```
Add a "Social Monitoring" worksheet:

Columns:
- Date
- Platform
- Post Type
- Content Summary
- Impressions
- Engagement (likes/comments/shares)
- Engagement Rate
- Link Clicks
- Best Performing Element
- Learnings

Create a weekly summary view showing:
- Total posts by platform
- Average engagement rate
- Best performing post
- Content type analysis
```

### Social Response Templates

**Create response library:**
```
Create a Social Response Templates section:

Comment Types:
1. Positive feedback
   - Thank you variations (5)
   - Engagement extenders (ask follow-up)

2. Questions
   - Redirect to DM template
   - Quick answer + link template
   - "Great question" acknowledgment

3. Complaints
   - Acknowledgment template
   - Move to private template
   - Resolution follow-up

4. Spam/Negative
   - Professional decline
   - Report guidance

Format each as a template I can quickly customize.
```

---

## Part 4: Review Management

### Unified Review Tracking

**Setup review tracker:**
```
Configure my Review Tracker worksheet:

Columns:
- Date
- Platform (Google/Yelp/Facebook/Industry-specific)
- Reviewer Name
- Rating (1-5)
- Review Text (summary)
- Response Status (Pending/Drafted/Responded)
- Response Date
- Response Text
- Sentiment (Positive/Neutral/Negative)
- Issues Mentioned
- Follow-up Needed

Summary section:
- Total reviews by platform
- Average rating by platform
- Response rate
- Average response time
- Sentiment breakdown
```

### Review Response Workflow

**Daily review check:**
```
Run my daily review check:

1. Check Gmail for new review notifications (GBP, Yelp, Facebook)
2. For each new review, extract:
   - Platform
   - Reviewer name
   - Rating
   - Key points
3. Add to my Review Tracker
4. Draft responses for any new reviews
5. Flag urgent reviews (1-2 stars) for immediate attention
6. Provide summary: X new reviews, Y need responses, Z are urgent
```

### Review Generation Campaign

**Systematic review building:**
```
Design a review generation system:

After-service flow:
1. Day 1: Thank you email (no ask)
2. Day 3: Satisfaction check
3. Day 7: Review request (for satisfied customers)

Templates needed:
- Thank you email
- Satisfaction check email
- Review request email (with direct link)
- Text message version of review request

Tracking:
- Add "Review Request Sent" column to customer tracking
- Track conversion: Request sent → Review received
```

---

## Part 5: Email Marketing Integration

### Newsletter System

**Weekly newsletter workflow:**
```
Run my weekly newsletter workflow:

1. Pull content from my Content Calendar for this week
2. Check my Social Monitoring for best-performing content
3. Review any news/updates from the business
4. Generate newsletter with:
   - Main story/update
   - Secondary content (from best social posts)
   - Upcoming events/promotions
   - Call-to-action
5. Create draft in Gmail
6. Update Content Calendar status

Newsletter format:
- Subject line (with A/B option)
- Preview text
- Header
- Main content (300-500 words)
- Secondary items (3 bullets)
- CTA button
- Footer
```

### Subscriber Growth Tracking

**Track email list health:**
```
Update my email list metrics in Command Center:

Weekly tracking:
- New subscribers
- Unsubscribes
- Net growth
- Total list size
- Open rate (last campaign)
- Click rate (last campaign)
- Bounce rate

Monthly analysis:
- Growth rate trend
- Engagement trend
- List quality score
- Source breakdown (where do subscribers come from)
```

---

## Part 6: Website and SEO Monitoring

### Analytics Dashboard

**Website metrics tracking:**
```
Configure my Website Analytics worksheet:

Weekly metrics:
- Total sessions
- Unique visitors
- Page views
- Bounce rate
- Average session duration
- Top 5 pages
- Top 5 traffic sources
- Conversions (leads/sales)
- Conversion rate

I'll manually input data from Google Analytics weekly.
Create the structure with formulas to calculate:
- Week-over-week changes
- Running averages
- Trend indicators
```

### SEO Health Monitoring

**SEO tracking integration:**
```
Add SEO tracking to my Command Center:

Monthly metrics from Search Console:
- Total clicks
- Total impressions
- Average CTR
- Average position
- Top 10 queries
- Top 10 pages
- Index coverage issues
- Core Web Vitals status

Create alerts for:
- Significant traffic drops (>20%)
- Position losses on key terms
- New technical issues
- Manual actions
```

---

## Part 7: Advertising Performance

### Ad Campaign Tracking

**Google Ads integration:**
```
Set up my Ad Performance worksheet:

Daily/Weekly tracking:
- Campaign name
- Status
- Budget
- Spend
- Impressions
- Clicks
- CTR
- Conversions
- Cost per conversion
- ROAS

Integrate with Google Ads MCP for automated updates.
Create summary views:
- Total spend vs budget
- Best performing campaigns
- Underperforming campaigns
- Recommendations
```

### Cross-Channel Attribution

**Track customer journey:**
```
Create a Customer Journey Tracking section:

Track touchpoints:
- First touch (how did they find us)
- Middle touches (engagement points)
- Last touch (what converted them)
- Total value

Channel attribution model:
- Organic search: X%
- Paid search: X%
- Social: X%
- Email: X%
- Direct: X%
- Referral: X%

Update monthly with insights from all platforms.
```

---

## Part 8: Competitor Intelligence

### Competitor Monitoring

**Setup competitor watch:**
```
Configure my Competitor Watch worksheet:

Competitors to track: [List 3-5 competitors]

For each competitor:
- Name
- Website URL
- Social links
- Google rating and review count
- Key differentiators
- Recent activity noted
- Strengths
- Weaknesses
- Opportunities for us

Monthly check items:
- Website changes
- New content/offers
- Review sentiment
- Social activity
- Ad presence
- Pricing changes
```

### Competitive Analysis Reports

**Quarterly competitor review:**
```
Run a quarterly competitive analysis:

Compare us vs. competitors on:
1. Online presence strength
   - Website quality
   - SEO visibility
   - Social following
   - Review ratings

2. Marketing activity
   - Content frequency
   - Ad presence
   - Email marketing (if visible)
   - Promotions

3. Customer perception
   - Review themes
   - Social sentiment
   - Common complaints
   - Praised elements

4. Opportunities
   - Gaps they're not filling
   - Weaknesses we can exploit
   - Channels they're ignoring
   - Content we can create

Summarize in my Competitor Watch worksheet.
```

---

## Part 9: Automated Workflows

### Morning Briefing

**Daily startup routine:**
```
Run my morning business briefing:

Check and report on:
1. New reviews overnight (any platform)
2. Social media mentions or messages
3. Email inquiries
4. Website contact form submissions
5. Ad budget status
6. Any scheduled content for today

Provide:
- Summary of overnight activity
- Priority items needing response
- Content scheduled for today
- Reminders for the day

Format as a quick scannable list.
```

### Weekly Review

**End of week analysis:**
```
Run my weekly online presence review:

Analyze this week:
1. Website traffic vs last week
2. Social engagement across platforms
3. Email campaign performance
4. Review activity
5. Ad performance
6. Content published vs planned

Provide:
- Week summary (5 bullet points)
- Wins this week
- Areas that need attention
- Priority actions for next week
- Update Dashboard metrics
```

### Monthly Strategy Session

**Monthly planning workflow:**
```
Run my monthly online presence strategy session:

Review last month:
1. All metrics from Command Center
2. Goals set vs achieved
3. Content performance analysis
4. ROI by channel

Plan next month:
1. Update goals based on learnings
2. Plan content themes
3. Set campaign budgets
4. Identify optimization opportunities

Deliverables:
1. Monthly report for stakeholders
2. Updated Content Calendar
3. New goals in Dashboard
4. Action items prioritized
```

---

## Part 10: Unified Reporting

### Weekly Stakeholder Update

**Generate weekly report:**
```
Generate my weekly stakeholder update:

Sections:
1. Executive Summary (3 bullets max)
2. Key Metrics This Week
   - Traffic: [X] (vs last week)
   - Leads: [X] (vs last week)
   - Reviews: [X] new, [X.X] avg rating
   - Social reach: [X]
3. Wins This Week
4. Challenges/Issues
5. Next Week's Focus
6. Action Items Needing Decision

Format: Brief, scannable, no jargon
Tone: Professional, confident, solution-oriented
```

### Monthly Executive Report

**Comprehensive monthly report:**
```
Generate my monthly executive report:

Data sources: My Command Center worksheets

Report sections:
1. Executive Summary
   - Overall performance assessment
   - Key achievements
   - Primary challenges
   - Strategic recommendations

2. Traffic & Conversions
   - Website metrics
   - Conversion funnel
   - Source analysis

3. Marketing Performance
   - Email metrics
   - Social media metrics
   - Advertising metrics
   - Content performance

4. Reputation & Reviews
   - Rating trends
   - Review volume
   - Response rates
   - Sentiment analysis

5. Competitive Position
   - Market observations
   - Competitive moves
   - Our positioning

6. Financial Summary
   - Marketing spend
   - Cost per acquisition
   - ROI by channel

7. Next Month Plan
   - Goals
   - Key initiatives
   - Resource needs
   - Expected outcomes

Format as a professional document I can share with stakeholders.
```

### Quarterly Business Review

**QBR preparation:**
```
Prepare my quarterly business review presentation:

Analyze last 3 months:
- All metrics trends
- Goal achievement rate
- Channel performance comparison
- Customer acquisition costs
- Lifetime value indicators

Strategic assessment:
- What's working well
- What needs improvement
- Market changes observed
- Competitive landscape shifts

Recommendations:
- Channel investment adjustments
- New initiatives to test
- Resources needed
- Risk factors

Next quarter planning:
- Revenue/growth targets
- Marketing budget allocation
- Key projects/campaigns
- Success metrics

Format as presentation outline with key data points.
```

---

## Part 11: Integration Patterns

### Pattern 1: Lead-to-Customer Journey

**Complete journey tracking:**
```
When I get a new lead, track their journey:

Lead info:
- Name: [Name]
- Email: [Email]
- Source: [How they found us]
- Interest: [What they want]

Actions:
1. Add to Subscriber list with segment "Lead"
2. Start nurture sequence
3. Add to Customer Journey tracking
4. Create follow-up task
5. Log source for attribution

When they convert to customer:
1. Update segment to "Customer"
2. Send to Google Ads as offline conversion
3. Add to customer list for remarketing
4. Trigger thank-you sequence
5. Schedule review request
```

### Pattern 2: Content-to-All-Platforms

**Unified content distribution:**
```
I've created a blog post. Distribute it everywhere:

Blog post: [Title]
URL: [Link]
Key points: [3-5 main ideas]
Target audience: [Description]

Create and schedule:
1. GBP post with link
2. LinkedIn post with key insight
3. Email highlight for newsletter
4. Social quote graphics (text descriptions)

Update Content Calendar with all pieces scheduled.
```

### Pattern 3: Reputation Alert System

**Crisis monitoring:**
```
Set up my reputation alert system:

Monitor for:
1. Any 1-2 star reviews (immediate alert)
2. Negative social mentions
3. Customer complaints via email
4. Website contact form complaints

When detected:
1. Alert me immediately
2. Draft initial response
3. Log in Review Tracker
4. Add to Action Items as urgent
5. Prepare escalation path if needed
```

---

## Part 12: ROI and Metrics

### Channel ROI Tracking

**Calculate ROI by channel:**
```
Calculate my online presence ROI:

Input data:
- Time spent per channel (hours/week)
- Your hourly rate: $[X]
- Tool costs: $[X]/month
- Ad spend: $[X]/month

Revenue attribution:
- Website conversions: $[X]
- Email-driven sales: $[X]
- Social-driven sales: $[X]
- Review-influenced sales: $[X]

Calculate:
- ROI by channel
- Cost per acquisition by channel
- Time efficiency by channel
- Recommendations for reallocation
```

### Efficiency Metrics

**Track time savings:**
```
Create an Efficiency Tracking worksheet:

Before Claude MCP:
- Weekly hours on online presence: [X]
- Tasks outsourced/cost: $[X]
- Campaigns per month: [X]

After Claude MCP:
- Weekly hours on online presence: [X]
- Tasks automated: [List]
- Campaigns per month: [X]

Track monthly:
- Time saved
- Cost saved
- Additional output
- Quality improvements
```

---

## Quick Reference Card

### Daily (15 minutes)
```
- Morning briefing
- Review check (respond to urgent)
- Email inbox scan
- Quick metrics glance
```

### Weekly (1 hour)
```
- Full metrics update
- Content calendar review
- Social scheduling
- Newsletter prep
- Weekly report
```

### Monthly (2 hours)
```
- Complete metrics analysis
- Content planning
- Competitive check
- Strategy adjustments
- Monthly report
```

### Quarterly (4 hours)
```
- Full business review
- Strategy planning
- Goal setting
- Resource allocation
- Stakeholder presentation
```

---

## Command Center Templates

### Morning Briefing Request
```
"Run my morning briefing for [business name]"
```

### Weekly Review Request
```
"Generate my weekly online presence review"
```

### Content Batch Request
```
"Plan next week's content across all platforms"
```

### Report Request
```
"Generate my [weekly/monthly] stakeholder report"
```

---

## Next Steps

1. **Create Command Center**: Build the master Google Sheet
2. **Populate brand assets**: Document your voice, messages, links
3. **Setup content calendar**: Plan first month of content
4. **Configure tracking**: Set up all metric tracking worksheets
5. **Establish routines**: Follow daily/weekly/monthly workflows
6. **Measure and optimize**: Track efficiency gains and ROI

---

*This guide is part of the Support Forge Academy MCP Mastery series. A unified online presence management system compounds in value over time as data accumulates and patterns emerge.*
