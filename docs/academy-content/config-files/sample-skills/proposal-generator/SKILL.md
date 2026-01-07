# Proposal Generator

A Claude Code skill that creates professional project proposals with pricing, timelines, and scope documentation.

## Trigger

Invoke with: `/proposal` or `/generate-proposal`

## Description

This skill creates comprehensive project proposals by:
1. Gathering project requirements through guided questions
2. Researching similar past projects for reference
3. Calculating pricing based on scope and complexity
4. Generating timeline estimates
5. Compiling into a professional proposal document

## Input

Interactive mode (recommended):
```
/proposal
```
Launches guided questionnaire.

Quick mode with parameters:
```
/proposal --client "Company Name" --type "website" --budget "10000-15000"
```

Optional flags:
- `--client` - Client/company name
- `--type` - Project type (website, app, automation, consulting)
- `--budget` - Budget range
- `--timeline` - Expected timeline
- `--template` - Use specific template (minimal, standard, detailed)
- `--output` - Output format (markdown, pdf, docx)

## Workflow

### Step 1: Discovery Questions
```
If interactive mode, ask:

1. Client Information
   - Company name
   - Contact person
   - Industry
   - Company size

2. Project Overview
   - What problem are we solving?
   - What does success look like?
   - Any specific requirements or constraints?

3. Scope Details
   - Project type (select from list)
   - Key features needed
   - Integrations required
   - Content requirements

4. Timeline & Budget
   - Desired start date
   - Target completion date
   - Budget range (if known)
   - Budget flexibility

5. Additional Context
   - Competitive considerations
   - Existing assets to use
   - Stakeholder involvement
```

### Step 2: Analyze Requirements
```
Based on inputs:
- Categorize complexity (simple, moderate, complex)
- Identify required skill sets
- Estimate effort in hours
- Flag any risks or unknowns
- Reference similar past projects
```

### Step 3: Calculate Pricing
```
Use pricing model:

Base rates (configurable):
- Discovery/Strategy: $150/hr
- Design: $125/hr
- Development: $150/hr
- Testing/QA: $100/hr
- Project Management: $125/hr

Apply multipliers:
- Rush timeline: 1.25x
- Enterprise client: 1.15x
- Complex integrations: +20% per integration
- Ongoing support: Add retainer option

Generate pricing options:
- Essential (minimum scope)
- Recommended (full scope)
- Premium (full scope + extras)
```

### Step 4: Build Timeline
```
Create project phases:

Phase 1: Discovery & Planning (Week 1-2)
- Kickoff meeting
- Requirements documentation
- Technical planning
- Design brief

Phase 2: Design (Week 3-4)
- Wireframes
- Visual design
- Client review & revisions

Phase 3: Development (Week 5-8)
- Frontend development
- Backend development
- Integration work
- Internal testing

Phase 4: Launch (Week 9-10)
- QA testing
- Client UAT
- Training
- Deployment

Phase 5: Post-Launch (Week 11-12)
- Bug fixes
- Optimization
- Documentation
- Handoff
```

### Step 5: Generate Document
```
Compile all sections into proposal format:
- Cover page
- Executive summary
- Understanding your needs
- Proposed solution
- Scope of work
- Timeline
- Investment
- Why us
- Terms & conditions
- Next steps
```

## Output Format

### Proposal Document Structure

