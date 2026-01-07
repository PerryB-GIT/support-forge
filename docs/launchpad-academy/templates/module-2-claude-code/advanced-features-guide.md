# Claude Code Advanced Features Reference

Power-user features for getting more from Claude Code.

---

## Git Integration

### Automated Commits
```bash
# Let Claude write commit messages
claude "Review staged changes and create a descriptive commit message"

# Full workflow
git add .
claude "Write a conventional commit message for these changes, then commit"
```

### Code Review
```bash
# Review a PR
claude "Review the changes in PR #42 and provide feedback"

# Compare branches
claude "Compare feature-branch to main and summarize the changes"
```

### Branch Management
```bash
claude "Create a new feature branch for user-authentication, based on main"
```

---

## Multi-File Operations

### Batch Edits
```
Apply consistent changes across multiple files:
1. Add copyright header to all .js files in src/
2. Update import paths from '../utils' to '@/utils'
3. Add TypeScript types to all function parameters
```

### Project-Wide Refactoring
```
Refactor the codebase:
- Rename all instances of 'userData' to 'userProfile'
- Update all files that import from 'utils/helpers.js'
- Ensure consistent naming convention (camelCase)
```

### Search and Transform
```
Find all TODO comments in the project and:
1. List them with file locations
2. Categorize by urgency
3. Create GitHub issues for high-priority items
```

---

## Background Tasks

### Long-Running Operations
```bash
# Run in background (doesn't block terminal)
claude --background "Analyze all JavaScript files and create a dependency graph"

# Check status
claude --status

# Get results
claude --results
```

### Scheduled Operations
```bash
# Using cron with Claude Code
# Add to crontab: crontab -e

# Daily code quality check at 9am
0 9 * * * cd /path/to/project && claude "Run code quality checks and save report to reports/daily-$(date +%Y%m%d).md"
```

---

## Hooks and Automation

### Pre-Commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit

# Run Claude Code check before commit
claude "Check staged files for:
- Security vulnerabilities
- Console.log statements
- Hardcoded credentials
Output: pass/fail with reasons" > /tmp/claude-check.txt

if grep -q "fail" /tmp/claude-check.txt; then
    cat /tmp/claude-check.txt
    exit 1
fi
```

### Post-Merge Hook
```bash
#!/bin/bash
# .git/hooks/post-merge

# Generate changelog entry
claude "Review the merged commits and create a changelog entry"
```

### Custom Triggers
```bash
# Watch for file changes and respond
fswatch -o ./src | while read; do
    claude "Files changed in src/. Check for any issues."
done
```

---

## Skills System

### Installing Skills
```bash
# From marketplace
claude "/install skill-name"

# From GitHub
claude "/install https://github.com/user/skill-repo"

# From local path
claude "/install ~/my-skills/custom-skill"
```

### Creating Custom Skills

**Skill structure:**
```
my-skill/
├── SKILL.md          # Skill definition
├── templates/        # Supporting templates
│   └── output.md
└── examples/         # Usage examples
    └── example.md
```

**SKILL.md format:**
```markdown
# Skill: Daily Report Generator

## Description
Generates daily status reports from git activity and project state.

## Trigger
/daily-report or "generate daily report"

## Inputs
- project_path: Path to project (default: current directory)
- date: Report date (default: today)

## Process
1. Get git commits from the specified date
2. Summarize changes by category
3. List open issues/PRs
4. Generate formatted report

## Output
Markdown report saved to reports/daily-{date}.md
```

### Skill Chaining
```
Run skills in sequence:
1. /code-review - Check code quality
2. /test-coverage - Verify test coverage
3. /documentation - Update docs
4. /changelog - Update changelog
```

---

## Context Management

### Context Windows
```bash
# Check current context usage
claude "/context"

# Clear context to start fresh
claude "/clear"

# Save context for later
claude "/save my-session-name"

