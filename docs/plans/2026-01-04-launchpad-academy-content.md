# Launchpad Academy - Course Content Outline

**Course:** Launchpad Academy ($997)
**Format:** Self-paced video course with downloadable resources
**Total Runtime Target:** 8-10 hours of video content
**Platform:** Thinkific (recommended)

---

## Course Structure Overview

| Module | Name | LAUNCH Phase | Est. Runtime |
|--------|------|--------------|--------------|
| 0 | Welcome & Setup | - | 15 min |
| 1 | Foundations | L - Landscape | 45 min |
| 2 | Claude Code Mastery | A - Architect | 90 min |
| 3 | MCP Server Deep Dive | U - Unlock | 75 min |
| 4 | Skills & Plugins | N - Network | 60 min |
| 5 | Automation Engines | C - Configure | 90 min |
| 6 | Cloud Deployment | C - Configure | 60 min |
| 7 | Security & Responsible AI | H - Harden | 45 min |
| 8 | Your First Agent Workflow | Capstone | 60 min |

**Total: ~9 hours of content**

---

## Module 0: Welcome & Course Setup
*Runtime: 15 minutes*

### Learning Objectives
- Understand what you'll build by the end of the course
- Set up your learning environment
- Join the community

### Lessons

#### 0.1 Welcome to AI Launchpad (5 min)
**Type:** Talking head + slides

**Content:**
- Who this course is for
- What you'll be able to do after completing it
- The LAUNCH Method overview
- How to get the most from this course

**Record:**
- You on camera, enthusiastic, relatable
- Show before/after: "manual tasks" → "AI-powered operations"
- Brief LAUNCH Method animation/graphic

---

#### 0.2 Your Learning Environment (5 min)
**Type:** Screencast

**Content:**
- How to navigate the course platform
- Downloading resources
- Where to ask questions
- Community access (Discord invite)

**Record:**
- Screen recording of Thinkific interface
- Show downloads section
- Show Discord server tour

---

#### 0.3 Prerequisites Check (5 min)
**Type:** Screencast + checklist

**Content:**
- Required: Computer (Windows/Mac/Linux)
- Required: Basic command line comfort
- Required: Credit card for service signups
- Helpful but not required: Coding experience

**Downloadable:**
- [ ] Prerequisites Checklist PDF
- [ ] Recommended hardware specs

---

## Module 1: Foundations (LANDSCAPE Phase)
*Runtime: 45 minutes*

### Learning Objectives
- Complete your AI Readiness Audit
- Set up all required accounts
- Understand the full Launchpad Stack
- Identify your automation opportunities

### Lessons

#### 1.1 The AI Readiness Audit (15 min)
**Type:** Talking head + screencast

**Content:**
- Why most AI implementations fail
- The "Tool Collector" trap
- How to audit your current tech stack
- Pain Point Prioritization framework

**Record:**
- Open with the problem (2 min talking head)
- Screen share: Walk through the audit worksheet
- Fill out a real example (your own or fictional business)

**Downloadable:**
- [ ] AI Readiness Audit Worksheet (Google Sheets template)
- [ ] Pain Point Prioritization Matrix (PDF)
- [ ] Current Tool Inventory Template

---

#### 1.2 Account Setup Marathon (20 min)
**Type:** Screencast (fast-paced montage style)

**Content:**
- Creating accounts for the entire stack
- Tips for password management
- Setting up 2FA properly
- Organizing credentials

**Accounts to create (show each):**
1. GitHub account + SSH key generation
2. Anthropic account (Claude API)
3. Google Cloud Console + project creation
4. AWS account + IAM user setup
5. n8n Cloud (or note self-hosted later)
6. Zapier account

**Record:**
- Speed through each signup (can use jump cuts)
- Pause on tricky parts (API key generation, IAM)
- Show 1Password/Bitwarden setup for credential storage

**Downloadable:**
- [ ] Account Setup Checklist (with links)
- [ ] Credentials Vault Template (Bitwarden export format)

---

#### 1.3 Understanding the Launchpad Stack (10 min)
**Type:** Animated diagram + talking head

