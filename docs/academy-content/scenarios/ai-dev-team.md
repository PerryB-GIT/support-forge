# AI Dev Team Assistant

## Overview

**Problem Solved:** Development teams waste significant time on code review coordination, PR management, and issue tracking administration. Senior developers spend hours reviewing straightforward PRs, while complex issues languish without proper documentation. Cross-team visibility is limited, and release notes require manual compilation.

**Solution:** An AI dev team assistant that automates PR labeling and assignment, performs initial code review checks, manages issue lifecycle, syncs data to tracking sheets, and generates release documentation - letting developers focus on writing code.

## Tools Used

| Tool | Purpose |
|------|---------|
| GitHub | Issue tracking, PR management, code review |
| Google Sheets | Sprint tracking, velocity metrics, resource allocation |
| Gmail | Team notifications, stakeholder updates |
| Google Drive | Documentation, architecture docs |
| Gemini | Code analysis, documentation generation |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AI DEV TEAM ASSISTANT WORKFLOW                    │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │          PULL REQUEST MANAGEMENT         │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Trigger: New PR Opened                           │
              └───────────────────────┬─────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ AI Analysis:                                     │
              │ - Determine PR type (feature/bugfix/refactor)    │
              │ - Assess complexity (S/M/L/XL)                   │
              │ - Identify affected areas                        │
              │ - Check for issues linked                        │
              │ - Run initial code checks                        │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ AUTO-LABEL    │           │ AUTO-ASSIGN       │           │ QUALITY CHECK │
│               │           │                   │           │               │
│ Apply labels: │           │ Based on:         │           │ Initial scan: │
│ - Type        │           │ - Code area       │           │ - Tests added?│
│ - Size        │           │ - Expertise       │           │ - Docs updated│
│ - Priority    │           │ - Workload        │           │ - Lint passing│
│ - Area        │           │ - Rotation        │           │ - Breaking?   │
└───────────────┘           └───────────────────┘           └───────────────┘
        │                             │                             │
        └─────────────────────────────┼─────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Add Initial Comment:                             │
              │ - Summary of changes                             │
              │ - Review checklist                               │
              │ - Potential concerns flagged                     │
              │ - Documentation reminders                        │
              └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │           ISSUE MANAGEMENT               │
                    └─────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ NEW ISSUE     │           │ ISSUE UPDATE      │           │ ISSUE STALE   │
│               │           │                   │           │               │
│ - Auto-label  │           │ - Track progress  │           │ - Remind      │
│ - Estimate    │           │ - Sync to sheets  │           │   assignee    │
│ - Assign      │           │ - Link related    │           │ - Escalate    │
│ - Prioritize  │           │                   │           │ - Re-triage   │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │        METRICS & REPORTING               │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Continuous Sync to Sheets:                       │
              │ - Issue status                                   │
              │ - PR progress                                    │
              │ - Sprint velocity                                │
              │ - Cycle time                                     │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ DAILY DIGEST  │           │ SPRINT REPORT     │           │ RELEASE NOTES │
│               │           │                   │           │               │
│ - Open PRs    │           │ - Velocity        │           │ - Auto-compile│
│ - Stale items │           │ - Burndown        │           │ - From merged │
│ - Blockers    │           │ - Completion %    │           │   PRs         │
└───────────────┘           └───────────────────┘           └───────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Dev Tracking Sheets

**Sheet 1: Issue Tracker**
| Column | Description |
|--------|-------------|
| A: Issue # | GitHub issue number |
| B: Title | Issue title |
| C: Type | Bug/Feature/Task/Chore |
| D: Priority | P0/P1/P2/P3 |
| E: Status | Open/In Progress/Review/Done |
| F: Assignee | Developer assigned |
| G: Estimate | Story points or hours |
| H: Sprint | Sprint number |
| I: Labels | Issue labels |
| J: Created | Creation date |
| K: Started | Work start date |
| L: Completed | Completion date |
| M: Cycle Time | Days to complete |
| N: GitHub Link | Direct link |
| O: Related PRs | Linked PRs |

