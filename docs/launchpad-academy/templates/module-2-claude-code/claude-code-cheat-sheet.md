# Claude Code Cheat Sheet

Quick reference guide for Claude Code power users.

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + C` | Cancel current operation |
| `Ctrl + D` | Exit Claude Code |
| `Ctrl + L` | Clear terminal (keeps context) |
| `Ctrl + U` | Clear current input line |
| `Ctrl + W` | Delete word before cursor |
| `Ctrl + A` | Move cursor to beginning of line |
| `Ctrl + E` | Move cursor to end of line |
| `Up Arrow` | Previous command/prompt |
| `Down Arrow` | Next command/prompt |
| `Tab` | Auto-complete file paths |
| `Shift + Enter` | Multi-line input |
| `Esc` | Cancel current input |

---

## Slash Commands

### Session Management

| Command | Description |
|---------|-------------|
| `/help` | Display all available commands |
| `/clear` | Clear conversation history and start fresh |
| `/compact` | Summarize conversation to reduce context size |
| `/status` | Show current session status and token usage |
| `/config` | View or modify configuration |
| `/logout` | Sign out of current session |

### Context & Memory

| Command | Description |
|---------|-------------|
| `/init` | Initialize CLAUDE.md in current directory |
| `/memory` | View what Claude remembers from this session |
| `/forget` | Clear specific memories or all session context |
| `/context` | Show current context window usage |

### File Operations

| Command | Description |
|---------|-------------|
| `/add <file>` | Add file to conversation context |
| `/add <folder>` | Add folder contents to context |
| `/tree` | Display project directory structure |
| `/diff` | Show pending file changes before applying |

### Tools & Integration

| Command | Description |
|---------|-------------|
| `/tools` | List available tools and MCP servers |
| `/mcp` | Manage MCP server connections |
| `/web` | Enable/disable web search |
| `/image` | Include image in conversation |

### Mode Switching

| Command | Description |
|---------|-------------|
| `/chat` | Switch to chat-only mode (no tools) |
| `/agent` | Switch to full agent mode (default) |
| `/code` | Focus mode for code generation |

### Output Control

| Command | Description |
|---------|-------------|
| `/verbose` | Enable detailed output |
| `/quiet` | Minimize output verbosity |
| `/export` | Export conversation to file |

---

## Common Tool Usage Patterns

### File Reading & Editing

```
# Read a specific file
"Read the contents of src/index.ts"

# Search across codebase
"Find all files that import the UserService class"

# Edit a file
"Update the timeout value in config.js from 5000 to 10000"

# Create a new file
"Create a new React component called UserProfile in src/components/"
```

### Code Analysis

```
# Understand code structure
"Explain how the authentication flow works in this project"

# Find bugs
"Review src/api/handlers.ts for potential security issues"

# Refactor suggestions
"Suggest improvements for the database query in models/user.js"
```

### Terminal Commands

```
# Run commands
"Run npm install and show me any errors"

# Check status
"Run git status and summarize the changes"

# Build projects
"Build the project and fix any TypeScript errors"
```

### Web & Research

```
# Web search
"Search for the latest Next.js 14 routing changes"

# Documentation lookup
"Find the official docs for AWS S3 presigned URLs"

# API research
"Look up the Stripe API for subscription management"
```

---

## Tips for Effective Sessions

### 1. Start with Context

Always begin sessions with relevant context:

```
I'm working on a Next.js e-commerce site. The project uses:
- TypeScript
- Tailwind CSS
- Prisma with PostgreSQL
- Stripe for payments

Today I need to implement the checkout flow.
```

### 2. Use CLAUDE.md Files

Create `CLAUDE.md` in your project root:

```markdown
# Project: My E-Commerce Store

## Tech Stack
- Next.js 14 with App Router
- TypeScript strict mode
- Tailwind CSS
- Prisma ORM

## Code Style
- Use functional components
- Prefer named exports
- Error handling with try/catch