**Content:**
- The complete stack overview
- How each tool connects to others
- Which tools are required vs optional
- Cost breakdown (monthly estimates)

**Record:**
- Animated diagram showing tool connections
- Talking head explaining each layer
- Cost calculator walkthrough

**Downloadable:**
- [ ] Launchpad Stack Diagram (PDF, high-res)
- [ ] Monthly Cost Calculator (Google Sheets)

---

## Module 2: Claude Code Mastery (ARCHITECT Phase)
*Runtime: 90 minutes*

### Learning Objectives
- Install and configure Claude Code
- Understand the Claude Code interface
- Master effective prompting for coding tasks
- Configure settings for your workflow

### Lessons

#### 2.1 Installing Claude Code (15 min)
**Type:** Screencast (3 versions)

**Content:**
- Installation on Windows (with WSL)
- Installation on Mac
- Installation on Linux
- Verifying installation works

**Record:**
- **Windows version:** Full WSL setup, then Claude Code install
- **Mac version:** Homebrew install, terminal setup
- **Linux version:** Quick apt/npm install
- Test command: `claude --version`

**Downloadable:**
- [ ] Installation Guide PDF (all platforms)
- [ ] Troubleshooting common errors

---

#### 2.2 Your First Claude Code Session (20 min)
**Type:** Screencast

**Content:**
- Launching Claude Code
- Understanding the interface
- Basic commands and shortcuts
- Reading and editing files
- Running shell commands

**Record:**
- Start Claude Code in a sample project
- Show: asking questions, reading files, making edits
- Demonstrate: /help, /clear, keyboard shortcuts
- Common gotchas and how to avoid them

**Downloadable:**
- [ ] Claude Code Cheat Sheet (keyboard shortcuts, commands)

---

#### 2.3 Prompting for Business Tasks (25 min)
**Type:** Talking head + screencast

**Content:**
- The difference between chat prompting and code prompting
- Giving context effectively
- Multi-step task prompting
- When to be specific vs when to let Claude decide

**Examples to record:**
1. "Analyze this spreadsheet and summarize key insights"
2. "Draft an email response to this client complaint"
3. "Create a project plan for launching X"
4. "Review this code and suggest improvements"

**Record:**
- Talking head: principles of good prompting (5 min)
- Screencast: 4 real examples with full prompts shown

**Downloadable:**
- [ ] Business Prompt Templates (20+ prompts)
- [ ] Prompt Engineering Quick Reference

---

#### 2.4 Configuring Claude Code Settings (15 min)
**Type:** Screencast

**Content:**
- The settings file location
- Key settings to customize
- Model selection
- API key configuration
- Custom instructions (CLAUDE.md)

**Record:**
- Walk through settings file
- Show how to set default model
- Create a CLAUDE.md with business context
- Test that settings apply

**Downloadable:**
- [ ] Sample CLAUDE.md templates (by industry)
- [ ] Recommended settings for business use

---

#### 2.5 Advanced Claude Code Features (15 min)
**Type:** Screencast

**Content:**
- Using Claude Code with git
- Multi-file operations
- Background tasks
- Hooks and automation triggers

**Record:**
- Git workflow: stage, commit, push with Claude
- Edit multiple files in one session
- Set up a simple hook

**Downloadable:**
- [ ] Advanced Features Reference Guide

---

## Module 3: MCP Server Deep Dive (UNLOCK Phase)
*Runtime: 75 minutes*

### Learning Objectives
- Understand what MCP servers are and why they matter
- Install and configure MCP servers
- Connect Claude to external services
- Troubleshoot common connection issues

### Lessons

#### 3.1 What Are MCP Servers? (10 min)
**Type:** Animated explainer + talking head

**Content:**
- MCP = Model Context Protocol
- How MCP extends Claude's capabilities
- The difference between built-in tools and MCP tools
- Security considerations

**Record:**
- Animated diagram: Claude → MCP Server → External Service
- Talking head: real-world analogy (MCP as "adapters")