**Sheet 2: PR Tracker**
| Column | Description |
|--------|-------------|
| A: PR # | GitHub PR number |
| B: Title | PR title |
| C: Author | Who opened |
| D: Type | Feature/Bugfix/Refactor/Docs |
| E: Size | S/M/L/XL |
| F: Status | Open/Review/Approved/Merged |
| G: Reviewer(s) | Assigned reviewers |
| H: Created | Open date |
| I: First Review | Time to first review |
| J: Merged | Merge date |
| K: Cycle Time | Days open to merge |
| L: Issues Linked | Related issues |
| M: Comments | Comment count |
| N: Changes | Lines changed |
| O: GitHub Link | Direct link |

**Sheet 3: Sprint Metrics**
| Column | Description |
|--------|-------------|
| A: Sprint | Sprint number |
| B: Start Date | Sprint start |
| C: End Date | Sprint end |
| D: Planned Points | Story points planned |
| E: Completed Points | Story points done |
| F: Velocity | Completion rate |
| G: Issues Completed | Count of issues done |
| H: Bugs Found | Bugs discovered |
| I: Bugs Fixed | Bugs resolved |
| J: PRs Merged | PRs merged this sprint |
| K: Avg PR Cycle | Average PR time |
| L: Notes | Sprint observations |

**Sheet 4: Team Workload**
| Column | Description |
|--------|-------------|
| A: Developer | Team member |
| B: Current Sprint Issues | Assigned issues |
| C: Total Points | Points assigned |
| D: Open PRs | PRs awaiting merge |
| E: Reviews Pending | Reviews assigned |
| F: Availability | Capacity notes |
| G: Code Areas | Expertise areas |

### Step 2: Configure PR Automation

**Workflow: PR Triage**
```yaml
Trigger: GitHub - New PR Opened
  │
  ├─ Node 1: Analyze PR Content
  │    - Get PR title, body, files changed
  │    - Parse linked issues
  │    - Calculate size (lines changed)
  │
  ├─ Node 2: Determine PR Type
  │    - Parse title/body for keywords
  │    - Check file paths
  │    - Infer: feature/bugfix/refactor/docs/chore
  │
  ├─ Node 3: Assess Complexity
  │    - S: < 50 lines, single file area
  │    - M: 50-200 lines, limited scope
  │    - L: 200-500 lines, multiple areas
  │    - XL: 500+ lines, significant change
  │
  ├─ Node 4: Identify Code Areas
  │    - Parse changed file paths
  │    - Map to team ownership
  │    - Check for cross-team changes
  │
  ├─ Node 5: Apply Labels
  │    - Type: feature/bugfix/refactor/docs
  │    - Size: size/S, size/M, size/L, size/XL
  │    - Area: frontend/backend/infra/etc.
  │
  ├─ Node 6: Assign Reviewer
  │    - Match code area to expert
  │    - Check current workload
  │    - Consider rotation for fairness
  │
  ├─ Node 7: Initial Analysis Comment
  │    - Gemini: Generate PR summary
  │    - Add review checklist
  │    - Flag potential concerns
  │
  └─ Node 8: Update Sheets
       - Add to PR Tracker
       - Update Team Workload
```

**Workflow: PR Quality Check**
```yaml
Trigger: GitHub - PR Updated (commits pushed)
  │
  ├─ Node 1: Run Quality Checks
  │    - Check for test files
  │    - Check for documentation updates
  │    - Verify PR description quality
  │    - Check for breaking change indicators
  │
  ├─ Node 2: If Issues Found
  │    - Add comment with checklist
  │    - Apply "needs-work" label
  │
  └─ Node 3: If All Pass
       - Apply "ready-for-review" label
       - Notify assigned reviewers
```

### Step 3: Issue Management Automation

