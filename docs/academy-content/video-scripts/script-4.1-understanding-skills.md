# Script 4.1: Understanding Skills

**Module:** 4 - Skills & Plugins (NETWORK Phase)
**Duration:** 10 minutes
**Lesson:** 4.1 - Understanding Skills

---

## INTRO (1 min)

[SCREEN: Module 4 title card "Skills & Plugins - NETWORK Phase"]

Welcome to Module 4. [PAUSE] We've unlocked MCP servers - Claude can now talk to external services. But there's another layer of extension: Skills.

[SCREEN: Skills icon with neural network visual]

Skills are like pre-programmed expertise you can give Claude. [PAUSE] Instead of explaining how to do something every time, you define it once as a skill, and Claude just... knows how.

In this lesson, we'll understand what skills are, how they differ from MCP servers, and what's possible with them.

---

## WHAT ARE SKILLS? (3 min)

[SCREEN: "Skills Explained" header with simple diagram]

Think about how you work with Claude normally. [PAUSE] You give instructions, context, maybe examples of what you want. Claude follows your guidance.

Now imagine packaging all that guidance into a reusable file. [PAUSE] That's a skill.

[SCREEN: Comparison - Regular prompt vs Skill]

**Without a skill:**
"I want you to create a git commit. Use conventional commit format. The message should start with feat:, fix:, or docs: depending on the change type. Include a body explaining why the change was made. Add the co-author line at the end..."

**With a skill:**
"/commit"

[PAUSE]

Same result. [PAUSE] But with a skill, all that instruction is pre-loaded. You invoke the skill, and Claude knows exactly what to do.

[SCREEN: Skill components diagram]

Skills are defined in files - usually a SKILL.md file that contains:

- A description of what the skill does [PAUSE]
- Instructions for how Claude should behave [PAUSE]
- Context about when to use it [PAUSE]
- Sometimes, supporting files for reference [PAUSE]

When you invoke a skill, Claude reads this file and follows its guidance.

---

## SKILLS VS MCP SERVERS (2 min)

[SCREEN: Side-by-side comparison table]

Let me clarify the difference between skills and MCP servers, because they complement each other.

[SCREEN: MCP column highlighting]

**MCP servers** give Claude new capabilities - new tools to call. [PAUSE] Without the Zapier MCP, Claude literally cannot access your Google Calendar. The MCP provides that capability.

[SCREEN: Skills column highlighting]

**Skills** give Claude new knowledge and workflows - guidance on how to use its capabilities. [PAUSE] A skill might tell Claude how to structure a commit message, how to analyze code, or how to create a specific type of document.

[SCREEN: Combined workflow example]

The powerful combination is both together. [PAUSE]

Example: You have Zapier MCP connected (capability). You create a skill called "morning-briefing" that tells Claude to check your calendar, scan your email for urgent items, and summarize your Drive activity (knowledge/workflow).

One skill invocation triggers a whole workflow using multiple MCP tools.

---

## TYPES OF SKILLS (2 min)

[SCREEN: "Skill Types" with three categories]

Skills come in a few flavors:

### Built-in Skills

[SCREEN: Built-in skills examples]

Some skills come pre-packaged. [PAUSE] Depending on your Claude Code configuration, you might have access to skills for code review, debugging, or documentation right out of the box.

These are maintained by Anthropic or the Claude Code community.

### Plugin Skills

[SCREEN: Plugin skills with superpowers logo]

Plugins are collections of skills bundled together. [PAUSE] The "Superpowers" plugin, which we'll install next lesson, includes skills for:

- Brainstorming
- Writing implementation plans
- Systematic debugging
- Code review workflows
- And more

Plugins are great because someone else has done the hard work of crafting well-designed skills.

### Custom Skills

[SCREEN: Custom skill icon]

You can create your own skills. [PAUSE] This is where it gets really powerful.

Got a specific workflow for your team? [PAUSE] Package it as a skill.
Always write proposals the same way? [PAUSE] Skill.
Have a checklist before deploying? [PAUSE] Skill.

We'll build a custom skill in lesson 4.4.

---

## HOW SKILLS ARE INVOKED (1.5 min)

[SCREEN: Claude Code terminal with skill invocation]

Invoking a skill is simple. [PAUSE] You use a slash command.

[SCREEN: Examples appearing]

```
/commit
/review-pr
/brainstorm
/morning
```

When you type one of these, Claude Code recognizes it as a skill invocation. [PAUSE] It loads the skill's instructions and Claude operates in that mode.

Some skills take arguments:

```
/review-pr 123
/deploy production
```

The argument provides context the skill needs.

[SCREEN: Skill tool call example]

Under the hood, when you invoke a skill, Claude Code calls a "Skill" tool, passing the skill name. [PAUSE] This loads the skill's SKILL.md file and any supporting context.

---

## WHAT MAKES A GOOD SKILL (1.5 min)

[SCREEN: "Good Skill Design" header]

Not all skills are created equal. [PAUSE] Here's what separates great skills from mediocre ones:

[SCREEN: Good skill characteristics]

**Specific purpose.** [PAUSE] A skill should do one thing well. "Code review" is good. "Do everything" is not.

**Clear instructions.** [PAUSE] The SKILL.md should tell Claude exactly how to behave - what to check, what format to use, what questions to ask.

**Appropriate scope.** [PAUSE] Skills should be complex enough to be worth packaging, but not so complex they try to do too much.

**Reusable.** [PAUSE] If you're only going to do something once, you don't need a skill. Skills shine for repeated workflows.

[SCREEN: Example of well-structured SKILL.md preview]

In lesson 4.4, we'll dissect the structure of a SKILL.md file and build one from scratch. [PAUSE] You'll see exactly how to craft instructions that produce consistent results.

---

## WRAP UP (30 sec)

[SCREEN: Lesson recap]

So that's skills in a nutshell. [PAUSE]

- Skills are packaged instructions that give Claude expertise
- They're different from MCP servers, which provide capabilities
- They come built-in, through plugins, or you create your own
- You invoke them with slash commands

[SCREEN: "Next: Installing the Superpowers Plugin" with arrow]

Next up, we're installing the Superpowers plugin - a collection of battle-tested skills that'll immediately level up your Claude Code experience.

Let's go.

---

**END OF SCRIPT 4.1**
