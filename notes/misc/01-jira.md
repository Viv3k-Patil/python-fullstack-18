# Jira Notes

## What Is Jira?

Jira is a **project management and issue tracking tool** by Atlassian. It's the industry standard for software teams to:
- Track bugs, tasks, and features
- Manage software development workflows
- Run Agile (Scrum/Kanban) projects
- Generate reports and dashboards

***

## Core Concepts

### 1. Issue

An **issue** is the basic unit in Jira — everything is an issue.

| Type | Description | Example |
|---|---|---|
| **Epic** | Large feature spanning multiple sprints | "User Authentication System" |
| **Story** | User-facing feature (completable in one sprint) | "As a user, I can login with email" |
| **Task** | Technical work not directly user-facing | "Setup database connection pool" |
| **Bug** | Defect or error to fix | "Login fails with invalid password" |
| **Sub-task** | Breakdown of a story/task | "Create login API endpoint" (sub-task of login story) |

### 2. Project

A **project** is a collection of issues for a specific product/team.

- **Software projects** → for development teams (Scrum/Kanban boards)
- **Service Management projects** → for IT support
- **Business projects** → for non-technical teams

**Example:** `USER-SERVICE` project contains all issues for the user service microservice.

### 3. Board

A **board** is a visual view of issues.

| Board Type | Use Case |
|---|---|
| **Scrum Board** | Fixed-length sprints (2 weeks), planning, retrospectives |
| **Kanban Board** | Continuous flow, no sprints, limit work in progress |

**Columns** represent workflow statuses (e.g., To Do → In Progress → Done).

### 4. Sprint

A **sprint** is a time-boxed iteration (usually 2 weeks) in Scrum.

- Team selects issues from backlog into sprint
- Work only on sprint issues during sprint
- Sprint ends with review and retrospective

### 5. Workflow

A **workflow** is the path an issue takes from creation to completion.

```
To Do → In Progress → Code Review → QA Testing → Done
```

Each arrow is a **transition** (requires permission to move).

### 6. Fields

Every issue has **fields** storing information:

| Field | Description | Required? |
|---|---|---|
| **Summary** | Short title of issue | Yes |
| **Description** | Detailed explanation | No |
| **Assignee** | Person working on it | No |
| **Reporter** | Person who created it | Yes |
| **Priority** | How important (Low/Medium/High/Highest) | No |
| **Status** | Current Workflow stage | Yes (auto) |
| **Labels** | Tags for filtering | No |
| **Components** | Project sections (e.g., "API", "Frontend") | No |
| **Story Points** | Effort estimate (Fibonacci: 1,2,3,5,8,13) | No |
| **Due Date** | When it should be done | No |
| **Attachment** | Screenshots, logs, files | No |

***

## Issue Lifecycle (Typical Workflow)

```
1. Create Issue (To Do)
   └─ Reporter fills Summary, Description, Type, Priority

2. Assign Issue
   └─ Lead assigns to developer

3. Start Work (In Progress)
   └─ Developer transitions status, adds comment

4. Code Review (In Review)
   └─ Pull request created, reviewer assigned

5. Testing (QA)
   └─ QA team tests, may reopen if bug found

6. Complete (Done)
   └─ Merged to main, deployed, verified
```

***

## Jira Screen Layout

When you open an issue, you see:

```
┌─────────────────────────────────────────────────────┐
│ USER-123  [BUG] Login fails with invalid password   │
├─────────────────────────────────────────────────────┤
│ Assignee: Rahul          Priority: High             │
│ Reporter: Priya          Status: In Progress        │
│ Sprint: Sprint 23        Due: May 25, 2026          │
├─────────────────────────────────────────────────────┤
│ Description:                                        │
│ User cannot login when password is wrong. Shows     │
│ "Internal Server Error" instead of "Invalid creds"  │
│                                                     │
│ Steps to reproduce:                                 │
│ 1. Go to /login                                    │
│ 2. Enter correct email, wrong password             │
│ 3. Click Login                                     │
├─────────────────────────────────────────────────────┤
│ Comments:                                           │
│ Rahul: Started working on this. Root cause: N/A    │
│ Priya: Can you reproduce in staging?               │
├─────────────────────────────────────────────────────┤
│ Activity | Comments | Attachments | History         │
└─────────────────────────────────────────────────────┘
```

***

## JQL (Jira Query Language)

JQL is how you **search and filter** issues powerfully.

### Basic Syntax

```sql
-- All issues in project
project = "USER-SERVICE"

-- Issues assigned to me
assignee = currentUser()

-- High priority bugs
priority = High AND type = Bug

-- Status is In Progress
status = "In Progress"
```

### Common Operators

| Operator | Meaning |
|---|---|
| `=` | Equals |
| `!=` | Not equals |
| `IN` | In a list |
| `NOT IN` | Not in a list |
| `>` `<` | Greater/less than (dates, numbers) |
| `>=` `<=` | Greater/less or equal |
| `AND` | Both conditions true |
| `OR` | Either condition true |
| `ORDER BY` | Sort results |

### Practical Examples

