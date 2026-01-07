# Google Workspace MCP Integration Guide

> **Support Forge AI Launchpad Academy**
> Master Google Sheets, Calendar, Drive, and Gmail through Claude

---

## Overview

Google Workspace is the backbone of modern business operations. With Zapier MCP, Claude can directly interact with your Google apps - reading spreadsheets, scheduling meetings, managing files, and handling email.

**What you'll learn:**
- Query and update Google Sheets data
- Create and manage calendar events
- Search and organize Google Drive files
- Send emails and manage your inbox

---

## Prerequisites

- [ ] Zapier MCP configured ([see setup guide](./zapier-mcp-setup.md))
- [ ] Google Workspace or personal Google account
- [ ] Connected Google apps in Zapier

---

## Google Sheets Integration

### Available Tools

| Tool | Description |
|------|-------------|
| `google_sheets_lookup_spreadsheet_row` | Find a row by column value |
| `google_sheets_lookup_spreadsheet_rows_advanced` | Find up to 500 rows |
| `google_sheets_create_spreadsheet_row` | Add a new row |
| `google_sheets_update_spreadsheet_row` | Update existing row |
| `google_sheets_create_spreadsheet` | Create new spreadsheet |
| `google_sheets_get_data_range` | Get data from specific range |
| `google_sheets_format_spreadsheet_row` | Format row styling |

### Example: Find a Customer Record

```
Find the row in my "Customer Database" spreadsheet where the Email column
contains "john@example.com"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_sheets_lookup_spreadsheet_row",
  "parameters": {
    "instructions": "Find the row where Email column equals john@example.com",
    "spreadsheet": "Customer Database",
    "lookup_key": "Email",
    "lookup_value": "john@example.com"
  }
}
```

### Example: Add a New Row

```
Add a new customer to my "Sales Leads" spreadsheet with:
- Name: Sarah Connor
- Email: sarah@skynet.com
- Phone: 555-0199
- Status: New Lead
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_sheets_create_spreadsheet_row",
  "parameters": {
    "instructions": "Create a new row with Name: Sarah Connor, Email: sarah@skynet.com, Phone: 555-0199, Status: New Lead",
    "spreadsheet": "Sales Leads",
    "worksheet": "Sheet1"
  }
}
```

### Example: Update a Record

```
In my "Inventory" spreadsheet, find the product "Widget Pro" and update
the Stock column to 150
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_sheets_update_spreadsheet_row",
  "parameters": {
    "instructions": "Find row where Product Name is 'Widget Pro' and update Stock to 150",
    "spreadsheet": "Inventory",
    "row": "lookup by Product Name = Widget Pro"
  }
}
```

### Example: Create a New Spreadsheet

```
Create a new spreadsheet called "Q1 2026 Budget" with columns:
Category, Budget, Actual, Variance
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_sheets_create_spreadsheet",
  "parameters": {
    "instructions": "Create spreadsheet titled Q1 2026 Budget",
    "title": "Q1 2026 Budget",
    "headers": ["Category", "Budget", "Actual", "Variance"]
  }
}
```

### Example: Get Range Data

```
Get all data from cells A1 to D10 in my "Monthly Report" spreadsheet
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_sheets_get_data_range",
  "parameters": {
    "instructions": "Get data from range A1:D10",
    "spreadsheet": "Monthly Report",
    "worksheet": "Sheet1",
    "a1_range": "A1:D10"
  }
}
```

---

## Google Calendar Integration

### Available Tools

| Tool | Description |
|------|-------------|
| `google_calendar_find_events` | Search for events |
| `google_calendar_create_detailed_event` | Create a new event |
| `google_calendar_quick_add_event` | Quick event from text |
| `google_calendar_update_event` | Modify existing event |
| `google_calendar_delete_event` | Remove an event |
| `google_calendar_find_busy_periods` | Check availability |
| `google_calendar_add_attendee_s_to_event` | Add attendees |

### Example: Find Today's Events

```
What meetings do I have scheduled for today?
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_calendar_find_events",
  "parameters": {
    "instructions": "Find all events scheduled for today, January 4, 2026",
    "end_time": "2026-01-04 00:00:00",
    "start_time": "2026-01-04 23:59:59"
  }
}
```

### Example: Create a Meeting

```
Schedule a meeting called "Project Kickoff" for tomorrow at 2pm for 1 hour
with attendees: alice@company.com and bob@company.com
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_calendar_create_detailed_event",
  "parameters": {
    "instructions": "Create Project Kickoff meeting for January 5, 2026 at 2pm, 1 hour duration",
    "summary": "Project Kickoff",
    "start__dateTime": "2026-01-05T14:00:00",
    "end__dateTime": "2026-01-05T15:00:00",
    "attendees": ["alice@company.com", "bob@company.com"],
    "description": "Initial project kickoff meeting"
  }
}
```