**Downloadable:**
- [ ] MCP Architecture Diagram

---

#### 3.2 Installing Your First MCP Server (20 min)
**Type:** Screencast

**Content:**
- The MCP config file structure
- Installing the Zapier MCP server
- Testing the connection
- Understanding tool availability

**Record:**
- Locate/create claude_mcp_config.json
- Add Zapier MCP configuration
- Restart Claude Code
- Verify tools appear with /tools command

**Downloadable:**
- [ ] MCP Config Starter Template
- [ ] Zapier MCP Setup Guide

---

#### 3.3 Connecting Google Services (20 min)
**Type:** Screencast

**Content:**
- Google Workspace MCP setup
- Calendar integration
- Drive integration
- Gmail integration
- OAuth authentication flow

**Record:**
- Full OAuth setup walkthrough
- Test each service: read calendar, list files, check email
- Show practical use case: "What's on my calendar today?"

**Downloadable:**
- [ ] Google MCP Config Template
- [ ] OAuth Troubleshooting Guide

---

#### 3.4 Connecting GitHub (15 min)
**Type:** Screencast

**Content:**
- GitHub MCP server setup
- Personal access token creation
- Repository access configuration
- Practical workflows

**Record:**
- Create GitHub PAT with correct scopes
- Configure MCP server
- Test: list repos, create issue, check PRs

**Downloadable:**
- [ ] GitHub MCP Config Template

---

#### 3.5 Troubleshooting MCP Connections (10 min)
**Type:** Screencast

**Content:**
- Common error messages and what they mean
- Authentication failures
- Permission issues
- Connection timeouts
- Where to find logs

**Record:**
- Show 5 common errors and how to fix each
- Demonstrate log file locations
- Quick diagnostic checklist

**Downloadable:**
- [ ] MCP Troubleshooting Flowchart

---

## Module 4: Skills & Plugins (NETWORK Phase)
*Runtime: 60 minutes*

### Learning Objectives
- Understand the Claude Code skills system
- Install pre-built skills
- Customize skills for your needs
- Create basic custom skills

### Lessons

#### 4.1 Understanding Skills (10 min)
**Type:** Talking head + screencast

**Content:**
- What are Claude Code skills?
- Built-in vs custom skills
- The skills directory structure
- How skills extend Claude's capabilities

**Record:**
- Talking head: skills as "superpowers"
- Screencast: explore .claude/skills directory
- Show skill anatomy (SKILL.md, supporting files)

---

#### 4.2 Installing the Superpowers Plugin (15 min)
**Type:** Screencast

**Content:**
- What Superpowers includes
- Installation process
- Available skills overview
- Testing key skills

**Record:**
- Full installation walkthrough
- Tour of included skills
- Demo: brainstorming, writing-plans, code-review

**Downloadable:**
- [ ] Superpowers Quick Reference

---

#### 4.3 Installing Industry Skills (15 min)
**Type:** Screencast

**Content:**
- Finding skills for your industry
- Installation from GitHub
- Configuration and customization
- Creating skill bundles

**Record:**
- Show where to find community skills
- Install 2-3 example skills
- Customize one for specific business need

**Downloadable:**
- [ ] Curated Skills Library (links by industry)

---

#### 4.4 Creating Your First Custom Skill (20 min)
**Type:** Screencast

**Content:**
- Skill file structure
- Writing SKILL.md
- Adding supporting files
- Testing your skill

**Record:**
- Create a simple skill from scratch (e.g., "daily-standup" skill)
- Write the SKILL.md with clear instructions
- Add any templates needed
- Test the skill in action

**Downloadable:**
- [ ] Skill Creation Template
- [ ] 5 Starter Skill Examples

---

## Module 5: Automation Engines (CONFIGURE Phase)
*Runtime: 90 minutes*

### Learning Objectives
- Set up n8n for advanced automations
- Create Zapier integrations
- Build multi-step workflows
- Connect automations to Claude

### Lessons

#### 5.1 Automation Strategy (10 min)
**Type:** Talking head

