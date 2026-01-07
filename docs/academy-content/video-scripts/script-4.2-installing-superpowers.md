# Script 4.2: Installing the Superpowers Plugin

**Module:** 4 - Skills & Plugins (NETWORK Phase)
**Duration:** 15 minutes
**Lesson:** 4.2 - Installing the Superpowers Plugin

---

## INTRO (1 min)

[SCREEN: Lesson title with Superpowers branding/logo]

The Superpowers plugin is one of the most popular Claude Code extensions out there. [PAUSE] It's a collection of carefully crafted skills that cover common development workflows.

In this lesson, we'll install Superpowers, take a tour of what's included, and demo some key skills so you can see them in action.

[SCREEN: Preview of skills included in Superpowers]

By the end, you'll have a toolkit of skills ready to use in your daily work.

---

## WHAT'S IN SUPERPOWERS (2 min)

[SCREEN: Superpowers skill list appearing one by one]

Before we install, let's preview what you're getting.

**superpowers:brainstorming** - Use this before any creative work. [PAUSE] Building a feature? Adding functionality? This skill helps you explore requirements and design before jumping into code.

**superpowers:writing-plans** - When you have specs or requirements, this skill creates structured implementation plans. [PAUSE] Think before you build.

**superpowers:executing-plans** - Takes a written plan and executes it methodically with review checkpoints.

**superpowers:test-driven-development** - Guides you through TDD workflow. [PAUSE] Write tests first, then implement.

**superpowers:systematic-debugging** - Hit a bug? [PAUSE] This skill walks you through diagnosis before proposing fixes.

**superpowers:requesting-code-review** - Get Claude to review your work before merging.

**superpowers:receiving-code-review** - When you get feedback, this skill helps you respond appropriately.

**superpowers:verification-before-completion** - Prevents premature "done" claims. [PAUSE] Requires running verification commands before celebrating.

**superpowers:using-git-worktrees** - Helps you work with Git worktrees for isolated feature development.

**superpowers:dispatching-parallel-agents** - When you have independent tasks, this coordinates parallel work.

[PAUSE]

These skills encode best practices. [PAUSE] Things like "don't claim it's fixed until you've verified" and "explore requirements before implementing."

---

## INSTALLATION (4 min)

[SCREEN: Terminal ready for installation]

Let's install it. [PAUSE] Open Claude Code in your terminal.

The Superpowers plugin is hosted on GitHub. [PAUSE] To install a plugin, you typically add it to your Claude Code configuration, but the exact method depends on how the plugin is distributed.

For Superpowers, we'll use the plugin marketplace approach.

[SCREEN: Typing the installation command]

In Claude Code, type:

```
/install-plugin superpowers
```

[SCREEN: Claude acknowledging and downloading]

Claude recognizes this command, finds the Superpowers plugin from the marketplace, and installs it. [PAUSE] You'll see it downloading and confirming successful installation.

If that command isn't available, here's the manual approach:

[SCREEN: Alternative installation steps]

First, find where your Claude Code plugins directory is:
- Windows: `%APPDATA%\Claude\plugins\`
- Mac: `~/Library/Application Support/Claude/plugins/`

Create a folder called `superpowers` in that directory.

[SCREEN: File browser showing directory creation]

Then, download the Superpowers plugin files from their GitHub repository and place them in that folder. [PAUSE] The key file is the plugin manifest that tells Claude Code what skills are available.

After installation, restart Claude Code to load the new plugin.

[SCREEN: Claude Code restarting and showing Superpowers loaded]

When Claude Code starts, you should see Superpowers listed in the available plugins.

### Verifying Installation

Type:

```
What skills do I have from the Superpowers plugin?
```

[SCREEN: Claude listing Superpowers skills]

Claude should list all the skills we previewed earlier. [PAUSE] If you see them, installation was successful.

---

## KEY SKILLS DEMO (6 min)

[SCREEN: "Skills Demo" header]

Let's see some of these in action.

### Brainstorming Demo

[SCREEN: Claude Code terminal]

Say you're about to build a user authentication feature. [PAUSE] Instead of diving into code, invoke brainstorming:

```
/superpowers:brainstorming I need to add user authentication to my Next.js app
```

[SCREEN: Claude entering brainstorming mode]

Watch what Claude does. [PAUSE] It doesn't immediately start coding. Instead, it asks questions:

- What authentication method? Email/password, OAuth, magic links?
- What's the user experience you want?
- Are there existing users to migrate?
- What security requirements do you have?

[SCREEN: Claude asking clarifying questions]

This is the skill in action. [PAUSE] It's forcing the exploration phase before implementation. You'll catch missing requirements and make better design decisions.

### Writing Plans Demo

[SCREEN: New prompt]

Once you've brainstormed and have clarity, move to planning:

```
/superpowers:writing-plans Create a plan for implementing OAuth with Google for our Next.js app
```

[SCREEN: Claude generating structured plan]

Claude produces a structured implementation plan:

1. Install required packages (next-auth, etc.)
2. Configure Google OAuth credentials
3. Set up NextAuth API route
4. Create sign-in/sign-out components
5. Add protected route middleware
6. Test authentication flow

[PAUSE]

Each step is specific and actionable. [PAUSE] This plan becomes your roadmap.

### Systematic Debugging Demo

[SCREEN: Simulated bug scenario]

Here's one I use constantly. [PAUSE] You hit an error. Your instinct is to start changing things randomly. Don't.

```
/superpowers:systematic-debugging The login form submits but nothing happens, no errors in console
```

[SCREEN: Claude in debugging mode]

The skill guides Claude to diagnose systematically:

- What's the expected behavior?
- What's the actual behavior?
- Let's add logging to trace the request...
- Let's check the network tab...
- Let's verify the API endpoint...

[SCREEN: Claude working through diagnosis]

It's not guessing. [PAUSE] It's following a methodical process. This almost always finds the root cause faster than random debugging.

### Verification Before Completion Demo

[SCREEN: Scenario - claiming something is fixed]

This skill has saved me from embarrassment multiple times. [PAUSE]

When you're about to say "it's done" or "it's fixed":

```
/superpowers:verification-before-completion I've fixed the login bug
```

[SCREEN: Claude requesting proof]

Claude doesn't just accept your claim. [PAUSE] It asks:

- What command should we run to verify?
- Show me the passing test output
- Can we reproduce the original issue to confirm it's gone?

[SCREEN: Claude requiring evidence]

You're required to provide evidence before Claude lets you mark it complete. [PAUSE] No more "oops, I thought I fixed it."

---

## WHEN TO USE WHICH SKILL (2 min)

[SCREEN: Decision flowchart]

Quick guide on when to reach for each skill:

[SCREEN: Flowchart appearing]

**Starting something new?** → Brainstorming first

**Have requirements, need a plan?** → Writing Plans

**Have a plan, ready to build?** → Executing Plans or Test-Driven Development

**Hit a bug or unexpected behavior?** → Systematic Debugging

**Think you're done?** → Verification Before Completion

**Want feedback on your code?** → Requesting Code Review

**Got feedback from someone else?** → Receiving Code Review

[SCREEN: "Next: Installing Industry Skills" with arrow]

That's Superpowers installed and demoed. [PAUSE] These skills will become second nature once you start using them.

Next, we'll look at finding and installing other skills from the community - industry-specific skills that might match your exact workflow.

---

**END OF SCRIPT 4.2**