```sql
-- My open issues
assignee = currentUser() AND status != Done

-- High priority bugs in current sprint
type = Bug AND priority = High AND sprint in openSprints()

-- Issues created last week
created >= -7d

-- Unassigned issues in project
assignee is EMPTY AND project = "USER-SERVICE"

-- Issues with specific label
labels = "urgent"

-- Multiple statuses
status IN ("In Progress", "In Review")

-- Ordered by priority
project = "USER-SERVICE" ORDER BY priority DESC, created ASC
```

### Saved Filters

Save frequent JQL queries as **filters** for quick access:
- "My Open Issues"
- "High Priority Bugs This Week"
- "Unassigned Issues in Sprint"

***

## Agile Board Features

### Scrum Board

**Key activities:**

1. **Backlog Grooming**
   - Review and prioritize issues
   - Estimate story points
   - Break down epics into stories

2. **Sprint Planning**
   - Select issues from backlog into sprint
   - Team commits to sprint goal
   - Set sprint duration (usually 2 weeks)

3. **Daily Standup**
   - Update issue status
   - Move issues across board columns

4. **Sprint Review**
   - Demo completed issues
   - Show velocity (points completed)

5. **Retrospective**
   - Discuss what went well/wrong
   - Plan improvements for next sprint

### Kanban Board

**Key features:**

- **Continuous flow** — no sprints
- **WIP Limits** — limit work in progress per column
- **Focus on cycle time** — how long from start to finish

***

## Common Actions (Quick Reference)

| Action | How to Do It |
|---|---|
| **Create Issue** | Click "+" → "Create issue" → fill fields → Create |
| **Quick Create** | Type `c` keyboard shortcut |
| **Assign Issue** | Click "Assignee" → select person → Update |
| **Transition Issue** | Click status dropdown → select new status → Confirm |
| **Add Comment** | Click "Comment" box → type → Add |
| **Log Work** | Click "…More" → "Log Work" → enter time spent |
| **Attach File** | Click "…More" → "Attach" → upload file |
| **Link Issues** | Click "Link" → choose type (blocks, relates to) → select issue |
| **Clone Issue** | Click "…More" → "Clone" → copy fields |
| **Move Issue** | Click "…More" → "Move" → change project/workflow |
| **Search Issues** | Click "Filters" → "Advanced issue search" → use JQL |
| **Export** | Click "…More" → "Export" → Excel/CSV/PDF |

***

## Issue Link Types

Links describe **relationships** between issues:

| Link Type | Meaning |
|---|---|
| **Blocks** | This issue prevents the other from being done |
| **is blocked by** | Opposite of blocks |
| **relates to** | General connection |
| **duplicates** | This issue is a duplicate of the other |
| **is duplicated by** | Opposite of duplicates |
| **causes** | This issue caused the other (often bugs) |
| **is caused by** | Opposite of causes |
| **depends on** | This issue needs the other first |
| **is depended on by** | Opposite of depends on |

**Example:**
```
USER-123 (Login API) blocks USER-124 (Login UI)
```

***

## Permissions and Roles

| Role | Can Do |
|---|---|
| **Browser** | View issues, comment |
| **Developer** | Transition issues, log work, attach files |
| **Project Lead** | Assign issues, edit workflow, manage board |
| **Admin** | Change project settings, permissions, fields |

***

## Best Practices

### For Individuals

1. **Update status daily** — Don't leave issues stuck in "In Progress"
2. **Add comments for context** — "Fixed", "Done" is not enough
3. **Log work time** — If team tracks velocity/capacity
4. **Link related issues** — Helps trace dependencies
5. **Use labels wisely** — `urgent`, `tech-debt`, `breaking-change`

### For Teams

1. **Define DoD** (Definition of Done) — What "Done" means
2. **Set WIP limits** — Don't overload team
3. **Groom backlog regularly** — Keep priorities clear
4. **Use consistent naming** — `USER-123: [BUG] Login fails`
5. **Review stale issues** — Close or re-prioritize old issues

***

## Reports and Dashboards

### Common Reports

| Report | Purpose |
|---|---|
| **Burndown Chart** | Work remaining in sprint |
| **Velocity Chart** | Points completed per sprint |
| **Cumulative Flow** | Work distribution across statuses |
| **Control Chart** | Cycle time per issue |
| **Sprint Health** | Sprint progress and risks |

### Dashboards

Custom dashboards show:
- Assigned issues
- Sprint progress
- Team workload
- Bug trends

***

## Summary Cheat Sheet

| Concept | Key Info |
|---|---|
| **Issue** | Basic unit (bug, story, task, epic) |
| **Project** | Collection of issues (e.g., `USER-SERVICE`) |
| **Board** | Visual view (Scrum or Kanban) |
| **Sprint** | 2-week iteration (Scrum only) |
| **Workflow** | Status flow (To Do → Done) |
| **JQL** | Search language (`project = X AND status = Y`) |
| **Assignee** | Person working on it |
| **Story Points** | Effort estimate (1,2,3,5,8,13) |
| **Links** | Relationships (blocks, relates to) |
| **Comments** | Discussion thread on issue |

**Golden rule:** If it's not in Jira, it doesn't exist. Always create an issue for work.