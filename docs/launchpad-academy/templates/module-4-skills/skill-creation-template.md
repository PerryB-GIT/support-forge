# Claude Code Skill Creation Template

This guide explains how to create custom skills for Claude Code. Skills are reusable workflows that Claude can execute when triggered by specific phrases or commands.

---

## What is a SKILL.md File?

A `SKILL.md` file defines a skill that Claude Code can invoke. When placed in your `~/.claude/skills/` directory (user skills) or `.claude/skills/` directory (project skills), Claude automatically discovers and can use these skills.

---

## SKILL.md Structure

### Required Sections

```markdown
# Skill Name

Brief one-line description of what the skill does.

## Trigger

List the phrases or commands that activate this skill:
- /command-name
- "natural language trigger phrase"

## Instructions

Step-by-step instructions for Claude to follow when executing this skill.

1. First step
2. Second step
3. Third step
```

### Optional Sections

```markdown
## Context

Background information or context Claude should understand before executing.

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| project_name | string | Yes | Name of the project |
| include_details | boolean | No | Whether to include details |

## Output Format

Description of how the output should be structured.

## Examples

### Example 1: Basic Usage
Input: /command basic
Output: [expected output]

### Example 2: With Options
Input: /command --detailed
Output: [expected output with details]

## Dependencies

- Tool or MCP server required
- File or configuration needed

## Notes

Any additional notes, warnings, or best practices.
```

---

## Best Practices

### 1. Clear Trigger Phrases
- Use descriptive slash commands: `/daily-standup` not `/ds`
- Include natural language alternatives
- Avoid conflicts with built-in commands

### 2. Explicit Instructions
- Number each step
- Be specific about expected behavior
- Include conditional logic where needed
- Specify error handling

### 3. Defined Outputs
- Describe the expected format
- Include examples when helpful
- Specify where output goes (clipboard, file, terminal)

### 4. Appropriate Scope
- One skill = one focused task
- Chain multiple skills for complex workflows
- Keep instructions under 500 words when possible

### 5. User Interaction
- Specify when to ask for input
- Define default behaviors
- Allow customization through parameters

---

## File Placement

### User Skills (Personal)
```
~/.claude/skills/
  my-skill/
    SKILL.md
    supporting-file.txt (optional)
```

### Project Skills (Shared)
```
.claude/skills/
  project-skill/
    SKILL.md
```

---

## Complete Example Template

```markdown
# Task Automation Skill

Automates [specific task] by [method].

## Trigger

- /task-name
- "run task automation"
- "automate [task]"

## Context

This skill is designed for [use case]. It assumes:
- [Assumption 1]
- [Assumption 2]

## Inputs

| Input | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| target | string | Yes | - | The target to process |
| verbose | boolean | No | false | Show detailed output |

## Instructions

1. **Validate Input**
   - Confirm the target exists
   - If not found, ask the user for clarification

2. **Process Task**
   - Execute the main operation
   - Log progress if verbose mode is enabled

3. **Generate Output**
   - Format results according to output specification
   - Present to user

4. **Handle Errors**
   - If operation fails, provide clear error message
   - Suggest remediation steps

## Output Format

```
## Task Results

**Target**: [target name]
**Status**: [Success/Failed]
**Details**: [summary]

### Actions Taken
- [action 1]
- [action 2]
```

## Examples

### Basic Usage
```
/task-name my-project
```

### With Verbose Output
```
/task-name my-project --verbose
```

## Dependencies

- Git repository (for version tracking)
- Read access to target directory

## Notes

- This skill modifies files; ensure you have backups
- Works best with projects following standard structure
```

---

## Testing Your Skill

1. **Create the skill file** in the appropriate location
2. **Restart Claude Code** or reload skills
3. **Test the trigger** by typing your trigger phrase
4. **Verify behavior** matches expectations
5. **Iterate** on instructions as needed

---

## Common Patterns

### Interactive Skill
```markdown
## Instructions

1. Ask the user for [required information]
2. Confirm understanding before proceeding
3. Execute task
4. Report results
```

### Automated Skill
```markdown
## Instructions

1. Gather information from [source]
2. Process without user interaction
3. Present completed results
```

### Hybrid Skill
```markdown
## Instructions

1. Attempt to gather information automatically
2. If information is missing, ask the user
3. Proceed with execution
4. Allow user to modify results
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Skill not recognized | Check file location and name (must be SKILL.md) |
| Wrong behavior | Review instructions for ambiguity |
| Missing context | Add more background in Context section |
| Inconsistent output | Define Output Format more explicitly |

---

## Next Steps

1. Copy this template
2. Fill in your skill details
3. Place in skills directory
4. Test and refine

See the `starter-skills/` directory for complete working examples.
