# Business Prompt Templates for Claude Code

Ready-to-use prompts for common business tasks. Copy, customize, and use.

---

## Table of Contents

1. [Email Drafting & Responses](#email-drafting--responses)
2. [Document Analysis & Summarization](#document-analysis--summarization)
3. [Project Planning](#project-planning)
4. [Code Review](#code-review)
5. [Data Analysis](#data-analysis)
6. [Meeting Preparation](#meeting-preparation)
7. [Client Communication](#client-communication)

---

## Email Drafting & Responses

### 1. Professional Follow-Up Email

**Prompt:**
```
Draft a professional follow-up email with these details:
- Recipient: [Name/Role]
- Previous meeting/conversation: [Brief context]
- Main follow-up points: [List 2-3 items]
- Desired next step: [What you want them to do]
- Tone: [Professional/Friendly/Formal]

Keep it concise (under 150 words) and include a clear call-to-action.
```

**Usage Notes:**
- Replace bracketed items with your specifics
- Works for sales follow-ups, meeting recaps, and check-ins
- Ask Claude to adjust tone if needed

---

### 2. Handling Difficult Client Email

**Prompt:**
```
Help me respond to this difficult client email:

[Paste the client's email here]

Context:
- My relationship with this client: [New/Long-term/VIP]
- The actual situation: [Brief factual explanation]
- What I can offer: [Solutions/compromises available]
- What I cannot do: [Limitations]

Draft a response that:
1. Acknowledges their concerns without being defensive
2. Explains the situation clearly
3. Proposes a concrete solution
4. Maintains the relationship
```

**Usage Notes:**
- Always provide context about what you CAN offer
- Claude will balance empathy with professionalism
- Review and personalize before sending

---

### 3. Cold Outreach Email

**Prompt:**
```
Create a cold outreach email for:
- Target: [Job title] at [Company type]
- My offering: [Product/Service in one sentence]
- Key benefit: [Main value proposition]
- Social proof: [Brief credibility point]
- Goal: [Meeting/Demo/Response]

Requirements:
- Subject line options (give me 3)
- Keep body under 100 words
- One clear CTA
- No pushy language
```

**Usage Notes:**
- Test different subject lines
- Personalize the opening for each recipient
- A/B test responses to improve

---

### 4. Project Status Update Email

**Prompt:**
```
Write a project status update email:

Project: [Name]
Audience: [Stakeholders/Client/Team]
Reporting period: [Week/Month/Sprint]

Progress:
- Completed: [List items]
- In progress: [List items]
- Blocked: [Any blockers]

Metrics (if applicable):
- [Metric 1]: [Value]
- [Metric 2]: [Value]

Next steps: [What's coming]
Any decisions needed: [Yes/No - if yes, what]

Format for easy scanning with bullet points and bold headers.
```

**Usage Notes:**
- Adjust detail level based on audience
- Include only relevant metrics
- Flag decisions needed prominently

---

## Document Analysis & Summarization

### 5. Contract Review Summary

**Prompt:**
```
Review this contract/agreement and provide:

[Paste contract text or add file]

I need:
1. Executive summary (2-3 sentences)
2. Key terms and obligations for each party
3. Important dates and deadlines
4. Potential concerns or unusual clauses
5. Questions I should ask before signing

My role in this agreement: [Buyer/Seller/Service Provider/Client]
```

**Usage Notes:**
- Not a substitute for legal advice
- Use for initial understanding before lawyer review
- Flag any clauses you're specifically concerned about

---

### 6. Meeting Notes Summarization

**Prompt:**
```
Summarize these meeting notes into an actionable format:

[Paste meeting notes or transcript]

Create:
1. Meeting summary (3-4 bullet points of key outcomes)
2. Decisions made (who decided what)
3. Action items table with:
   - Task
   - Owner
   - Due date
   - Priority (High/Medium/Low)
4. Open questions or parking lot items
5. Next meeting topics (if applicable)
```

**Usage Notes:**
- Works with rough notes or transcripts
- Ask Claude to format for your project management tool
- Can request follow-up email draft based on summary

---

### 7. Competitive Analysis Document

**Prompt:**
```
Help me analyze our competitor based on this information:

Competitor: [Name]
Their website: [URL - Claude can web search]
Our company: [Brief description]
Our target market: [Description]

Research and provide:
1. Their positioning and value proposition
2. Pricing model (if public)
3. Key features/services
4. Apparent target customer
5. Strengths vs. our offering
6. Weaknesses/opportunities for us
7. How they market themselves

Format as a one-page competitive brief.
```

**Usage Notes:**
- Enable web search for current information
- Verify claims with primary sources
- Update quarterly for accuracy

---

### 8. Report Executive Summary

**Prompt:**
```
Create an executive summary for this report:

[Paste report or add file]

Target audience: [C-suite/Board/Investors/Team leads]
Their main concerns: [What they care about most]
Time to read: [30 seconds/1 minute/2 minutes]

Include:
- The main finding or recommendation (lead with this)
- 3-5 supporting points
- Key data points that matter
- Recommended action or decision needed
- Risk or opportunity if no action taken
```

**Usage Notes:**
- Specify audience for appropriate detail level
- Ask for different lengths for different stakeholders
- Can request visual/chart suggestions

---

## Project Planning

### 9. Project Kickoff Document

**Prompt:**
```
Create a project kickoff document for:

Project name: [Name]
Project type: [Website/App/Campaign/Implementation]
Client/Stakeholder: [Who it's for]
Timeline: [Start date to end date]
Budget: [If relevant]
Team: [Roles involved]

Include sections for:
1. Project overview and objectives
2. Scope (in/out of scope)
3. Key milestones and dates
4. Roles and responsibilities (RACI if complex)
5. Communication plan
6. Success metrics
7. Risks and mitigation
8. Next steps

Make it practical and actionable, not generic filler.
```

**Usage Notes:**
- Customize sections for your project type
- Add company-specific requirements
- Can generate as markdown or request other formats

---

### 10. Sprint Planning Breakdown

**Prompt:**
```
Help me break down this feature into sprint tasks:

Feature: [Describe the feature]
Tech stack: [Technologies used]
Sprint length: [1 week/2 weeks]
Team capacity: [X story points or hours]

For each task, provide:
- Task title
- Description (what "done" looks like)
- Estimated effort [hours or story points]
- Dependencies
- Acceptance criteria

Also identify:
- What can be parallelized
- Biggest technical risks
- Suggested task order
```

**Usage Notes:**
- Adjust complexity based on team experience
- Include buffer for unknowns
- Review estimates with technical team

---

### 11. Resource Allocation Plan

**Prompt:**
```
Help me create a resource allocation plan:

Project duration: [X weeks/months]
Available team members:
- [Name]: [Role], [Hours available per week]
- [Name]: [Role], [Hours available per week]
- [Add more as needed]

Major workstreams:
1. [Workstream]: [Estimated total hours]
2. [Workstream]: [Estimated total hours]
3. [Add more]

Constraints:
- [Any vacations, other commitments, etc.]

Create a week-by-week allocation showing who works on what,
flagging any over-allocation or gaps.
```

**Usage Notes:**
- Be realistic about availability
- Include buffer for meetings and context-switching
- Update weekly as actuals come in

---

## Code Review

### 12. Pull Request Review

**Prompt:**
```
Review this pull request for:

[Paste code diff or describe changes]

Context:
- Feature/fix being implemented: [Description]
- Tech stack: [Languages/frameworks]
- Team standards: [Link to style guide or key rules]

Review for:
1. Logic errors or bugs
2. Security vulnerabilities
3. Performance issues
4. Code style and readability
5. Test coverage
6. Documentation needs

Format feedback as:
- Critical (must fix before merge)
- Suggested (should fix, non-blocking)
- Nitpicks (style preferences)

Include specific line references and suggested fixes.
```

**Usage Notes:**
- Provide context about what the code should do
- Mention any known constraints
- Can request different focus areas

---

### 13. Code Refactoring Plan

**Prompt:**
```
Analyze this code and create a refactoring plan:

[Paste code or file path]

Current issues I've noticed:
- [Issue 1]
- [Issue 2]

Goals:
- [Improve readability/performance/testability/etc.]

Constraints:
- Must maintain backward compatibility: [Yes/No]
- Time budget: [Hours/days available]
- Test coverage requirement: [Percentage or description]

Provide:
1. Priority-ordered list of refactoring tasks
2. Estimated effort for each
3. Risk assessment for each change
4. Suggested order of implementation
5. Before/after examples for key changes
```

**Usage Notes:**
- Start with highest-impact, lowest-risk changes
- Consider doing in separate PRs
- Plan for regression testing

---

### 14. Technical Debt Assessment

**Prompt:**
```
Assess the technical debt in this codebase/file:

[Add files or describe the area]

Evaluate:
1. Code quality issues (duplication, complexity, etc.)
2. Outdated dependencies and security risks
3. Missing tests or documentation
4. Architectural concerns
5. Performance bottlenecks

For each issue found, provide:
- Severity (High/Medium/Low)
- Effort to fix (Quick/Medium/Large)
- Business impact if not addressed
- Recommended priority

Create a technical debt backlog I can add to our sprint planning.
```

**Usage Notes:**
- Focus on specific areas, not entire codebase at once
- Link findings to business impact for stakeholder buy-in
- Schedule regular debt reduction sprints

---

## Data Analysis

### 15. Data Interpretation Report

**Prompt:**
```
Analyze this data and provide insights:

[Paste data, CSV content, or describe dataset]

Context:
- This data represents: [What it measures]
- Time period: [When it's from]
- Business question: [What we're trying to understand]

Provide:
1. Summary statistics (mean, median, trends)
2. Key patterns or anomalies
3. Comparison to benchmarks (if provided: [benchmarks])
4. Actionable insights (what should we do?)
5. Data quality issues noticed
6. Suggested follow-up analyses

Present findings for [Technical/Non-technical] audience.
```

**Usage Notes:**
- Include context about what "good" looks like
- Specify if you need visualizations described
- Can request SQL queries for follow-up

---

### 16. KPI Dashboard Requirements

**Prompt:**
```
Help me define KPIs and dashboard requirements for:

Business area: [Sales/Marketing/Operations/Product]
Audience: [Who will use this dashboard]
Review cadence: [Daily/Weekly/Monthly]

Current goals:
1. [Goal 1 with target]
2. [Goal 2 with target]
3. [Goal 3 with target]

For each KPI, define:
- KPI name and definition
- Calculation formula
- Data source
- Target/benchmark
- Red/yellow/green thresholds
- Visualization type recommended
- Drill-down dimensions needed

Also suggest 2-3 KPIs I might be missing.
```

**Usage Notes:**
- Start with outcomes, work backward to metrics
- Limit to 5-7 KPIs per dashboard
- Include leading and lagging indicators

---

### 17. Survey Analysis

**Prompt:**
```
Analyze these survey results:

[Paste survey data or summary]

Survey context:
- Purpose: [What we were measuring]
- Respondents: [Who took it, sample size]
- Time period: [When conducted]

Provide:
1. Response rate and data quality assessment
2. Key findings by question/section
3. Sentiment analysis of open-ended responses
4. Segmentation insights (if demographic data included)
5. Statistical significance notes
6. Recommended actions based on findings
7. Suggested follow-up questions for next survey
```

**Usage Notes:**
- Note sample size limitations
- Group open-ended responses by theme
- Compare to previous surveys if available

---

## Meeting Preparation

### 18. Client Meeting Prep Brief

**Prompt:**
```
Prepare me for a client meeting:

Client: [Company name]
Meeting type: [Kickoff/Review/Sales/Problem-solving]
Attendees: [Names and roles]
Meeting length: [Duration]
My goal: [What I want to achieve]

What I know:
- Our history with them: [Brief background]
- Current project/deal status: [Where things stand]
- Recent interactions: [Any relevant context]

Create:
1. Pre-meeting research points (things to look up)
2. Agenda suggestion
3. Key talking points for my goals
4. Potential questions they might ask (with suggested responses)
5. Questions I should ask them
6. Red flags to watch for
7. Concrete next steps to propose
```

**Usage Notes:**
- Review LinkedIn profiles of attendees
- Prepare for multiple scenarios
- Have a backup plan if meeting goes off-track

---

### 19. Presentation Outline

**Prompt:**
```
Create a presentation outline for:

Topic: [What you're presenting]
Audience: [Who they are, what they care about]
Time slot: [X minutes]
Goal: [Inform/Persuade/Train/Decide]
Key message: [One sentence summary]

Desired outcome: [What you want audience to do/think after]

Provide:
1. Slide-by-slide outline with:
   - Slide title
   - Key points (3 max per slide)
   - Suggested visual/data
   - Speaker notes
2. Transition language between sections
3. Engagement moments (questions, polls, demos)
4. Backup slides for Q&A
5. Time allocation per section
```

**Usage Notes:**
- Less is more - cut ruthlessly
- Practice timing with speaker notes
- Prepare for questions by anticipating objections

---

### 20. Interview Question Bank

**Prompt:**
```
Create interview questions for:

Role: [Job title]
Level: [Junior/Mid/Senior/Lead]
Key skills needed:
1. [Skill 1]
2. [Skill 2]
3. [Skill 3]

Team context: [Brief description of team/company]
Interview stage: [Phone screen/Technical/Behavioral/Final]

Provide:
1. 5 role-specific technical questions with ideal answer points
2. 5 behavioral questions (STAR format) with what to listen for
3. 3 culture fit questions
4. 2 questions to assess growth potential
5. Red flags to watch for in responses
6. Questions the candidate might ask (with good responses)
```

**Usage Notes:**
- Standardize questions for fair comparison
- Score responses on consistent rubric
- Leave time for candidate questions

---

## Client Communication

### 21. Proposal Template

**Prompt:**
```
Help me create a proposal for:

Client: [Company name]
Project: [What they need]
Our solution: [What we're proposing]
Budget range: [If known]
Timeline expectation: [If known]
Decision makers: [Who will approve]

Their pain points:
1. [Pain point 1]
2. [Pain point 2]

Create a proposal with:
1. Executive summary (their problem, our solution, expected outcome)
2. Understanding of their needs (show we listened)
3. Proposed solution (phased if appropriate)
4. Deliverables and timeline
5. Investment (pricing structure)
6. Why us (differentiators, social proof)
7. Next steps and call to action
8. Terms and assumptions

Keep it under [X] pages.
```

**Usage Notes:**
- Lead with their needs, not your capabilities
- Make pricing clear and justified
- Include case studies if available

---

### 22. Scope Change Communication

**Prompt:**
```
Help me communicate a scope change to the client:

Original scope: [What was agreed]
Requested change: [What they want to add/change]
Impact:
- Timeline: [How it affects schedule]
- Budget: [Additional cost if any]
- Resources: [Team impact]

My recommendation: [Accept/Modify/Decline and why]

Draft communication that:
1. Acknowledges their request positively
2. Clearly explains the impact
3. Presents options (if applicable)
4. Requests decision by [date]
5. Documents the change formally

Tone: [Collaborative/Firm/Flexible]
```

**Usage Notes:**
- Never say "no" without offering alternatives
- Get scope changes in writing
- Reference original agreement

---

### 23. Bad News Delivery

**Prompt:**
```
Help me deliver difficult news to a client:

The news: [What happened - delay, issue, cost increase, etc.]
Why it happened: [Honest explanation]
Our responsibility: [What we own]
Impact on them: [How it affects their business]
What we're doing about it: [Remediation plan]
What we need from them: [If anything]

Draft a communication that:
1. Leads with the news (no burying)
2. Takes appropriate responsibility
3. Shows we have a plan
4. Offers something (discount, extra service, etc.) if appropriate
5. Provides next steps and timeline
6. Opens door for discussion

Tone: [Apologetic but not groveling, professional, solutions-focused]
```

**Usage Notes:**
- Deliver bad news fast - delays make it worse
- Have solutions ready before communicating
- Follow up written communication with a call

---

### 24. Client Testimonial Request

**Prompt:**
```
Help me request a testimonial from a satisfied client:

Client: [Name, Company]
Project we did: [Brief description]
Results achieved: [Specific outcomes]
Our relationship: [How long, how close]
What I want: [Written quote/Video/Case study/Reference call]

Draft an email that:
1. Thanks them genuinely
2. References specific success we had together
3. Makes the ask easy to say yes to
4. Offers to write a draft they can edit
5. Gives them options (written, video, LinkedIn)
6. Respects their time

Include a draft testimonial they can approve/edit based on our results.
```

**Usage Notes:**
- Ask when they're happiest (after a win)
- Make it easy - provide draft
- Offer reciprocity (referral, testimonial swap)

---

## How to Customize These Templates

### Adding Context

Always improve results by adding:
- Industry-specific terminology
- Company voice/tone guidelines
- Examples of previous similar work
- Specific constraints or requirements

### Creating Variations

Ask Claude to:
```
"Give me 3 variations of this with different tones:
formal, friendly, and urgent"
```

### Building on Templates

```
"Use the output you just created and now:
1. Make it shorter by 50%
2. Add more specific metrics
3. Translate to [language]"
```

### Saving Your Best Prompts

Create a personal prompt library:
1. Save prompts that worked well
2. Note what context made them effective
3. Update based on feedback
4. Share with team for consistency

---

## Quick Reference: Prompt Formula

**Effective prompts include:**

1. **Context**: Background information Claude needs
2. **Task**: What you want done (be specific)
3. **Format**: How you want the output structured
4. **Constraints**: Length, tone, what to avoid
5. **Examples**: Show what good looks like (optional but helpful)

**Template structure:**
```
Context: [Who you are, what situation you're in]
Task: [Exactly what you need]
Requirements: [Specific elements to include]
Format: [How to structure the output]
Constraints: [Length, tone, things to avoid]
```
