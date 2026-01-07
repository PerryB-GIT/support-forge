# Script 2.4: Configuring Settings

**Duration:** 15 minutes (~2250-2550 words)
**Lesson:** Module 2, Lesson 4
**Purpose:** Settings file configuration, CLAUDE.md setup, customization options

---

## OPENING

[SCREEN: "Configuring Settings" title]

Claude Code works great out of the box. But when you configure it for your specific needs, it becomes a true partner that understands your business.

[PAUSE]

[SCREEN: Configuration options overview]

In this lesson, we're covering the settings file, the CLAUDE.md file, and other customizations that make Claude Code feel like it was built just for you.

[PAUSE]

Let's set it up right.

[PAUSE]

---

## PART 1: THE SETTINGS FILE

[SCREEN: Settings file location]

Claude Code uses a settings file to control its behavior. Let's find it and understand what we can configure.

[PAUSE]

[SCREEN: Default settings location by OS]

The settings file location varies by operating system. On Mac and Linux, look in your home directory under .claude (dot claude). On Windows with WSL, same location within your Ubuntu home directory.

[PAUSE]

[SCREEN: Navigate to settings]

In your terminal, type: cd ~/.claude

[PAUSE]

Then: ls to see what's there.

[PAUSE]

[SCREEN: settings.json file]

You'll see a file called settings.json or similar. This is where Claude Code stores its configuration.

[PAUSE]

[SCREEN: Viewing the file]

Let's look at it. You can ask Claude Code directly: "Show me my Claude Code settings file"

[PAUSE]

Or use a text editor. In terminal: cat settings.json

[PAUSE]

[SCREEN: Default settings content]

The default settings are minimal. Claude Code works without much configuration. But we can add options to enhance the experience.

[PAUSE]

---

## PART 2: KEY SETTINGS OPTIONS

[SCREEN: Available settings categories]

Let me walk you through the most useful settings you can configure.

[PAUSE]

[SCREEN: Model selection setting]

Model selection. You can specify which Claude model to use. The default is usually the latest, which is what you want. But if you needed to use a specific version for compatibility, you could set it here.

[PAUSE]

[SCREEN: API key configuration]

API key location. If you're using an API key directly instead of browser authentication, you configure where that key comes from here. Usually an environment variable reference.

[PAUSE]

[SCREEN: Default behaviors]

Default behaviors. Things like whether to auto-confirm file operations, that's risky but some people prefer it, or whether to show cost estimates by default.

[PAUSE]

[SCREEN: Theme and display]

Theme and display options. Some versions support different visual themes or output formatting preferences.

[PAUSE]

[SCREEN: Editing settings]

To edit settings, you can ask Claude: "Help me configure my Claude Code settings for better performance"

[PAUSE]

Or edit the file directly in a text editor. Make sure to use valid JSON (jay-son) syntax. One wrong comma and the file won't parse.

[PAUSE]

---

## PART 3: THE CLAUDE.md FILE (PROJECT CONTEXT)

[SCREEN: CLAUDE.md introduction]

Now for the real customization power: the CLAUDE.md file. This is where you give Claude persistent context about your projects.

[PAUSE]

[SCREEN: What CLAUDE.md does]

When Claude Code starts in a directory that contains a CLAUDE.md file, it automatically reads that file. The content becomes part of Claude's context, so it knows about your project without you having to explain it every time.

[PAUSE]

[SCREEN: Where to place it]

Place CLAUDE.md in the root of any project directory. When you launch Claude Code in that directory, it loads automatically.

[PAUSE]

[SCREEN: What to include]

What should go in this file? Let me show you a template.

[PAUSE]

[SCREEN: Template section - Project Overview]

Start with a project overview. What is this project? What does it do? Who is it for?

[PAUSE]

[SCREEN: Template section - Tech Stack]

Then your tech stack. What programming languages, frameworks, and tools does this project use? Claude can then give suggestions that fit your stack.

[PAUSE]

[SCREEN: Template section - Coding Standards]

Coding standards. Do you prefer certain naming conventions? Tab or spaces? Specific formatting rules? Document them here.

[PAUSE]

[SCREEN: Template section - Project Structure]

Project structure. Describe how your files and folders are organized. This helps Claude know where to put new files or where to look for existing ones.

[PAUSE]

[SCREEN: Template section - Common Tasks]

Common tasks. What do you frequently ask Claude to help with in this project? List them and any relevant details.

[PAUSE]

[SCREEN: Template section - Important Notes]

Important notes. Any gotchas, warnings, or context that would prevent mistakes. "Never modify the database schema directly" or "The production API key is stored in environment variables, not the code."

[PAUSE]

---

## PART 4: CREATING YOUR CLAUDE.md

[SCREEN: Hands-on creation]

Let's create a CLAUDE.md file together. I'll demonstrate with a hypothetical project.

[PAUSE]

[SCREEN: Example project setup]

Let's say you have a project called "client-portal" that's a Next.js (next-J-S) application for your consulting business.

[PAUSE]

[SCREEN: Navigate to project]

Navigate to your project: cd ~/projects/client-portal

[PAUSE]

[SCREEN: Create the file]

Ask Claude: "Create a CLAUDE.md file for this project. It's a Next.js application for my consulting business client portal. I use TypeScript, Tailwind CSS, and PostgreSQL for the database."

[PAUSE]

[SCREEN: Claude generates the file]

Claude will generate a starting CLAUDE.md based on what you described. Review it, then customize.

[PAUSE]

