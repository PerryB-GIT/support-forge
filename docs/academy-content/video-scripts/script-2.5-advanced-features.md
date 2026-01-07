# Script 2.5: Advanced Features

**Duration:** 15 minutes (~2250-2550 words)
**Lesson:** Module 2, Lesson 5
**Purpose:** Git integration, multi-file operations, hooks and automation

---

## OPENING

[SCREEN: "Advanced Features" title]

You've mastered the basics. Now let's unlock the advanced features that make Claude Code truly powerful for real-world development.

[PAUSE]

[SCREEN: Topics overview]

In this lesson, we're covering Git integration, multi-file operations, and hooks that automate your workflow. These are the features that separate casual users from power users.

[PAUSE]

Let's level up.

[PAUSE]

---

## PART 1: GIT INTEGRATION

[SCREEN: Git logo with Claude Code]

Claude Code has deep integration with Git. If you're managing code, and even if you're just managing configuration files, Git tracking makes everything safer and more organized.

[PAUSE]

[SCREEN: Why Git matters]

Why does this matter? Version control means you can always go back. If Claude makes a change that breaks something, you can revert. If you want to compare what changed, you can diff. It's your safety net.

[PAUSE]

[SCREEN: Initializing Git with Claude]

Let's set up a project with Git. In your terminal, navigate to a project folder and ask Claude: "Initialize a Git repository in this project and create a proper .gitignore file"

[PAUSE]

[SCREEN: Claude sets up Git]

Claude will run git init, create a dot gitignore (dot git-ignore) file with sensible defaults, and maybe even create an initial commit. All through conversation.

[PAUSE]

[SCREEN: Tracking changes]

As you work with Claude, it automatically stages and commits changes with meaningful commit messages. You can see this in action.

[PAUSE]

[SCREEN: Example workflow]

Make a change. Ask Claude: "Create a new file called config.py with database connection settings"

[PAUSE]

Claude creates the file. If you then type: git status

[PAUSE]

You'll see the new file ready to be committed.

[PAUSE]

[SCREEN: Asking for commits]

You can also ask Claude to commit directly: "Commit this change with a meaningful commit message"

[PAUSE]

Claude will write a descriptive commit message based on what changed. No more "fixed stuff" commit messages.

[PAUSE]

[SCREEN: Viewing history]

To see what's happened: "Show me the recent commit history for this project"

[PAUSE]

Claude will run git log and present the history in a readable format.

[PAUSE]

[SCREEN: Reverting changes]

If something goes wrong: "Revert the last commit, it broke the login feature"

[PAUSE]

Claude understands Git operations and can help you undo changes safely.

[PAUSE]

---

## PART 2: BRANCHING AND COLLABORATION

[SCREEN: Branching concept]

Branches let you work on features without affecting your main code. Claude Code handles branching naturally.

[PAUSE]

[SCREEN: Creating a branch]

Ask: "Create a new branch called feature-dashboard for adding a dashboard page"

[PAUSE]

[SCREEN: Claude creates branch]

Claude runs git checkout dash b (git checkout dash B) feature-dashboard, switching you to a new branch.

[PAUSE]

[SCREEN: Working on the branch]

Now all changes happen on this branch. You can ask Claude to build the dashboard feature, make changes, commit them, all isolated from your main code.

[PAUSE]

[SCREEN: Switching branches]

To go back: "Switch to the main branch"

[PAUSE]

Claude runs git checkout main. Your dashboard changes aren't there because they're on the other branch.

[PAUSE]

[SCREEN: Merging branches]

When the feature is ready: "Merge the feature-dashboard branch into main"

[PAUSE]

Claude handles the merge. If there are conflicts, Claude can help you resolve them too.

[PAUSE]

[SCREEN: Working with remotes]

For collaboration, you'll want to push to a remote repository like GitHub: "Push this branch to GitHub"

[PAUSE]