**Content:**
- When to use n8n vs Zapier
- Identifying automation opportunities
- The automation ROI calculator
- Avoiding over-automation

**Record:**
- Decision framework: n8n (complex, self-hosted) vs Zapier (simple, hosted)
- Walk through ROI calculator
- Warning signs of over-automation

**Downloadable:**
- [ ] Automation ROI Calculator
- [ ] n8n vs Zapier Decision Matrix

---

#### 5.2 n8n Installation & Setup (20 min)
**Type:** Screencast

**Content:**
- n8n Cloud vs self-hosted
- Docker installation (self-hosted)
- Initial configuration
- Your first workflow

**Record:**
- **Cloud path:** Sign up, tour interface
- **Self-hosted path:** Docker compose setup, access via browser
- Create simple workflow: webhook → transform → output

**Downloadable:**
- [ ] n8n Docker Compose Template
- [ ] n8n First Workflow Template

---

#### 5.3 Building n8n Workflows (25 min)
**Type:** Screencast

**Content:**
- Workflow design principles
- Common nodes and their uses
- Error handling in workflows
- Testing and debugging

**Build 3 example workflows:**
1. Lead capture: Form → Google Sheet → Email notification
2. Content pipeline: RSS → AI summarize → Slack post
3. Client onboarding: Webhook → Create folder → Send welcome email

**Record:**
- Build each workflow step-by-step
- Show testing and execution
- Demonstrate error handling

**Downloadable:**
- [ ] 10 n8n Workflow Templates (importable JSON)

---

#### 5.4 Zapier Essentials (20 min)
**Type:** Screencast

**Content:**
- Zapier interface tour
- Creating Zaps
- Multi-step Zaps
- Using Zapier with Claude (via MCP)

**Build 2 example Zaps:**
1. New email with label → Create task in project manager
2. Calendar event → Prepare briefing doc

**Record:**
- Build each Zap
- Show trigger/action configuration
- Test end-to-end

**Downloadable:**
- [ ] 10 Zapier Templates (shareable links)

---

#### 5.5 Connecting Automations to Claude (15 min)
**Type:** Screencast

**Content:**
- Triggering workflows from Claude
- Having Claude call n8n webhooks
- Automation orchestration patterns
- Best practices

**Record:**
- Set up n8n webhook that Claude can call
- Create Claude workflow that triggers automation
- Show full loop: Claude → n8n → External service → Response

**Downloadable:**
- [ ] Claude-to-n8n Integration Guide

---

## Module 6: Cloud Deployment (CONFIGURE Phase continued)
*Runtime: 60 minutes*

### Learning Objectives
- Deploy applications to AWS
- Use Google Cloud services
- Set up proper environments
- Manage costs effectively

### Lessons

#### 6.1 AWS Fundamentals for AI (15 min)
**Type:** Screencast

**Content:**
- AWS Console navigation
- Key services overview (EC2, S3, Lambda, Amplify)
- IAM best practices
- Cost management

**Record:**
- Console tour focused on relevant services
- Set up billing alerts
- Review IAM user we created earlier

**Downloadable:**
- [ ] AWS Services Cheat Sheet
- [ ] Cost Optimization Checklist

---

#### 6.2 Deploying with AWS Amplify (20 min)
**Type:** Screencast

**Content:**
- What is Amplify?
- Connecting to GitHub
- Deployment configuration
- Custom domains

**Record:**
- Create new Amplify app from GitHub repo
- Configure build settings
- Set up custom domain
- Show automatic deployments on push

**Downloadable:**
- [ ] Amplify Deployment Guide
- [ ] amplify.yml Templates

---

#### 6.3 Google Cloud for AI Workloads (15 min)
**Type:** Screencast

**Content:**
- Google Cloud Console tour
- Vertex AI overview
- BigQuery basics
- When to use GCP vs AWS

**Record:**
- Console navigation
- Create a Vertex AI endpoint (quick demo)
- BigQuery: run a simple query
- Decision framework for GCP vs AWS

**Downloadable:**
- [ ] GCP Quick Start Guide
- [ ] Vertex AI Starter Template