# Restore context
claude "/restore my-session-name"
```

### Selective Context
```
Read only specific sections:
- Read lines 100-200 of large-file.js
- Read only function definitions in auth.js
- Read only test files matching *test*.js
```

### Context Compression
```
Summarize the codebase context:
- Main components and their purposes
- Key files and their roles
- Important patterns used

Then clear detailed context but keep summary.
```

---

## Output Formats

### Structured Output
```
Analyze this code and return JSON:
{
  "complexity": "low/medium/high",
  "issues": ["array of issues"],
  "suggestions": ["array of suggestions"],
  "score": 0-100
}
```

### File Generation
```
Create the following files:
1. src/components/Button.jsx - React button component
2. src/components/Button.test.js - Jest tests
3. src/components/Button.css - Styles

Use consistent naming and import patterns.
```

### Report Generation
```
Generate a project health report including:

## Summary
[Executive summary]

## Metrics
| Metric | Value | Status |
|--------|-------|--------|
| Test coverage | X% | [emoji] |
| Code quality | X/10 | [emoji] |
| Dependencies | X outdated | [emoji] |

## Recommendations
[Prioritized list]
```

---

## API Integration

### Calling External APIs
```
Fetch data from our API and process it:
1. GET https://api.example.com/users
2. Filter for active users
3. Generate a summary report
4. Save to reports/users-summary.md

Use the API_KEY environment variable for authentication.
```

### Webhook Triggers
```bash
# Trigger Claude Code from webhook
curl -X POST http://localhost:3000/claude-webhook \
  -H "Content-Type: application/json" \
  -d '{"task": "process-new-file", "file": "uploads/data.csv"}'
```

---

## Performance Optimization

### Efficient File Reading
```
# Bad: Reading entire large file
Read large-dataset.json

# Good: Reading specific parts
Read lines 1-100 of large-dataset.json
Read only the "users" key from large-dataset.json
```

### Caching Strategies
```bash
# Enable response caching
export CLAUDE_CACHE=1

# Cache directory
export CLAUDE_CACHE_DIR=~/.claude/cache

# Cache TTL (seconds)
export CLAUDE_CACHE_TTL=3600
```

### Batch Processing
```
Process these 20 files efficiently:
- Group by file type
- Apply common transformations in batch
- Only make individual changes where needed
```

---

## Debugging

### Verbose Mode
```bash
# Enable debug output
claude --debug "Your prompt here"

# Log to file
claude --debug --log-file debug.log "Your prompt"
```

### Inspect Context
```bash
# See what's in context
claude "/debug context"

# Check tool availability
claude "/tools"

# View active settings
claude "/settings"
```

### Replay Sessions
```bash
# Save session for debugging
claude --save-session debug-session "Your prompt"

# Replay with modifications
claude --replay debug-session --modify "Changed approach"
```

---

## Team Collaboration

### Shared Configurations
```bash
# Project-level settings (commit to repo)
.claude/
├── settings.json      # Team settings
├── skills/            # Shared skills
└── templates/         # Shared templates

# Gitignore personal overrides
echo ".claude/local/" >> .gitignore
```

### Documentation Generation
```
Generate documentation for this project:
1. README.md - Project overview
2. CONTRIBUTING.md - Contribution guidelines
3. API.md - API documentation
4. CHANGELOG.md - Version history

Use existing code comments and structure.
```

---

## Quick Reference

### Useful Aliases
```bash
# Add to ~/.bashrc
alias cc="claude"
alias ccr="claude 'Review this file'"
alias cct="claude 'Write tests for this'"
alias ccf="claude 'Fix the issue:'"
alias ccd="claude 'Document this code'"
```

### Command Shortcuts
| Shortcut | Action |
|----------|--------|
| `/clear` | Clear context |
| `/help` | Show help |
| `/tools` | List available tools |
| `/model [name]` | Switch model |
| `/save [name]` | Save session |
| `/restore [name]` | Restore session |

---

*AI Launchpad Academy - Support Forge*
