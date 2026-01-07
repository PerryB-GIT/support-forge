# MCP Server Troubleshooting Guide

A comprehensive guide to diagnosing and resolving common MCP (Model Context Protocol) server issues in Claude Code.

---

## Table of Contents

1. [Quick Diagnostic Checklist](#quick-diagnostic-checklist)
2. [Common Error Messages](#common-error-messages)
3. [Connection Issues](#connection-issues)
4. [Authentication Failures](#authentication-failures)
5. [Permission Issues](#permission-issues)
6. [Timeout Problems](#timeout-problems)
7. [Log File Locations](#log-file-locations)
8. [Diagnostic Flowchart](#diagnostic-flowchart)
9. [Service-Specific Issues](#service-specific-issues)
10. [Getting Help](#getting-help)

---

## Quick Diagnostic Checklist

Run through this checklist before diving into specific issues:

- [ ] **Is Claude Code running?** - Restart if unresponsive
- [ ] **Is your internet connection stable?** - Test with `ping google.com`
- [ ] **Is Node.js installed?** - Run `node --version` (requires v18+)
- [ ] **Is npx available?** - Run `npx --version`
- [ ] **Are API keys set correctly?** - Check for typos, whitespace
- [ ] **Are API keys expired?** - Regenerate if needed
- [ ] **Is the MCP config file valid JSON?** - Use a JSON validator
- [ ] **Have you removed all comments from JSON?** - JSON doesn't support comments
- [ ] **Are required services enabled?** - Check Google Cloud Console, etc.
- [ ] **Is your firewall blocking connections?** - Check firewall rules

---

## Common Error Messages

### "Connection Refused" / "ECONNREFUSED"

**What it means:** Claude Code cannot establish a connection to the MCP server.

**Causes:**
- MCP server process failed to start
- Wrong port or address configured
- Firewall blocking the connection
- Network issues

**Solutions:**

1. **Check if npx can run the server manually:**
   ```bash
   npx -y @modelcontextprotocol/server-github
   ```
   If this fails, there's an issue with the package or Node.js installation.

2. **Verify Node.js installation:**
   ```bash
   node --version    # Should be 18.0.0 or higher
   npm --version     # Should be 8.0.0 or higher
   ```

3. **Clear npx cache:**
   ```bash
   # Windows
   rmdir /s /q %LOCALAPPDATA%\npm-cache\_npx

   # Mac/Linux
   rm -rf ~/.npm/_npx
   ```

4. **Check firewall settings:**
   - Windows: Allow Node.js through Windows Defender Firewall
   - Mac: System Preferences > Security & Privacy > Firewall
   - Linux: Check iptables or ufw rules

---

### "Authentication Failed" / "Unauthorized" / "401"

**What it means:** Your API key or token is invalid or not being sent correctly.

**Causes:**
- Incorrect API key
- Expired token
- Whitespace in the key
- Wrong environment variable name

**Solutions:**

1. **Verify your API key:**
   - Re-copy from the source (Zapier, GitHub, etc.)
   - Check for leading/trailing whitespace
   - Ensure no line breaks in the key

2. **Test the API key directly:**
   ```bash
   # GitHub
   curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user

   # Should return your user info, not an error
   ```

3. **Check environment variable:**
   ```bash
   # Windows PowerShell
   echo $env:GITHUB_PERSONAL_ACCESS_TOKEN

   # Mac/Linux
   echo $GITHUB_PERSONAL_ACCESS_TOKEN
   ```

4. **Regenerate the token:**
   - GitHub: github.com/settings/tokens
   - Zapier: zapier.com/mcp
   - Google: console.cloud.google.com

---

### "Permission Denied" / "Forbidden" / "403"

**What it means:** Authentication succeeded, but you don't have permission for that action.

**Causes:**
- Insufficient OAuth scopes
- Missing API permissions
- Organization restrictions
- Resource-level permissions

**Solutions:**

1. **Check required scopes:**
   - GitHub: Verify token has `repo`, `workflow`, etc.
   - Google: Check OAuth consent screen scopes
   - Zapier: Ensure actions are configured in dashboard

2. **Organization access (GitHub):**
   - Go to github.com/settings/tokens
   - Click "Configure SSO" if your org uses SAML
   - Authorize the token for your organization

3. **Google API permissions:**
   - Enable required APIs in Google Cloud Console
   - Verify OAuth consent screen includes needed scopes
   - Check if you're a test user (for unverified apps)

4. **Regenerate with correct permissions:**
   - Create a new token with all required scopes
   - Revoke the old token for security

---

### "Not Found" / "404"

**What it means:** The requested resource doesn't exist or isn't accessible.

**Causes:**
- Typo in repository/resource name
- Private resource without proper access
- Resource was deleted
- Wrong API endpoint

**Solutions:**

1. **Verify resource exists:**
   - Check the exact spelling of repo/file names
   - Confirm the resource wasn't recently deleted
   - Verify you have access (can see it in browser)

2. **Check access level:**
   - Private repos require `repo` scope
   - Organization repos may need additional access

3. **Verify API endpoint:**
   - Check MCP server documentation
   - Ensure you're using the correct service

---

### "Rate Limited" / "429"

**What it means:** You've exceeded the API request limit.

**Causes:**
- Too many requests in a short period
- Shared IP address hitting limits
- Automated scripts running too fast

**Solutions:**

1. **Wait and retry:**
   - Most rate limits reset within an hour
   - GitHub: 5000 requests/hour (authenticated)
   - Google: Varies by API

2. **Check your rate limit status:**
   ```bash
   # GitHub
   curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/rate_limit
   ```

3. **Reduce request frequency:**
   - Batch operations when possible
   - Add delays between requests
   - Cache results locally

4. **Request higher limits:**
   - GitHub: Contact support for enterprise
   - Google: Request quota increase in Cloud Console

---

### "Timeout" / "ETIMEDOUT"

**What it means:** The request took too long to complete.

**Causes:**
- Slow network connection
- Server overloaded
- Large file operations
- DNS resolution issues

**Solutions:**

See [Timeout Problems](#timeout-problems) section below.

---

### "Invalid JSON" / "Unexpected token"

**What it means:** The MCP configuration file has syntax errors.

**Causes:**
- Comments in JSON file (not allowed)
- Missing commas or brackets
- Trailing commas
- Unescaped characters

**Solutions:**

1. **Remove all comments:**
   - JSON does not support `//` or `/* */` comments
   - Template files include comments for learning only

2. **Validate your JSON:**
   - Use jsonlint.com or similar
   - VS Code will highlight JSON errors

3. **Common JSON mistakes:**
   ```json
   // WRONG - trailing comma
   {
     "key": "value",
   }

   // CORRECT
   {
     "key": "value"
   }
   ```

4. **Check for special characters:**
   - Escape backslashes: `\\`
   - Escape quotes: `\"`

---

## Connection Issues

### Server Won't Start

**Symptoms:**
- "spawn ENOENT" error
- "command not found"
- Server immediately exits

**Diagnostic Steps:**

1. **Verify command exists:**
   ```bash
   which npx        # Mac/Linux
   where npx        # Windows
   ```

2. **Check Node.js installation:**
   ```bash
   node --version
   npm --version
   npx --version
   ```

3. **Reinstall Node.js if needed:**
   - Download from nodejs.org
   - Use nvm for version management

4. **Try running the server manually:**
   ```bash
   npx -y @modelcontextprotocol/server-github
   ```

### Intermittent Disconnections

**Symptoms:**
- MCP works sometimes, fails others
- Random connection drops
- "Socket hang up" errors

**Solutions:**

1. **Check network stability:**
   ```bash
   ping -c 10 api.github.com    # Mac/Linux
   ping -n 10 api.github.com    # Windows
   ```

2. **Disable VPN temporarily** - VPNs can cause connection issues

3. **Check for proxy issues:**
   ```bash
   echo $HTTP_PROXY
   echo $HTTPS_PROXY
   ```

4. **Increase timeout settings** (if available in config)

---

## Authentication Failures

### Token Not Being Used

**Symptoms:**
- Authentication fails despite correct token
- Works in browser but not in Claude Code

**Solutions:**

1. **Verify environment variable is set:**
   ```bash
   # Windows PowerShell
   $env:GITHUB_PERSONAL_ACCESS_TOKEN

   # Windows CMD
   echo %GITHUB_PERSONAL_ACCESS_TOKEN%

   # Mac/Linux
   echo $GITHUB_PERSONAL_ACCESS_TOKEN
   ```

2. **Restart Claude Code** after setting environment variables

3. **Check variable name matches exactly:**
   - `GITHUB_PERSONAL_ACCESS_TOKEN` (not `GITHUB_TOKEN`)
   - Case-sensitive on Mac/Linux

### OAuth Token Expired

**Symptoms:**
- Was working, suddenly stopped
- "Token expired" message

**Solutions:**

1. **For Zapier MCP:**
   - Zapier handles refresh automatically
   - Reconnect the service in Zapier dashboard

2. **For GitHub tokens:**
   - Check expiration at github.com/settings/tokens
   - Generate new token if expired

3. **For Google OAuth:**
   - Zapier handles refresh automatically
   - Direct integration: implement refresh token logic

---

## Permission Issues

### Organization Access Denied

**Symptoms:**
- Can access personal repos but not org repos
- "Resource not accessible" error

**Solutions:**

1. **Authorize token for organization:**
   - github.com/settings/tokens
   - Click "Configure SSO" next to token
   - Authorize for your organization

2. **Check organization settings:**
   - Organization may restrict third-party access
   - Admin may need to approve OAuth apps

3. **Use fine-grained token:**
   - Select organization as resource owner
   - Admin approval may be required

### API Not Enabled

**Symptoms:**
- Google API returns "API not enabled"
- 403 error mentioning API enablement

**Solutions:**

1. **Enable API in Google Cloud Console:**
   - Go to console.cloud.google.com
   - Navigate to APIs & Services > Library
   - Search for and enable required API

2. **Wait a few minutes:**
   - API enablement can take 1-5 minutes

---

## Timeout Problems

### Slow Operations

**Symptoms:**
- Operations take very long
- Eventually timeout
- Works for small requests, fails for large

**Causes:**
- Large file operations
- Network latency
- Server overload

**Solutions:**

1. **Break up large operations:**
   - Instead of fetching entire repo, fetch specific files
   - Paginate large result sets

2. **Check network latency:**
   ```bash
   ping api.github.com
   traceroute api.github.com    # Mac/Linux
   tracert api.github.com       # Windows
   ```

3. **Try different network:**
   - Switch from WiFi to ethernet
   - Try mobile hotspot
   - Disable VPN

### DNS Resolution Timeout

**Symptoms:**
- "getaddrinfo ENOTFOUND"
- DNS lookup failures

**Solutions:**

1. **Test DNS resolution:**
   ```bash
   nslookup api.github.com
   ```

2. **Try different DNS servers:**
   - Google: 8.8.8.8, 8.8.4.4
   - Cloudflare: 1.1.1.1, 1.0.0.1

3. **Flush DNS cache:**
   ```bash
   # Windows
   ipconfig /flushdns

   # Mac
   sudo dscacheutil -flushcache

   # Linux
   sudo systemd-resolve --flush-caches
   ```

---

## Log File Locations

### Windows

```
Claude Code logs:
%USERPROFILE%\.claude\logs\

MCP server logs:
%USERPROFILE%\.claude\mcp-logs\

Node.js/npm logs:
%USERPROFILE%\AppData\Roaming\npm-cache\_logs\
```

### macOS

```
Claude Code logs:
~/.claude/logs/

MCP server logs:
~/.claude/mcp-logs/

Node.js/npm logs:
~/.npm/_logs/
```

### Linux

```
Claude Code logs:
~/.claude/logs/

MCP server logs:
~/.claude/mcp-logs/

Node.js/npm logs:
~/.npm/_logs/
```

### Reading Logs

```bash
# View most recent log
cat ~/.claude/logs/$(ls -t ~/.claude/logs/ | head -1)

# Search for errors
grep -i error ~/.claude/logs/*.log

# Watch logs in real-time
tail -f ~/.claude/logs/latest.log
```

---

## Diagnostic Flowchart

```
                    +------------------+
                    | MCP Not Working? |
                    +--------+---------+
                             |
                             v
                +------------+-------------+
                | Can you ping the         |
                | service API?             |
                | (ping api.github.com)    |
                +------------+-------------+
                             |
              +--------------+--------------+
              |                             |
              v                             v
+-------------+-------------+    +----------+----------+
|        NO                 |    |        YES          |
| Network/DNS issue         |    |                     |
| - Check internet          |    v                     |
| - Check firewall          | +-----------+-----------+
| - Try different DNS       | | Is the error          |
+---------------------------+ | authentication        |
                              | related? (401/403)    |
                              +-----------+-----------+
                                          |
                       +------------------+------------------+
                       |                                     |
                       v                                     v
          +------------+------------+           +------------+------------+
          |          YES            |           |          NO             |
          | Authentication issue    |           |                         |
          | - Verify API key        |           v                         |
          | - Check expiration      |  +--------+---------+               |
          | - Regenerate token      |  | Is it a timeout  |               |
          +-------------------------+  | or connection    |               |
                                       | error?           |               |
                                       +--------+---------+               |
                                                |                         |
                                 +--------------+--------------+          |
                                 |                             |          |
                                 v                             v          |
                    +------------+------------+   +------------+----------+
                    |          YES            |   |          NO           |
                    | Timeout/Connection      |   |                       |
                    | - Check network speed   |   v                       |
                    | - Disable VPN           |  +-----------+-----------+
                    | - Break up large ops    |  | Is it a "not found"  |
                    +-------------------------+  | error? (404)         |
                                                 +-----------+-----------+
                                                             |
                                          +------------------+------------------+
                                          |                                     |
                                          v                                     v
                             +------------+------------+           +------------+------------+
                             |          YES            |           |          NO             |
                             | Resource not found      |           | Other error             |
                             | - Check spelling        |           | - Check logs            |
                             | - Verify exists         |           | - Search error message  |
                             | - Check private access  |           | - Ask for help          |
                             +-------------------------+           +-------------------------+

```

---

## Service-Specific Issues

### Zapier MCP

**Common Issues:**

1. **"Action not configured":**
   - Go to zapier.com/mcp
   - Add the specific action you need
   - Reconnect the service if necessary

2. **"Zapier connection lost":**
   - Re-authenticate at zapier.com/mcp
   - Generate new API key
   - Update your MCP config

3. **Action fails silently:**
   - Check Zapier task history
   - Verify connected app permissions
   - Test action manually in Zapier

### GitHub MCP

**Common Issues:**

1. **"Bad credentials":**
   - Token expired or revoked
   - Wrong token format (classic vs fine-grained)
   - Copy/paste error

2. **Can't access organization repos:**
   - Configure SSO for token
   - Check org third-party access policy
   - Use fine-grained token with org access

3. **Push rejected:**
   - Branch protection rules
   - Required reviews
   - Insufficient permissions

### Google Services (via Zapier)

**Common Issues:**

1. **"Insufficient permission":**
   - Reconnect Google account in Zapier
   - Approve additional scopes
   - Check Google account security settings

2. **"Quota exceeded":**
   - Wait for quota reset
   - Request quota increase in Cloud Console
   - Reduce request frequency

3. **Calendar events not appearing:**
   - Check calendar ID is correct
   - Verify timezone settings
   - Ensure event falls within search range

---

## Getting Help

### Self-Help Resources

1. **Documentation:**
   - MCP Protocol: modelcontextprotocol.io
   - Claude Code: docs.anthropic.com
   - Zapier MCP: zapier.com/mcp

2. **Community:**
   - Anthropic Discord
   - GitHub Discussions
   - Stack Overflow (tag: mcp-protocol)

### Information to Include When Asking for Help

When seeking help, include:

1. **Error message** (exact text)
2. **What you were trying to do**
3. **Steps to reproduce**
4. **Your configuration** (remove sensitive data)
5. **Operating system and version**
6. **Node.js version** (`node --version`)
7. **Relevant log output**

### Example Help Request

```
Issue: GitHub MCP returns 401 error

Error message: "Bad credentials"

Steps to reproduce:
1. Configure GitHub MCP with PAT
2. Try to list repositories
3. Get 401 error

Configuration (sanitized):
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "[REDACTED]"
      }
    }
  }
}

Environment:
- Windows 11
- Node.js v20.10.0
- Claude Code v1.x.x

What I've tried:
- Verified token is not expired
- Regenerated token with repo scope
- Checked no whitespace in token
```

---

## Quick Reference Card

| Error | Likely Cause | Quick Fix |
|-------|--------------|-----------|
| ECONNREFUSED | Server not running | Restart Claude Code |
| 401 Unauthorized | Bad API key | Regenerate token |
| 403 Forbidden | Missing permissions | Add required scopes |
| 404 Not Found | Resource doesn't exist | Check spelling/access |
| 429 Rate Limited | Too many requests | Wait 1 hour |
| ETIMEDOUT | Network/server slow | Check connection |
| Invalid JSON | Config syntax error | Validate JSON |
| spawn ENOENT | Node.js not found | Install/reinstall Node |

---

*Last updated: Module 3 - MCP Server Deep Dive*
