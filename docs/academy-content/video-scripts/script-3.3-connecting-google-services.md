# Script 3.3: Connecting Google Services

**Module:** 3 - MCP Server Deep Dive (UNLOCK Phase)
**Duration:** 20 minutes
**Lesson:** 3.3 - Connecting Google Services via Zapier MCP

---

## INTRO (1 min)

[SCREEN: Lesson title with Google Workspace icons - Calendar, Drive, Gmail]

Google services are probably central to how you work. [PAUSE] Calendar for scheduling, Drive for files, Gmail for communication.

In this lesson, we're connecting all three through Zapier MCP. [PAUSE] By the end, Claude will be able to check your schedule, find your documents, and help manage your email.

[SCREEN: Diagram showing Claude connected to Google services through Zapier]

Let's set each one up.

---

## GOOGLE CALENDAR SETUP (6 min)

[SCREEN: Google Calendar logo prominently displayed]

We'll start with Calendar since it's the most immediately useful. [PAUSE] Nothing beats asking Claude "what's on my schedule today" and getting a real answer.

### Adding Calendar Actions

[SCREEN: Zapier interface, navigating to add actions]

Head to your Zapier MCP settings. [PAUSE] Click "Add Actions" and search for Google Calendar.

You'll see a bunch of options. [PAUSE] Let me tell you which ones are most useful:

[SCREEN: List of Calendar actions with checkmarks on recommended ones]

**Find Events** - This is essential. [PAUSE] It lets Claude search your calendar by date, keywords, or attendees. Add this one first.

**Create Detailed Event** - Lets Claude add events to your calendar. [PAUSE] Great for when you're in flow and say "schedule a meeting with John next Tuesday at 2pm."

**Quick Add Event** - A simpler version. [PAUSE] You give Claude natural language like "Lunch with Sarah Friday noon" and it figures out the details.

**Update Event** - Modify existing events. [PAUSE] "Move my 3pm to 4pm."

**Delete Event** - Remove events. [PAUSE] Use with caution, obviously.

Add at least Find Events and Create Detailed Event to start.

[SCREEN: OAuth flow for Google Calendar]

When you add your first Calendar action, Zapier prompts you to connect your Google account. [PAUSE] Click through the OAuth flow, grant calendar permissions, and you're set.

### Testing Calendar

[SCREEN: Claude Code terminal]

Back in Claude Code, let's test it. [PAUSE] Type:

```
What meetings do I have this week?
```

[SCREEN: Claude calling google_calendar_find_events and returning results]

Claude calls the find_events tool, gets your calendar data, and presents it clearly. [PAUSE] You'll see event names, times, and any attendees.

Now try creating an event:

```
Add a reminder to my calendar for tomorrow at 9am called "Review project proposal"
```

[SCREEN: Claude calling create_detailed_event]

Claude creates the event and confirms it. [PAUSE] Check your actual Google Calendar - it's really there.

[PAUSE]

That's Google Calendar connected. [PAUSE] You can now manage your schedule entirely through conversation.

---

## GOOGLE DRIVE SETUP (6 min)

[SCREEN: Google Drive logo]

Next up, Google Drive. [PAUSE] This one's incredibly useful for finding documents you can never remember the name of.

### Adding Drive Actions

[SCREEN: Zapier interface, adding Drive actions]

Back in Zapier, add these Google Drive actions:

[SCREEN: List of Drive actions]

**Find a File** - Search for files by name. [PAUSE] "Where's that Q4 budget spreadsheet?"

**Find a Folder** - Search for folders. [PAUSE] Useful for organizing and navigating.

**Get File Permissions** - See who has access to a file. [PAUSE] Good for security checks.

**Create Folder** - Make new folders. [PAUSE] "Create a folder called 'Client Projects 2024'."

**Upload File** - Move files into Drive. [PAUSE] Claude can take a local file and put it in Drive.

**Copy File** - Duplicate files. [PAUSE] Great for templates.

