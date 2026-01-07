# Script 4.4: Creating Your First Custom Skill

**Module:** 4 - Skills & Plugins (NETWORK Phase)
**Duration:** 20 minutes
**Lesson:** 4.4 - Creating Your First Custom Skill

---

## INTRO (1 min)

[SCREEN: Lesson title "Creating Your First Custom Skill"]

This is where everything comes together. [PAUSE] You've seen what skills can do. You've installed skills from others. Now you're building your own.

Custom skills let you encode your exact workflows. [PAUSE] The way you like commits formatted. Your team's code review checklist. Your personal morning routine.

[SCREEN: "Your Workflow, Automated" tagline]

By the end of this lesson, you'll have a working custom skill and the knowledge to build as many more as you need.

Let's build.

---

## SKILL ANATOMY (4 min)

[SCREEN: "SKILL.md Structure" header]

Every skill starts with a SKILL.md file. [PAUSE] Let me break down the structure.

### The Basic Template

[SCREEN: Full SKILL.md template appearing]

```markdown
# Skill Name

## Description
One-line description of what this skill does.

## When to Use
Trigger conditions - when should Claude suggest or use this skill?

## Instructions
Step-by-step guidance for Claude when this skill is invoked.

## Input
What arguments or context does this skill expect?

## Output
What should the final result look like?

## Examples
Sample invocations and expected behavior.
```

[PAUSE]

Let's understand each section.

### Description

[SCREEN: Highlighting Description section]

Keep it brief. [PAUSE] This shows up when listing available skills. "Generate morning briefing from calendar and email" tells you exactly what it does.

### When to Use

[SCREEN: Highlighting When to Use section]

This is optional but powerful. [PAUSE] It tells Claude when to proactively suggest this skill.

"Use when the user asks about their schedule for the day" means Claude might say "Would you like me to run your morning briefing?" when relevant.

### Instructions

[SCREEN: Highlighting Instructions section]

This is the heart of your skill. [PAUSE] Write this like you're training a new team member.

Be specific. [PAUSE] Don't say "format it nicely" - say "use markdown headers, bullet points for lists, and code blocks for any commands."

Include decision trees. [PAUSE] "If the user hasn't specified a branch, ask which branch. If they say 'main' or 'master', confirm before proceeding."

### Input and Output

[SCREEN: Highlighting Input/Output sections]

Input defines what the skill expects. [PAUSE] Arguments, context, files to read.

Output defines what success looks like. [PAUSE] A file created? A message displayed? Data returned?

### Examples

[SCREEN: Highlighting Examples section]

Concrete examples help Claude understand edge cases. [PAUSE] Show a few different invocation patterns and what should happen for each.

---

## BUILDING A MORNING BRIEFING SKILL (8 min)

[SCREEN: "Project: Morning Briefing Skill" header]

Let's build something practical. [PAUSE] A morning briefing skill that checks your calendar, looks for important emails, and summarizes your day.

### Step 1: Create the Folder

[SCREEN: File browser creating folder]

Navigate to your skills directory and create a new folder:

```
skills/
  morning-briefing/
```

### Step 2: Create SKILL.md

[SCREEN: Creating the file in editor]

Inside that folder, create SKILL.md:

[SCREEN: Writing the skill content]

```markdown
# Morning Briefing

## Description
Generate a comprehensive morning briefing including calendar events,
important emails, and daily priorities.

## When to Use
- When user types /morning or /morning-briefing
- When user asks "what's on my schedule today"
- When user asks for a daily summary

## Instructions

When this skill is invoked, follow these steps in order:

### 1. Get Today's Date Context
Note the current date and day of week. Consider if it's a
Monday (include weekend context) or Friday (note upcoming weekend).

### 2. Calendar Review
Use the Google Calendar MCP tools to:
- Fetch all events for today
- Fetch events for tomorrow (preview)
- Identify any conflicts or back-to-back meetings

Present calendar as a timeline format:
```
TODAY'S SCHEDULE
----------------
9:00 AM - Team standup (30 min)
10:00 AM - Client call with Acme (1 hr)
[2 hour gap]
1:00 PM - Lunch with Sarah (1 hr)
```

### 3. Email Scan
Use Gmail MCP tools to:
- Find unread emails from the last 24 hours
- Prioritize emails from known important contacts
- Flag any emails with "urgent" or "asap" in subject

Summarize as:
```
EMAIL SUMMARY
-------------
- 3 unread emails
- 1 flagged as urgent: "Q4 Budget Review" from CFO
- Notable: Response needed on Project Alpha proposal
```

### 4. Daily Priorities
Based on calendar and email analysis, suggest top 3 priorities
for the day. Consider:
- Meetings that need prep
- Deadlines mentioned in emails
- Gaps in schedule for deep work

### 5. Delivery Format
Present everything in a clean, scannable format. Start with
a one-line summary: "You have X meetings today, Y urgent items."

Keep total briefing under 500 words unless the day is unusually complex.

## Input
- No arguments required for basic briefing
- Optional: "tomorrow" or specific date for different day
- Optional: "detailed" for expanded email summaries

## Output
A formatted briefing in the terminal, ready to read in under 2 minutes.

## Examples

### Basic Invocation
User: /morning
Response: Full briefing for today

### Specific Date
User: /morning tomorrow
Response: Briefing for tomorrow's schedule

### Detailed Mode
User: /morning detailed
Response: Briefing with full email previews instead of summaries
```

