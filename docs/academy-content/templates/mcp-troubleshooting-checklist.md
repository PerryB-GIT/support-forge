# MCP Troubleshooting Checklist

**Issue Type:** [Connection / Authentication / Tool Not Working / Performance]
**Date:** [Date]
**Reported by:** [Name]

---

## Instructions

Work through this checklist systematically when MCP tools aren't working. Check off each item as you verify it. Most issues are resolved in the first section.

---

## Quick Diagnostic Commands

Run these first to understand your current state:

```bash
# Check Claude Code version
claude --version

# Check if Claude Code is running
claude --help

# Check Node.js version (needs 18+)
node --version

# Check npm version
npm --version

# Check if MCP config exists
cat ~/.claude/claude_desktop_config.json    # Mac/Linux
type %APPDATA%\Claude\claude_desktop_config.json   # Windows
```

---

## Section 1: Basic Connectivity (Check First)

### Internet & Network

| Check | Status | Action if Failed |
|-------|--------|------------------|
| [ ] Internet connection working | | Check network, restart router |
| [ ] Can access https://zapier.com | | Check firewall, VPN settings |
| [ ] Can access https://api.anthropic.com | | Check if blocked by network |
| [ ] No VPN interfering | | Try disabling VPN temporarily |
| [ ] Firewall allows outbound HTTPS | | Add exception for node.js |

### Claude Code Status

| Check | Status | Action if Failed |
|-------|--------|------------------|
| [ ] Claude Code is installed | | Run `npm install -g @anthropic-ai/claude-code` |
| [ ] Running latest version | | Run `npm update -g @anthropic-ai/claude-code` |
| [ ] Claude Code starts without error | | Check error message, see Section 4 |
| [ ] Authenticated to Claude | | Run `claude` and re-authenticate |
| [ ] Claude responds to basic prompts | | Test: "What time is it?" |

---

## Section 2: MCP Configuration

### Config File Location

**Mac/Linux:** `~/.claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

| Check | Status | Action if Failed |
|-------|--------|------------------|
| [ ] Config file exists | | Create from template |
| [ ] Config file is valid JSON | | Use JSON validator |
| [ ] File has correct permissions | | Mac/Linux: `chmod 600` |
| [ ] No syntax errors (trailing commas, etc.) | | Check with `cat` and review |

### Config File Validation

Run this to check JSON validity:
```bash
# Mac/Linux
cat ~/.claude/claude_desktop_config.json | python -m json.tool

# Windows PowerShell
Get-Content $env:APPDATA\Claude\claude_desktop_config.json | ConvertFrom-Json
```

| Check | Status | Action if Failed |
|-------|--------|------------------|
| [ ] JSON parses without error | | Fix syntax errors |
| [ ] mcpServers key exists | | Add mcpServers section |
| [ ] Server names are unique | | Rename duplicates |
| [ ] All required fields present | | Check template for format |

---

## Section 3: Individual MCP Server Issues

### Zapier MCP

| Check | Status | Action if Failed |
|-------|--------|------------------|
| [ ] Zapier account is active | | Log in at zapier.com |
| [ ] MCP is enabled in Zapier | | https://actions.zapier.com/mcp/start |
| [ ] MCP URL is correct in config | | Copy fresh URL from Zapier |
| [ ] URL format is correct | | Should start with https://actions.zapier.com/mcp/ |
| [ ] Zapier apps are connected | | Check Zapier connected accounts |
| [ ] Apps have required permissions | | Re-authorize apps in Zapier |

**Test Zapier connection:**
```bash
# In Claude Code, ask:
"Use Zapier to list my recent calendar events"
```

### n8n MCP

| Check | Status | Action if Failed |
|-------|--------|------------------|
| [ ] n8n instance is running | | Check n8n dashboard |
| [ ] API is enabled in n8n | | Settings > API > Enable |
| [ ] API key is valid | | Generate new key if needed |
| [ ] Base URL is correct | | Include https:// |
| [ ] Workflows are active | | Check workflow status |

**Test n8n connection:**
```bash
# Try reaching n8n API directly
curl -H "X-N8N-API-KEY: your-key" https://your-n8n.com/api/v1/workflows
```

### GitHub MCP

| Check | Status | Action if Failed |
|-------|--------|------------------|
| [ ] Personal access token is valid | | Generate new at github.com/settings/tokens |
| [ ] Token has required scopes | | Need: repo, read:user |
| [ ] Token isn't expired | | Check token settings |
| [ ] Environment variable is set | | Check GITHUB_PERSONAL_ACCESS_TOKEN |

### Other MCP Servers

| Check | Status | Action if Failed |
|-------|--------|------------------|
| [ ] npx can run the package | | Try `npx -y [package-name] --help` |
| [ ] Package is available on npm | | Check npmjs.com |
| [ ] No conflicting npm versions | | Try `npm cache clean --force` |
| [ ] Required env vars are set | | Check server documentation |

---

## Section 4: Common Error Messages

### "MCP server failed to start"

| Possible Cause | Solution |
|----------------|----------|
| npx not found | Install Node.js, ensure npm in PATH |
| Package not found | Check package name spelling |
| Network error | Check internet, firewall |
| Permission denied | Check file/folder permissions |
| Port in use | Another process using required port |

### "Authentication failed"

| Possible Cause | Solution |
|----------------|----------|
| API key expired | Generate new key |
| API key invalid | Check for typos, whitespace |
| Wrong API key format | Check documentation for format |
| Account suspended | Check account status |
| Rate limited | Wait and retry |

### "Tool not found"

| Possible Cause | Solution |
|----------------|----------|
| MCP server not loaded | Check config, restart Claude Code |
| Tool not enabled | Enable in provider settings (Zapier, etc.) |
| Tool name misspelled | Check exact tool name |
| Permissions missing | Grant required permissions |

### "Timeout" errors

| Possible Cause | Solution |
|----------------|----------|
| Slow network | Check connection speed |
| Server overloaded | Wait and retry |
| Request too large | Break into smaller requests |
| Firewall blocking | Add exception |

---

## Section 5: Environment Issues

### Node.js Problems

| Check | Status | Action if Failed |
|-------|--------|------------------|
| [ ] Node.js v18+ installed | | Download from nodejs.org |
| [ ] Node in PATH | | Reinstall or add to PATH |
| [ ] npm working | | Comes with Node.js |
| [ ] npx working | | Try `npx --version` |
| [ ] No conflicting Node versions | | Use nvm to manage versions |

### Path Issues (Windows)

| Check | Status | Action if Failed |
|-------|--------|------------------|
| [ ] Node in system PATH | | Add via System Properties |
| [ ] npm in PATH | | Usually same location as Node |
| [ ] No spaces in paths | | Move to path without spaces |
| [ ] Using correct slashes | | Windows uses backslash |

### Path Issues (Mac/Linux)

| Check | Status | Action if Failed |
|-------|--------|------------------|
| [ ] Node in PATH | | Check `.bashrc` or `.zshrc` |
| [ ] Permissions on config folder | | `chmod 755 ~/.claude` |
| [ ] Permissions on config file | | `chmod 600` for sensitive files |
| [ ] Shell can find npx | | `which npx` |

---

## Section 6: Reset & Recovery

### Soft Reset (Try First)

```bash
# 1. Quit Claude Code completely

