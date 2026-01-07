# Script 3.2: Installing Your First MCP Server

**Module:** 3 - MCP Server Deep Dive (UNLOCK Phase)
**Duration:** 20 minutes
**Lesson:** 3.2 - Installing Your First MCP Server

---

## INTRO (1 min)

[SCREEN: Lesson title "Installing Your First MCP Server" with Zapier logo]

Alright, time to get our hands dirty. [PAUSE] In this lesson, we're installing your first MCP server - the Zapier MCP.

Why Zapier? [PAUSE] Because it gives you access to a ton of services through a single connection. Google Sheets, Calendar, Drive, Gmail, GitHub, Canva, Google Ads, LinkedIn, Figma - all through one MCP server.

[SCREEN: Grid of service logos that Zapier MCP supports]

By the end of this lesson, you'll have Zapier MCP running and Claude will be able to interact with all these services.

Let's do it.

---

## WHAT YOU'LL NEED (2 min)

[SCREEN: Checklist appearing item by item]

Before we start, let's make sure you've got everything ready.

First, you need Claude Code installed and working. [PAUSE] If you're watching this in order, you did that in Module 1. If not, go back and complete that first.

Second, you'll need a Zapier account. [PAUSE] The free tier works fine for getting started. Head to zapier.com and sign up if you haven't already.

Third - and this is important - you'll need to enable Zapier's MCP integration. [PAUSE] This is done through Zapier's interface, and I'll walk you through it step by step.

[SCREEN: Browser showing zapier.com homepage]

One thing to know: Zapier MCP requires you to authorize specific "actions" for each service. [PAUSE] So we're not just connecting "Google" - we're connecting specific capabilities like "find calendar events" or "create spreadsheet row."

This is actually a nice security feature. [PAUSE] You have granular control over exactly what Claude can do.

---

## SETTING UP ZAPIER MCP (6 min)

[SCREEN: Browser navigating to Zapier MCP setup]

Okay, let's set this up. Open your browser and go to zapier.com. [PAUSE] Log into your account.

Now, Zapier has a dedicated MCP feature. [PAUSE] Navigate to your account settings - click your profile icon in the top right, then look for "MCP" or "AI Actions" in the menu.

[SCREEN: Zapier interface showing MCP/AI Actions section]

When you first open this, you'll see an option to enable MCP access. [PAUSE] Click that, and Zapier will generate your MCP server URL and authentication token.

[SCREEN: Zapier showing generated MCP credentials with parts redacted]

You'll see two things here:

First is your MCP server URL. [PAUSE] This is the endpoint Claude Code will connect to. It looks something like: mcp.zapier.com/api/mcp/your-unique-id.

Second is your authentication. [PAUSE] Zapier handles this through the URL itself - there's a unique identifier that authenticates your requests.

Copy that URL. [PAUSE] You're gonna need it for the config file.

[SCREEN: Highlighting the "Add Actions" button]

Before we leave Zapier, we need to add some actions. [PAUSE] Click "Add Actions" or "Edit Actions."

This is where you tell Zapier what Claude's allowed to do. [PAUSE] Start by adding a few basic ones:

[SCREEN: Adding actions one by one]

Search for "Google Sheets" and add "Lookup Spreadsheet Row" [PAUSE]
Search for "Google Calendar" and add "Find Events" [PAUSE]
Search for "Google Drive" and add "Find a File" [PAUSE]

Each time you add an action, Zapier will ask you to connect the relevant account. [PAUSE] Click through the OAuth flow for Google - you've probably done this before with other apps.

[SCREEN: Google OAuth consent screen]

Once you've added a few actions and connected your accounts, you're ready to configure Claude Code.

---

## THE CLAUDE CODE CONFIG FILE (5 min)

[SCREEN: VS Code or text editor opening config file location]

Now we need to tell Claude Code about this MCP server. [PAUSE] This happens in a configuration file.

On Windows, open File Explorer and navigate to:

[SCREEN: File path displayed prominently]

```
%APPDATA%\Claude\
```

Type that right into the address bar. [PAUSE] You should see a Claude folder. If there's no claude_desktop_config.json file, we'll create one.

[SCREEN: Creating/opening the config file]

Open or create claude_desktop_config.json. [PAUSE] Here's the structure you need:

[SCREEN: JSON configuration appearing with syntax highlighting]

```json
{
  "mcpServers": {
    "zapier": {
      "url": "YOUR_ZAPIER_MCP_URL_HERE"
    }
  }
}
```

Replace YOUR_ZAPIER_MCP_URL_HERE with the URL you copied from Zapier. [PAUSE] Make sure you keep the quotes around it.

[SCREEN: Completed config file with redacted URL]

Let me break down what's happening here.

The mcpServers object contains all your MCP connections. [PAUSE] Each key - like "zapier" - is a name you choose. It's just a label.

Inside each server config, the url field tells Claude Code where to find that MCP server. [PAUSE] For Zapier's hosted MCP, that's all you need.

Some MCP servers need more config - like a command to run locally, or environment variables. [PAUSE] We'll see that with other servers later. But Zapier keeps it simple.

Save the file. [PAUSE]

---

## RESTARTING CLAUDE CODE (2 min)

[SCREEN: Terminal showing Claude Code]

Important step: Claude Code needs to restart to pick up the new configuration. [PAUSE]

If you've got Claude Code running in a terminal, exit it by typing /exit or just close the terminal window.

[SCREEN: Closing and reopening terminal]

Now open a fresh terminal and start Claude Code again with the `claude` command.

[SCREEN: Claude Code starting up, watching for MCP connection messages]

Watch the startup output. [PAUSE] You should see a message indicating that MCP servers are being connected. Something like "Connected to MCP server: zapier."

If you see errors instead, don't worry - we've got a whole troubleshooting lesson coming up. [PAUSE] For now, let's assume it connected.

---

## TESTING THE CONNECTION (3 min)

[SCREEN: Claude Code terminal ready for input]

Moment of truth. [PAUSE] Let's test that Zapier MCP is actually working.

Type this:

[SCREEN: User typing the test prompt]

```
What MCP tools do you have access to from Zapier?
```

[SCREEN: Claude responding with a list of available tools]

Claude should respond with a list of the actions you added in Zapier. [PAUSE] You'll see things like google_sheets_lookup_spreadsheet_row, google_calendar_find_events, and whatever else you configured.

If you see this list, congratulations - you've successfully connected your first MCP server. [PAUSE]

Let's try an actual query. [PAUSE] Type:

[SCREEN: User typing a real test]

```
What events do I have on my calendar tomorrow?
```

[SCREEN: Claude calling the MCP tool and returning calendar data]

Watch what happens. [PAUSE] Claude recognizes this needs calendar access, calls the google_calendar_find_events tool through Zapier, gets your actual calendar data, and presents it to you.

[PAUSE]

That's it. [PAUSE] Claude is now connected to your Google Calendar. Not a demo. Not a simulation. Your real calendar.

---

## ADDING MORE ACTIONS (1 min)

[SCREEN: Back to Zapier interface showing "Add Actions"]

Quick note before we wrap up. [PAUSE] You can always go back to Zapier and add more actions.

Want Claude to send emails? Add Gmail actions. [PAUSE]
Want to create GitHub issues? Add GitHub actions. [PAUSE]
Want to post to LinkedIn? Add LinkedIn actions. [PAUSE]

Every action you add in Zapier becomes a new tool Claude can use. [PAUSE] You don't need to change your Claude Code config - just add actions in Zapier and they're automatically available.

[SCREEN: "Next: Connecting Google Services" with arrow]

In the next lesson, we'll go deeper on Google services. [PAUSE] We'll connect Calendar, Drive, and Gmail, and you'll see how powerful this integration really is.

See you there.

---

**END OF SCRIPT 3.2**