[SCREEN: Completed SKILL.md file]

### Step 3: Save and Test

[SCREEN: Saving the file]

Save the file. [PAUSE] Now let's test it.

[SCREEN: Claude Code terminal]

Restart Claude Code to pick up the new skill, then type:

```
/morning-briefing
```

[SCREEN: Claude executing the skill]

Watch Claude work. [PAUSE] It follows your instructions - checking calendar, scanning emails, synthesizing priorities.

[SCREEN: Morning briefing output appearing]

The output follows your specified format. [PAUSE] Timeline view for calendar, summary for emails, prioritized action items.

### Step 4: Refine

[SCREEN: Iterating on the skill]

First run probably isn't perfect. [PAUSE] Maybe the email section is too verbose. Maybe you want a different calendar format.

Edit the SKILL.md, save, and run again. [PAUSE] Skills load fresh each time, so changes apply immediately.

This refinement loop is how you dial in the perfect skill.

---

## BEST PRACTICES (4 min)

[SCREEN: "Skill Writing Best Practices" header]

After building a few skills, here's what I've learned:

### Be Specific, Not Vague

[SCREEN: Good vs bad instruction examples]

**Bad:** "Format the output nicely."

**Good:** "Use H2 headers for each section. Bullet points for lists of 3+ items. Bold for emphasis on key terms."

Claude can interpret vague instructions, but specific ones give consistent results.

### Include Edge Cases

[SCREEN: Edge case handling]

What if there are no calendar events? [PAUSE] What if the email API fails? Your skill should handle these:

```markdown
If no calendar events are found, say "Your calendar is clear today -
great opportunity for deep work!" rather than just "No events."

If email tools are unavailable, note "Email summary unavailable -
MCP connection may need refresh" and continue with other sections.
```

### Use Conditional Logic

[SCREEN: Conditional instruction example]

```markdown
If today is Monday:
- Include "Weekend email catchup" as a suggested priority
- Note any events from Friday that may need follow-up

If today is Friday:
- Preview Monday's first meeting
- Suggest reviewing weekly goals
```

This makes your skill smarter and more contextual.

### Test Multiple Scenarios

[SCREEN: Testing checklist]

Before considering a skill "done," test:
- Normal case (typical day with events and emails)
- Empty case (no events, no emails)
- Heavy case (packed calendar, overflowing inbox)
- Edge case (weekend, holiday, unusual situation)

### Keep Skills Focused

[SCREEN: Single responsibility principle]

One skill, one job. [PAUSE]

If your skill is trying to do morning briefing AND plan your week AND summarize your projects... break it up.

```
/morning - daily briefing
/weekly-plan - week planning
/project-status - project summaries
```

Small, focused skills compose better than one mega-skill.

---

## SHARING YOUR SKILLS (2 min)

[SCREEN: "Sharing Skills" with GitHub icon]

Built something great? [PAUSE] Share it with the community.

### Create a GitHub Repository

[SCREEN: GitHub repo creation]

Make a repository for your skills. [PAUSE] Structure it clearly:

```
my-claude-skills/
  README.md          (overview of all skills)
  morning-briefing/
    SKILL.md
    README.md        (specific skill docs)
  code-review/
    SKILL.md
    checklist.md     (supporting file)
```

### Write Good Documentation

[SCREEN: README example]

For each skill, explain:
- What it does
- What MCP servers it requires (if any)
- How to customize it for their needs
- Example output

### License It

[SCREEN: License choice]

Add a license so people know they can use it. [PAUSE] MIT is common for skills - use it freely, no warranty.

---

## WRAP UP (1 min)

[SCREEN: Module 4 completion graphic]

Congratulations. [PAUSE] You've completed Module 4.

You now understand:
- What skills are and how they extend Claude
- How to install and use the Superpowers plugin
- How to find and customize community skills
- How to build your own skills from scratch

[SCREEN: Skills you can now create - list appearing]

The skills you can create are limited only by your imagination:
- Code generation with your team's patterns
- Deployment workflows for your infrastructure
- Documentation generation in your format
- Meeting notes that extract action items
- Client communication templates
- Whatever your workflow demands

[SCREEN: Course progress - Modules 1-4 complete, future modules teased]

You've come a long way from installation. [PAUSE] Claude Code is no longer just a coding assistant - it's an integrated system connected to your services, extended with powerful skills, and customized for how you work.

In the next module, we'll put everything together with real project workflows. [PAUSE] See you there.

---

**END OF SCRIPT 4.4**

---

**END OF MODULE 4**