---

#### 6.4 Cost Management & Optimization (10 min)
**Type:** Talking head + screencast

**Content:**
- Setting up billing alerts
- Identifying cost spikes
- Reserved instances and savings plans
- Free tier maximization

**Record:**
- Set up AWS budget alert
- Set up GCP budget alert
- Review cost optimization strategies

**Downloadable:**
- [ ] Cloud Cost Tracking Spreadsheet

---

## Module 7: Security & Responsible AI (HARDEN Phase)
*Runtime: 45 minutes*

### Learning Objectives
- Secure your AI implementation
- Handle credentials properly
- Understand responsible AI principles
- Avoid common pitfalls

### Lessons

#### 7.1 Credential Security (15 min)
**Type:** Screencast

**Content:**
- API key rotation schedules
- Secrets management
- Environment variables
- What NOT to do (horror stories)

**Record:**
- Set up key rotation reminder
- Show proper .env usage
- Demonstrate AWS Secrets Manager (quick)
- Real examples of exposed keys and consequences

**Downloadable:**
- [ ] Credential Security Checklist
- [ ] Key Rotation Schedule Template

---

#### 7.2 Access Control & Auditing (10 min)
**Type:** Screencast

**Content:**
- Principle of least privilege
- Role-based access
- Audit logging
- Monitoring for suspicious activity

**Record:**
- Review IAM policies
- Set up CloudWatch basic monitoring
- Check audit logs

**Downloadable:**
- [ ] Access Control Review Checklist

---

#### 7.3 Responsible AI Principles (15 min)
**Type:** Talking head + slides

**Content:**
- What AI should NOT be used for
- Human oversight requirements
- Bias awareness
- Data privacy (GDPR, CCPA basics)
- Transparency with customers

**Record:**
- Talking head with clear principles
- Real-world case studies (good and bad)
- Decision framework for "should AI do this?"

**Downloadable:**
- [ ] Responsible AI Policy Template
- [ ] AI Use Decision Flowchart

---

#### 7.4 Documentation & Handoff (5 min)
**Type:** Screencast

**Content:**
- What to document
- Runbook format
- Knowledge transfer best practices

**Record:**
- Show documentation template
- Fill out example sections

**Downloadable:**
- [ ] System Runbook Template
- [ ] Documentation Checklist

---

## Module 8: Your First Agent Workflow (CAPSTONE)
*Runtime: 60 minutes*

### Learning Objectives
- Build a complete end-to-end workflow
- Integrate all skills learned
- Test and refine
- Deploy to production

### Lessons

#### 8.1 Capstone Project Overview (5 min)
**Type:** Talking head

**Content:**
- What we're building: Client Onboarding Agent
- Components involved
- Success criteria

**Record:**
- Explain the capstone project
- Set expectations
- Motivate: "This is what you'll be able to do"

---

#### 8.2 Building the Client Onboarding Agent (40 min)
**Type:** Screencast

**Content:**
Step-by-step build of a complete workflow:

1. **Trigger**: New client form submission (via n8n webhook)
2. **Claude Processing**:
   - Analyze client info
   - Generate welcome email draft
   - Create project folder structure
3. **Automations**:
   - Create Google Drive folder
   - Add to CRM (or Google Sheet)
   - Schedule kickoff calendar event
4. **Notifications**:
   - Send welcome email
   - Slack notification to team

**Record:**
- Build entire workflow in real-time
- Pause to explain key decisions
- Show testing at each stage
- Handle an error and fix it

**Downloadable:**
- [ ] Complete Workflow Files (n8n export, Claude skill)
- [ ] Customization Guide

---

#### 8.3 Testing & Refinement (10 min)
**Type:** Screencast

**Content:**
- End-to-end testing
- Edge cases to consider
- Refinement based on results
- Performance optimization

**Record:**
- Run full workflow test
- Identify an issue and fix it
- Show iteration cycle

---

#### 8.4 Certification & Next Steps (5 min)
**Type:** Talking head

**Content:**
- Congratulations!
- Certification quiz instructions
- How to get your badge
- Next steps: Pro tier, community, ongoing learning

