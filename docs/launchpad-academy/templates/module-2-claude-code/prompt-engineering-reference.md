# Prompt Engineering Quick Reference

Master the art of communicating effectively with Claude Code for business tasks.

---

## The CRISP Framework

Use CRISP for consistently effective prompts:

| Letter | Element | Description |
|--------|---------|-------------|
| **C** | Context | Background information Claude needs |
| **R** | Role | Who Claude should act as |
| **I** | Instructions | Specific task to perform |
| **S** | Specifics | Details, constraints, format requirements |
| **P** | Parameters | Output format, length, style |

### CRISP Example
```
Context: I'm preparing for a client meeting tomorrow with Acme Corp,
a mid-size manufacturing company considering our consulting services.

Role: Act as my executive assistant with knowledge of B2B sales.

Instructions: Create a meeting prep document that includes:
- Company research summary
- Key talking points
- Questions to ask them
- Potential objections and responses

Specifics: Focus on their digital transformation challenges mentioned
in their recent press release. Meeting is 30 minutes.

Parameters: Format as a bulleted document, keep under 1 page.
```

---

## Prompt Patterns

### 1. Direct Request
Best for: Simple, clear tasks
```
Create a README.md for this project
```

### 2. Step-by-Step
Best for: Complex, multi-part tasks
```
I need to set up a new client project. Please:
1. Create a folder structure for the project
2. Initialize a git repository
3. Create a basic README with placeholder sections
4. Set up a .gitignore file
```

### 3. Examples-Based
Best for: Specific output format
```
Generate 5 email subject lines for our newsletter.

Style like these examples:
- "3 AI tools that saved me 10 hours this week"
- "The automation mistake everyone makes"
- "Why your competitors are moving faster"
```

### 4. Constraints-First
Best for: Avoiding unwanted output
```
Write a project update email.

Constraints:
- Maximum 150 words
- No technical jargon
- Must mention timeline
- Professional but friendly tone
```

### 5. Role-Play
Best for: Domain-specific tasks
```
You are a senior financial analyst. Review this quarterly
report and identify the top 3 areas of concern for
the executive team.
```

---

## Magic Phrases

### For Better Outputs
| Phrase | Effect |
|--------|--------|
| "Think step by step" | Forces systematic reasoning |
| "Let's verify this" | Triggers fact-checking |
| "Be specific about..." | Gets detailed information |
| "In simple terms" | Reduces jargon |
| "What are the tradeoffs?" | Gets balanced analysis |

### For Output Control
| Phrase | Effect |
|--------|--------|
| "Keep it under X words" | Controls length |
| "Format as [table/list/JSON]" | Controls structure |
| "Use markdown formatting" | Gets formatted output |
| "No explanations, just the answer" | Reduces verbosity |
| "Include examples" | Gets concrete demonstrations |

### For Quality
| Phrase | Effect |
|--------|--------|
| "Double-check your work" | Reduces errors |
| "What am I missing?" | Gets additional considerations |
| "What could go wrong?" | Gets risk analysis |
| "Is there a simpler approach?" | Avoids over-engineering |

---

## Context Techniques

### File Context
```
# Good: Specific file
Read src/auth/login.js and explain the authentication flow

# Bad: Vague reference
Look at the auth stuff and explain it
```

### Project Context
```
# Good: Clear scope
This is a Next.js e-commerce site using Stripe for payments.
I need to add a feature for...

# Bad: Assumes knowledge
Add the cart feature
```

### Historical Context
```
# Good: Reference previous work
Earlier we created the user model. Now I need to add
email verification to the signup flow.

# Bad: Assumes memory across sessions
Continue where we left off
```

---

## Anti-Patterns (What NOT to Do)

### 1. Vague Requests
```
❌ "Make it better"
✅ "Improve readability by adding comments and breaking long functions into smaller ones"
```

### 2. Overloading
```
❌ "Write a full e-commerce platform with user auth, payments, inventory,
    shipping, analytics, and admin dashboard"
✅ "Let's start with user authentication. Create a signup/login flow using JWT"
```

### 3. Ambiguous References
```
❌ "Fix that bug we discussed"
✅ "Fix the null pointer exception in processOrder() at line 47"
```

### 4. Missing Context
```
❌ "Why isn't this working?"
✅ "Running 'npm test' gives error 'Cannot find module xyz'. Here's my package.json..."
```

---

## Business Task Templates

### Email Drafting
```
Write a [type] email to [recipient].

Context: [situation]
Tone: [professional/friendly/urgent]
Key points to include:
- [point 1]
- [point 2]
Length: [short/medium/detailed]
```

### Report Generation
```
Create a [type] report on [topic].

Include:
- Executive summary
- Key findings
- Data/metrics: [specify]
- Recommendations
- Next steps

Audience: [who will read this]
Format: [document structure]
```

### Analysis Request
```
Analyze [subject] from [files/data].

Focus on:
- [aspect 1]
- [aspect 2]

Deliverable: [what you want]
Format: [how to present]
```

### Meeting Prep
```
Prepare for my meeting with [who] about [topic].

Create:
- Agenda (30 min meeting)
- Key talking points
- Questions to ask
- Potential concerns to address

Background: [context about relationship/history]
```

---

## Iteration Techniques

### Refinement Loop
```
1. Initial: "Create a marketing email for our new feature"
2. Refine: "Good, but make it more urgent and add a clear CTA"
3. Polish: "Perfect. Now create 3 subject line variations"
```

### A/B Variations
```
Create two versions of this landing page copy:
Version A: Focus on features
Version B: Focus on benefits

I'll test both to see which converts better.
```

### Building Up
```
Start with: "Outline a blog post about AI in small business"
Then: "Expand section 2 about automation opportunities"
Then: "Add specific examples and statistics"
```

---

## Quick Reference Card

### Starting a Task
```
I need to [action] for [purpose].
Context: [background]
Requirements: [constraints]
```

### Getting Specific Output
```
Output as [format].
Include [required elements].
Keep it [length/style].
```

### Troubleshooting
```
I'm getting [error/issue].
Expected: [what should happen]
Actual: [what's happening]
I've tried: [attempted solutions]
```

### Review Request
```
Review [file/text] for [purpose].
Focus on: [areas]
Flag: [what to highlight]
```

---

*AI Launchpad Academy - Support Forge*