**Move File** - Reorganize your Drive. [PAUSE] "Move the proposal to the Sales folder."

Connect your Google account when prompted. [PAUSE] Same OAuth flow as before.

### Testing Drive

[SCREEN: Claude Code terminal]

Let's try some searches:

```
Find any files in my Google Drive related to "invoice"
```

[SCREEN: Claude calling google_drive_find_a_file and returning results]

Claude searches your Drive and returns matching files with their names and links. [PAUSE] You can click the links to open them directly.

Try something more specific:

```
Do I have a folder called "Projects" in my Drive?
```

[SCREEN: Claude searching for folders]

Claude finds it and can tell you what's inside, who has access, when it was modified.

[PAUSE]

Here's a powerful workflow. [PAUSE] Say:

```
Find my most recent presentation file and tell me who it's shared with
```

[SCREEN: Claude chaining Find File with Get Permissions]

Claude chains two actions together - finds the file, then checks its permissions. [PAUSE] This is where MCP gets powerful. Claude can combine multiple tools to answer complex questions.

---

## GMAIL SETUP (5 min)

[SCREEN: Gmail logo]

Gmail integration is powerful but deserves extra caution. [PAUSE] We're talking about reading and potentially sending emails.

### Adding Gmail Actions

[SCREEN: Zapier interface, adding Gmail actions]

Here's what I recommend starting with:

[SCREEN: List of Gmail actions with security notes]

**Find Email** - Search your inbox. [PAUSE] "Find emails from John about the project." Essential and low-risk.

**Create Draft** - Write draft emails. [PAUSE] Claude composes the email, but you review and send. Safer than direct sending.

**Add Label to Email** - Organize emails. [PAUSE] Great for inbox management workflows.

**Archive Email** - Clean up your inbox. [PAUSE]

**Send Email** - Actually send messages. [PAUSE] Only add this if you trust Claude with send access. I'd recommend starting with Create Draft instead.

Connect your Google account. [PAUSE] Gmail permissions are a bit more sensitive, so Google might show extra warnings. That's normal.

### Testing Gmail

[SCREEN: Claude Code terminal]

Start with a safe search:

```
Find my most recent unread emails
```

[SCREEN: Claude calling gmail_find_email with query parameters]

Claude searches using Gmail's query syntax and returns your unread messages. [PAUSE] You'll see sender, subject, and a snippet of the content.

Now try drafting:

```
Draft a reply to that last email thanking them and saying I'll review it by Friday
```

[SCREEN: Claude calling gmail_create_draft]

Claude creates a draft in your Gmail. [PAUSE] It's sitting there waiting for you to review. Open Gmail, check the Drafts folder, and you'll see it.

[PAUSE]

This workflow is perfect. [PAUSE] Claude helps you write emails quickly, but you maintain control over what actually gets sent.

---

## PRACTICAL WORKFLOWS (2 min)

[SCREEN: "Putting It All Together" header with workflow diagram]

Now you've got Calendar, Drive, and Gmail connected. [PAUSE] Let me show you some workflows that combine them.

### Morning Briefing

[SCREEN: Example prompt and response]

```
Give me a morning briefing: What's on my calendar today, any urgent emails, and find any documents I need for today's meetings
```

Claude checks your calendar, searches for unread important emails, and finds relevant files. [PAUSE] One question, multiple services, complete picture.

### Meeting Prep

```
I have a meeting with Acme Corp tomorrow. Find any recent emails from them and any documents in Drive related to Acme.
```

Claude does the research across services so you're prepared.

### Email to Calendar

```
Check my email for any meeting requests I haven't responded to and add them to my calendar
```

Claude bridges the gap between your inbox and calendar.

[SCREEN: "Next: Connecting GitHub" with arrow]

That's Google services connected. [PAUSE] In the next lesson, we'll add GitHub integration for developers who want Claude working with their code repositories.

---

**END OF SCRIPT 3.3**