**Workflow: Issue Triage**
```yaml
Trigger: GitHub - New Issue Created
  │
  ├─ Node 1: Parse Issue Content
  │    - Extract title, body, labels
  │    - Identify type from template
  │
  ├─ Node 2: Auto-Categorize
  │    - Gemini: Analyze issue description
  │    - Determine: Bug/Feature/Task
  │    - Suggest priority
  │    - Identify affected area
  │
  ├─ Node 3: Estimate Complexity
  │    - Based on description
  │    - Historical similar issues
  │    - Suggest story points
  │
  ├─ Node 4: Apply Labels
  │    - Type label
  │    - Priority label
  │    - Area label
  │
  ├─ Node 5: Add to Sprint
  │    - If priority P0/P1: Add to current sprint
  │    - Otherwise: Add to backlog
  │
  └─ Node 6: Update Sheets
       - Add to Issue Tracker
       - Update backlog
```

**Workflow: Stale Issue Management**
```yaml
Trigger: Daily 9:00 AM
  │
  ├─ Node 1: Find Stale Issues
  │    - In Progress > 7 days without update
  │    - Open > 30 days without assignment
  │    - Blocked > 3 days
  │
  ├─ Node 2: For Each Stale Issue
  │    │
  │    ├─ If In Progress Too Long
  │    │    - Comment reminder
  │    │    - Ask for status update
  │    │
  │    └─ If Unassigned Too Long
  │         - Tag tech lead
  │         - Request triage decision
  │
  └─ Node 3: Alert Team
       - Daily digest with stale items
       - Escalation for critical items
```

### Step 4: Metrics and Reporting

**Workflow: Continuous Sync**
```yaml
Trigger: GitHub - Issue/PR Status Change
  │
  ├─ Node 1: Parse Event
  │    - Get issue/PR number
  │    - Get new status
  │    - Get timestamp
  │
  ├─ Node 2: Update Sheets
  │    - Find corresponding row
  │    - Update status column
  │    - Calculate cycle time if closed
  │
  └─ Node 3: Trigger Calculations
       - Update sprint burndown
       - Recalculate velocity
       - Update team workload
```

**Workflow: Release Notes Generation**
```yaml
Trigger: Manual OR Tag Created
  │
  ├─ Node 1: Get Merged PRs Since Last Release
  │    - Query GitHub for merged PRs
  │    - Filter by date range
  │
  ├─ Node 2: Categorize Changes
  │    - Group by type (feature/fix/improvement)
  │    - Extract linked issues
  │    - Get PR descriptions
  │
  ├─ Node 3: Gemini - Generate Notes
  │    - Create user-friendly descriptions
  │    - Highlight breaking changes
  │    - Credit contributors
  │
  ├─ Node 4: Format and Save
  │    - Create markdown document
  │    - Save to Drive/repo
  │
  └─ Node 5: Notify Team
       - Share release notes draft
       - Request review before publish
```

## Example Prompts/Commands

### PR Analysis
```
Analyze this pull request for review preparation:

PR Title: [TITLE]
PR Description: [DESCRIPTION]

Files Changed:
[LIST_OF_FILES_WITH_ADDITIONS_DELETIONS]

Linked Issues: [ISSUE_NUMBERS]

Provide:
1. Summary of changes (2-3 sentences, non-technical)
2. PR Type (feature/bugfix/refactor/docs/chore)
3. Size Assessment (S/M/L/XL) with justification
4. Affected Areas (frontend/backend/infra/api/etc.)
5. Review Focus Areas (what reviewers should pay attention to)
6. Potential Risks or Concerns
7. Suggested Reviewers (based on code areas)
8. Review Checklist:
   - [ ] Tests added/updated
   - [ ] Documentation updated
   - [ ] No console.logs or debug code
   - [ ] Error handling present
   - [ ] Edge cases considered

Format as a GitHub comment (use markdown).
```

### Issue Triage
```
Triage this GitHub issue:

Title: [ISSUE_TITLE]
Body: [ISSUE_BODY]
Reporter: [REPORTER_USERNAME]
Labels Already Applied: [EXISTING_LABELS]

Determine:
1. Issue Type:
   - Bug (something broken)
   - Feature (new capability)
   - Task (maintenance/chore)
   - Improvement (enhancement to existing)

2. Priority:
   - P0 (Critical - blocking production)
   - P1 (High - significant impact, fix soon)
   - P2 (Medium - important but not urgent)
   - P3 (Low - nice to have)

3. Complexity/Estimate:
   - XS (< 2 hours)
   - S (2-4 hours)
   - M (1-2 days)
   - L (3-5 days)
   - XL (> 1 week)

4. Affected Area:
   - Frontend
   - Backend
   - Infrastructure
   - API
   - Database
   - Other

5. Additional Information Needed:
   - What questions should we ask?
   - What reproduction steps are missing?

6. Related Issues (if any patterns detected)

Format as labels to apply and a triage comment.
```

