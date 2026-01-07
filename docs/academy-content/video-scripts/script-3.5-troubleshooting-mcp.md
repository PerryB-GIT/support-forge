# Script 3.5: Troubleshooting MCP Connections

**Module:** 3 - MCP Server Deep Dive (UNLOCK Phase)
**Duration:** 10 minutes
**Lesson:** 3.5 - Troubleshooting MCP Connections

---

## INTRO (1 min)

[SCREEN: Lesson title "Troubleshooting MCP Connections" with wrench icon]

MCP is powerful, but sometimes things break. [PAUSE] Connections fail, tools don't show up, actions timeout.

Don't worry - it happens to everyone. [PAUSE] In this lesson, I'll show you how to diagnose and fix the most common MCP issues.

[SCREEN: "Common Issues" list preview]

By the end, you'll know exactly where to look when something goes wrong.

---

## ISSUE 1: MCP SERVER NOT CONNECTING (3 min)

[SCREEN: Error message "Failed to connect to MCP server"]

The most common issue: Claude Code starts but your MCP server doesn't connect. [PAUSE]

### Check Your Config File

[SCREEN: File path and config file location]

First, verify your config file exists and is valid JSON. [PAUSE]

On Windows, check:
```
%APPDATA%\Claude\claude_desktop_config.json
```

On Mac:
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

[SCREEN: Example of invalid JSON with arrow pointing to error]

Common JSON mistakes:

- Missing comma between entries [PAUSE]
- Trailing comma after last entry [PAUSE]
- Missing quotes around strings [PAUSE]
- Wrong bracket type - curly braces vs square brackets [PAUSE]

Use a JSON validator if you're unsure. [PAUSE] Search "JSON validator" online, paste your config, and it'll show any syntax errors.

### Verify the URL

[SCREEN: Config file with URL highlighted]

For Zapier MCP, make sure your URL is correct. [PAUSE] It should be the full URL from your Zapier MCP settings.

Double-check you copied the entire thing. [PAUSE] These URLs are long and it's easy to miss the end.

### Restart Properly

[SCREEN: Terminal showing exit and restart sequence]

Did you actually restart Claude Code? [PAUSE] Config changes only take effect on startup.

Exit completely - use /exit or close the terminal. [PAUSE] Then start fresh.

---

## ISSUE 2: TOOLS NOT SHOWING UP (2 min)

[SCREEN: Claude saying "I don't have access to those tools"]

You've connected the MCP server, but Claude says it doesn't have certain tools. [PAUSE]

### Check Zapier Actions

[SCREEN: Zapier MCP interface showing actions list]

The most likely cause: you haven't added that action in Zapier. [PAUSE]

Go to your Zapier MCP settings and review your actions list. [PAUSE] If you want Claude to send emails but you haven't added the Gmail Send Email action, it won't work.

Add the missing action, and it's instantly available. [PAUSE] No Claude Code restart needed for Zapier changes.

### Account Connection Issues

[SCREEN: Zapier showing disconnected account warning]

Sometimes an account connection expires. [PAUSE] Zapier shows a warning icon next to disconnected accounts.

Click into the action and reconnect. [PAUSE] Re-authorize through OAuth, and you're back in business.

---

## ISSUE 3: ACTIONS FAILING OR TIMING OUT (2 min)

[SCREEN: Error message "Tool execution failed" or timeout]

The MCP connects, the tool exists, but when Claude tries to use it... error. [PAUSE]

### Check Permissions

[SCREEN: Google permissions screen]

For Google services, make sure you granted the right permissions. [PAUSE] If Claude can't read your calendar, maybe you didn't authorize calendar access during OAuth.

Fix: go to Zapier, disconnect and reconnect the account, and make sure you check all the permission boxes.

### Service-Side Issues

[SCREEN: Service status page example]

Sometimes it's not you - it's them. [PAUSE] Google has outages. GitHub has outages. Zapier has outages.

If things were working and suddenly stopped, check status pages:
- status.google.com
- githubstatus.com
- status.zapier.com

[SCREEN: Status page showing incident]

If there's an incident, just wait it out.

### Rate Limits

[SCREEN: "Rate limit exceeded" error]

If you're making lots of requests quickly, you might hit rate limits. [PAUSE] This is especially common with Gmail.

Solution: slow down. [PAUSE] Space out your requests, or wait a few minutes before trying again.

---

## ISSUE 4: AUTHENTICATION ERRORS (1 min)

[SCREEN: "Authentication failed" or "Invalid token" error]

Auth errors usually mean your connection expired or was revoked. [PAUSE]

### Zapier MCP URL Changed

[SCREEN: Zapier settings showing MCP URL]

If you regenerated your Zapier MCP URL, your old one won't work. [PAUSE] Update your config file with the new URL.

### OAuth Token Expired

Google and GitHub tokens can expire. [PAUSE] Go to Zapier, find the affected action, and reconnect the account.

---

## DEBUGGING TECHNIQUES (1 min)

[SCREEN: "Debugging Tips" header]

When you're stuck, here's your debugging checklist:

[SCREEN: Checklist items appearing]

1. **Ask Claude what tools it has.** [PAUSE] Type "What MCP tools do you have access to?" This confirms what's actually connected.

2. **Try a simple action first.** [PAUSE] Don't test with complex queries. Try "Find events on my calendar for today" - something basic.

3. **Check Zapier's task history.** [PAUSE] Zapier logs every action. You can see what was called, what parameters were sent, and what errors occurred.

4. **Look at Claude Code's startup output.** [PAUSE] When Claude Code starts, it shows MCP connection status. Errors appear there.

5. **Test outside Claude.** [PAUSE] If Google Calendar isn't working, can you access it normally? Isolate whether it's an MCP issue or a service issue.

---

## GETTING HELP (30 sec)

[SCREEN: Help resources]

If you're still stuck after all this:

[SCREEN: Resource links]

- **Anthropic's Discord** - Active community, people share MCP issues and solutions
- **Zapier Support** - For Zapier-specific MCP issues
- **GitHub Issues** - For Claude Code bugs, check the official repo

[SCREEN: Module 3 completion graphic]

That wraps up Module 3. [PAUSE] You've learned what MCP is, installed Zapier MCP, connected Google services and GitHub, and now you know how to fix things when they break.

[SCREEN: "Next: Module 4 - Skills & Plugins" with arrow]

In Module 4, we're moving to Skills and Plugins - ways to extend Claude's capabilities even further. [PAUSE] See you there.

---

**END OF SCRIPT 3.5**
