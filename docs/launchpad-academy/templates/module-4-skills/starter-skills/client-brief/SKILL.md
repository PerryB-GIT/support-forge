# Client Brief

Create a structured client brief by gathering essential information about a client and organizing it into a comprehensive document.

## Trigger

- /client-brief
- /new-client
- /create-brief
- "create a client brief"
- "new client brief"
- "onboard a new client"

## Context

This skill helps create comprehensive client briefs for new projects or clients. It systematically gathers all necessary information and produces a standardized document that can be shared with team members and referenced throughout the project lifecycle.

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| client_name | string | No | Name of the client (will ask if not provided) |
| project_type | string | No | Type of project: website, app, consulting, etc. |
| template | string | No | Brief template: standard, minimal, comprehensive |

## Instructions

1. **Start the Brief**
   - Ask for the client/company name if not provided
   - Ask for the project type
   - Create a new brief document

2. **Gather Client Information**
   - Company name and legal entity
   - Industry/sector
   - Company size (employees, revenue range if known)
   - Primary contact name and role
   - Contact email and phone
   - Website and social media links
   - Physical location if relevant

3. **Understand the Project**
   - Project name/title
   - Project description (what are we building/doing?)
   - Problem being solved
   - Success criteria (how will we know it's successful?)
   - Target audience/users

4. **Define Scope and Requirements**
   - Key deliverables (list what we're providing)
   - Features/functionality required
   - Technical requirements or constraints
   - Design requirements or brand guidelines
   - Content requirements (who provides what?)
   - Integration needs (third-party services, APIs)

5. **Establish Timeline and Budget**
   - Project start date
   - Key milestones
   - Final deadline
   - Budget range
   - Payment terms/schedule

6. **Identify Stakeholders**
   - Decision makers (who approves?)
   - Day-to-day contacts
   - Technical contacts
   - Other stakeholders to keep informed

7. **Note Special Considerations**
   - Compliance requirements (GDPR, HIPAA, etc.)
   - Security requirements
   - Accessibility requirements
   - Any risks or concerns
   - Competitor references

8. **Define Communication**
   - Preferred communication channel
   - Meeting frequency
   - Reporting requirements
   - Escalation process

9. **Capture Next Steps**
   - Immediate action items
   - What we need from client
   - What client needs from us
   - First milestone/checkpoint

10. **Generate and Save Brief**
    - Compile all information into the output format
    - Ask where to save the file
    - Offer to create a client folder structure
    - Suggest follow-up actions

## Output Format

```markdown
# Client Brief: [Client Name]

**Project**: [Project Name]
**Created**: [Date]
**Last Updated**: [Date]
**Status**: [Draft/Active/Completed]

---

## Client Information

| Field | Value |
|-------|-------|
| Company | [Company Name] |
| Industry | [Industry] |
| Size | [Size] |
| Website | [URL] |
| Location | [Location] |

### Primary Contact
- **Name**: [Contact Name]
- **Role**: [Title/Role]
- **Email**: [Email]
- **Phone**: [Phone]

### Additional Contacts
| Name | Role | Email | Notes |
|------|------|-------|-------|
| [Name] | [Role] | [Email] | [Notes] |

---

## Project Overview

### Description
[2-3 paragraph description of the project]

### Problem Statement
[What problem are we solving?]

### Success Criteria
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

### Target Audience
[Description of who will use this]

---

## Scope & Deliverables

### Deliverables
1. [Deliverable 1]
2. [Deliverable 2]
3. [Deliverable 3]

### Features/Requirements
- [ ] [Feature 1]
- [ ] [Feature 2]
- [ ] [Feature 3]

### Out of Scope
- [Item explicitly not included]

### Technical Requirements
- [Requirement 1]
- [Requirement 2]

### Design Requirements
- Brand guidelines: [Yes/No - location]
- Design system: [Details]

---

## Timeline

| Milestone | Date | Status |
|-----------|------|--------|
| Project Kickoff | [Date] | [Status] |
| [Milestone 1] | [Date] | [Status] |
| [Milestone 2] | [Date] | [Status] |
| Final Delivery | [Date] | [Status] |

---

## Budget

| Item | Amount |
|------|--------|
| Total Budget | [Amount] |
| Payment Schedule | [Terms] |

---

## Communication

- **Primary Channel**: [Slack/Email/etc.]
- **Meeting Cadence**: [Weekly/Bi-weekly/etc.]
- **Status Reports**: [Frequency and format]

---

## Special Considerations

### Compliance
- [Any compliance requirements]

### Security
- [Security requirements]

### Risks
- [Risk 1]
- [Risk 2]

---

## Next Steps

### We Need From Client
- [ ] [Item 1]
- [ ] [Item 2]

### Client Needs From Us
- [ ] [Item 1]
- [ ] [Item 2]

### Action Items
| Action | Owner | Due Date |
|--------|-------|----------|
| [Action] | [Person] | [Date] |

---

## Notes

[Any additional notes or context]

---

*Brief created by [Your Name] on [Date]*
```

## Examples

### Example: New Website Client

**User**: /client-brief

**Claude**: Let's create a new client brief.

**What is the client/company name?**

**User**: Sweet Meadow Bakery

**Claude**: **What type of project is this?**

**User**: Website redesign

**Claude**: Great! Creating a brief for Sweet Meadow Bakery - Website Redesign.

Let's gather the client information first.

**What industry/sector is Sweet Meadow Bakery in?**

**User**: Food & Beverage - Local bakery

**Claude**: **Who is your primary contact at Sweet Meadow Bakery?**

**User**: Maria Johnson, owner, maria@sweetmeadowbakery.com

[Claude continues gathering information through the remaining sections...]

---

After completing all questions, Claude generates:

# Client Brief: Sweet Meadow Bakery

**Project**: Website Redesign
**Created**: January 6, 2025
**Status**: Draft

---

## Client Information

| Field | Value |
|-------|-------|
| Company | Sweet Meadow Bakery |
| Industry | Food & Beverage - Local Bakery |
| Size | Small Business (5 employees) |
| Website | sweetmeadow-bakery.com |
| Location | Portland, OR |

### Primary Contact
- **Name**: Maria Johnson
- **Role**: Owner
- **Email**: maria@sweetmeadowbakery.com
- **Phone**: (503) 555-0142

[...rest of brief...]

---

Brief saved to `clients/sweet-meadow-bakery/brief.md`

Would you like me to:
1. Create a full project folder structure?
2. Draft a kickoff meeting agenda?
3. Send the brief to the client for review?

## Dependencies

- File system access for saving briefs
- Gmail MCP for sending briefs (optional)
- Google Drive MCP for storing in cloud (optional)

## Notes

- This skill is interactive and takes 5-10 minutes to complete thoroughly
- For returning clients, suggest reviewing the previous brief first
- The brief should be treated as a living document - update it as the project evolves
- Consider saving briefs in a consistent location: `clients/[client-name]/brief.md`
- For sensitive information (budgets, contracts), consider access controls
- The minimal template skips some sections for quick/small projects
- The comprehensive template adds sections for legal, detailed technical specs, etc.
