# GitHub MCP Integration Guide

> **Support Forge AI Launchpad Academy**
> Complete GitHub workflow automation through Claude

---

## Overview

GitHub is the backbone of modern software development. With Zapier MCP, Claude can manage your entire development workflow - from creating issues and branches to opening pull requests and conducting code reviews.

**What you'll learn:**
- Manage issues and project tracking
- Create and manage branches
- Open and review pull requests
- Automate repository workflows

---

## Prerequisites

- [ ] Zapier MCP configured ([see setup guide](./zapier-mcp-setup.md))
- [ ] GitHub account with repository access
- [ ] GitHub connected in Zapier with appropriate scopes

### Required GitHub Scopes

When connecting GitHub in Zapier, ensure these scopes are granted:
- `repo` - Full repository access
- `read:org` - Organization membership
- `gist` - Gist access
- `user:read` - User profile access

---

## Available Tools

### Repository & Branch Management

| Tool | Description |
|------|-------------|
| `github_find_repository` | Find a specific repository |
| `github_find_branch` | Find branches or list all |
| `github_create_branch` | Create new branch |
| `github_delete_branch` | Delete a branch |

### Issues

| Tool | Description |
|------|-------------|
| `github_find_issue` | Search for issues |
| `github_create_issue` | Create new issue |
| `github_update_issue` | Update existing issue |
| `github_add_labels_to_issue` | Add labels |
| `github_create_comment` | Comment on issue/PR |

### Pull Requests

| Tool | Description |
|------|-------------|
| `github_find_pull_request` | Search for PRs |
| `github_create_pull_request` | Create new PR |
| `github_update_pull_request` | Update PR |
| `github_submit_review` | Submit PR review |

### Other

| Tool | Description |
|------|-------------|
| `github_create_or_update_file` | Create/update files |
| `github_create_gist` | Create gists |
| `github_find_user` | Find GitHub user |
| `github_find_organization` | Find organization |

---

## Repository & Branch Operations

### Example: Find a Repository

```
Find the repository "my-app" owned by "my-org"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_find_repository",
  "parameters": {
    "instructions": "Find the my-app repository owned by my-org",
    "owner": "my-org",
    "repo": "my-app"
  }
}
```

### Example: List All Branches

```
Show me all branches in the support-forge/docs repository
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_find_branch",
  "parameters": {
    "instructions": "List all branches in support-forge/docs",
    "repo": "support-forge/docs"
  }
}
```

### Example: Create a Feature Branch

```
Create a new branch called "feature/user-authentication" from main in
the my-org/my-app repository
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_create_branch",
  "parameters": {
    "instructions": "Create feature/user-authentication branch from main",
    "repo": "my-org/my-app",
    "branch_name": "feature/user-authentication",
    "ref": "main"
  }
}
```

### Example: Delete a Branch

```
Delete the branch "feature/old-feature" from my-org/my-app
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_delete_branch",
  "parameters": {
    "instructions": "Delete the feature/old-feature branch",
    "repo": "my-org/my-app",
    "branch_name": "feature/old-feature"
  }
}
```

---

## Issue Management

### Example: Find Open Issues

```
Find all open issues in my-org/my-app labeled as "bug"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_find_issue",
  "parameters": {
    "instructions": "Find open issues with bug label",
    "repo": "my-org/my-app",
    "state": "open",
    "search_key": "label",
    "search_value": "bug"
  }
}
```

### Example: Find Issue by Title

```
Find the issue titled "Fix login timeout" in my-org/my-app
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_find_issue",
  "parameters": {
    "instructions": "Find issue with title 'Fix login timeout'",
    "repo": "my-org/my-app",
    "search_key": "title",
    "search_value": "Fix login timeout"
  }
}
```

### Example: Create an Issue

```
Create a new issue in my-org/my-app:
Title: "Add dark mode support"
Description: "Users have requested a dark mode option. This should include:
- Toggle in settings
- Persist preference in localStorage
- System preference detection"
Labels: enhancement, frontend
Assign to: johndoe
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_create_issue",
  "parameters": {
    "instructions": "Create issue for dark mode support with specified details",
    "repo": "my-org/my-app",
    "title": "Add dark mode support",
    "body": "Users have requested a dark mode option. This should include:\n\n- Toggle in settings\n- Persist preference in localStorage\n- System preference detection",
    "labels": "enhancement, frontend",
    "assignee": "johndoe"
  }
}
```

### Example: Update an Issue

```
Update issue #42 in my-org/my-app:
- Add label "priority-high"
- Assign to janedoe
- Add to milestone "v2.0"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_update_issue",
  "parameters": {
    "instructions": "Update issue 42 with new labels, assignee, and milestone",
    "repo": "my-org/my-app",
    "issue_id": "42",
    "labels": "enhancement, frontend, priority-high",
    "assignee": "janedoe",
    "milestone": "v2.0"
  }
}
```