### Example: Quick Add Event

```
Add "Dentist appointment next Tuesday at 10am" to my calendar
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_calendar_quick_add_event",
  "parameters": {
    "instructions": "Quick add dentist appointment",
    "text": "Dentist appointment next Tuesday at 10am"
  }
}
```

### Example: Find Free Time

```
When am I free this Friday afternoon?
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_calendar_find_busy_periods_in_calendar",
  "parameters": {
    "instructions": "Find busy periods on Friday January 10, 2026 from 12pm to 6pm",
    "start_time": "2026-01-10T12:00:00",
    "end_time": "2026-01-10T18:00:00"
  }
}
```

### Example: Update Event

```
Change my "Team Standup" meeting tomorrow to start at 9:30am instead of 9am
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_calendar_update_event",
  "parameters": {
    "instructions": "Update Team Standup on January 5 to start at 9:30am",
    "eventid": "[event_id_from_find]",
    "start__dateTime": "2026-01-05T09:30:00"
  }
}
```

---

## Google Drive Integration

### Available Tools

| Tool | Description |
|------|-------------|
| `google_drive_find_a_file` | Search for files |
| `google_drive_find_a_folder` | Search for folders |
| `google_drive_upload_file` | Upload a file |
| `google_drive_create_folder` | Create new folder |
| `google_drive_copy_file` | Copy a file |
| `google_drive_move_file` | Move file to folder |
| `google_drive_add_file_sharing_preference` | Share a file |
| `google_drive_export_file` | Export to different format |

### Example: Find a File

```
Find the file called "Project Proposal" in my Google Drive
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_drive_find_a_file",
  "parameters": {
    "instructions": "Find file named Project Proposal",
    "title": "Project Proposal"
  }
}
```

### Example: Create a Folder

```
Create a new folder called "2026 Projects" in my Drive
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_drive_create_folder",
  "parameters": {
    "instructions": "Create folder named 2026 Projects",
    "title": "2026 Projects"
  }
}
```

### Example: Share a File

```
Share the "Marketing Plan" document with view access for anyone with the link
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_drive_add_file_sharing_preference",
  "parameters": {
    "instructions": "Share Marketing Plan with anyone who has the link can view",
    "file_id": "[file_id]",
    "permission": "anyone with link can view"
  }
}
```

### Example: Move a File

```
Move the "Final Report.docx" file to the "Archive" folder
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_drive_move_file",
  "parameters": {
    "instructions": "Move Final Report.docx to Archive folder",
    "file": "[file_id]",
    "folder": "[archive_folder_id]"
  }
}
```

### Example: Export Document

```
Export my Google Doc "Meeting Notes" as a PDF
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_drive_export_file",
  "parameters": {
    "instructions": "Export Meeting Notes as PDF",
    "file": "[file_id]",
    "export_format": "pdf"
  }
}
```

---

## Gmail Integration

### Available Tools

| Tool | Description |
|------|-------------|
| `gmail_find_email` | Search for emails |
| `gmail_send_email` | Send new email |
| `gmail_create_draft` | Create email draft |
| `gmail_reply_to_email` | Reply to email |
| `gmail_add_label_to_email` | Add label |
| `gmail_archive_email` | Archive email |
| `gmail_create_draft_reply` | Draft a reply |

### Example: Find Recent Emails

```
Find the last 5 emails from john@example.com
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__gmail_find_email",
  "parameters": {
    "instructions": "Find last 5 emails from john@example.com",
    "query": "from:john@example.com"
  }
}
```

### Example: Search by Subject

```
Find all emails with "Invoice" in the subject from the last week
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__gmail_find_email",
  "parameters": {
    "instructions": "Find emails with Invoice in subject from last week",
    "query": "subject:Invoice after:2025-12-28"
  }
}
```

### Example: Send an Email

```
Send an email to sarah@company.com with subject "Project Update" and body
"Hi Sarah, the project is on track for delivery next week. Best, Team"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__gmail_send_email",
  "parameters": {
    "instructions": "Send project update email to sarah@company.com",
    "to": ["sarah@company.com"],
    "subject": "Project Update",
    "body": "Hi Sarah,\n\nThe project is on track for delivery next week.\n\nBest,\nTeam",
    "body_type": "plain"
  }
}
```

### Example: Create a Draft

```
Create a draft email to the team about the upcoming holiday schedule
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__gmail_create_draft",
  "parameters": {
    "instructions": "Create draft about holiday schedule",
    "to": ["team@company.com"],
    "subject": "Holiday Schedule Reminder",
    "body": "<p>Hi Team,</p><p>Please review the upcoming holiday schedule...</p>",
    "body_type": "html"
  }
}
```

