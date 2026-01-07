# AI SEO Manager

## Overview

**Problem Solved:** SEO is complex and time-consuming. Businesses struggle to track keyword rankings, identify optimization opportunities, monitor competitor movements, and create SEO-optimized content. The result: missed organic traffic, wasted content efforts, and poor search visibility.

**Solution:** An AI SEO manager that tracks keyword rankings in Google Sheets, analyzes content for optimization opportunities, generates SEO-focused content briefs, and produces regular performance reports - turning SEO from guesswork into a systematic process.

## Tools Used

| Tool | Purpose |
|------|---------|
| Google Sheets | Keyword tracking, ranking data, content inventory |
| Google Drive | Content briefs, reports, documentation |
| Gmail | Alerts, reports, team notifications |
| Gemini | Content optimization, keyword analysis, brief generation |
| n8n | Workflow orchestration |
| Code by Zapier | Custom data processing, API calls |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                       AI SEO MANAGER WORKFLOW                        │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │         KEYWORD TRACKING                 │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Daily/Weekly: Track Keyword Rankings            │
              │ - Target keywords list                          │
              │ - Current position                              │
              │ - Position change                               │
              │ - Search volume                                 │
              │ - Ranking URL                                   │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ IMPROVED      │           │ STABLE            │           │ DECLINED      │
│ Position up   │           │ No significant    │           │ Position down │
│               │           │ change            │           │               │
│ Action:       │           │ Action:           │           │ Action:       │
│ - Log win     │           │ - Monitor         │           │ - Alert team  │
│ - Analyze why │           │ - Consider push   │           │ - Analyze why │
└───────────────┘           └───────────────────┘           │ - Create fix  │
                                                            │   task        │
                                                            └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │       CONTENT OPTIMIZATION               │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Content Audit Workflow                           │
              │ - Analyze existing pages                         │
              │ - Identify optimization opportunities            │
              │ - Generate recommendations                       │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ For Each Page:                                   │
              │ - Title tag optimization                         │
              │ - Meta description                               │
              │ - Header structure (H1, H2s)                     │
              │ - Keyword density                                │
              │ - Internal linking opportunities                 │
              │ - Content gaps                                   │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Output: Prioritized optimization tasks           │
              └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │        CONTENT BRIEF GENERATION          │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Trigger: New target keyword added                │
              │                                                  │
              │ Generate:                                        │
              │ - Primary & secondary keywords                   │
              │ - Search intent analysis                         │
              │ - Competitor content analysis                    │
              │ - Recommended outline                            │
              │ - Target word count                              │
              │ - Internal linking suggestions                   │
              │ - FAQ section ideas                              │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Save brief to Drive + Email to content team      │
              └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │          REPORTING & ALERTS              │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ Daily Alert   │           │ Weekly Report     │           │ Monthly       │
│ - Ranking     │           │ - Traffic trends  │           │ Analysis      │
│   changes     │           │ - Top performers  │           │ - Deep dive   │
│ - Issues      │           │ - Opportunities   │           │ - Strategy    │
│   detected    │           │ - Tasks completed │           │   recommendations│
└───────────────┘           └───────────────────┘           └───────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up SEO Tracking Sheets

**Sheet 1: Keyword Tracker**
| Column | Description |
|--------|-------------|
| A: Keyword | Target keyword |
| B: Search Volume | Monthly searches |
| C: Difficulty | Competition level (1-100) |
| D: Priority | High/Medium/Low |
| E: Current Position | Today's ranking |
| F: Previous Position | Last check position |
| G: Change | Position change (+/-) |
| H: Best Position | Historical best |
| I: Target URL | Page we're optimizing |
| J: Last Updated | Timestamp |
| K: Status | Tracking/Achieved/Lost |
| L: Notes | Context/strategy notes |

