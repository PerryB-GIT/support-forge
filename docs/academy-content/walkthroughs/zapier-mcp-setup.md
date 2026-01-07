# Zapier MCP Setup Guide

> **Support Forge AI Launchpad Academy**
> Complete guide to setting up Zapier's Model Context Protocol integration with Claude

---

## Overview

Zapier MCP (Model Context Protocol) allows Claude to interact directly with 7,000+ apps through natural language. Instead of building custom integrations, you get instant access to Google Workspace, GitHub, Canva, LinkedIn, and dozens more services.

**What you'll achieve:**
- Connect Claude to your favorite apps
- Execute actions through natural conversation
- Build automated workflows without code

---

## Prerequisites

Before starting, ensure you have:

- [ ] **Zapier Account** - Free tier works, but paid unlocks more actions
- [ ] **Claude Desktop App** or **Claude Code CLI** installed
- [ ] **Admin access** to apps you want to connect (Google, GitHub, etc.)
- [ ] **Basic familiarity** with JSON configuration files

---

## Step 1: Create Your Zapier MCP Connection

### 1.1 Access Zapier MCP

1. Log into your Zapier account at [zapier.com](https://zapier.com)
2. Navigate to **MCP** in the left sidebar (or visit `zapier.com/mcp`)
3. Click **"Create MCP Server"**

### 1.2 Generate Your MCP URL

Zapier will provide you with a unique MCP endpoint URL:

```
https://actions.zapier.com/mcp/YOUR_UNIQUE_ID/sse
```

**Important:** Keep this URL private. Anyone with access can execute actions on your connected accounts.

---

## Step 2: Configure Claude Desktop

### 2.1 Locate Your Config File

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Linux:**
```
~/.config/Claude/claude_desktop_config.json
```

### 2.2 Add Zapier MCP Configuration

Edit your config file to include the Zapier MCP server:

```json
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": [
        "-y",
        "@anthropic-ai/mcp-remote",
        "https://actions.zapier.com/mcp/YOUR_UNIQUE_ID/sse"
      ]
    }
  }
}
```

### 2.3 Alternative: Direct SSE Configuration

If you prefer direct SSE without npx:

```json
{
  "mcpServers": {
    "zapier": {
      "transport": {
        "type": "sse",
        "url": "https://actions.zapier.com/mcp/YOUR_UNIQUE_ID/sse"
      }
    }
  }
}
```

---

## Step 3: Configure Claude Code CLI

### 3.1 Locate Claude Code Settings

**Windows:**
```
%APPDATA%\claude-code\settings.json
```

**macOS/Linux:**
```
~/.config/claude-code/settings.json
```

### 3.2 Add MCP Server Configuration

```json
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": [
        "-y",
        "@anthropic-ai/mcp-remote",
        "https://actions.zapier.com/mcp/YOUR_UNIQUE_ID/sse"
      ],
      "env": {}
    }
  }
}
```

---

## Step 4: Connect Your Apps in Zapier

### 4.1 Add Tools to Your MCP Server

1. In Zapier MCP dashboard, click **"Add Tools"**
2. Search for the app you want (e.g., "Google Sheets")
3. Select specific actions you want Claude to access

### 4.2 Authenticate Each App

For each tool, you'll need to:

1. Click **"Connect Account"**
2. Follow the OAuth flow for that service
3. Grant necessary permissions
4. Test the connection

### 4.3 Recommended Initial Setup

Start with these essential tools:

| App | Recommended Actions |
|-----|---------------------|
| Google Sheets | Create Row, Lookup Row, Update Row |
| Google Calendar | Find Events, Create Event |
| Google Drive | Find File, Upload File |
| Gmail | Find Email, Send Email, Create Draft |
| GitHub | Find Issue, Create Issue, Create PR |

---

## Step 5: Verify Your Setup

### 5.1 Restart Claude

After saving your config, completely restart Claude Desktop or Claude Code.

### 5.2 Test Tool Availability

Ask Claude to list available tools:

```
What Zapier MCP tools do you have access to?
```

### 5.3 Run a Simple Test

Try a basic action:

```
Find the most recent email in my Gmail inbox
```

If successful, you'll see Claude execute the `mcp__zapier__gmail_find_email` tool.

---

## Configuration Examples

### Minimal Configuration

```json
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-remote", "https://actions.zapier.com/mcp/abc123/sse"]
    }
  }
}
```

### Full Configuration with Multiple MCP Servers

```json
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": [
        "-y",
        "@anthropic-ai/mcp-remote",
        "https://actions.zapier.com/mcp/YOUR_ZAPIER_ID/sse"
      ],
      "env": {}
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxxxxxxxxxx"
      }
    }
  }
}
```

---

## Common Errors and Fixes

### Error: "MCP server not found"

**Cause:** Config file syntax error or wrong path

**Fix:**
1. Validate JSON syntax at [jsonlint.com](https://jsonlint.com)
2. Ensure no trailing commas
3. Check file is in correct location

```json
// WRONG - trailing comma
{
  "mcpServers": {
    "zapier": { ... },  // <- Remove this comma if last item
  }
}

// CORRECT
{
  "mcpServers": {
    "zapier": { ... }
  }
}
```

### Error: "Connection refused" or "SSE timeout"

**Cause:** Network issue or invalid MCP URL

**Fix:**
1. Verify your MCP URL is correct in Zapier dashboard
2. Check if you're behind a corporate firewall
3. Try regenerating the MCP URL in Zapier

### Error: "Tool not found: mcp__zapier__..."

**Cause:** Tool not added to your Zapier MCP server

**Fix:**
1. Go to Zapier MCP dashboard
2. Click "Add Tools"
3. Add the specific action you need
4. Restart Claude

### Error: "Authentication failed"

**Cause:** OAuth token expired or revoked

**Fix:**
1. In Zapier, go to "Connections"
2. Find the affected app
3. Click "Reconnect"
4. Re-authenticate

### Error: "npx not found"

**Cause:** Node.js not installed or not in PATH

**Fix:**
1. Install Node.js from [nodejs.org](https://nodejs.org)
2. Restart your terminal/computer
3. Verify with `node --version` and `npx --version`

---

## Pro Tips

### 1. Organize Your Tools

Don't add every possible tool. Start with 5-10 essential actions and add more as needed. Too many tools can slow down Claude's response time.

### 2. Use Descriptive Instructions

When calling tools, provide clear instructions:

```
// Good
"Find all events on my Google Calendar for January 15, 2026 between 9am and 5pm"

// Less effective
"Check my calendar"
```

### 3. Test in Zapier First

Before using a tool through Claude, test it in Zapier's interface to understand the required parameters and expected output.

### 4. Monitor Usage

Zapier has task limits on free/lower tiers. Monitor your usage in the Zapier dashboard to avoid hitting limits.

### 5. Secure Your MCP URL

- Never commit your MCP URL to version control
- Use environment variables when possible:

```json
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-remote", "${ZAPIER_MCP_URL}"]
    }
  }
}
```

### 6. Create Focused MCP Servers

Consider creating multiple Zapier MCP servers for different purposes:
- One for work (Google Workspace, Slack)
- One for development (GitHub, Jira)
- One for marketing (LinkedIn, Google Ads)

---

## Next Steps

Now that Zapier MCP is configured, explore our integration-specific guides:

- [Google Workspace MCP Guide](./google-workspace-mcp.md)
- [GitHub MCP Guide](./github-mcp.md)
- [Design Tools MCP Guide](./design-tools-mcp.md)
- [Marketing MCP Guide](./marketing-mcp.md)
- [AI Studio MCP Guide](./ai-studio-mcp.md)
- [Code Execution MCP Guide](./code-execution-mcp.md)

---

## Quick Reference

| Action | Command |
|--------|---------|
| Add tools | Zapier Dashboard > MCP > Add Tools |
| Get MCP URL | Zapier Dashboard > MCP > Copy URL |
| Config location (Windows) | `%APPDATA%\Claude\claude_desktop_config.json` |
| Config location (macOS) | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Test connection | Ask Claude "What Zapier tools are available?" |

---

*Support Forge AI Launchpad Academy - Building the Future of AI Integration*