### Example: Reply to an Email

```
Reply to the last email from boss@company.com saying "Thanks, I'll have
that ready by EOD"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__gmail_reply_to_email",
  "parameters": {
    "instructions": "Reply to last email from boss@company.com",
    "thread_id": "[thread_id_from_find]",
    "body": "Thanks, I'll have that ready by EOD.",
    "body_type": "plain"
  }
}
```

---

## Gmail Search Query Reference

Use these operators in your `query` parameter:

| Operator | Example | Description |
|----------|---------|-------------|
| `from:` | `from:john@example.com` | Sender's email |
| `to:` | `to:me` | Recipient |
| `subject:` | `subject:meeting` | Subject line |
| `in:` | `in:inbox` | Location |
| `is:` | `is:unread` | Email state |
| `has:` | `has:attachment` | Has attachments |
| `filename:` | `filename:pdf` | Attachment type |
| `after:` | `after:2026-01-01` | After date |
| `before:` | `before:2026-01-31` | Before date |
| `label:` | `label:important` | Has label |
| `larger:` | `larger:5M` | Size filter |

**Combined example:**
```
from:boss@company.com subject:urgent has:attachment after:2026-01-01
```

---

## Common Errors and Fixes

### Error: "Spreadsheet not found"

**Cause:** Spreadsheet name doesn't match exactly

**Fix:**
- Check exact spelling and capitalization
- Try using the spreadsheet ID instead (from URL)
- Ensure the connected account has access

### Error: "Calendar event creation failed"

**Cause:** Invalid date/time format

**Fix:**
- Use ISO 8601 format: `2026-01-15T14:00:00`
- Include timezone if needed: `2026-01-15T14:00:00-05:00`
- Ensure end time is after start time

### Error: "File not found in Drive"

**Cause:** File is in shared drive or specific folder

**Fix:**
- Specify the drive: `drive: "Shared drives/Team Drive"`
- Search in specific folder
- Check if file was recently deleted

### Error: "Insufficient permissions"

**Cause:** OAuth scope limitations

**Fix:**
- Disconnect and reconnect the app in Zapier
- Grant additional permissions during OAuth
- Check workspace admin restrictions

---

## Pro Tips

### 1. Use Sheet IDs for Reliability

Instead of spreadsheet names, use IDs from the URL:
```
https://docs.google.com/spreadsheets/d/1234567890abcdef/edit
                                        ^^^^^^^^^^^^^^^^
                                        This is the ID
```

### 2. Batch Operations

For multiple updates, describe them together:
```
Update the following rows in my "Inventory" sheet:
- Widget A: set Stock to 50
- Widget B: set Stock to 75
- Widget C: set Stock to 100
```

### 3. Use Headers for Worksheets

When creating spreadsheets that you'll update later, always include headers:
```json
{
  "headers": ["Name", "Email", "Phone", "Status", "Created Date"]
}
```

### 4. Calendar Time Zones

Always be explicit about timezones for meetings with external attendees:
```
Schedule meeting at 2pm Eastern time (not just 2pm)
```

### 5. Email HTML for Rich Content

Use HTML body type for formatted emails:
```json
{
  "body": "<h1>Weekly Update</h1><p>Here's what happened...</p><ul><li>Item 1</li></ul>",
  "body_type": "html"
}
```

### 6. Drive File Organization

Create a consistent folder structure and reference it in your requests:
```
Create a folder called "Client Name - Project" in the "Active Projects" folder
```

---

## Workflow Examples

### Daily Stand-up Workflow

```
1. Find today's calendar events
2. Get rows from "Sprint Tasks" where Status is "In Progress"
3. Create draft email summarizing both to team@company.com
```

### Invoice Processing Workflow

```
1. Find emails with "Invoice" in subject from last 24 hours
2. For each invoice email, create a row in "Invoice Tracker" spreadsheet
3. Move processed emails to "Processed" label
```

### Meeting Prep Workflow

```
1. Find calendar event "Client Meeting" for tomorrow
2. Find file "Client Proposal" in Drive
3. Create sharing link for the proposal
4. Create draft email to attendees with meeting agenda and proposal link
```

---

## Next Steps

- [GitHub MCP Guide](./github-mcp.md) - Development workflow integration
- [Design Tools MCP Guide](./design-tools-mcp.md) - Canva and Figma
- [Code Execution MCP Guide](./code-execution-mcp.md) - Run Python/JS through Claude

---

*Support Forge AI Launchpad Academy - Building the Future of AI Integration*
