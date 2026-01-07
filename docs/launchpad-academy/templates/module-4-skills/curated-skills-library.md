# Curated Skills Library

A collection of Claude Code skills organized by industry and use case.

---

## Business & Operations

### Client Management

| Skill | Description | Source |
|-------|-------------|--------|
| **client-brief** | Generate client briefing documents | Included |
| **client-onboarding** | Automate new client setup workflow | Included |
| **proposal-generator** | Create customized proposals | Included |
| **meeting-prep** | Prepare meeting agendas and materials | Included |
| **client-report** | Generate status reports for clients | Included |

### Daily Operations

| Skill | Description | Source |
|-------|-------------|--------|
| **daily-standup** | Generate daily standup summaries | Included |
| **project-status** | Create project status updates | Included |
| **email-response** | Draft professional email responses | Included |
| **task-prioritizer** | Organize and prioritize task lists | Community |
| **time-tracker** | Log and summarize time entries | Community |

---

## Marketing & Sales

### Content Creation

| Skill | Description | Source |
|-------|-------------|--------|
| **blog-post** | Generate blog post drafts | Community |
| **social-media** | Create social media content batches | Community |
| **email-campaign** | Draft email marketing sequences | Community |
| **landing-page** | Generate landing page copy | Community |
| **ad-copy** | Create advertising copy variations | Community |

### Sales Support

| Skill | Description | Source |
|-------|-------------|--------|
| **sales-email** | Personalized sales outreach | Community |
| **competitor-analysis** | Research and summarize competitors | Community |
| **pricing-calculator** | Generate custom pricing proposals | Community |
| **objection-handler** | Prepare responses to common objections | Community |

---

## Development & Technical

### Code Quality

| Skill | Description | Source |
|-------|-------------|--------|
| **code-review** | Systematic code review | Superpowers |
| **test-generator** | Generate test cases | Community |
| **documentation** | Auto-generate code docs | Community |
| **refactor-suggest** | Identify refactoring opportunities | Community |
| **security-audit** | Basic security vulnerability scan | Community |

### DevOps

| Skill | Description | Source |
|-------|-------------|--------|
| **deploy-helper** | Deployment preparation and checks | Community |
| **docker-config** | Generate Docker configurations | Community |
| **ci-pipeline** | Create CI/CD pipeline configs | Community |
| **env-setup** | Environment variable management | Community |
| **log-analyzer** | Parse and summarize log files | Community |

---

## Consulting & Professional Services

### Consulting

| Skill | Description | Source |
|-------|-------------|--------|
| **discovery-call** | Prepare for discovery calls | Community |
| **sow-generator** | Create Statements of Work | Community |
| **deliverable-review** | Check deliverables against requirements | Community |
| **recommendation** | Generate strategic recommendations | Community |

### Research & Analysis

| Skill | Description | Source |
|-------|-------------|--------|
| **market-research** | Compile market research summaries | Community |
| **swot-analysis** | Generate SWOT analysis documents | Community |
| **roi-calculator** | Calculate and present ROI | Community |
| **benchmark-report** | Industry benchmark comparisons | Community |

---

## E-Commerce

### Product Management

| Skill | Description | Source |
|-------|-------------|--------|
| **product-description** | Generate product descriptions | Community |
| **seo-optimizer** | Optimize product pages for SEO | Community |
| **inventory-report** | Summarize inventory status | Community |
| **price-analysis** | Competitor price comparisons | Community |

### Customer Service

| Skill | Description | Source |
|-------|-------------|--------|
| **support-response** | Draft customer support replies | Community |
| **faq-generator** | Create FAQ content from tickets | Community |
| **review-response** | Respond to product reviews | Community |
| **refund-processor** | Handle refund request workflows | Community |

---

## Healthcare & Wellness

### Practice Management

| Skill | Description | Source |
|-------|-------------|--------|
| **appointment-prep** | Prepare for patient appointments | Community |
| **care-summary** | Generate care plan summaries | Community |
| **follow-up** | Create follow-up communications | Community |