### Example: Add Labels to Issue

```
Add the labels "needs-review" and "documentation" to issue #15
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_add_labels_to_issue",
  "parameters": {
    "instructions": "Add needs-review and documentation labels to issue 15",
    "repo": "my-org/my-app",
    "issue_number": "15",
    "labels": "needs-review, documentation"
  }
}
```

### Example: Comment on an Issue

```
Add a comment to issue #42 saying "I've started working on this.
Expected completion by Friday."
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_create_comment",
  "parameters": {
    "instructions": "Add status update comment to issue 42",
    "repo": "my-org/my-app",
    "issue_id": "42",
    "body": "I've started working on this. Expected completion by Friday."
  }
}
```

---

## Pull Request Operations

### Example: Find Open PRs

```
Find all open pull requests in my-org/my-app
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_find_pull_request",
  "parameters": {
    "instructions": "Find all open pull requests",
    "repo": "my-org/my-app",
    "state": "open"
  }
}
```

### Example: Find PR by Author

```
Find pull requests created by johndoe in my-org/my-app
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_find_pull_request",
  "parameters": {
    "instructions": "Find PRs by author johndoe",
    "repo": "my-org/my-app",
    "search_key": "author",
    "search_value": "johndoe"
  }
}
```

### Example: Create a Pull Request

```
Create a pull request in my-org/my-app:
- From: feature/user-authentication
- To: main
- Title: "Add user authentication system"
- Description: Include what was implemented and testing notes
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_create_pull_request",
  "parameters": {
    "instructions": "Create PR for user authentication feature",
    "repo": "my-org/my-app",
    "head": "feature/user-authentication",
    "base": "main",
    "title": "Add user authentication system",
    "body": "## Summary\n\nThis PR implements user authentication including:\n\n- Login/logout functionality\n- JWT token management\n- Password reset flow\n\n## Testing\n\n- Unit tests added for auth service\n- Manual testing completed\n- E2E tests passing\n\n## Checklist\n\n- [x] Code reviewed\n- [x] Tests passing\n- [x] Documentation updated"
  }
}
```

### Example: Create and Instantly Merge PR

```
Create a pull request from hotfix/critical-fix to main and merge it immediately
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_create_pull_request",
  "parameters": {
    "instructions": "Create PR and instantly merge",
    "repo": "my-org/my-app",
    "head": "hotfix/critical-fix",
    "base": "main",
    "title": "Hotfix: Critical security patch",
    "body": "Emergency fix for critical security vulnerability.",
    "instant_merge": "true"
  }
}
```

### Example: Update a Pull Request

```
Update PR #28 to change the target branch to "develop" instead of "main"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_update_pull_request",
  "parameters": {
    "instructions": "Change PR 28 target branch to develop",
    "repo": "my-org/my-app",
    "pull_number": "28",
    "base": "develop"
  }
}
```

### Example: Submit a PR Review

```
Approve PR #28 in my-org/my-app with the comment "LGTM! Great work on
the refactoring."
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_submit_review",
  "parameters": {
    "instructions": "Approve PR 28 with positive comment",
    "repo": "my-org/my-app",
    "pull_number": "28",
    "event": "APPROVE",
    "body": "LGTM! Great work on the refactoring."
  }
}
```

### Example: Request Changes

```
Request changes on PR #28 with the comment "Please add unit tests for
the new validation logic."
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_submit_review",
  "parameters": {
    "instructions": "Request changes on PR 28",
    "repo": "my-org/my-app",
    "pull_number": "28",
    "event": "REQUEST_CHANGES",
    "body": "Please add unit tests for the new validation logic."
  }
}
```

---

## File & Gist Operations

### Example: Create a File

```
Create a new file CONTRIBUTING.md in the root of my-org/my-app on main branch
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_create_or_update_file",
  "parameters": {
    "instructions": "Create CONTRIBUTING.md file",
    "repo": "my-org/my-app",
    "path": "CONTRIBUTING.md",
    "branch": "main",
    "message": "docs: add contributing guidelines",
    "content": "# Contributing\n\nThank you for your interest in contributing!\n\n## How to Contribute\n\n1. Fork the repository\n2. Create a feature branch\n3. Make your changes\n4. Submit a pull request"
  }
}
```

### Example: Update a File

```
Update the version number in package.json from 1.0.0 to 1.1.0
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_create_or_update_file",
  "parameters": {
    "instructions": "Update version in package.json to 1.1.0",
    "repo": "my-org/my-app",
    "path": "package.json",
    "branch": "main",
    "message": "chore: bump version to 1.1.0",
    "sha": "[current_file_sha]"
  }
}
```

