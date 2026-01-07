# Daily Standup Generator

A Claude Code skill that generates a structured daily standup summary from your calendar, tasks, and recent activity.

## Trigger

Invoke with: `/daily-standup` or `/standup`

## Description

This skill automatically compiles your daily standup by:
1. Fetching today's calendar events
2. Reviewing open tasks and their status
3. Analyzing recent git commits (if in a repo)
4. Identifying blockers based on overdue items
5. Generating a formatted standup ready for sharing

## Input

No required input - the skill gathers context automatically.

Optional flags:
- `--format slack` - Format for Slack posting
- `--format markdown` - Format as markdown (default)
- `--format plain` - Plain text format
- `--team` - Include team member mentions
- `--yesterday` - Generate for yesterday instead of today

## Workflow

### Step 1: Gather Context
```
1. Check if MCP Zapier tools are available for calendar/sheets access
2. If in a git repository, get recent commits
3. Read any local task files if present
```

### Step 2: Fetch Calendar Events
```
Use Google Calendar MCP:
- Get today's events from primary calendar
- Extract: event name, time, duration, attendees
- Identify meetings vs focus time vs breaks
```

### Step 3: Fetch Tasks
```
If Google Sheets MCP available:
- Look for tasks sheet
- Filter for: assigned to me, status = In Progress or Todo
- Sort by priority and due date

If local task file exists:
- Parse TODO.md, tasks.md, or similar
- Extract incomplete items
```

### Step 4: Analyze Git Activity
```
If in git repository:
- Get commits from last 24 hours by current user
- Summarize: files changed, type of work
- Identify any incomplete work (WIP commits)
```

### Step 5: Identify Blockers
```
Analyze gathered data for:
- Overdue tasks
- Dependencies waiting on others
- Meetings that might block focus time
- Any items marked as blocked
```

### Step 6: Generate Standup
```
Compile into standard format:

## Daily Standup - [Date]

### What I Did Yesterday
- [Completed items, commits, delivered work]

### What I'm Doing Today
- [Priority tasks, scheduled work, meetings]

### Blockers
- [Identified blockers, or "None"]

### Notes
- [Any additional context]
```

## Output Format

### Default (Markdown)
```markdown
## Daily Standup - January 15, 2025

### What I Did Yesterday
- Completed user authentication flow (3 commits)
- Fixed payment processing bug (#123)
- Reviewed PR for reporting feature

### What I'm Doing Today
- Sprint planning meeting (10:00 AM)
- Continue work on dashboard redesign
- Code review for team submissions

### Blockers
- Waiting on API documentation from backend team
- Design specs needed for mobile view

### Today's Schedule
- 10:00 AM - Sprint Planning (1h)
- 2:00 PM - 1:1 with Manager (30m)
- 4:00 PM - Team sync (30m)
```

### Slack Format
```
:sunrise: *Daily Standup - January 15*

*Yesterday:*
• Completed user auth flow
• Fixed payment bug #123
• Reviewed reporting PR

*Today:*
• Sprint planning @ 10am
• Dashboard redesign
• Code reviews

*Blockers:*
• Waiting on backend API docs
• Need mobile design specs
```

## Examples

### Basic Usage
```
> /daily-standup

Generating your daily standup...
Fetching calendar... 3 events found
Checking tasks... 5 open items
Analyzing git activity... 4 commits yesterday

## Daily Standup - January 15, 2025
[output]
```

### With Slack Format
```
> /daily-standup --format slack

:sunrise: *Daily Standup - January 15*
[slack-formatted output]
```

## Configuration

Create a `.standup-config.json` in your project or home directory:

```json
{
  "default_format": "markdown",
  "include_git": true,
  "calendar_id": "primary",
  "tasks_sheet_id": "YOUR_SHEET_ID",
  "slack_channel": "#standups",
  "team_members": ["@alice", "@bob"],
  "work_start_hour": 9,
  "work_end_hour": 17
}
```

## Dependencies

### Required MCP Servers
- `zapier` - For Google Calendar and Sheets access

### Optional
- Git repository access for commit history
- Local task files (TODO.md, tasks.md)

## Error Handling

| Error | Handling |
|-------|----------|
| No calendar access | Skip calendar section, note in output |
| No tasks found | Include "No tracked tasks" |
| Not in git repo | Skip git analysis |
| MCP unavailable | Fall back to manual input prompt |

## Tips

1. Run this first thing in the morning before your standup meeting
2. Copy output directly to Slack or your team's standup channel
3. Add the `--team` flag to include @mentions for blocked-by items
4. Use `--yesterday` on Mondays to include Friday's work

## Related Skills

- `/weekly-summary` - Generate weekly progress report
- `/time-audit` - Analyze how time was spent
- `/blocker-report` - Detailed blocker analysis
