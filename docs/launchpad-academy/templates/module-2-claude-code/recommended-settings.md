# Claude Code Recommended Settings for Business Use

Optimize your Claude Code configuration for professional workflows.

---

## Settings File Location

Claude Code settings are stored in:
- **Global:** `~/.claude/settings.json`
- **Project:** `.claude/settings.json` (in project root)

Project settings override global settings.

---

## Essential Settings

### Basic Configuration
```json
{
  "model": "claude-sonnet-4-20250514",
  "maxTokens": 4096,
  "temperature": 0.7,
  "apiKey": "${ANTHROPIC_API_KEY}"
}
```

### Setting Explanations

| Setting | Purpose | Recommended Value |
|---------|---------|-------------------|
| `model` | Which Claude model to use | `claude-sonnet-4-20250514` for balance |
| `maxTokens` | Maximum response length | `4096` for most tasks |
| `temperature` | Creativity vs consistency | `0.7` for business tasks |

---

## Model Selection Guide

### Available Models

| Model | Best For | Speed | Cost |
|-------|----------|-------|------|
| `claude-3-haiku` | Quick tasks, simple queries | Fastest | Lowest |
| `claude-sonnet-4-20250514` | General business use | Fast | Medium |
| `claude-opus-4-20250514` | Complex analysis, important docs | Slower | Highest |

### When to Use Each

**Use Haiku for:**
- Quick file searches
- Simple reformatting
- Basic Q&A
- Syntax checking

**Use Sonnet for (Default):**
- Email drafting
- Code review
- Document analysis
- Most daily tasks

**Use Opus for:**
- Complex strategy docs
- Detailed analysis
- Multi-step reasoning
- Critical business decisions

---

## Business-Optimized Settings

### For Consulting Work
```json
{
  "model": "claude-sonnet-4-20250514",
  "temperature": 0.6,
  "maxTokens": 8192,
  "systemPrompt": "You are a professional business consultant. Be precise, data-driven, and actionable in your recommendations."
}
```

### For Technical Work
```json
{
  "model": "claude-sonnet-4-20250514",
  "temperature": 0.3,
  "maxTokens": 4096,
  "systemPrompt": "You are a senior software engineer. Write clean, well-documented code. Follow best practices."
}
```

### For Creative/Marketing
```json
{
  "model": "claude-sonnet-4-20250514",
  "temperature": 0.8,
  "maxTokens": 4096,
  "systemPrompt": "You are a creative marketing professional. Generate engaging, original content while maintaining brand voice."
}
```

### For Data Analysis
```json
{
  "model": "claude-opus-4-20250514",
  "temperature": 0.2,
  "maxTokens": 8192,
  "systemPrompt": "You are a data analyst. Be methodical, verify calculations, and present findings clearly with supporting evidence."
}
```

---

## CLAUDE.md Configuration

The `CLAUDE.md` file in your project root provides persistent context.

### Business Template
```markdown
# Project Configuration

## About This Project
- **Client:** [Company Name]
- **Project Type:** [Website/App/Consulting]
- **Industry:** [Industry]

## Communication Style
- Professional but approachable
- Use industry-appropriate terminology
- Be concise and actionable

## Technical Stack
- [List key technologies]

## Important Contacts
- Project Lead: [Name]
- Technical Contact: [Name]

## Key Dates
- Project Start: [Date]
- Key Milestones: [List]

## Constraints
- [Budget limitations]
- [Technical restrictions]
- [Compliance requirements]
```

### Quick Tips for CLAUDE.md
1. Keep it under 500 lines for best performance
2. Put most important info at the top
3. Update as project evolves
4. Use clear section headers
5. Include examples of desired output style

---

## Environment Variables

### Required
```bash
# In ~/.bashrc or ~/.zshrc
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```

### Optional
```bash
# Model override
export CLAUDE_MODEL="claude-sonnet-4-20250514"

# Custom config location
export CLAUDE_CONFIG_DIR="~/.claude"

# Debug mode
export CLAUDE_DEBUG=1
```

---

## Security Settings

### API Key Best Practices

**DO:**
- Store API key in environment variable
- Use different keys for dev/production
- Rotate keys quarterly
- Set spending limits in Anthropic console

**DON'T:**
- Hardcode keys in settings files
- Commit keys to git
- Share keys across team (use individual keys)
- Use production keys for testing

### Secure Settings Example
```json
{
  "model": "claude-sonnet-4-20250514",
  "apiKey": "${ANTHROPIC_API_KEY}",
  "logLevel": "warn",
  "telemetry": false
}
```

---

## Performance Tuning

### For Speed
```json
{
  "model": "claude-3-haiku",
  "maxTokens": 1024,
  "temperature": 0.5,
  "streamOutput": true
}
```

### For Quality
```json
{
  "model": "claude-opus-4-20250514",
  "maxTokens": 8192,
  "temperature": 0.4,
  "streamOutput": false
}
```

### For Cost Efficiency
```json
{
  "model": "claude-3-haiku",
  "maxTokens": 2048,
  "cacheResponses": true
}
```

---

## Workspace Organization

### Recommended Directory Structure
```
~/work/
├── clients/
│   ├── client-a/
│   │   ├── .claude/
│   │   │   └── settings.json
│   │   └── CLAUDE.md
│   └── client-b/
│       ├── .claude/
│       │   └── settings.json
│       └── CLAUDE.md
├── internal/
│   └── ...
└── templates/
    └── ...
```

### Per-Client Settings
Each client folder gets its own:
- `CLAUDE.md` with client context
- `.claude/settings.json` with appropriate model/style
- Relevant MCP configurations

---

## Quick Setup Checklist

- [ ] Set `ANTHROPIC_API_KEY` environment variable
- [ ] Create global `~/.claude/settings.json`
- [ ] Set default model to Sonnet
- [ ] Configure spending alerts in Anthropic console
- [ ] Create CLAUDE.md template for new projects
- [ ] Set up project-specific settings for key clients
- [ ] Test configuration with simple prompt

---

## Troubleshooting Settings

### Settings Not Applied
```bash
# Check which settings file is being used
claude --debug

# Verify JSON syntax
python -m json.tool ~/.claude/settings.json
```

### Model Not Found
- Verify model name spelling
- Check API key has access to model
- Ensure account tier supports model

### API Key Issues
```bash
# Test key directly
curl -H "x-api-key: $ANTHROPIC_API_KEY" \
  https://api.anthropic.com/v1/models
```

---

*AI Launchpad Academy - Support Forge*