If your remote is set up, Claude pushes the changes. Your team can then see and review them.

[PAUSE]

---

## PART 3: MULTI-FILE OPERATIONS

[SCREEN: Multi-file work header]

Real projects have many files. Claude Code handles complex, multi-file operations efficiently.

[PAUSE]

[SCREEN: File awareness]

Claude can be aware of multiple files simultaneously. Ask: "List all Python files in this project"

[PAUSE]

Claude scans the directory and shows you the files.

[PAUSE]

[SCREEN: Cross-file changes]

Here's where it gets powerful. Ask: "I'm renaming the User class to Customer. Update all files where it's referenced."

[PAUSE]

[SCREEN: Claude refactors]

Claude identifies every file that references User, shows you the changes it wants to make, and with your confirmation, updates them all consistently.

[PAUSE]

[SCREEN: Creating related files]

You can also create multiple related files at once: "Create a full CRUD (crud) API for a Product model. I need the model file, the route handlers, and the service layer."

[PAUSE]

Claude creates multiple files that work together, following consistent patterns.

[PAUSE]

[SCREEN: Dependency awareness]

Claude understands dependencies between files. If file A imports from file B, Claude tracks that relationship. When you change file B, Claude can identify what in file A might be affected.

[PAUSE]

[SCREEN: Project-wide search]

Need to find something? "Find everywhere we use the sendEmail function in this project"

[PAUSE]

Claude searches across all files and shows you the locations.

[PAUSE]

---

## PART 4: CODE REVIEW AND ANALYSIS

[SCREEN: Code review capabilities]

Claude Code isn't just for writing code. It's excellent at reviewing and analyzing code too.

[PAUSE]

[SCREEN: Requesting a review]

Ask: "Review the auth.py file and suggest improvements"

[PAUSE]