[SCREEN: Example CLAUDE.md content]

Here's what a good CLAUDE.md might look like:

[PAUSE]

[SCREEN: Show file content]

Heading: Client Portal Project. Description: Next.js app for consulting clients to view project status, invoices, and documents.

Tech stack section: Next.js 14 with App Router, TypeScript, Tailwind CSS, PostgreSQL with Prisma (PRIZ-ma) ORM (O-R-M), hosted on Vercel.

Coding standards: use TypeScript strict mode, functional React components, Tailwind for styling, no inline styles, meaningful variable names.

Project structure: app directory for routes, components directory for reusable UI, lib directory for utilities and database access.

Common tasks: adding new pages, updating Prisma schema, creating API routes, styling components.

Important notes: environment variables in dot env file, never commit secrets, run prisma migrate before testing schema changes.

[PAUSE]

[SCREEN: Commit to version control]

Once you've created your CLAUDE.md, commit it to your git repository. It becomes part of your project documentation.

[PAUSE]

---

## PART 5: GLOBAL VS PROJECT SETTINGS

[SCREEN: Global vs project scope]

There are two levels of configuration: global and project-specific.

[PAUSE]

[SCREEN: Global settings scope]

Global settings apply to Claude Code everywhere. These live in your home directory. Things like API keys, general preferences, and default behaviors.

[PAUSE]

[SCREEN: Project settings scope]

Project settings apply to a specific project. These live in the project directory. CLAUDE.md is the primary example. It only affects Claude Code when you're working in that project.

[PAUSE]

[SCREEN: Override behavior]

When both exist, project settings can override global settings. This lets you have general preferences but customize for specific projects.

[PAUSE]

[SCREEN: Example scenario]

For example, your global setting might prefer tabs for indentation. But one project you inherited uses spaces. The project's CLAUDE.md can specify "use spaces" for that project only.

[PAUSE]

---

## PART 6: ADVANCED CUSTOMIZATIONS

[SCREEN: Advanced options header]

Let's touch on some advanced customization options for power users.

[PAUSE]

[SCREEN: Custom aliases]

Shell aliases. You can create command shortcuts. In your bash or zsh config, add something like: alias cc equals claude. Now you can just type cc instead of claude.

[PAUSE]

[SCREEN: Project-specific startup]

Project-specific startup commands. Some people create scripts that navigate to a project and launch Claude Code with specific options. Automates the workflow.

[PAUSE]

[SCREEN: Integration with editor]

Editor integration. If you use VS Code, there are extensions that integrate with Claude Code. You can launch Claude sessions right from your editor.

[PAUSE]

[SCREEN: Multiple API keys]

Multiple API keys. If you have different Anthropic accounts for work and personal use, you can configure different API keys and switch between them.

[PAUSE]

[SCREEN: Environment-based config]

Environment-based configuration. Using environment variables, you can have different settings for development versus production environments. Useful for teams.

[PAUSE]

---

## PART 7: MAINTAINING YOUR CONFIGURATION

[SCREEN: Configuration maintenance]

Configuration isn't set-and-forget. Here's how to maintain it.

[PAUSE]

[SCREEN: Regular updates]

Update CLAUDE.md as your project evolves. When you add a new feature, update the file. When you change conventions, update the file. Keep it current.

[PAUSE]

[SCREEN: Version control]

Keep CLAUDE.md in version control. It's documentation. When new team members join, they benefit from the context you've built.

[PAUSE]

[SCREEN: Backup global settings]

Backup your global settings periodically. If you get a new computer or need to reinstall, you'll want those preferences preserved.

[PAUSE]

[SCREEN: Share with team]

If you're on a team, share configurations. Standardize on a CLAUDE.md template. Ensure everyone's Claude Code experience is consistent.

[PAUSE]

---

## PRACTICAL EXERCISE

[SCREEN: Exercise instructions]

Here's your exercise.

[PAUSE]

[SCREEN: Step 1]

Step one: Navigate to a project you're working on. If you don't have one, create a practice project with a clear purpose.

[PAUSE]

[SCREEN: Step 2]

Step two: Create a CLAUDE.md file. Include at least: project overview, tech stack, coding standards, and one important note.

[PAUSE]

[SCREEN: Step 3]

Step three: Exit and relaunch Claude Code in that directory. Ask Claude something project-specific and notice how it references your CLAUDE.md context.

[PAUSE]

[SCREEN: Step 4]

Step four: Check your global settings file. Understand what's configured there. Make one change, like adding a preference, and verify it takes effect.

[PAUSE]

[SCREEN: Verification]

You'll know it worked when Claude's responses feel more tailored to your specific project without you having to explain context.

[PAUSE]

---

## CLOSING

[SCREEN: Configuration benefits summary]

Proper configuration transforms Claude Code from a general-purpose tool into your personalized AI assistant. It knows your stack, follows your standards, and understands your projects.

[PAUSE]

[SCREEN: Time investment payoff]

The time you spend on configuration pays off every single session. You'll spend less time explaining context and more time getting actual work done.

[PAUSE]

[SCREEN: Next lesson preview]

Next up, the final lesson of Module 2: Advanced Features. We'll cover Git integration, working across multiple files, and using hooks to automate your workflow even further.

[PAUSE]

Set up your configuration, then I'll see you there.

[PAUSE]

[SCREEN: Fade to "Next: Advanced Features" with Support Forge branding]

---

**END OF SCRIPT 2.4**

*Approximate word count: 1,850 words*
*Estimated runtime: 14:30-15:30*
