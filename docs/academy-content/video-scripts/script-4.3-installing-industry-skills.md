# Script 4.3: Installing Industry Skills

**Module:** 4 - Skills & Plugins (NETWORK Phase)
**Duration:** 15 minutes
**Lesson:** 4.3 - Installing Industry Skills

---

## INTRO (1 min)

[SCREEN: Lesson title "Installing Industry Skills"]

Superpowers is great for general development workflows. [PAUSE] But what if you need something more specific?

Maybe you're doing data analysis and need skills for that. [PAUSE] Or you're a DevOps engineer who needs deployment skills. Or you work with specific frameworks like React or Django.

[SCREEN: Various industry/specialty icons]

The Claude Code community has created skills for tons of use cases. [PAUSE] In this lesson, we'll find these skills, install them from GitHub, and customize them for your needs.

---

## FINDING SKILLS (3 min)

[SCREEN: "Where to Find Skills" header]

Skills are shared in several places. [PAUSE] Let me show you where to look.

### GitHub

[SCREEN: GitHub search interface]

GitHub is the primary source. [PAUSE] Search for "claude code skills" or "claude skills" and you'll find repositories full of them.

Some popular repositories to check:

[SCREEN: Repository examples with names]

- **anthropics/claude-code-skills** - Official collection from Anthropic
- **awesome-claude-skills** - Community curated list
- Individual developer repos with specialized skills

When you find a skill repository, look for a few things:

[SCREEN: What to look for in a repo]

- **SKILL.md files** - The actual skill definitions
- **README** - Explains what skills are included and how to use them
- **Recent updates** - Active maintenance is a good sign
- **Stars and forks** - Community validation

### Claude Code Marketplace

[SCREEN: Marketplace concept]

Some skills are available through a marketplace or registry. [PAUSE] Check Claude Code's documentation for the latest on official skill distribution.

### Community Forums

[SCREEN: Discord/Forum icons]

Anthropic's Discord and various AI developer communities often share skills. [PAUSE] Search for "skill" in these communities and you'll find people sharing their creations.

---

## INSTALLING FROM GITHUB (5 min)

[SCREEN: Step-by-step installation header]

Let's walk through installing a skill from GitHub. [PAUSE]

### Step 1: Find the Repository

[SCREEN: Browser showing a GitHub skill repo]

I'll use an example. Say you found a repository called "document-skills" that has skills for creating presentations, PDFs, and Word documents.

Navigate to the repo. [PAUSE] Find the skill files - usually in a folder structure like:

```
/skills
  /pdf-creation
    SKILL.md
  /presentation
    SKILL.md
  /docx
    SKILL.md
```

### Step 2: Clone or Download

[SCREEN: Git clone command]

You have two options. [PAUSE] Clone the whole repository:

```
git clone https://github.com/example/document-skills.git
```

Or download just the files you need by clicking "Download ZIP" or copying individual files.

### Step 3: Place in Skills Directory

[SCREEN: File system showing skills directory]

Skills go in your Claude Code configuration directory:

Windows:
```
%APPDATA%\Claude\skills\
```

Mac:
```
~/Library/Application Support/Claude/skills/
```

[SCREEN: Moving files into place]

Create a folder for each skill. [PAUSE] The folder name becomes part of the skill's invocation name.

```
skills/
  document-skills/
    pdf-creation/
      SKILL.md
    presentation/
      SKILL.md
```

### Step 4: Restart Claude Code

[SCREEN: Restarting Claude Code]

Exit and restart Claude Code. [PAUSE] The new skills are loaded on startup.

### Step 5: Verify

```
What skills do I have related to documents?
```

[SCREEN: Claude listing the new document skills]

Claude should now show your newly installed skills.

---

## CUSTOMIZING SKILLS (4 min)

[SCREEN: "Customization" header with edit icon]

Here's where it gets powerful. [PAUSE] Skills are just text files. You can modify them.

### Why Customize?

[SCREEN: Customization scenarios]

- The skill is almost what you need, but not quite
- You want to add your company's specific guidelines
- You need to change the output format
- You want to combine elements from multiple skills

### How to Customize

[SCREEN: Opening SKILL.md in editor]

Open the SKILL.md file in your text editor. [PAUSE] Let's look at a typical structure:

```markdown
# PDF Creation Skill

## Description
Create professional PDF documents from content.

## Instructions
When invoked, follow these steps:
1. Ask what type of document the user needs
2. Gather the content
3. Format according to [specific guidelines]
4. Generate the PDF

## Output Format
- Use professional formatting
- Include page numbers
- Add headers with document title
```

[SCREEN: Making edits to the skill]

Say you want to add your company branding. [PAUSE] Edit the instructions:

```markdown
## Instructions
When invoked, follow these steps:
1. Ask what type of document the user needs
2. Gather the content
3. Apply Acme Corp branding:
   - Logo in top right
   - Blue (#0066CC) headers
   - Arial font family
4. Generate the PDF
```

[SCREEN: Saving the modified skill]

Save the file. [PAUSE] No restart needed for skill content changes - Claude reads the file fresh each time.

### Creating Skill Variants

[SCREEN: Copying a skill to create variant]

Sometimes you want the original AND a customized version. [PAUSE] Just copy the folder:

```
skills/
  pdf-creation/
    SKILL.md          (original)
  pdf-creation-branded/
    SKILL.md          (your customized version)
```

Now you have both `/pdf-creation` and `/pdf-creation-branded` available.

---

## ORGANIZING YOUR SKILLS LIBRARY (2 min)

[SCREEN: "Skills Organization" header]

As you collect skills, organization matters. [PAUSE]

### Use Clear Naming

[SCREEN: Good vs bad folder names]

**Good:**
- `code-review-frontend`
- `deploy-aws-amplify`
- `morning-briefing`

**Avoid:**
- `skill1`
- `new-skill`
- `test`

The folder name is what you'll type every day. Make it memorable.

### Group Related Skills

[SCREEN: Organized folder structure]

```
skills/
  development/
    code-review/
    debugging/
    testing/
  deployment/
    aws-deploy/
    vercel-deploy/
  productivity/
    morning-briefing/
    meeting-notes/
```

This keeps things tidy as your collection grows.

### Document Your Customizations

[SCREEN: README in skills folder]

If you customize a skill, add a comment at the top noting what you changed:

```markdown
<!-- Customized 2024-01-15: Added Acme Corp branding requirements -->
# PDF Creation Skill
...
```

Future you will thank present you.

---

## WRAP UP (30 sec)

[SCREEN: Lesson summary]

You now know how to:

- Find skills on GitHub and in community forums
- Install skills to your Claude Code configuration
- Customize skills to match your specific needs
- Organize your growing skills library

[SCREEN: "Next: Creating Your First Custom Skill" with arrow]

But why stop at customizing other people's skills? [PAUSE] In the next lesson, we'll build a skill from scratch. You'll understand exactly how skills work and be able to create whatever workflow you need.

---

**END OF SCRIPT 4.3**