**Sheet 2: Ranking History**
| Column | Description |
|--------|-------------|
| A: Date | Check date |
| B: Keyword | Target keyword |
| C: Position | Ranking that day |
| D: URL | Page ranking |
| E: SERP Features | Featured snippet, etc. |

**Sheet 3: Content Inventory**
| Column | Description |
|--------|-------------|
| A: URL | Page URL |
| B: Title | Current title tag |
| C: Primary Keyword | Target keyword |
| D: Secondary Keywords | Supporting keywords |
| E: Word Count | Content length |
| F: Last Updated | Content update date |
| G: Organic Traffic | Monthly organic visits |
| H: Ranking Keywords | Keywords ranking for |
| I: Optimization Score | 1-100 health score |
| J: Priority | Optimization priority |
| K: Status | Optimized/Needs Work/New |

**Sheet 4: Optimization Tasks**
| Column | Description |
|--------|-------------|
| A: Task ID | Unique identifier |
| B: URL | Page to optimize |
| C: Task Type | Title/Meta/Content/Links |
| D: Description | What needs to be done |
| E: Priority | High/Medium/Low |
| F: Assigned To | Team member |
| G: Status | To Do/In Progress/Done |
| H: Due Date | Target completion |
| I: Impact Estimate | Expected improvement |

### Step 2: Configure Keyword Tracking

**Workflow: Daily Rank Tracking**
```yaml
Trigger: Daily 6:00 AM
  │
  ├─ Node 1: Get Keyword List
  │    - Pull from Keyword Tracker sheet
  │    - Filter to "Tracking" status
  │
  ├─ Node 2: For Each Keyword
  │    │
  │    ├─ Check Current Ranking
  │    │    - Use rank tracking API or scraping
  │    │    - Get position, URL, SERP features
  │    │
  │    └─ Compare to Previous
  │         - Calculate position change
  │         - Identify significant moves (+/- 5)
  │
  ├─ Node 3: Update Sheets
  │    - Log to Ranking History
  │    - Update Keyword Tracker current positions
  │
  ├─ Node 4: Flag Significant Changes
  │    - Improved +10 or more: Win!
  │    - Dropped -10 or more: Alert!
  │    - Entered top 10: Milestone!
  │    - Lost page 1: Priority fix!
  │
  └─ Node 5: Send Daily Summary
       - Email with changes
       - Highlight wins and concerns
```

### Step 3: Content Optimization Workflow

**Workflow: Page Analysis**
```yaml
Trigger: New URL added to Content Inventory OR Weekly scan
  │
  ├─ Node 1: Fetch Page Content
  │    - Get HTML content
  │    - Extract text, headers, meta tags
  │
  ├─ Node 2: Gemini Analysis
  │    - Analyze against target keyword
  │    - Check title tag optimization
  │    - Evaluate meta description
  │    - Assess header structure
  │    - Calculate keyword usage
  │    - Identify missing elements
  │
  ├─ Node 3: Score Content
  │    - Title: 0-20 points
  │    - Meta: 0-15 points
  │    - Headers: 0-15 points
  │    - Content depth: 0-25 points
  │    - Internal links: 0-15 points
  │    - Technical: 0-10 points
  │    - Total: Optimization Score
  │
  ├─ Node 4: Generate Recommendations
  │    - Specific, actionable tasks
  │    - Priority ranking
  │    - Expected impact
  │
  └─ Node 5: Update Sheets
       - Update Content Inventory
       - Create tasks in Optimization Tasks
       - Alert team if score < 50
```

### Step 4: Content Brief Generation