### Release Notes Generation
```
Generate release notes from these merged PRs:

Version: [VERSION]
Release Date: [DATE]
Previous Version: [PREV_VERSION]

Merged PRs:
[LIST_OF_PR_TITLES_AND_DESCRIPTIONS]

Create release notes with:

1. Highlights (2-3 most important changes)

2. New Features
   - User-facing feature descriptions
   - How to use them

3. Improvements
   - Enhancements to existing features
   - Performance improvements

4. Bug Fixes
   - What was fixed
   - Impact of the fix

5. Breaking Changes (if any)
   - What changed
   - Migration steps

6. Contributors
   - List of people who contributed

7. Technical Notes (optional)
   - API changes
   - Deprecations

Write for end users, not developers. Be concise but informative.
Use emojis sparingly for category headers.
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| PR opened | Analyze, label, assign, comment | Real-time |
| PR updated | Re-check quality, update sheets | Real-time |
| PR merged | Update issue status, calculate metrics | Real-time |
| PR stale (5 days) | Remind author and reviewers | Daily check |
| Issue created | Triage, label, estimate | Real-time |
| Issue assigned | Update sheets, notify | Real-time |
| Issue stale (7 days) | Reminder comment | Daily check |
| Issue closed | Calculate cycle time, update metrics | Real-time |
| Daily 9:00 AM | Team digest (open work, blockers) | Daily |
| Sprint end | Sprint report generation | Bi-weekly |
| Tag created | Release notes generation | On demand |

## Expected Outcomes

### Quantitative Results
- **PR review time:** 30% faster from better preparation
- **Issue triage time:** 80% reduction with auto-categorization
- **Stale item reduction:** 50% fewer stuck items
- **Documentation coverage:** 100% of PRs have summaries
- **Metrics accuracy:** Real-time vs. manual weekly updates

### Qualitative Benefits
- Consistent PR standards
- Fair reviewer distribution
- Better visibility into work status
- Reduced context-switching for devs
- Automated release documentation

## ROI Estimate

### Assumptions
- Developer salary: $120,000/year ($60/hour)
- Team size: 6 developers
- Time on PR/issue admin: 3 hours/week per dev
- Post-automation time: 1 hour/week per dev

### Calculation
| Metric | Value |
|--------|-------|
| Weekly time saved per dev | 2 hours |
| Team weekly savings | 12 hours |
| Monthly savings | 48 hours |
| Monthly value | $2,880 |
| Annual value | $34,560 |
| Tool costs (estimated) | $50/month |
| **Net annual ROI** | **$33,960** |

### Additional Value
- Faster PR reviews = faster feature delivery
- Better documentation = easier onboarding
- Data-driven planning = better estimates

## Advanced Extensions

1. **Code Review AI:** Automated code suggestions
2. **Dependency Updates:** Auto-PRs for dependency bumps
3. **Test Coverage Checks:** Block merges below threshold
4. **Cross-Repo Tracking:** Multi-repository dashboards
5. **On-Call Integration:** Auto-assign urgent issues

## Sample Label Schema

```yaml
Type Labels:
  - type/bug
  - type/feature
  - type/refactor
  - type/docs
  - type/chore
  - type/test

Priority Labels:
  - priority/critical
  - priority/high
  - priority/medium
  - priority/low

Size Labels:
  - size/XS
  - size/S
  - size/M
  - size/L
  - size/XL

Status Labels:
  - status/in-progress
  - status/needs-review
  - status/blocked
  - status/ready-to-merge

Area Labels:
  - area/frontend
  - area/backend
  - area/api
  - area/infra
  - area/database
  - area/ci-cd

Quality Labels:
  - needs/tests
  - needs/docs
  - needs/design-review
  - breaking-change
```