### Documentation

| Skill | Description | Source |
|-------|-------------|--------|
| **hipaa-check** | Review docs for HIPAA compliance | Community |
| **consent-form** | Generate consent form templates | Community |

---

## Legal & Compliance

### Document Preparation

| Skill | Description | Source |
|-------|-------------|--------|
| **contract-review** | Review contracts for key terms | Community |
| **nda-generator** | Create NDA documents | Community |
| **compliance-check** | Check docs against requirements | Community |
| **policy-writer** | Generate policy documents | Community |

---

## Installation Guide

### From Course Resources (Included Skills)

```bash
# Skills included in the course
cd ~/.claude/skills/
cp -r /path/to/course/skills/* ./
```

### From GitHub (Community Skills)

```bash
# Clone skill repository
git clone https://github.com/user/skill-name ~/.claude/skills/skill-name

# Or use Claude Code
claude "/install https://github.com/user/skill-name"
```

### Skill Verification

```bash
# List installed skills
claude "/skills"

# Test a skill
claude "/skill-name --test"
```

---

## Creating Custom Skills

### Basic Structure

```
my-skill/
├── SKILL.md          # Required: Skill definition
├── templates/        # Optional: Output templates
├── examples/         # Optional: Usage examples
└── prompts/          # Optional: Prompt fragments
```

### SKILL.md Template

```markdown
# Skill: [Name]

## Description
[What this skill does]

## Trigger
[How to invoke - command or phrase]

## Inputs
- [input_name]: [description] (default: [value])

## Process
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Output
[What gets produced]

## Examples
[Usage example]
```

---

## Skill Sources

### Official Sources
- **Course Materials** - `/docs/launchpad-academy/templates/module-4-skills/`
- **Superpowers Plugin** - Built-in with plugin install
- **Anthropic Skills** - github.com/anthropics/claude-code-skills

### Community Sources
- **Claude Code Community** - github.com/claude-code-community/skills
- **Awesome Claude** - github.com/awesome-claude/skills
- **Industry Packs** - Various GitHub repositories

### Quality Guidelines
When selecting community skills:
- [ ] Check last update date (< 6 months)
- [ ] Review star count and forks
- [ ] Read through SKILL.md
- [ ] Test in sandbox first
- [ ] Check for security issues

---

## Skill Customization

### Modifying Existing Skills

```bash
# Copy skill for customization
cp -r ~/.claude/skills/daily-standup ~/.claude/skills/my-standup

# Edit SKILL.md
nano ~/.claude/skills/my-standup/SKILL.md
```

### Adding Context

```markdown
# In SKILL.md, add project-specific context

## Project Context
- Company: [Your Company]
- Industry: [Your Industry]
- Tone: [Communication style]
- Terminology: [Industry terms to use]
```

### Creating Skill Bundles

```bash
# Create industry bundle
mkdir ~/.claude/skill-bundles/marketing
cp -r ~/.claude/skills/blog-post ~/.claude/skill-bundles/marketing/
cp -r ~/.claude/skills/social-media ~/.claude/skill-bundles/marketing/
cp -r ~/.claude/skills/email-campaign ~/.claude/skill-bundles/marketing/

# Load bundle
claude "/load-bundle marketing"
```

---

## Recommended Starter Packs

### For Consultants
1. client-brief
2. proposal-generator
3. meeting-prep
4. sow-generator
5. recommendation

### For Developers
1. code-review (Superpowers)
2. test-generator
3. documentation
4. deploy-helper
5. log-analyzer

### For Marketers
1. blog-post
2. social-media
3. email-campaign
4. seo-optimizer
5. ad-copy

### For Operations
1. daily-standup
2. project-status
3. email-response
4. task-prioritizer
5. client-report

---

## Contributing Skills

Share your skills with the community:

1. Create a GitHub repository
2. Include complete SKILL.md
3. Add usage examples
4. Document any dependencies
5. Submit to community skill registry

---

*AI Launchpad Academy - Support Forge*
