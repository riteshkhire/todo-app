# Todo App — Design Document

**Date:** 2026-03-13
**Purpose:** Learn Git collaboration (branches, pull requests, code review) by building a real app together.

---

## Goal

Build a simple Flask-based Todo app as a hands-on learning exercise. The app itself is the vehicle — the real goal is experiencing a real-world Git collaboration workflow: feature branches, pull requests, code review, and merging.

---

## App Overview

A single-page web app built with Python (Flask) that lets a user manage a list of todos. No database, no login — just a working local app at `localhost:5000`.

**A todo item looks like this:**
```python
{
  "id": 1,
  "text": "Buy groceries",
  "completed": False
}
```

---

## Features

| # | Feature | Branch | Owner |
|---|---------|--------|-------|
| 1 | View all todos | `feature/view-todos` | You |
| 2 | Add a todo | `feature/add-todo` | You |
| 3 | Delete a todo | `feature/delete-todo` | Collaborator (simulated) |
| 4 | Mark todo as complete | `feature/mark-complete` | Collaborator (simulated) |
| 5 | Filter by status (All / Active / Completed) | `feature/filter-todos` | You |

---

## Project Structure

```
todo-app/
├── app.py              # Main Flask application (routes + in-memory data)
├── requirements.txt    # Python dependencies (flask)
├── templates/
│   └── index.html      # Single HTML page (Jinja2 template)
└── static/
    └── style.css       # Basic styling
```

---

## Architecture

- **Backend:** Flask (Python) handles routes and serves HTML
- **Frontend:** Plain HTML with Jinja2 templating — no JavaScript frameworks
- **Data storage:** In-memory Python list (resets when server restarts)
- **Styling:** Simple custom CSS in `static/style.css`

---

## Collaboration Workflow

Every feature follows this exact pattern:

### When you build a feature:
1. `git pull origin main` — get latest code
2. `git checkout -b feature/<name>` — create your branch
3. Write the code (guided step by step)
4. `git add .` — stage changes
5. `git commit -m "descriptive message"` — save a snapshot
6. `git push origin feature/<name>` — send to GitHub
7. Open a Pull Request on GitHub
8. Collaborator reviews and leaves comments
9. You merge the PR
10. `git checkout main && git pull` — sync back to main

### When the collaborator builds a feature:
- You'll see their branch and PR appear
- You review their code and merge their PR
- This teaches you the reviewer side of collaboration

---

## Git Concepts You'll Learn

| Concept | When you'll encounter it |
|---------|--------------------------|
| Repository (repo) | Step 1 — creating it |
| Branch | Every feature |
| Commit | After writing each feature |
| Push | After committing |
| Pull Request (PR) | After pushing |
| Code review | When reviewing collaborator's PR |
| Merge | Closing a PR |
| Pull | Syncing main after a merge |
| Merge conflict | Intentionally triggered once for practice |

---

## Success Criteria

- [ ] Repo created on GitHub with a `main` branch
- [ ] All 5 features built and merged via PRs
- [ ] You have opened at least 3 PRs yourself
- [ ] You have reviewed and merged at least 1 PR from the collaborator
- [ ] You experienced and resolved at least 1 merge conflict
- [ ] The app runs locally and all 5 features work

---

## Out of Scope

- User authentication / login
- Database (SQLite, PostgreSQL, etc.)
- Deployment (Heroku, Railway, etc.)
- JavaScript frameworks (React, Vue, etc.)
- Tests

These can be added as follow-up learning exercises after completing this project.
