# Google Search Console SEO Mastery with Claude

> Transform raw search data into actionable SEO strategies using intelligent analysis and automated monitoring.

## Why Search Console Matters

Google Search Console (GSC) is your direct line to understanding how Google sees your website:

| Data Point | Business Impact |
|------------|-----------------|
| Search queries | Know exactly what brings people to your site |
| Click-through rates | Identify optimization opportunities |
| Indexing status | Catch technical issues before they hurt rankings |
| Core Web Vitals | Page experience directly affects rankings |
| Mobile usability | Mobile-first indexing means mobile issues = ranking issues |

**The challenge**: GSC provides mountains of data but no actionable insights. Most businesses export data, look at it once, and never act on it.

**The solution**: Systematic data extraction, intelligent analysis, and automated monitoring workflows.

---

## Integration Architecture

Google Search Console doesn't have a direct MCP integration, but we create powerful SEO systems using:

```
[GSC Manual Export] → [Google Sheets] → [Claude Analysis] → [Action Items]
                                              ↓
                                    [Tracking Dashboard]
                                              ↓
                                    [Automated Alerts]
```

---

## Part 1: Setting Up Your SEO Dashboard

### Step 1: Create the Master SEO Dashboard

**Setup request:**
```
Create a Google Sheet called "SEO Command Center" with these worksheets:

1. "Weekly Performance" - columns: Week Starting, Total Clicks, Total Impressions,
   Average CTR, Average Position, Week-over-Week Change

2. "Top Queries" - columns: Query, Clicks, Impressions, CTR, Position,
   Trend (up/down/stable), Priority Action

3. "Page Performance" - columns: Page URL, Clicks, Impressions, CTR,
   Average Position, Issues, Optimization Notes

4. "Keyword Tracking" - columns: Target Keyword, Current Position,
   Previous Position, Change, Target Page, Last Updated

5. "Technical Issues" - columns: Issue Type, Affected URLs,
   First Detected, Status, Resolution Date, Notes

6. "Content Opportunities" - columns: Query, Impressions, Current CTR,
   Potential CTR, Estimated Click Gain, Content Action, Priority

7. "Competitor Keywords" - columns: Keyword, Our Position, Search Volume Est.,
   Content Gap, Action Plan
```

### Step 2: Export GSC Data

**Manual export instructions** (do this weekly):

