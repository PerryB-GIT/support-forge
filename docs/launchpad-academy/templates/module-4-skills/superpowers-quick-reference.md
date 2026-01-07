# Superpowers Plugin Quick Reference

The Superpowers plugin provides enhanced skills for Claude Code. This reference covers all available skills and how to use them effectively.

---

## Installation

```bash
# Install Superpowers plugin
claude "/install superpowers"

# Verify installation
claude "/plugins"
```

---

## Available Skills

### Workflow & Planning Skills

#### `/superpowers:brainstorming`
**Use when:** Starting any creative work - features, components, modifications
**Purpose:** Explores requirements and design before implementation

```
/superpowers:brainstorming
I need to add user authentication to my app
```

---

#### `/superpowers:writing-plans`
**Use when:** You have specs/requirements for multi-step tasks
**Purpose:** Creates structured implementation plans

```
/superpowers:writing-plans
Implement the user dashboard feature per the requirements in docs/dashboard-spec.md
```

---

#### `/superpowers:executing-plans`
**Use when:** You have a written plan to execute
**Purpose:** Executes plans with review checkpoints

```
/superpowers:executing-plans
Execute the plan in plans/authentication-implementation.md
```

---

### Code Quality Skills

#### `/superpowers:requesting-code-review`
**Use when:** Completing tasks, implementing features, before merging
**Purpose:** Verifies work meets requirements

```
/superpowers:requesting-code-review
Review the changes in src/auth/ for the login feature
```

---

#### `/superpowers:receiving-code-review`
**Use when:** You've received review feedback
**Purpose:** Helps process and implement review suggestions

```
/superpowers:receiving-code-review
Address the feedback from PR #42 review comments
```

---

#### `/superpowers:test-driven-development`
**Use when:** Implementing any feature or bugfix
**Purpose:** Write tests before implementation code

```
/superpowers:test-driven-development
Implement the password reset feature using TDD
```

---

#### `/superpowers:systematic-debugging`
**Use when:** Encountering bugs, test failures, unexpected behavior
**Purpose:** Methodical diagnosis before proposing fixes

```
/superpowers:systematic-debugging
Users report intermittent login failures - investigate
```

---

#### `/superpowers:verification-before-completion`
**Use when:** About to claim work is complete
**Purpose:** Run verification before making success claims

```
/superpowers:verification-before-completion
Verify the payment integration is complete and working
```

---

### Task Management Skills

#### `/superpowers:dispatching-parallel-agents`
**Use when:** Facing 2+ independent tasks without shared state
**Purpose:** Run multiple tasks in parallel

```
/superpowers:dispatching-parallel-agents
Tasks:
1. Add input validation to signup form
2. Update the footer copyright year
3. Fix broken link on about page
```

---

#### `/superpowers:subagent-driven-development`
**Use when:** Executing plans with independent tasks
**Purpose:** Manages implementation across subtasks

```
/superpowers:subagent-driven-development
Implement the 5 API endpoints defined in the plan
```

---

### Git & Workflow Skills

#### `/superpowers:using-git-worktrees`
**Use when:** Starting feature work that needs isolation
**Purpose:** Creates isolated git worktrees

```
/superpowers:using-git-worktrees
Create a worktree for the payment-integration feature
```

---

#### `/superpowers:finishing-a-development-branch`
**Use when:** Implementation complete, tests pass
**Purpose:** Guides branch completion (merge, PR, cleanup)

```
/superpowers:finishing-a-development-branch
Ready to wrap up the user-auth branch
```

---

### Documentation Skills

#### `/superpowers:writing-skills`
**Use when:** Creating or editing Claude Code skills
**Purpose:** Proper skill structure and verification

```
/superpowers:writing-skills
Create a skill for generating weekly reports
```

---

#### `/superpowers:using-superpowers`
**Use when:** Starting a conversation
**Purpose:** Establishes skill availability

```
/superpowers:using-superpowers
```

---

## Quick Reference Table

| Skill | Trigger | Best For |
|-------|---------|----------|
| `brainstorming` | Starting creative work | New features, designs |
| `writing-plans` | Have specs/requirements | Multi-step implementation |
| `executing-plans` | Have written plan | Systematic execution |
| `requesting-code-review` | Work complete | Quality verification |
| `receiving-code-review` | Got feedback | Processing reviews |
| `test-driven-development` | Any implementation | Quality code |
| `systematic-debugging` | Bugs/failures | Root cause analysis |
| `verification-before-completion` | Claiming done | Final checks |
| `dispatching-parallel-agents` | Multiple independent tasks | Parallel execution |
| `subagent-driven-development` | Plan with subtasks | Implementation |
| `using-git-worktrees` | Need isolation | Feature branches |
| `finishing-a-development-branch` | Ready to merge | Branch completion |
| `writing-skills` | Creating skills | Skill development |

---

## Workflow Examples

### New Feature Development
```
1. /superpowers:brainstorming - Define requirements
2. /superpowers:writing-plans - Create implementation plan
3. /superpowers:using-git-worktrees - Create isolated branch
4. /superpowers:test-driven-development - Implement with tests
5. /superpowers:verification-before-completion - Verify everything works
6. /superpowers:requesting-code-review - Get review
7. /superpowers:finishing-a-development-branch - Merge/PR
```

### Bug Fix Workflow
```
1. /superpowers:systematic-debugging - Find root cause
2. /superpowers:test-driven-development - Write failing test
3. Implement fix
4. /superpowers:verification-before-completion - Verify fix
5. /superpowers:finishing-a-development-branch - Complete
```

### Large Task Execution
```
1. /superpowers:writing-plans - Break down task
2. /superpowers:dispatching-parallel-agents - Parallel work
3. /superpowers:verification-before-completion - Verify all parts
```

---

## Tips for Effective Use

### Do
- Use brainstorming before any significant new work
- Always verify before claiming completion
- Use TDD for any code changes
- Use systematic debugging instead of guessing

### Don't
- Skip planning for complex features
- Claim work complete without verification
- Implement fixes without finding root cause
- Run parallel agents for dependent tasks

---

## Configuration

Superpowers settings can be customized:

```json
// .claude/superpowers-config.json
{
  "defaultReviewLevel": "thorough",
  "requireVerification": true,
  "parallelAgentLimit": 5,
  "planFormat": "markdown"
}
```

---

## Troubleshooting

### Skills not appearing
```bash
# Reinstall
claude "/uninstall superpowers"
claude "/install superpowers"
```

### Skill fails to execute
- Check Claude Code is updated
- Verify plugin is enabled
- Review error message for specifics

---

*AI Launchpad Academy - Support Forge*