```markdown
---
title: Project Proposal
client: [Client Name]
date: [Date]
valid_until: [Date + 30 days]
prepared_by: [Your Name]
---

# [Project Name] Proposal

## For [Client Name]

Prepared by [Your Company]
[Date]

---

## Executive Summary

[2-3 paragraph overview of the proposed project, key benefits,
and why your company is the right partner]

**Project Highlights:**
- [Key deliverable 1]
- [Key deliverable 2]
- [Key deliverable 3]

**Investment:** $[Amount] - $[Amount]
**Timeline:** [X] weeks

---

## Understanding Your Needs

### The Challenge
[Description of the problem or opportunity]

### Your Goals
1. [Goal 1]
2. [Goal 2]
3. [Goal 3]

### Success Metrics
- [Metric 1]
- [Metric 2]

---

## Proposed Solution

### Overview
[High-level description of the proposed solution]

### Key Features

#### [Feature Category 1]
- [Feature 1.1]
- [Feature 1.2]
- [Feature 1.3]

#### [Feature Category 2]
- [Feature 2.1]
- [Feature 2.2]

### Technology Stack
- Frontend: [Technologies]
- Backend: [Technologies]
- Infrastructure: [Technologies]

---

## Scope of Work

### Included in This Proposal

#### Phase 1: Discovery & Planning
- Kickoff meeting and stakeholder interviews
- Requirements documentation
- Technical architecture planning
- Project plan and timeline

#### Phase 2: Design
- Wireframes for all key pages
- Visual design concepts
- Design system documentation
- Mobile responsive designs

#### Phase 3: Development
- Frontend development
- Backend/API development
- Third-party integrations
- Content management setup

#### Phase 4: Testing & Launch
- Quality assurance testing
- User acceptance testing
- Deployment to production
- Launch support

#### Phase 5: Training & Handoff
- Admin training session
- Documentation delivery
- 30-day post-launch support

### Not Included (Available as Add-ons)
- Content creation/copywriting
- Photography/custom illustrations
- SEO optimization package
- Ongoing maintenance retainer

---

## Timeline

| Phase | Duration | Milestone |
|-------|----------|-----------|
| Discovery | 2 weeks | Requirements approved |
| Design | 2 weeks | Designs approved |
| Development | 4 weeks | Beta ready |
| Testing | 1 week | QA complete |
| Launch | 1 week | Site live |

**Total Timeline:** 10 weeks

```
[Visual Gantt chart or timeline graphic]
```

---

## Investment

### Option A: Essential
**$[X,XXX]**

Includes:
- [Core feature 1]
- [Core feature 2]
- [Core feature 3]

Best for: Getting started with core functionality

---

### Option B: Recommended
**$[X,XXX]** *(Most Popular)*

Everything in Essential, plus:
- [Additional feature 1]
- [Additional feature 2]
- [Additional feature 3]

Best for: Complete solution with room to grow

---

### Option C: Premium
**$[X,XXX]**

Everything in Recommended, plus:
- [Premium feature 1]
- [Premium feature 2]
- [Priority support]
- [Extended warranty]

Best for: Maximum impact and ongoing partnership

---

### Payment Terms

- 40% upon project start
- 30% at design approval
- 30% at project completion

We accept: Bank transfer, credit card, check

---

## Why [Your Company]

### Our Expertise
[Brief description of relevant experience]

### Relevant Work
- **[Project 1]**: [Brief description and result]
- **[Project 2]**: [Brief description and result]
- **[Project 3]**: [Brief description and result]

### Client Testimonial
> "[Quote from happy client]"
> — [Client Name], [Company]

### Your Team
- **[Name]** - [Role]
- **[Name]** - [Role]
- **[Name]** - [Role]

---

## Terms & Conditions

1. **Proposal Validity**: This proposal is valid for 30 days
2. **Revisions**: [X] rounds of revisions included
3. **Timeline**: Contingent on timely feedback and content
4. **Intellectual Property**: Full ownership transfers upon final payment
5. **Confidentiality**: All project details kept confidential

---

## Next Steps

1. **Review** this proposal and let us know any questions
2. **Select** your preferred option
3. **Sign** the agreement to reserve your start date
4. **Kickoff** - We'll schedule your kickoff call within 48 hours

Ready to get started? Reply to this proposal or:
- Email: [email]
- Phone: [phone]
- Schedule a call: [calendly link]

---

*We're excited about the possibility of working together!*

[Your Company]
[Address]
[Website]
```

## Configuration

Create a `.proposal-config.json`:

```json
{
  "company": {
    "name": "Your Company",
    "address": "123 Main St, City, ST 12345",
    "website": "https://yourcompany.com",
    "email": "hello@yourcompany.com",
    "phone": "(555) 123-4567",
    "logo": "https://..."
  },
  "rates": {
    "strategy": 150,
    "design": 125,
    "development": 150,
    "qa": 100,
    "pm": 125
  },
  "multipliers": {
    "rush": 1.25,
    "enterprise": 1.15,
    "complex_integration": 0.20
  },
  "defaults": {
    "validity_days": 30,
    "revision_rounds": 3,
    "payment_schedule": [40, 30, 30],
    "support_period_days": 30
  },
  "templates": {
    "default": "standard",
    "available": ["minimal", "standard", "detailed", "enterprise"]
  },
  "past_projects_sheet": "YOUR_SHEET_ID"
}
```

## Dependencies

### Required
- None (works with local data)

### Optional MCP Servers
- `zapier` - For Google Sheets (past projects reference)
- `google-drive` - For saving proposals
- `gmail` - For sending proposals

## Examples

### Interactive Mode
```
> /proposal

Let's create a proposal! I'll ask you a few questions.

What's the client's company name?
> Acme Corporation

What type of project is this?
1. Website (design/development)
2. Web Application
3. Automation/Integration
4. Consulting/Strategy
> 1

Brief description of what they need?
> Complete website redesign with new CMS and e-commerce

What's their budget range?
1. $5,000 - $10,000
2. $10,000 - $25,000
3. $25,000 - $50,000
4. $50,000+
5. Not discussed yet
> 2

When do they want to launch?
> March 1st

Generating proposal...

Proposal saved to: ./proposals/acme-corp-website-2025-01-05.md

Would you like me to:
1. Open the proposal for review
2. Send to client via email
3. Create PDF version
4. Make adjustments
```

### Quick Mode
```
> /proposal --client "Acme Corp" --type website --budget "15000" --template minimal

Generating minimal proposal for Acme Corp...

Created: ./proposals/acme-corp-website-minimal.md
```

## Related Skills

- `/sow-generator` - Generate Statement of Work
- `/contract` - Generate service agreement
- `/invoice` - Create project invoice
- `/scope-calculator` - Estimate project scope
