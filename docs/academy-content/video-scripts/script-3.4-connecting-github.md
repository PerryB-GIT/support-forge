# Script 3.4: Connecting GitHub

**Module:** 3 - MCP Server Deep Dive (UNLOCK Phase)
**Duration:** 15 minutes
**Lesson:** 3.4 - Connecting GitHub via Zapier MCP

---

## INTRO (1 min)

[SCREEN: Lesson title with GitHub logo]

If you're a developer, this lesson's for you. [PAUSE] We're connecting GitHub to Claude through Zapier MCP.

When this is set up, Claude can create issues, manage pull requests, search repositories, and help with your Git workflow - all through conversation.

[SCREEN: Examples of GitHub actions - issue creation, PR management]

No more context-switching between your terminal and the GitHub website. [PAUSE] Just tell Claude what you need.

Let's set it up.

---

## GITHUB AUTHENTICATION OPTIONS (2 min)

[SCREEN: "GitHub Auth Options" with comparison]

Before we dive in, let's talk about authentication. [PAUSE] GitHub has a few ways to connect.

Through Zapier MCP, you'll connect using OAuth. [PAUSE] When you add GitHub actions in Zapier, it walks you through authorizing your GitHub account. This is the easiest approach and what we'll use today.

The alternative is creating a Personal Access Token, or PAT. [PAUSE] This gives you more granular control but requires more setup. Some dedicated GitHub MCP servers use PATs.

[SCREEN: Comparison table - Zapier OAuth vs PAT]

For most users, Zapier's OAuth is perfect. [PAUSE] It's quick to set up and Zapier handles the token management.

If you're working with enterprise GitHub or need specific permission scopes, you might need the PAT approach - but that's an advanced topic.

---

## ADDING GITHUB ACTIONS IN ZAPIER (4 min)

[SCREEN: Zapier interface, searching for GitHub]

Let's add GitHub capabilities. [PAUSE] Go to your Zapier MCP settings and click "Add Actions."

Search for "GitHub" and you'll see a lot of options. [PAUSE] Here are the most useful ones:

[SCREEN: GitHub actions appearing one by one with descriptions]

### Essential Actions

**Find Issue** - Search for issues in your repos. [PAUSE] "Find all open bugs in the frontend repo."

**Create Issue** - Create new issues. [PAUSE] Super useful when you're coding and spot something. Just tell Claude, keep coding.

**Create Comment** - Add comments to issues or PRs. [PAUSE]

**Find Pull Request** - Search for PRs by state, author, or keywords. [PAUSE]

**Create Pull Request** - Open new PRs. [PAUSE] Claude can even write the description based on your commits.

**Find Repository** - Search your repos. [PAUSE]

**Find Branch** - List or find branches. [PAUSE]

### Nice to Have

**Create Branch** - Make new branches. [PAUSE] "Create a feature branch called fix-login-bug."

**Update Issue** - Modify existing issues. [PAUSE] Change labels, assignees, status.

**Update Pull Request** - Modify PR details. [PAUSE]

**Add Labels to Issue** - Organize with labels. [PAUSE]

[SCREEN: OAuth flow for GitHub]

When you add your first GitHub action, Zapier prompts you to connect. [PAUSE] Click "Connect," and you'll be taken to GitHub's authorization page.

Review the permissions Zapier's requesting. [PAUSE] It'll need access to your repositories, issues, and pull requests. Click "Authorize."

[SCREEN: Successful connection message]

Once connected, all your GitHub actions are live. [PAUSE]

---

## TESTING GITHUB INTEGRATION (4 min)

[SCREEN: Claude Code terminal]

Let's verify everything works. [PAUSE] Start Claude Code and try:

```
What GitHub tools do you have access to?
```

[SCREEN: Claude listing GitHub-related tools]

You should see the GitHub actions you added - create_issue, find_pull_request, and so on.

### Finding Issues

Let's search for issues:

```
Find open issues in my [repo-name] repository
```

[SCREEN: Claude calling github_find_issue and returning results]

Replace [repo-name] with an actual repository you have. [PAUSE] Claude searches and returns the issues with their titles, numbers, and status.

### Creating an Issue

Now let's create one:

```
Create an issue in [repo-name] titled "Update documentation for API endpoints" with the body "Need to document the new /users and /products endpoints added in v2.0"
```

[SCREEN: Claude calling github_create_issue]

Claude creates the issue and gives you the URL. [PAUSE] Click it - you'll see the issue in GitHub, created exactly as specified.

### Pull Request Workflow

Here's where it gets powerful:

```
Find any pull requests in [repo-name] that are waiting for review
```

[SCREEN: Claude searching PRs with state filter]

Claude finds PRs that need attention. [PAUSE] You can then ask:

```
Add a comment to PR #[number] saying "Looks good, will review in detail tomorrow"
```

[SCREEN: Claude adding comment to PR]

Comment added. [PAUSE] No browser needed.

---

## PRACTICAL GITHUB WORKFLOWS (3 min)

[SCREEN: "Developer Workflows" header]

Let me share some workflows that'll change how you work with GitHub.

### Bug Discovery During Coding

[SCREEN: Scenario illustration]

You're deep in code, find a bug that's unrelated to what you're working on. [PAUSE] Old workflow: open browser, go to GitHub, create issue, lose focus.

New workflow:

```
Create an issue: the login form doesn't validate email format properly. Label it as a bug, low priority.
```

[SCREEN: Claude creating issue with labels]

Done. [PAUSE] Issue created, labeled, you never left your editor.

### End of Day PR Check

```
Show me all my open pull requests across all repositories and their review status
```

[SCREEN: Claude aggregating PR information]

Claude gives you a complete picture of your pending work.

### Code Review Assistance

You're reviewing a PR and want to leave feedback:

```
Add a comment to PR #42 in the frontend repo: "The error handling looks good but we should add a test for the edge case when the user array is empty"
```

[SCREEN: Claude adding detailed comment]

Your code review comment is posted without breaking your flow.

### Issue Triage

```
Find all issues labeled "needs-triage" in my project and list them with their creation date
```

[SCREEN: Claude finding and organizing issues]

Perfect for sprint planning or weekly reviews.

---

## SECURITY NOTE (1 min)

[SCREEN: Security warning icon]

Quick note on security. [PAUSE] GitHub access is powerful. Claude can create issues, comments, and PRs on your behalf.

A few best practices:

[SCREEN: Best practices list]

**Review before confirming.** [PAUSE] When Claude says it's about to create a PR or issue, read what it's going to post.

**Start with read-only.** [PAUSE] If you're nervous, just add the "Find" actions first. No Create or Update. Get comfortable, then add more.

**Check your Zapier logs.** [PAUSE] Zapier keeps a log of all actions taken. You can audit what Claude did.

**Repository scope.** [PAUSE] When you authorized GitHub, you chose which repos Zapier can access. Be intentional about that choice.

[SCREEN: "Next: Troubleshooting MCP Connections" with arrow]

Alright, GitHub is connected. [PAUSE] You've now got Google services and GitHub accessible through Claude. In the next lesson, we'll cover what to do when things don't work - because troubleshooting MCP is a skill worth having.

---

**END OF SCRIPT 3.4**