### Example: Create a Public Gist

```
Create a public gist called "useful-bash-aliases.sh" with common bash aliases
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_create_gist",
  "parameters": {
    "instructions": "Create public gist with bash aliases",
    "filename": "useful-bash-aliases.sh",
    "description": "Common bash aliases for productivity",
    "content": "# Git aliases\nalias gs='git status'\nalias gc='git commit'\nalias gp='git push'\n\n# Navigation\nalias ..='cd ..'\nalias ...='cd ../..'\n\n# List\nalias ll='ls -la'",
    "public": "true"
  }
}
```

---

## User & Organization Operations

### Example: Find a User

```
Find GitHub user "octocat"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_find_user",
  "parameters": {
    "instructions": "Find GitHub user octocat",
    "desired_username": "octocat"
  }
}
```

### Example: Find an Organization

```
Find the GitHub organization "microsoft"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_find_organization",
  "parameters": {
    "instructions": "Find microsoft organization",
    "name": "microsoft"
  }
}
```

### Example: Check Organization Membership

```
Check if user "johndoe" is a member of organization "my-org"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__github_check_organization_membership",
  "parameters": {
    "instructions": "Check if johndoe is member of my-org",
    "org": "my-org",
    "username": "johndoe"
  }
}
```

---

## Common Errors and Fixes

### Error: "Resource not accessible by integration"

**Cause:** Insufficient permissions for the repository

**Fix:**
1. Verify the connected GitHub account has access
2. For organization repos, check if SSO is required
3. Reconnect GitHub in Zapier with appropriate scopes

### Error: "Reference already exists"

**Cause:** Trying to create a branch that already exists

**Fix:**
1. Use `github_find_branch` first to check
2. Delete the existing branch if needed
3. Use a different branch name

### Error: "Merge conflict"

**Cause:** Automatic merge not possible

**Fix:**
1. Cannot be resolved through MCP
2. Resolve conflicts locally
3. Use `instant_merge: false` and handle manually

### Error: "Base branch was modified"

**Cause:** Target branch changed during PR creation

**Fix:**
1. Retry the operation
2. Sync your feature branch with base first
3. Use specific commit SHA for `ref`

### Error: "Validation Failed"

**Cause:** Invalid field values (labels, assignees, milestones)

**Fix:**
- Verify labels exist in the repository
- Verify assignees have repository access
- Verify milestone exists and is open

---

## Pro Tips

### 1. Use Full Repository References

Always use `owner/repo` format for reliability:
```
my-org/my-app (correct)
my-app (may be ambiguous)
```

### 2. Conventional Commit Messages

When creating files or commits, follow conventional commits:
```
feat: add user authentication
fix: resolve login timeout issue
docs: update API documentation
chore: bump dependencies
```

### 3. PR Templates in Descriptions

Include structured information in PR bodies:
```markdown
## Summary
Brief description of changes

## Changes Made
- Change 1
- Change 2

## Testing
How it was tested

## Screenshots
If applicable
```

### 4. Issue Templates

Use consistent issue formats:
```markdown
## Description
What's the issue?

## Steps to Reproduce
1. Step 1
2. Step 2

## Expected Behavior
What should happen

## Actual Behavior
What actually happens
```

### 5. Label Strategy

Use consistent label prefixes:
- `type/bug`, `type/feature`, `type/docs`
- `priority/high`, `priority/medium`, `priority/low`
- `status/in-progress`, `status/review`, `status/blocked`

### 6. Branch Naming Convention

Use descriptive branch names:
```
feature/user-authentication
bugfix/login-timeout
hotfix/security-patch
docs/api-documentation
```

---

## Workflow Examples

### Bug Report to Fix Workflow

```
1. Create issue with bug details and labels
2. Create feature branch for the fix
3. After fix, create pull request
4. Submit review when ready
5. Update issue to closed after merge
```

### Feature Development Workflow

```
1. Find or create issue for feature
2. Create feature branch from main
3. Develop feature (outside MCP)
4. Create PR with description
5. Request review
6. Merge after approval
7. Delete feature branch
8. Close related issue
```

### Release Workflow

```
1. Find all PRs merged since last release
2. Create release branch from main
3. Update version file
4. Create release PR
5. Merge to main
6. Create gist with release notes
```

---

## Next Steps

- [Google Workspace MCP Guide](./google-workspace-mcp.md) - Sheets, Calendar, Drive, Gmail
- [Design Tools MCP Guide](./design-tools-mcp.md) - Canva and Figma
- [Code Execution MCP Guide](./code-execution-mcp.md) - Run Python/JS through Claude

---

*Support Forge AI Launchpad Academy - Building the Future of AI Integration*
