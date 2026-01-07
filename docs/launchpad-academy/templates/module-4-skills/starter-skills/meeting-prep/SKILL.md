# Meeting Prep

Prepare for an upcoming meeting by gathering context, reviewing relevant materials, and generating an agenda with talking points.

## Trigger

- /meeting-prep
- /prep-meeting
- "prepare for meeting"
- "meeting preparation"
- "help me prepare for my meeting"

## Context

This skill helps users prepare for meetings by checking their calendar, gathering relevant context from recent work, and creating a structured preparation document. It's designed to reduce meeting anxiety and ensure productive discussions.

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| meeting_name | string | No | Specific meeting to prepare for (if not provided, will check calendar) |
| time_range | string | No | How far ahead to look (default: next 24 hours) |

## Instructions

1. **Identify the Meeting**
   - If meeting name provided, use that
   - Otherwise, use Google Calendar MCP to check for upcoming meetings in the next 24 hours
   - If multiple meetings found, list them and ask which one to prepare for
   - If no meetings found, ask the user to describe the meeting

2. **Gather Meeting Details**
   - Meeting title and time
   - Attendees (who will be there)
   - Any existing agenda or description
   - Previous meeting notes if this is a recurring meeting

3. **Collect Context**
   - Ask the user: "What is the main purpose of this meeting?"
   - Ask: "What topics do you want to cover?"
   - Ask: "Are there any decisions that need to be made?"
   - Ask: "Is there anything you need from other attendees?"

4. **Review Relevant Materials**
   - If this is a project meeting, check recent git commits related to the project
   - Look for any recent documents or files mentioned
   - Note any open issues or tasks that might be relevant

5. **Generate Preparation Document**
   - Create a structured prep document using the output format
   - Include talking points for each topic
   - Add questions to ask
   - Note any follow-up items from previous meetings

6. **Offer Additional Help**
   - Ask if user wants to add this prep to their calendar event notes
   - Offer to set a reminder 15 minutes before the meeting

## Output Format

```markdown
# Meeting Prep: [Meeting Title]

**Date/Time**: [Date and Time]
**Attendees**: [List of attendees]
**Duration**: [Expected duration]

---

## Meeting Purpose
[One sentence summary of why this meeting is happening]

## Key Topics

### 1. [Topic Name]
**Context**: [Brief background]
**Talking Points**:
- [Point 1]
- [Point 2]
**Questions to Ask**:
- [Question 1]

### 2. [Topic Name]
**Context**: [Brief background]
**Talking Points**:
- [Point 1]
**Questions to Ask**:
- [Question 1]

## Decisions Needed
- [ ] [Decision 1]
- [ ] [Decision 2]

## Things to Request
- [Request 1 from Person A]
- [Request 2 from Person B]

## Supporting Materials
- [Link or reference to relevant document]
- [Recent commit/change to mention]

## Notes from Previous Meeting
[Summary if applicable, or "N/A - First meeting"]

---

*Prepared at [TIME] | Meeting in [X hours/minutes]*
```

## Examples

### Example: Project Sync Meeting

**User**: /meeting-prep

**Claude**: Let me check your calendar for upcoming meetings...

I found these meetings in the next 24 hours:
1. "Weekly Team Sync" - Today at 2:00 PM (5 attendees)
2. "1:1 with Sarah" - Tomorrow at 10:00 AM
3. "Client Review - Acme Corp" - Tomorrow at 2:00 PM

Which meeting would you like to prepare for?

**User**: The client review

**Claude**: Great! Preparing for "Client Review - Acme Corp" tomorrow at 2:00 PM.

**What is the main purpose of this meeting?**

**User**: Review the dashboard redesign and get sign-off

**Claude**: **What topics do you want to cover?**

**User**: New dashboard layout, mobile responsiveness, timeline for launch

**Claude**: **Are there any decisions that need to be made?**

**User**: They need to approve the color scheme and confirm the launch date

**Claude**: **Is there anything you need from the client?**

**User**: Final logo assets and content for the about page

[Claude generates the full prep document]

## Dependencies

- Google Calendar MCP (optional, for automatic meeting detection)
- Git access (optional, for pulling recent commit context)

## Notes

- This skill works best when calendar integration is available
- Even without calendar access, users can manually describe the meeting
- The skill focuses on preparation, not note-taking during the meeting
- For recurring meetings, maintaining a notes file helps track continuity