## Important Files
- src/lib/db.ts - Database connection
- src/lib/stripe.ts - Stripe configuration
```

### 3. Be Specific with Requests

**Less effective:**
```
"Fix the bug"
```

**More effective:**
```
"The login form in src/components/LoginForm.tsx throws an error
when submitting empty fields. Add validation to show error
messages instead of crashing."
```

### 4. Use Incremental Development

Break large tasks into steps:

```
1. "First, create the database schema for user subscriptions"
2. "Now create the API endpoint for creating subscriptions"
3. "Add the frontend form to handle subscription signup"
4. "Finally, add error handling and loading states"
```

### 5. Request Explanations When Needed

```
"Create the authentication middleware and explain each step
so I can maintain it later"
```

### 6. Use /compact Regularly

For long sessions, periodically run:
```
/compact
```
This preserves important context while freeing up token space.

### 7. Leverage Multi-File Edits

```
"Update the User type across all files that reference it to
include the new 'subscription' field"
```

### 8. Ask for Tests

```
"Create unit tests for the calculateDiscount function using Jest"
```

### 9. Request Documentation

```
"Add JSDoc comments to all exported functions in src/utils/"
```

### 10. Use Git Integration

```
"Show me what changed since the last commit"
"Create a commit message for these changes"
"Help me resolve the merge conflict in package.json"
```

---

## Context Window Management

### Checking Usage

```
/context
```

### Signs You Need to Compact

- Responses getting slower
- Claude forgetting earlier context
- Errors about context length

### Best Practices

1. **Start focused**: Only add relevant files
2. **Compact after milestones**: Complete a feature, then `/compact`
3. **Use multiple sessions**: One session per major task
4. **Be selective with code**: Add specific files, not entire folders

---

## Error Handling Quick Fixes

| Error | Quick Fix |
|-------|-----------|
| "Context too long" | Run `/compact` or start new session |
| "Tool not available" | Check `/tools` and MCP status |
| "Rate limited" | Wait 60 seconds, then retry |
| "Authentication failed" | Run `/logout` then re-authenticate |
| "File not found" | Check path, use absolute paths |
| "Permission denied" | Check file permissions, run with appropriate access |

---

## Quick Command Templates

### Daily Workflow

```bash
# Morning: Start fresh session with project context
claude
/add .
"What did I work on last session? Review recent git commits."

# During work: Regular compaction
/compact

# End of day: Summary
"Summarize what we accomplished today for my notes"
/export daily-notes.md
```

### Code Review

```
"Review the changes in this PR for:
1. Code quality issues
2. Potential bugs
3. Security concerns
4. Performance problems
Give me a summary with line-specific feedback."
```

### Debug Session

```
"I'm getting this error: [paste error]

The relevant code is in src/api/handler.ts.
Help me:
1. Understand what's causing the error
2. Find the root cause
3. Implement a fix"
```

### Documentation Sprint

```
"I need to document the API. For each endpoint in src/api/:
1. Add JSDoc comments with params and returns
2. Create a README with usage examples
3. Generate TypeScript types for responses"
```

---

## MCP Server Quick Reference

### Checking Connected Servers

```
/tools
```

### Common MCP Integrations

| Server | Use Case |
|--------|----------|
| Zapier | Automate workflows, connect apps |
| GitHub | Manage repos, issues, PRs |
| Google Drive | Access documents and spreadsheets |
| Slack | Send messages and manage channels |
| Database | Query databases directly |

### Adding Context from MCP

```
"Use Zapier to find my recent emails about the project deadline"
"Check GitHub for open issues in the frontend repo"
"Get the latest sales data from the Google Sheet"
```

---

## Session Best Practices Summary

1. **Initialize context** - Use CLAUDE.md and `/add` relevant files
2. **Be specific** - Clear requests get better results
3. **Work incrementally** - Break big tasks into steps
4. **Manage context** - Use `/compact` and `/clear` appropriately
5. **Verify changes** - Review edits before accepting
6. **Learn from errors** - Ask Claude to explain what went wrong
7. **Export important work** - Save key outputs with `/export`
