# Claude Code Troubleshooting Guide

Quick solutions for common issues when installing and using Claude Code.

---

## Installation Issues

### "claude: command not found"

**Cause:** Claude Code not in system PATH

**Solution (Windows/WSL):**
```bash
# Check if installed
npm list -g @anthropic-ai/claude-code

# Reinstall globally
npm install -g @anthropic-ai/claude-code

# Verify PATH includes npm global bin
echo $PATH | grep -o '[^:]*npm[^:]*'
```

**Solution (Mac/Linux):**
```bash
# Check npm global bin location
npm config get prefix

# Add to PATH in ~/.bashrc or ~/.zshrc
export PATH="$PATH:$(npm config get prefix)/bin"
source ~/.bashrc
```

---

### "EACCES: permission denied"

**Cause:** npm trying to write to protected directory

**Solution:**
```bash
# Option 1: Fix npm permissions
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# Option 2: Use nvm (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
nvm use 18
npm install -g @anthropic-ai/claude-code
```

---

### "node: command not found"

**Cause:** Node.js not installed or not in PATH

**Solution:**
```bash
# Install Node.js via nvm (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install 18
```

---

## Authentication Issues

### "Invalid API key"

**Cause:** API key not set or incorrect

**Solution:**
```bash
# Set API key (temporary)
export ANTHROPIC_API_KEY="sk-ant-..."

# Set permanently in ~/.bashrc
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
source ~/.bashrc

# Verify it's set
echo $ANTHROPIC_API_KEY
```

**Check API key validity:**
1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Navigate to API Keys
3. Verify key is active and not expired
4. Check usage limits haven't been exceeded

---

### "Rate limit exceeded"

**Cause:** Too many API requests in short time

**Solution:**
- Wait 60 seconds and retry
- Check your usage at console.anthropic.com
- Consider upgrading your API tier
- Use more efficient prompts (fewer tokens)

---

### "Insufficient credits"

**Cause:** Account balance depleted

**Solution:**
1. Visit [console.anthropic.com/billing](https://console.anthropic.com/billing)
2. Add payment method
3. Purchase credits or enable auto-reload

---

## Runtime Issues

### Claude Code freezes or hangs

**Cause:** Large file being processed or network timeout

**Solutions:**
```bash
# Kill and restart
pkill -f claude
claude

# Clear cache
rm -rf ~/.claude/cache

# Check for large files in context
# Avoid opening files > 1MB
```

---

### "Context length exceeded"

**Cause:** Too much text in conversation

**Solutions:**
- Start a new conversation: `/clear`
- Be more concise in prompts
- Read specific file sections instead of entire files
- Use `--limit` flag when reading files

---

### Slow response times

**Cause:** Network issues or complex queries

**Solutions:**
- Check internet connection
- Use a faster model for simple tasks: `--model claude-3-haiku`
- Break complex tasks into smaller steps
- Reduce context by being specific about files needed

---

### "File not found" errors

**Cause:** Wrong path or file doesn't exist

**Solutions:**
```bash
# Use absolute paths
claude "Read /home/user/project/file.js"

# Verify file exists
ls -la /path/to/file

# Check current directory
pwd
```

---

## MCP Server Issues

### MCP server won't connect

**Cause:** Configuration error or server not running

**Solutions:**
```bash
# Check MCP config location
cat ~/.claude/claude_mcp_config.json

# Validate JSON syntax
python -m json.tool ~/.claude/claude_mcp_config.json

# Check server is running (for local servers)
ps aux | grep mcp
```

---

### "Tool not available"

**Cause:** MCP server not configured or authentication failed

**Solutions:**
1. Verify MCP server is listed in config
2. Check API keys for the MCP service
3. Restart Claude Code after config changes
4. Use `/tools` to see available tools

---

### OAuth authentication failed (Google services)

**Cause:** Token expired or permissions revoked

**Solutions:**
1. Re-authenticate:
   ```bash
   # Remove cached credentials
   rm -rf ~/.claude/google-credentials
   ```
2. Restart Claude Code
3. Re-authorize when prompted
4. Check Google Cloud Console for active OAuth consent

---

## Performance Issues

### High memory usage

**Cause:** Large context or many open sessions

**Solutions:**
```bash
# Clear conversation history
/clear

# Close other Claude Code sessions
pkill -f claude

# Restart with fresh session
claude
```

---

### Commands executing slowly

**Cause:** Network latency or overloaded API

**Solutions:**
- Use local tools when possible
- Check API status: [status.anthropic.com](https://status.anthropic.com)
- Try again during off-peak hours
- Use smaller model for quick tasks

---

## Common Error Messages Quick Reference

| Error | Likely Cause | Quick Fix |
|-------|--------------|-----------|
| `ENOENT` | File/directory not found | Check path exists |
| `EACCES` | Permission denied | Use sudo or fix permissions |
| `ECONNREFUSED` | Server not running | Start the required service |
| `ETIMEDOUT` | Network timeout | Check internet, retry |
| `EPERM` | Operation not permitted | Check file permissions |
| `429` | Rate limited | Wait and retry |
| `401` | Unauthorized | Check API key |
| `403` | Forbidden | Check permissions/scopes |
| `500` | Server error | Retry later |

---

## Getting More Help

### Collect Debug Information
```bash
# System info
uname -a
node --version
npm --version

# Claude Code version
claude --version

# Check logs
cat ~/.claude/logs/latest.log
```

### Where to Get Help
1. **Discord Community** - #tech-support channel
2. **GitHub Issues** - [github.com/anthropics/claude-code](https://github.com/anthropics/claude-code/issues)
3. **Course Office Hours** - Weekly live Q&A
4. **Email** - support@support-forge.com

### Before Asking for Help
- [ ] Note the exact error message
- [ ] Note what you were trying to do
- [ ] Check this guide first
- [ ] Search existing issues
- [ ] Collect debug information above

---

*AI Launchpad Academy - Support Forge*