**Workflow: SEO Brief Creator**
```yaml
Trigger: New keyword added with "Create Brief" flag
  │
  ├─ Node 1: Keyword Research
  │    - Get search volume, difficulty
  │    - Find related keywords
  │    - Identify questions (PAA)
  │
  ├─ Node 2: Competitor Analysis
  │    - Analyze top 5 ranking pages
  │    - Extract common topics
  │    - Identify content gaps
  │    - Note word counts, formats
  │
  ├─ Node 3: Gemini - Generate Brief
  │    - Search intent analysis
  │    - Recommended outline
  │    - Key topics to cover
  │    - Questions to answer
  │    - Internal linking opportunities
  │    - Target specifications
  │
  ├─ Node 4: Create Document
  │    - Format as Google Doc
  │    - Save to Drive /SEO/Briefs/
  │
  └─ Node 5: Notify Team
       - Email brief to content writer
       - Add to content calendar
       - Create tracking entry
```

### Step 5: Reporting Automation

**Workflow: Weekly SEO Report**
```yaml
Trigger: Weekly Monday 8:00 AM
  │
  ├─ Node 1: Compile Metrics
  │    - Keyword ranking changes
  │    - Top performers
  │    - Biggest drops
  │    - New rankings achieved
  │
  ├─ Node 2: Content Performance
  │    - Pages gaining traffic
  │    - Pages losing traffic
  │    - Optimization tasks completed
  │
  ├─ Node 3: Gemini Analysis
  │    - Summarize week's performance
  │    - Identify trends
  │    - Recommend priorities
  │
  ├─ Node 4: Create Report
  │    - Executive summary
  │    - Key metrics table
  │    - Priority actions
  │    - Save to Drive
  │
  └─ Node 5: Distribute
       - Email to stakeholders
       - Include action items
```

## Example Prompts/Commands

### Page SEO Analysis
```
Analyze this webpage for SEO optimization:

URL: [URL]
Target Keyword: [KEYWORD]
Current Ranking: [POSITION]

Page Content:
Title Tag: [TITLE]
Meta Description: [META]
H1: [H1]
H2s: [LIST]
Word Count: [COUNT]
Main Content: [FIRST_500_WORDS]

Evaluate and score (out of 100):
1. Title tag optimization (keyword placement, length, appeal)
2. Meta description (keyword, CTA, length 150-160 chars)
3. Header structure (H1 unique, H2 keywords, hierarchy)
4. Content depth (comprehensive coverage, keyword usage)
5. On-page elements (images, internal links, schema opportunities)

For each area, provide:
- Current score
- Specific issues found
- Exact recommendations with examples
- Priority level (High/Medium/Low)
- Expected impact on rankings
```

### Content Brief Generation
```
Create a comprehensive SEO content brief for:

Target Keyword: [PRIMARY_KEYWORD]
Search Volume: [VOLUME]
Keyword Difficulty: [SCORE]
Search Intent: [INFORMATIONAL/TRANSACTIONAL/NAVIGATIONAL]

Top-ranking competitor pages:
1. [URL1] - [WORD_COUNT] - [KEY_TOPICS]
2. [URL2] - [WORD_COUNT] - [KEY_TOPICS]
3. [URL3] - [WORD_COUNT] - [KEY_TOPICS]

Related keywords to include:
[LIST_OF_SECONDARY_KEYWORDS]

Common questions (People Also Ask):
[PAA_QUESTIONS]

Generate a brief that includes:

1. **Content Overview**
   - Recommended title tag (with keyword)
   - Meta description (150-160 chars)
   - Target word count
   - Content format recommendation

2. **Detailed Outline**
   - H1 recommendation
   - H2 sections with brief descriptions
   - H3 subsections where needed
   - FAQ section with questions to answer

3. **Content Requirements**
   - Key points each section must cover
   - Statistics or data to include
   - Examples or case studies needed
   - Internal linking opportunities
   - External authority sources to reference

4. **Technical SEO Notes**
   - Schema markup recommendations
   - Image optimization notes
   - URL slug recommendation

5. **Differentiation Strategy**
   - How to outperform competitors
   - Unique angles to explore
   - Content gaps to fill
```

