# Daily Standup

Run an interactive daily standup to capture yesterday's accomplishments, today's plans, and any blockers.

## Trigger

- /standup
- /daily-standup
- "run standup"
- "daily standup"
- "start my standup"

## Context

This skill facilitates daily standup meetings commonly used in Agile development. It follows the three-question format and produces a formatted summary that can be shared with teammates or logged for reference.

## Instructions

1. **Greet and Start**
   - Display the current date
   - Announce the start of the daily standup

2. **Ask Question 1: Yesterday**
   - Ask: "What did you accomplish yesterday?"
   - Wait for the user's response
   - Accept multiple items (user can list several accomplishments)

3. **Ask Question 2: Today**
   - Ask: "What are you planning to work on today?"
   - Wait for the user's response
   - Accept multiple items

4. **Ask Question 3: Blockers**
   - Ask: "Do you have any blockers or impediments?"
   - Wait for the user's response
   - If user says "none" or "no", record as "No blockers"

5. **Generate Summary**
   - Format the standup using the output format below
   - Display the formatted summary

6. **Offer Actions**
   - Ask if the user wants to:
     - Copy to clipboard
     - Save to a file (suggest `standup-YYYY-MM-DD.md`)
     - Post to Slack (if MCP available)
   - Execute the chosen action

## Output Format

```markdown
# Daily Standup - [DATE]

## Yesterday
- [accomplishment 1]
- [accomplishment 2]
- ...

## Today
- [task 1]
- [task 2]
- ...

## Blockers
- [blocker 1] or "No blockers"

---
*Standup completed at [TIME]*
```

## Examples

### Example Interaction

**Claude**: Good morning! Starting your daily standup for Tuesday, January 7, 2025.

**What did you accomplish yesterday?**

**User**: Fixed the login bug, reviewed Sarah's PR, and updated the documentation

**Claude**: Got it!

**What are you planning to work on today?**

**User**: Implement the new dashboard feature and write tests for it

**Claude**: Perfect!

**Do you have any blockers or impediments?**

**User**: Waiting on API specs from the backend team

**Claude**: Here's your standup summary:

```
# Daily Standup - January 7, 2025

## Yesterday
- Fixed the login bug
- Reviewed Sarah's PR
- Updated the documentation

## Today
- Implement the new dashboard feature
- Write tests for dashboard feature

## Blockers
- Waiting on API specs from the backend team

---
*Standup completed at 9:15 AM*
```

Would you like me to copy this to your clipboard, save it to a file, or post it somewhere?

## Notes

- Keep responses focused; this isn't meant to be a long conversation
- If the user provides brief answers, that's fine - standups should be quick
- The skill should complete in under 2 minutes
- Formatting is intentionally simple for easy pasting into various tools