1. Go to [Search Console](https://search.google.com/search-console)
2. Select your property
3. Navigate to **Performance** > **Search results**
4. Set date range to **Last 28 days** (or Last 7 days for weekly)
5. Click **Export** > **Google Sheets**
6. Repeat for **Pages** and **Queries** tabs

### Step 3: Process Exported Data

**After export, request:**
```
I've exported my GSC data to a sheet called "Search Console Export - [Date]".
Process this data and:
1. Update my "Weekly Performance" summary
2. Identify top 20 queries by impressions and update "Top Queries"
3. Find pages with high impressions but low CTR (under 2%)
4. Flag any significant position changes (>3 positions up or down)
5. Add opportunities to "Content Opportunities" worksheet
```

---

## Part 2: Keyword Tracking and Analysis

### Setting Up Keyword Tracking

**Initial setup:**
```
I want to track these target keywords for my business:
- [keyword 1]
- [keyword 2]
- [keyword 3]
- [keyword 4]
- [keyword 5]

For each keyword, set up tracking in my "Keyword Tracking" worksheet:
1. Add the keyword
2. Set current position to "Not tracked yet"
3. Add the target page URL
4. Mark today as "Last Updated"
```

### Weekly Keyword Position Update

**Update workflow:**
```
I've just exported my GSC query data. Update my keyword tracking:

Data from export:
[Paste query data]

For each tracked keyword:
1. Update current position
2. Calculate change from previous position
3. Flag any keywords that dropped more than 3 positions
4. Identify any new keywords ranking in top 20 that I'm not tracking
```

### Keyword Opportunity Analysis

**Find new opportunities:**
```
Analyze my GSC query data for keyword opportunities:

Look for queries where:
1. Position is 8-20 (page 1 potential with optimization)
2. Impressions > 100 (meaningful search volume)
3. CTR < 3% (room for title/description improvement)

For each opportunity, suggest:
- Content optimization action
- Title tag improvement
- Meta description improvement
- Priority score (1-5)
```

**Example analysis request:**
```
Here's my query data from GSC:
[Paste data]

Find queries ranking positions 4-10 with:
- At least 500 impressions
- CTR below average for that position

These are my biggest quick wins - what content improvements would help each one?
```

---

## Part 3: CTR Optimization

### Understanding CTR Benchmarks

Position-based CTR benchmarks to measure against:

| Position | Expected CTR | Action if Below |
|----------|--------------|-----------------|
| 1 | 25-35% | Optimize title for engagement |
| 2 | 15-20% | Strong title, check SERP features |
| 3 | 10-15% | Title and description optimization |
| 4-5 | 5-10% | Content depth, featured snippet attempt |
| 6-10 | 2-5% | Major content upgrade needed |

### CTR Analysis Workflow

**Weekly CTR check:**
```
Analyze my top 50 pages by impressions for CTR performance:

[Paste GSC page data]

For each page:
1. Compare actual CTR to expected CTR for that position
2. Calculate CTR gap (expected - actual)
3. Prioritize pages by: (CTR gap * impressions) = opportunity score
4. List top 10 pages needing title/description optimization
```

### Title Tag Optimization

**Generate improved titles:**
```
These pages have below-average CTR for their position.
Generate improved title tags for each:

1. Page: /services/web-design
   Current title: "Web Design Services"
   Query: "professional web design services"
   Position: 4, CTR: 2.1% (expected: 7%)

2. Page: /blog/seo-guide
   Current title: "SEO Guide 2024"
   Query: "complete seo guide"
   Position: 6, CTR: 1.5% (expected: 4%)

For each, provide:
- New title (under 60 characters)
- Reasoning for the change
- Expected CTR improvement
```

### Meta Description Optimization

**Batch description generation:**
```
Generate compelling meta descriptions for these high-impression, low-CTR pages:

[List of pages with current descriptions]

Each description should:
- Be under 155 characters
- Include primary keyword naturally
- Have a clear value proposition
- Include a subtle call-to-action
- Create curiosity or urgency
```

---

## Part 4: Technical SEO Monitoring

### Coverage Issues Tracking

**Process coverage report:**
```
I've exported my GSC Coverage report. Analyze for critical issues:

[Paste coverage data]

Prioritize issues by:
1. Errors (highest priority)
2. Excluded pages that shouldn't be excluded
3. Valid with warnings

For each issue type, provide:
- Impact assessment
- Recommended fix
- Implementation difficulty
```

### Core Web Vitals Monitoring

**Setup CWV tracking:**
```
Add a "Core Web Vitals" worksheet to my SEO Command Center:

Columns:
- Date Checked
- LCP (Largest Contentful Paint) - Mobile
- LCP - Desktop
- FID/INP (Interaction) - Mobile
- FID/INP - Desktop
- CLS (Layout Shift) - Mobile
- CLS - Desktop
- Passing URLs
- Needs Improvement
- Poor URLs
- Priority Fixes

I'll update this monthly from GSC. Help me interpret the data each time.
```

**CWV analysis request:**
```
Analyze my Core Web Vitals from GSC:
- LCP: 3.2s (Poor)
- INP: 180ms (Needs Improvement)
- CLS: 0.08 (Good)
- Poor URLs: 15
- Needs Improvement: 42
- Good: 198

What are the likely causes and prioritized fixes?
```

### Mobile Usability Tracking

**Process mobile issues:**
```
My GSC mobile usability report shows these issues:
[Paste issues]

For each issue:
1. Explain the SEO impact
2. Provide specific fix instructions
3. Estimate fix complexity (easy/medium/hard)
4. Suggest testing method after fix
```

---

## Part 5: Content Performance Analysis

### Top Pages Analysis

**Monthly content review:**
```
Analyze my top 25 pages by organic traffic from GSC:

[Paste page data]

For each page, evaluate:
1. Traffic trend (growing, stable, declining)
2. Primary ranking queries
3. CTR vs position benchmark
4. Content freshness (if you can tell from URL/title)
5. Recommended action (update, expand, leave, consolidate)
```

### Content Decay Detection

**Find declining content:**
```
Compare my GSC data from this month vs. 3 months ago:

This month: [Paste current data]
3 months ago: [Paste historical data]

Identify content decay:
1. Pages that lost >20% traffic
2. Pages that dropped >5 positions
3. Pages with declining CTR

For each declining page:
- Diagnose likely cause
- Recommend update strategy
- Priority score (based on potential traffic recovery)
```

### Content Gap Analysis

**Find what's missing:**
```
Analyze my GSC query data to find content gaps:

[Paste query data]

Look for:
1. Queries with high impressions but no dedicated page
2. Queries where I rank for a general page but could rank higher with targeted content
3. Question queries I don't address directly
4. Long-tail variations I could target

For each gap, suggest:
- Content type (blog post, landing page, FAQ addition)
- Target keyword
- Suggested title
- Key points to cover
```

---

## Part 6: Automated Monitoring Workflows

### Weekly SEO Check

**Setup weekly routine:**
```
Create a "Weekly SEO Checklist" in my dashboard with these items:

Every Monday:
[ ] Export GSC performance data (last 7 days)
[ ] Export GSC query data
[ ] Export GSC page data
[ ] Check for new coverage errors
[ ] Review security issues (if any)

After export, run analysis:
[ ] Update Weekly Performance summary
[ ] Flag any pages with >20% traffic change
[ ] Identify new ranking keywords
[ ] Update keyword position tracking
[ ] Add new content opportunities
```

**Weekly analysis request:**
```
Run my weekly SEO analysis:

Performance data: [Paste]
Query data: [Paste]
Page data: [Paste]

Provide:
1. Week-over-week performance summary
2. Top 5 gains this week
3. Top 5 losses this week
4. New keyword opportunities discovered
5. Priority actions for this week (max 3)
```

### Monthly SEO Report

**Comprehensive monthly analysis:**
```
Generate my monthly SEO report from GSC data:

This month: [Paste data]
Previous month: [Paste data]

Report sections:
1. Executive Summary (3-5 bullet points)
2. Traffic Performance (clicks, impressions, CTR, position)
3. Top 10 Performing Pages
4. Top 10 Growing Keywords
5. Issues and Declines
6. Technical Health Update
7. Recommendations for Next Month
8. Goals for Next 30 Days

Format as a report I can share with stakeholders.
```

### Alert System

**Setup monitoring alerts:**
```
Create an "SEO Alerts" worksheet with these columns:
- Date
- Alert Type
- Severity (High/Medium/Low)
- Details
- Status
- Resolution

Alert triggers I want to track:
1. Any page loses >50% traffic week-over-week
2. New coverage errors appear
3. Core Web Vitals move from Good to Poor
4. Top 10 keyword drops out of top 20
5. Site-wide CTR drops >10%
6. Manual action detected

When I do weekly checks, help me populate this based on the data.
```

---

## Part 7: Integration Patterns

### Pattern 1: GSC + Google Ads Integration

**Connect search data:**
```
Cross-reference my GSC query data with Google Ads:

GSC queries (organic): [Paste]
Google Ads keywords: [Paste from Ads export]

Identify:
1. High-performing organic keywords I'm not bidding on
2. Keywords where I rank #1 organically (reduce ad spend?)
3. Keywords where I rank poorly but ads perform well (content opportunity)
4. Search intent alignment between organic and paid

Update my "Keyword Strategy" worksheet with recommendations.
```

### Pattern 2: GSC + Content Calendar

**Plan content from data:**
```
Based on my GSC content gap analysis, create a content calendar:

Gaps identified:
[List of keyword gaps]

Create a 12-week content plan in my "Content Calendar" worksheet:
- Week
- Target Keyword
- Content Type
- Working Title
- Word Count Target
- Status
- Publish Date
- Post-Publish: Track GSC metrics

Prioritize by: Search volume estimate * ranking potential
```

### Pattern 3: GSC + Client Reporting

**Generate client reports:**
```
Generate an SEO report for my client using their GSC data:

Client: [Name]
Website: [URL]
Reporting period: Last 30 days
Previous period: 30 days before that

Data: [Paste GSC export]

Create a professional report with:
1. Performance highlights (celebrate wins)
2. Key metrics with trend indicators
3. Top performing content
4. Keyword ranking improvements
5. Technical health status
6. Recommended next steps
7. Goals for next month

Tone: Professional but accessible to non-technical readers
```

---

## Part 8: Advanced SEO Strategies

### Featured Snippet Optimization

**Find snippet opportunities:**
```
Analyze my GSC data for featured snippet opportunities:

[Paste query data]

Look for:
1. Question queries where I rank positions 2-10
2. "How to" queries with high impressions
3. Definition queries
4. Comparison queries
5. List-based queries

For each opportunity:
- Current page ranking
- Current position
- Content modification needed
- Snippet format to target (paragraph, list, table)
```

### Cannibalization Detection

**Find competing pages:**
```
Analyze my GSC data for keyword cannibalization:

[Paste query data with pages]

Identify queries where:
1. Multiple pages from my site rank
2. Clicks are split between pages
3. Pages compete for similar queries

For each cannibalization issue:
- List the competing pages
- Recommend: Merge, redirect, or differentiate
- Suggest primary page to consolidate to
```

### Seasonal SEO Planning

**Plan for seasonality:**
```
Analyze my GSC data across multiple months to identify seasonal patterns:

Month 1 data: [Paste]
Month 2 data: [Paste]
Month 3 data: [Paste]

Identify:
1. Keywords with strong seasonal patterns
2. Pages that perform better in certain months
3. Upcoming seasonal opportunities to prepare for

Create a seasonal SEO calendar noting:
- When to publish seasonal content
- When to update existing seasonal pages
- When to increase internal linking to seasonal pages
```

---

## Part 9: Workflow Automation

### Daily Quick Check (2 minutes)

```
Quick GSC check items:
1. Any new security or manual action alerts?
2. Significant coverage errors?
3. Server errors in last 24 hours?

If I report any issues, help me prioritize and create action items.
```

### Weekly Deep Dive (30 minutes)

```
Run my weekly GSC deep dive:

1. Export and paste: Performance overview
2. Export and paste: Top queries (last 7 days)
3. Export and paste: Top pages (last 7 days)
4. Note any new coverage issues

I'll paste each in sequence. After all data is provided:
- Update my SEO Command Center
- Highlight the 3 most important findings
- Assign action items with priority
```

### Monthly Strategy Session (1 hour)

```
Conduct my monthly SEO strategy session:

Data to analyze:
- Full month GSC export: [Paste]
- Previous month comparison: [Paste]
- Core Web Vitals current status: [Describe]
- Coverage report summary: [Describe]
- Actions completed this month: [List]

Session agenda:
1. Review last month's goals - did we hit them?
2. Analyze performance trends
3. Evaluate content performance
4. Review technical health
5. Set 3 specific goals for next month
6. Create prioritized action list
7. Update keyword tracking priorities
```

---

## Part 10: ROI Measurement

### Tracking SEO Value

**Setup ROI tracking:**
```
Add "SEO ROI Tracking" to my SEO Command Center:

Columns:
- Month
- Organic Clicks (from GSC)
- Estimated Value per Click ($)
- Total Organic Traffic Value
- Time Invested (hours)
- Tools/Content Cost
- Net SEO Value
- YoY Growth %

Help me calculate: If my average conversion rate is 2.5% and average order value
is $150, what's each organic click worth?
```

### Value Per Keyword

**Calculate keyword value:**
```
Calculate the value of my top ranking keywords:

For each keyword in my tracking list:
1. Monthly clicks (from GSC)
2. Estimated CPC (I'll provide or estimate)
3. Monthly value if I had to pay for those clicks
4. Annual organic value

This helps justify SEO investment and prioritize keywords.
```

### Competitive Value Analysis

**Understand competitive position:**
```
Estimate the competitive value of my organic rankings:

My top 20 keywords: [List with positions and clicks]

If competitors rank #1 for these keywords and I don't:
- What traffic am I missing?
- What's the opportunity cost?

If I rank #1:
- What's the defensive value?
- What would it cost competitors to displace me?
```

---

## Quick Reference Card

### Weekly Data Exports
```
GSC > Performance > Last 7 days > Export
GSC > Pages > Last 7 days > Export
GSC > Queries > Last 7 days > Export
```

### Key Metrics to Track
```
- Clicks (traffic)
- Impressions (visibility)
- CTR (engagement)
- Position (rankings)
- Coverage errors (technical)
- Core Web Vitals (UX)
```

### Priority Actions by Metric

**Declining Clicks:**
```
1. Check position changes
2. Review CTR trends
3. Look for algorithm updates
4. Audit technical issues
```

**Low CTR:**
```
1. Optimize title tags
2. Improve meta descriptions
3. Add structured data
4. Check SERP competition
```

**Position Drops:**
```
1. Content freshness update
2. Build internal links
3. Improve page experience
4. Check for technical issues
```

---

## Next Steps

1. **Create dashboard**: Set up your SEO Command Center in Sheets
2. **Export baseline**: Get your first GSC data export
3. **Establish tracking**: Set up keyword position tracking
4. **Find quick wins**: Run CTR analysis for immediate opportunities
5. **Build routine**: Follow weekly and monthly workflows

---

*This guide is part of the Support Forge Academy MCP Mastery series. SEO is a long-term investment - consistent monitoring and optimization compound over time.*