[SCREEN: Claude's analysis]

Claude reads the file and provides feedback. Security concerns, performance issues, code style suggestions, potential bugs. It's like having a senior developer review your work.

[PAUSE]

[SCREEN: Specific review focus]

You can focus the review: "Review auth.py specifically for security vulnerabilities"

[PAUSE]

Now Claude's analysis concentrates on security, checking for things like SQL injection (S-Q-L injection), insecure password handling, and authentication bypasses.

[PAUSE]

[SCREEN: Comparing files]

Compare implementations: "Compare how we handle errors in api/users.py versus api/products.py and suggest how to make them consistent"

[PAUSE]

Claude analyzes both files and suggests a unified error handling approach.

[PAUSE]

[SCREEN: Documentation generation]

Generate documentation: "Create documentation for the utils module, including function descriptions and usage examples"

[PAUSE]

Claude reads the code and produces documentation you can include in your project.

[PAUSE]

---

## PART 5: HOOKS AND AUTOMATION

[SCREEN: Hooks concept]

Hooks are automated actions that run at specific times. Claude Code supports hooks that can transform your workflow.

[PAUSE]

[SCREEN: Pre-commit hooks]

Pre-commit hooks run before every commit. You might format code, run linters, or check for security issues automatically.

[PAUSE]

[SCREEN: Setting up hooks]

Ask: "Set up a pre-commit hook that formats Python files using Black before committing"

[PAUSE]

[SCREEN: Claude configures hook]

Claude creates the hook script, sets permissions, and now every commit automatically formats your code.

[PAUSE]

[SCREEN: Custom automation]

You can create custom automation too: "Every time I create a new route file, automatically add it to the routes index"

[PAUSE]

Claude can help build scripts that monitor for specific changes and respond automatically.

[PAUSE]

[SCREEN: Integration with CI/CD]

For teams, this connects to CI/CD (C-I-C-D). Continuous Integration, Continuous Deployment. Your Git hooks can trigger automated testing, deployment pipelines, and more.

[PAUSE]

[SCREEN: Example workflow automation]

Example workflow: you write code, commit it, pre-commit hook formats and lints it, push to GitHub triggers automated tests, passing tests trigger deployment. All automated.

[PAUSE]

---

## PART 6: WORKING WITH EXTERNAL TOOLS

[SCREEN: External tools integration]

Claude Code can invoke external tools and incorporate their output.

[PAUSE]

[SCREEN: Running tests]

Ask: "Run the test suite and show me any failures"

[PAUSE]

Claude runs pytest (pie-test) or your test framework, captures the output, and presents failures clearly.

[PAUSE]

[SCREEN: Analyzing test failures]

Better yet: "Run the tests. If any fail, analyze the failures and suggest fixes."

[PAUSE]

Claude runs tests, sees the failures, reads the relevant code, and proposes solutions.

[PAUSE]

[SCREEN: Linting and formatting]

Integrate linters: "Run ESLint (E-S-lint) on the JavaScript files and fix any issues automatically"

[PAUSE]

Claude runs the linter and applies fixes where it can.

[PAUSE]

[SCREEN: Database operations]

Database operations: "Show me the current database schema from our Prisma models"

[PAUSE]

Claude reads your Prisma files and explains the schema structure.

[PAUSE]

[SCREEN: API testing]

API testing: "Call our local API endpoint /api/users with a GET request and show me the response"

[PAUSE]

Claude can use curl (curl) or similar tools to test your APIs during development.

[PAUSE]

---

## PART 7: BEST PRACTICES FOR ADVANCED USE

[SCREEN: Best practices header]

A few best practices as you use these advanced features.

[PAUSE]

[SCREEN: Commit frequently]

Commit frequently. Small, focused commits are easier to understand and revert if needed. Ask Claude to commit after completing each logical piece of work.

[PAUSE]

[SCREEN: Review before confirming]

For multi-file changes, review carefully. When Claude proposes changes across ten files, read what's changing. One mistake could propagate everywhere.

[PAUSE]

[SCREEN: Use branches for experiments]

Use branches for experiments. "Create a branch called experiment-new-auth" lets you try things without risk. Delete the branch if it doesn't work out.

[PAUSE]

[SCREEN: Keep hooks simple]

Keep hooks simple and fast. If your pre-commit hook takes thirty seconds, you'll start skipping it. Quick checks only.

[PAUSE]

[SCREEN: Document your automation]

Document your automation. If you set up complex hooks or scripts, add comments explaining what they do. Future you will thank present you.

[PAUSE]

---

## MODULE 2 WRAP-UP

[SCREEN: Module 2 complete graphic]

Congratulations. You've completed Module 2: Claude Code Mastery.

[PAUSE]

[SCREEN: Skills acquired list]

You can now: install and configure Claude Code, have productive conversations using effective prompts, customize Claude for your specific projects, work with Git for version control, handle multi-file operations, and set up automation with hooks.

[PAUSE]

[SCREEN: What's next preview]

In the coming modules, we'll apply these skills to build real automation systems. You'll connect Claude Code with n8n, Zapier, and the cloud services you set up in Module 1.

[PAUSE]

[SCREEN: Architect phase complete]

The Architect phase is complete. You've got the skills. Now we move to Unify, where everything connects.

[PAUSE]

---

## CLOSING

[SCREEN: Practice reminder]

Before moving on, practice what you've learned. Pick a project, set up Git, create a CLAUDE.md file, make some changes across multiple files, commit them properly.

[PAUSE]

The more you practice these advanced features, the more natural they'll become.

[PAUSE]

[SCREEN: Community celebration]

Share your progress in the community. Completing Module 2 is a real milestone. You're now ahead of most people who are just chatting with AI casually.

[PAUSE]

[SCREEN: Fade to module completion with Support Forge branding]

Great work. I'll see you in Module 3.

[PAUSE]

---

**END OF SCRIPT 2.5**

*Approximate word count: 1,950 words*
*Estimated runtime: 14:30-15:30*
