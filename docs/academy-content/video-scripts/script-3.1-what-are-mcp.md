# Script 3.1: What Are MCP Servers?

**Module:** 3 - MCP Server Deep Dive (UNLOCK Phase)
**Duration:** 10 minutes
**Lesson:** 3.1 - What Are MCP Servers?

---

## INTRO (1 min)

[SCREEN: Module 3 title card with "MCP Server Deep Dive" and unlock icon]

Alright, welcome to Module 3. [PAUSE] This is where things get really exciting.

You've got Claude Code installed. You've run some commands. But right now, Claude's kind of... isolated. It can see your files and run terminal commands, but that's about it.

[SCREEN: Simple graphic showing Claude in a "bubble" disconnected from external services]

What if Claude could check your calendar? [PAUSE] Read your emails? [PAUSE] Update a Google Sheet? [PAUSE] Create issues on GitHub?

That's exactly what MCP servers unlock.

---

## WHAT IS MCP? (3 min)

[SCREEN: MCP logo and "Model Context Protocol" text]

MCP stands for Model Context Protocol. [PAUSE] It's an open standard that Anthropic created to let AI assistants connect to external tools and data sources.

Think of it like this. [PAUSE] Your phone can do a lot on its own, right? But apps make it way more powerful. MCP servers are like apps for Claude.

[SCREEN: Diagram showing Claude in center, with arrows pointing to icons for Calendar, Email, GitHub, Sheets, etc.]

Each MCP server gives Claude new capabilities. [PAUSE] A Zapier MCP server lets Claude work with Google services, Canva, LinkedIn, and dozens of other tools. [PAUSE] An n8n (en-eight-en) MCP server lets Claude trigger automation workflows.

The key thing to understand is that MCP servers run locally on your machine. [PAUSE] Claude doesn't connect directly to these services. Instead, it talks to the MCP server running on your computer, and that server handles the actual API calls.

[SCREEN: Flow diagram - Claude → MCP Server (local) → External API]

This architecture matters for a few reasons we'll get into, especially around security.

---

## HOW MCP EXTENDS CLAUDE (3 min)

[SCREEN: Split view - Claude Code terminal on left, MCP tools list on right]

When you connect an MCP server, Claude gains new tools. [PAUSE] Real, callable functions that it can use during a conversation.

Let me show you what I mean. When I have the Zapier MCP connected, Claude can see tools like:

[SCREEN: Scrolling list of actual Zapier MCP tools]

- google_calendar_find_events
- google_sheets_create_spreadsheet_row
- gmail_send_email
- github_create_issue
- canva_create_design

These aren't just suggestions. [PAUSE] These are actual functions Claude can call. When you say "check my calendar for tomorrow," Claude looks at its available tools, sees google_calendar_find_events, and calls it with the right parameters.

[SCREEN: Example showing Claude calling a tool and receiving structured data back]

The response comes back as structured data. Claude reads it, processes it, and gives you a human-readable answer.

This is the magic of MCP. [PAUSE] You're not copy-pasting data between apps anymore. You're not manually checking three different services. Claude handles the coordination.

---

## SECURITY CONSIDERATIONS (2 min)

[SCREEN: Security shield icon with "MCP Security Model" header]

Now let's talk security, because this is important.

When you set up an MCP server, you're giving Claude the ability to take real actions. [PAUSE] Send emails. Modify files. Create calendar events. This is powerful, but it requires trust.

[SCREEN: Bullet points appearing one by one]

Here's how the security model works:

First, MCP servers run locally. [PAUSE] Your credentials stay on your machine. Claude Code talks to the local server, not directly to Google or GitHub.

Second, you control what's connected. [PAUSE] You explicitly add each MCP server to your configuration. Nothing connects automatically.

Third, most actions require confirmation. [PAUSE] When Claude wants to do something significant, it'll ask you first. You'll see exactly what it's about to do before it happens.

[SCREEN: Example of Claude asking for confirmation before sending an email]

Fourth, you can revoke access anytime. [PAUSE] Remove an MCP server from your config, and Claude loses those capabilities instantly.

The general rule is: only connect services you're comfortable Claude having access to. [PAUSE] And always review what Claude's about to do, especially when you're first getting started.

---

## WHAT WE'LL COVER (1 min)

[SCREEN: Module 3 roadmap showing all lessons]

Over the next few lessons, we're gonna get hands-on.

In lesson 3.2, you'll install your first MCP server using Zapier. [PAUSE] We'll walk through the config file and test that it's working.

Lesson 3.3 connects Google services - Calendar, Drive, and Gmail. [PAUSE] You'll see Claude actually read your calendar and interact with your files.

Lesson 3.4 covers GitHub integration. [PAUSE] We'll set up a Personal Access Token and give Claude access to your repos.

And lesson 3.5 is troubleshooting. [PAUSE] Because things don't always work the first time, and knowing how to debug MCP issues will save you hours.

[SCREEN: "Next: Installing Your First MCP Server" with arrow]

Ready to unlock Claude's full potential? [PAUSE] Let's install your first MCP server.

---

**END OF SCRIPT 3.1**