### Weekly Report Summary
```
Generate an SEO weekly report summary from this data:

Reporting Period: [DATE_RANGE]

Keyword Performance:
- Total keywords tracked: [COUNT]
- Improved: [COUNT] keywords
- Declined: [COUNT] keywords
- Stable: [COUNT] keywords
- Average position change: [+/- X]

Top Wins:
[LIST_OF_IMPROVED_KEYWORDS_WITH_CHANGES]

Biggest Drops:
[LIST_OF_DECLINED_KEYWORDS_WITH_CHANGES]

New Rankings:
[KEYWORDS_NOW_RANKING_THAT_WERENT]

Content Updates Completed:
[LIST_OF_PAGES_OPTIMIZED]

Create a report that includes:
1. Executive Summary (3-4 sentences, key takeaways)
2. Performance Highlights (wins to celebrate)
3. Areas of Concern (issues needing attention)
4. Priority Actions for Next Week (3-5 specific tasks)
5. Trend Analysis (what patterns are emerging)

Format for executive readability - use tables and bullets.
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| Daily 6:00 AM | Track keyword rankings | Daily |
| Keyword position drops 10+ | Send alert email | Real-time |
| Keyword enters top 10 | Send celebration email | Real-time |
| New keyword added with "brief" flag | Generate content brief | Real-time |
| Weekly Monday 8:00 AM | Generate weekly SEO report | Weekly |
| Monthly (1st) | Comprehensive SEO audit report | Monthly |
| New page added to inventory | Analyze and score | Real-time |
| Page score drops below 50 | Create optimization tasks | Real-time |

## Expected Outcomes

### Quantitative Results
- **Tracking coverage:** 100% of target keywords monitored daily
- **Response time:** Issues identified within 24 hours
- **Content optimization:** 95% of pages scored and prioritized
- **Brief creation time:** 10 minutes (vs. 2+ hours)
- **Reporting time:** 5 minutes (vs. 3+ hours)

### Qualitative Benefits
- Systematic, data-driven SEO approach
- No ranking drops go unnoticed
- Consistent content optimization
- Clear prioritization of efforts
- Better resource allocation

## ROI Estimate

### Assumptions
- SEO Manager salary: $70,000/year ($35/hour)
- Current SEO admin time: 15 hours/week
- Post-automation time: 5 hours/week
- Organic traffic value: $2 per visit
- Current monthly organic traffic: 10,000 visits

### Calculation
| Metric | Value |
|--------|-------|
| Weekly time saved | 10 hours |
| Monthly time saved | 40 hours |
| Monthly labor savings | $1,400 |
| Annual labor savings | $16,800 |
| Estimated traffic increase (20%) | 2,000 visits/month |
| Monthly traffic value increase | $4,000 |
| Annual traffic value | $48,000 |
| Tool costs (estimated) | $100/month |
| **Net annual ROI** | **$63,600** |

## Advanced Extensions

1. **Competitor Monitoring:** Track competitor rankings and content
2. **Backlink Tracking:** Monitor new and lost backlinks
3. **Technical SEO Audits:** Automated site health checks
4. **Content Decay Detection:** Identify aging content needing updates
5. **SERP Feature Tracking:** Monitor featured snippets, PAA, etc.

## Sample Keyword Strategy Template

```yaml
Priority Tier System:

Tier 1 - Primary Keywords:
  - High search volume (1000+)
  - High business value
  - Currently ranking 10-30
  - Quick win potential
  - Check: Daily
  - Action threshold: Any movement

Tier 2 - Secondary Keywords:
  - Medium search volume (100-999)
  - Supporting topics
  - Currently ranking 30-50
  - Check: Every 3 days
  - Action threshold: +/- 10 positions

Tier 3 - Long-tail Keywords:
  - Lower search volume (<100)
  - Specific intent
  - May not be ranking yet
  - Check: Weekly
  - Action threshold: Enter/exit top 100

Content Targeting:
  - Each page targets 1 primary keyword
  - 3-5 secondary keywords per page
  - Natural long-tail coverage
  - Internal linking between related terms
```
