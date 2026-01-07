# Zapier MCP Server Setup Guide

Connect Claude Code to 6,000+ apps through Zapier's MCP integration.

---

## Overview

The Zapier MCP server allows Claude Code to:
- Trigger Zaps from conversations
- Access Zapier's built-in tools
- Interact with connected apps (Google, Slack, etc.)
- Execute multi-step automations

---

## Prerequisites

- [ ] Zapier account (free tier works)
- [ ] Claude Code installed and working
- [ ] API access enabled on Zapier account

---

## Step 1: Get Your Zapier MCP Credentials

### 1.1 Access Zapier MCP Settings

1. Log into [zapier.com](https://zapier.com)
2. Navigate to **Settings** → **Developer**
3. Click **MCP Servers** or **API Access**
4. Generate a new API key if needed

### 1.2 Note Your Credentials

You'll need:
- **API Key:** `zap_xxxxxxxxxxxx`
- **Account ID:** Found in settings
- **Webhook URLs:** For any custom triggers

---

## Step 2: Configure Claude Code

### 2.1 Locate MCP Config File

```bash
# Default location
~/.claude/claude_mcp_config.json

# Create if it doesn't exist
mkdir -p ~/.claude
touch ~/.claude/claude_mcp_config.json
```

### 2.2 Add Zapier Configuration

Edit `claude_mcp_config.json`:

```json
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": ["-y", "@zapier/mcp-server"],
      "env": {
        "ZAPIER_API_KEY": "zap_your_api_key_here"
      }
    }
  }
}
```

### 2.3 Alternative: Use Environment Variable

```bash
# Add to ~/.bashrc
export ZAPIER_API_KEY="zap_your_api_key_here"
```

Then update config:
```json
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": ["-y", "@zapier/mcp-server"],
      "env": {
        "ZAPIER_API_KEY": "${ZAPIER_API_KEY}"
      }
    }
  }
}
```

---

## Step 3: Verify Connection

### 3.1 Restart Claude Code

```bash
# Close any running instances
pkill -f claude

# Start fresh
claude
```

### 3.2 Check Available Tools

```
/tools
```

You should see Zapier tools listed, such as:
- `zapier_trigger_zap`
- `zapier_list_zaps`
- `zapier_get_app_actions`

### 3.3 Test Connection

```
List my active Zaps
```

If successful, Claude will return your Zap list.

---

## Step 4: Configure Zapier Actions

### 4.1 Create a Test Zap

1. In Zapier, create a new Zap
2. Set trigger: **Webhooks by Zapier** → **Catch Hook**
3. Set action: **Google Sheets** → **Create Spreadsheet Row** (or similar)
4. Note the webhook URL

### 4.2 Enable Claude Trigger

Add to your MCP config:

```json
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": ["-y", "@zapier/mcp-server"],
      "env": {
        "ZAPIER_API_KEY": "${ZAPIER_API_KEY}",
        "ZAPIER_WEBHOOK_URL": "https://hooks.zapier.com/hooks/catch/xxxxx/yyyyy/"
      }
    }
  }
}
```

---

## Common Zapier Actions via Claude

### Trigger a Zap
```
Trigger the "New Lead" Zap with this data:
- name: John Smith
- email: john@example.com
- source: website
```

### List Available Zaps
```
Show me all my active Zaps
```

### Send to Google Sheets
```
Add a row to my "Leads" spreadsheet with:
- Date: today
- Lead Name: Jane Doe
- Status: New
```

### Post to Slack
```
Send a message to the #general channel:
"Weekly report is ready for review"
```

### Create Calendar Event
```
Create a meeting for tomorrow at 2pm:
- Title: Client Call - Acme Corp
- Duration: 30 minutes
- Add to my primary calendar
```

---

## Troubleshooting

### "Zapier tools not showing"

**Check:**
1. Config file syntax is valid JSON
2. API key is correct
3. Claude Code was restarted after config change

```bash
# Validate JSON
python -m json.tool ~/.claude/claude_mcp_config.json
```

### "Authentication failed"

**Solutions:**
1. Verify API key in Zapier dashboard
2. Regenerate API key if expired
3. Check key hasn't been revoked

### "Zap not triggering"

**Check:**
1. Zap is turned ON
2. Webhook URL is correct
3. Zap has been tested in Zapier first

### "Rate limit exceeded"

**Solutions:**
1. Wait a few minutes
2. Upgrade Zapier plan for higher limits
3. Batch operations where possible

---

## Best Practices

### Security
- Never share API keys
- Use environment variables, not hardcoded values
- Rotate keys periodically
- Monitor Zapier task usage

### Performance
- Test Zaps manually first
- Use simple triggers initially
- Add complexity gradually
- Monitor for failures in Zapier dashboard

### Organization
- Name Zaps descriptively
- Use folders to organize Zaps
- Document webhook URLs
- Keep a log of Claude-triggered actions

---

## Example Workflows

### Daily Standup Automation
```
Every morning, run my standup routine:
1. Get yesterday's completed tasks from Asana
2. Check today's calendar events
3. Create standup message in Slack #team channel
```

### Lead Capture
```
When I say "new lead", capture the info and:
1. Add to Google Sheets "Leads" spreadsheet
2. Create follow-up task in Todoist for tomorrow
3. Send notification to Slack #sales channel
```

### Report Distribution
```
After I finish the weekly report:
1. Export as PDF
2. Upload to Google Drive
3. Email to distribution list
4. Post link in Slack #reports
```

---

## Quick Reference

| Action | Command Example |
|--------|-----------------|
| List Zaps | "Show my Zaps" |
| Trigger Zap | "Trigger [Zap name] with [data]" |
| Send email | "Send email via Zapier to [address]" |
| Post to Slack | "Post to Slack #channel: [message]" |
| Add sheet row | "Add to [spreadsheet]: [data]" |
| Create task | "Create task in [app]: [details]" |

---

*AI Launchpad Academy - Support Forge*