**Record:**
- Celebration moment
- Clear instructions for certification
- Invitation to deeper engagement

---

## Downloadable Resources Summary

### Templates & Worksheets
| Resource | Module | Format |
|----------|--------|--------|
| AI Readiness Audit Worksheet | 1 | Google Sheets |
| Pain Point Prioritization Matrix | 1 | PDF |
| Current Tool Inventory | 1 | Google Sheets |
| Account Setup Checklist | 1 | PDF |
| Credentials Vault Template | 1 | JSON |
| Launchpad Stack Diagram | 1 | PDF |
| Monthly Cost Calculator | 1 | Google Sheets |
| Installation Guide | 2 | PDF |
| Claude Code Cheat Sheet | 2 | PDF |
| Business Prompt Templates | 2 | PDF |
| CLAUDE.md Templates | 2 | MD files |
| MCP Config Templates | 3 | JSON |
| Troubleshooting Flowchart | 3 | PDF |
| Skill Creation Template | 4 | MD files |
| Automation ROI Calculator | 5 | Google Sheets |
| n8n Workflow Templates | 5 | JSON |
| Zapier Templates | 5 | Links |
| AWS Cheat Sheet | 6 | PDF |
| Cloud Cost Tracker | 6 | Google Sheets |
| Security Checklists | 7 | PDF |
| Responsible AI Policy | 7 | DOCX |
| System Runbook Template | 7 | MD |
| Capstone Workflow Files | 8 | ZIP |

### Estimated Creation Time
| Asset Type | Count | Time Each | Total |
|------------|-------|-----------|-------|
| Video lessons | 35 | 2-3 hrs | ~90 hrs |
| Downloadable PDFs | 15 | 1 hr | ~15 hrs |
| Templates (Sheets/Docs) | 10 | 2 hrs | ~20 hrs |
| Config files | 8 | 30 min | ~4 hrs |
| Workflow exports | 5 | 1 hr | ~5 hrs |

**Total estimated creation time: ~135 hours**

---

## Recording Equipment & Setup Recommendations

### Minimum Setup
- **Screen recording:** OBS Studio (free) or Loom
- **Microphone:** Blue Yeti or similar USB condenser
- **Camera (optional):** Built-in webcam or Logitech C920

### Recommended Setup
- **Screen recording:** Camtasia or ScreenFlow
- **Microphone:** Shure SM7B or Rode NT-USB
- **Camera:** Sony ZV-1 or similar
- **Lighting:** Ring light or key light

### Recording Tips
1. Record in 1080p minimum (4K if possible)
2. Use a consistent intro/outro
3. Keep lessons under 20 minutes when possible
4. Leave room for editing (pauses, retakes)
5. Record audio separately for better quality
6. Use keyboard shortcuts display (KeyCastr on Mac)

---

## Course Platform Setup (Thinkific)

### Module Structure
- Enable drip content (optional) - release weekly or all-at-once
- Require completion before next module (optional)
- Enable discussions per module

### Pricing Setup
- One-time payment: $997
- Payment plan: $127/month × 12 months (or 3 × $397)
- Coupon codes for launches

### Integrations
- Stripe/PayPal for payments
- Discord webhook for community access
- Email automation (welcome sequence)

---

## Launch Checklist

### Pre-Launch (2 weeks before)
- [ ] All videos recorded and edited
- [ ] All downloads created and uploaded
- [ ] Course structure finalized in Thinkific
- [ ] Payment processing tested
- [ ] Email sequences created
- [ ] Discord community ready
- [ ] Launchpad page on support-forge.com live

### Launch Week
- [ ] Soft launch to email list
- [ ] Gather initial feedback
- [ ] Fix any issues
- [ ] Full public launch
- [ ] Social media promotion

### Post-Launch (ongoing)
- [ ] Monitor community questions
- [ ] Weekly Q&A calls
- [ ] Collect testimonials
- [ ] Update content as tools change
- [ ] Track completion rates

---

*Content outline created: January 4, 2026*