# 2. Clear npx cache
npx clear-npx-cache

# 3. Restart Claude Code
claude

# 4. Test MCP tools
```

### Full Reset

```bash
# 1. Backup config
cp ~/.claude/claude_desktop_config.json ~/.claude/claude_desktop_config.json.backup

# 2. Reinstall Claude Code
npm uninstall -g @anthropic-ai/claude-code
npm cache clean --force
npm install -g @anthropic-ai/claude-code

# 3. Restore config
cp ~/.claude/claude_desktop_config.json.backup ~/.claude/claude_desktop_config.json

# 4. Restart and test
claude
```

### Fresh Start (Last Resort)

```bash
# 1. Remove all Claude Code data
rm -rf ~/.claude  # Mac/Linux
rmdir /s %APPDATA%\Claude  # Windows

# 2. Reinstall
npm uninstall -g @anthropic-ai/claude-code
npm install -g @anthropic-ai/claude-code

# 3. Start fresh
claude

# 4. Reconfigure MCP from template
```

---

## Section 7: Getting Help

### Information to Gather

Before asking for help, collect:

| Information | Command/Location |
|-------------|------------------|
| Claude Code version | `claude --version` |
| Node.js version | `node --version` |
| Operating system | |
| Error message | Copy full text |
| Config file | (Remove secrets first) |
| What you tried | List steps taken |
| When it last worked | |

### Where to Get Help

1. **Claude Code Documentation**: https://docs.anthropic.com/claude-code
2. **MCP Documentation**: https://modelcontextprotocol.io
3. **Zapier Support**: https://help.zapier.com
4. **GitHub Issues**: Check for known issues
5. **Community Forums**: Discord, Reddit, Stack Overflow

### Sample Help Request

```
**Issue**: MCP tools not loading in Claude Code

**Environment**:
- Claude Code v1.0.0
- Node.js v20.10.0
- macOS 14.2

**Error Message**:
[Paste full error here]

**Config** (secrets removed):
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://actions.zapier.com/mcp/xxx/sse"]
    }
  }
}

**Steps Tried**:
1. Restarted Claude Code
2. Verified config file is valid JSON
3. Checked Zapier MCP is enabled
4. Reinstalled Claude Code

**When Last Worked**: January 1, 2025
```

---

## Resolution Log

| Date | Issue | Root Cause | Solution |
|------|-------|------------|----------|
| | | | |
| | | | |
| | | | |

---

*Template from AI Launchpad Academy - support-forge.com*
