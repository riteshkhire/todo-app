# Todo App — Git Collaboration Learning Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a Flask Todo app while learning real-world Git collaboration — branches, commits, pull requests, code review, and merge conflicts.

**Architecture:** Single Flask app with in-memory todo storage, Jinja2 HTML templates, and plain CSS. Each feature is built on its own branch and merged into `main` via a pull request.

**Tech Stack:** Python 3, Flask, HTML/CSS, Git, GitHub

> **Note for Claude:** You are playing TWO roles here:
> - **Teacher/Guide:** Explain every concept and command before the user runs it
> - **Collaborator ("Alex"):** Simulate a second developer who also pushes branches and opens PRs
>
> Always explain WHY before HOW. Never skip explanations.

---

## Phase 0: Setup — Before Any Code

### Task 0.1: Install prerequisites

**Step 1: Check Python is installed**

Run: `python3 --version`
Expected: `Python 3.x.x` (any version 3.8+)

If not installed: go to https://python.org and download it.

**Step 2: Check Git is installed**

Run: `git --version`
Expected: `git version 2.x.x`

If not installed: go to https://git-scm.com and download it.

**Step 3: Check pip is installed**

Run: `pip3 --version`
Expected: `pip 23.x.x ...`

---

### Task 0.2: Configure Git identity (first-time setup)

> **What is this?** Git records WHO made each change. You need to tell Git your name and email once.

**Step 1: Set your name**

```bash
git config --global user.name "Your Name"
```

**Step 2: Set your email** (use the same email as your GitHub account)

```bash
git config --global user.email "you@example.com"
```

**Step 3: Verify**

```bash
git config --list
```

Expected: You'll see your name and email in the output.

---

### Task 0.3: Create a GitHub account and repo

> **What is GitHub?** GitHub is a website that stores your Git repositories online so others can collaborate with you.

**Step 1:** Go to https://github.com and create a free account if you don't have one.

**Step 2:** Click the **"+"** button in the top-right → **"New repository"**

**Step 3:** Fill in:
- Repository name: `todo-app`
- Description: `Learning Git collaboration with a Flask Todo app`
- Visibility: **Public**
- Check **"Add a README file"**

**Step 4:** Click **"Create repository"**

You now have a repo at: `https://github.com/YOUR-USERNAME/todo-app`

---

### Task 0.4: Clone the repo to your computer

> **What is cloning?** Cloning downloads the GitHub repo to your computer so you can work on it locally.

**Step 1: Copy your repo URL from GitHub** (green "Code" button → copy the HTTPS URL)

**Step 2: Navigate to where you want to work**

```bash
cd ~/todo-app
```

Wait — this folder already exists from our design doc. Let's initialize git here instead:

```bash
cd ~/todo-app
git init
git remote add origin https://github.com/YOUR-USERNAME/todo-app.git
git pull origin main
```

> **What just happened?**
> - `git init` — turned this folder into a Git repository
> - `git remote add origin ...` — told Git where the GitHub repo lives ("origin" is just a nickname for the URL)
> - `git pull origin main` — downloaded the README from GitHub

**Step 3: Verify**

```bash
git status
```

Expected: `On branch main, nothing to commit, working tree clean`

---

### Task 0.5: Create the initial project structure

> **What are we doing?** Setting up the skeleton of the app before adding any features. We'll commit this to `main` so both "developers" start from the same foundation.

**Step 1: Create the folder structure**

```bash
mkdir -p templates static
```

**Step 2: Create `requirements.txt`**

Create file `requirements.txt` with this content:
```
flask==3.0.0
```

**Step 3: Create `app.py`** (the skeleton, no features yet)

Create file `app.py` with this content:
```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for todos
todos = []
next_id = 1

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)
```

**Step 4: Create `templates/index.html`** (the skeleton HTML page)

Create file `templates/index.html` with this content:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Todo App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>My Todo List</h1>
    <!-- Features will be added here -->
</body>
</html>
```

**Step 5: Create `static/style.css`**

Create file `static/style.css` with this content:
```css
body {
    font-family: Arial, sans-serif;
    max-width: 600px;
    margin: 40px auto;
    padding: 0 20px;
}

h1 {
    color: #333;
}
```

**Step 6: Install Flask**

```bash
pip3 install flask
```

**Step 7: Test that the skeleton runs**

```bash
python3 app.py
```

Open your browser to `http://localhost:5000` — you should see "My Todo List" as a heading.

Press `Ctrl+C` to stop the server.

**Step 8: Commit everything to main**

> **What is a commit?** A commit is a saved snapshot of your code. Think of it like a checkpoint in a video game.

```bash
git add .
git commit -m "Initial project structure — skeleton Flask app"
git push origin main
```

> **Breaking down `git add .`:**
> - `git add` tells Git "I want to include this in my next snapshot"
> - The `.` means "everything in this folder"
>
> **Breaking down `git commit -m "..."`:**
> - `git commit` creates the snapshot
> - `-m "..."` is the message describing what you did

Go to GitHub and refresh — you'll see your files there.

---

## Phase 1: Feature 1 — View Todos (YOU build this)

### Task 1.1: Create your first feature branch

> **What is a branch?** A branch is like a parallel universe of your code. You make changes there without affecting `main`. When you're happy, you merge it back.
>
> Think of `main` as the "official" version. Branches are your "draft" versions.

**Step 1: Make sure you're on main and up to date**

```bash
git checkout main
git pull origin main
```

> **`git checkout main`** — switches you to the main branch
> **`git pull origin main`** — downloads any new changes from GitHub

**Step 2: Create a new branch for this feature**

```bash
git checkout -b feature/view-todos
```

> **`-b`** means "create a new branch AND switch to it"
> You're now on branch `feature/view-todos`.

**Step 3: Verify you're on the right branch**

```bash
git branch
```

Expected: You'll see a `*` next to `feature/view-todos` — the `*` shows your current branch.

---

### Task 1.2: Implement the View Todos feature

**Step 1: Update `templates/index.html`** to display todos

Replace the `<!-- Features will be added here -->` comment with:
```html
    <ul id="todo-list">
        {% for todo in todos %}
            <li class="{{ 'completed' if todo.completed else '' }}">
                {{ todo.text }}
            </li>
        {% else %}
            <li>No todos yet. Add one below!</li>
        {% endfor %}
    </ul>
```

> **What is `{% for todo in todos %}`?** This is Jinja2 templating — Flask's way of putting Python data into HTML. It loops through every todo and creates an `<li>` for each one.

**Step 2: Add some styling to `static/style.css`**

Add at the bottom of the file:
```css
#todo-list {
    list-style: none;
    padding: 0;
}

#todo-list li {
    padding: 10px;
    margin: 5px 0;
    background: #f5f5f5;
    border-radius: 4px;
}

#todo-list li.completed {
    text-decoration: line-through;
    color: #999;
}
```

**Step 3: Add some test data to `app.py`** so you can see the list working

Temporarily add to `app.py` right after `next_id = 1`:
```python
# Temporary test data — will be removed later
todos = [
    {"id": 1, "text": "Buy groceries", "completed": False},
    {"id": 2, "text": "Read a book", "completed": True},
]
next_id = 3
```

**Step 4: Test it**

```bash
python3 app.py
```

Open `http://localhost:5000` — you should see two todos listed. "Read a book" should be crossed out.

Press `Ctrl+C` to stop.

**Step 5: Remove the temporary test data**

Revert `app.py` to:
```python
todos = []
next_id = 1
```

---

### Task 1.3: Commit and push your feature branch

> **Why commit often?** Each commit is a restore point. If you break something, you can go back. Small commits also make it easier for teammates to understand your changes.

**Step 1: Check what you changed**

```bash
git status
```

You'll see `templates/index.html` and `static/style.css` listed as modified.

**Step 2: See exactly what changed**

```bash
git diff
```

> **`git diff`** shows you the exact lines you added (green `+`) and removed (red `-`). This is useful for reviewing before committing.

Press `q` to exit the diff view.

**Step 3: Stage and commit**

```bash
git add .
git commit -m "feat: add view todos feature with todo list display"
```

**Step 4: Push your branch to GitHub**

```bash
git push origin feature/view-todos
```

> **What just happened?** You pushed your branch to GitHub. It exists there now, but it hasn't been merged into `main` yet. That's what a Pull Request is for.

---

### Task 1.4: Open your first Pull Request

> **What is a Pull Request (PR)?** A PR is a formal request to merge your branch into `main`. It gives teammates a chance to review your code before it becomes "official."

**Step 1:** Go to `https://github.com/YOUR-USERNAME/todo-app`

**Step 2:** You'll see a yellow banner saying "feature/view-todos had recent pushes" — click **"Compare & pull request"**

**Step 3:** Fill in the PR form:
- **Title:** `feat: add view todos feature`
- **Description:**
  ```
  ## What this does
  Adds a todo list to the main page that displays all todos.

  ## How to test
  1. Run `python3 app.py`
  2. Open http://localhost:5000
  3. You should see "No todos yet. Add one below!"
  ```

**Step 4:** Click **"Create pull request"**

> You've opened your first PR! In a real team, your teammates would now review it and leave comments.

---

### Task 1.5: Merge your first Pull Request

> **For now**, since this is a solo exercise, you'll merge your own PR. In a real team, someone else would review and merge it.

**Step 1:** On the PR page, scroll down and click **"Merge pull request"**

**Step 2:** Click **"Confirm merge"**

**Step 3:** Click **"Delete branch"** (good hygiene — keeps the repo clean)

**Step 4: Sync your local machine with the merge**

```bash
git checkout main
git pull origin main
```

> **`git pull`** downloads the merged code from GitHub. Now your local `main` matches GitHub's `main`.

**Step 5: Verify**

```bash
git log --oneline
```

You'll see your commit in the history.

---

## Phase 2: Feature 2 — Add a Todo (YOU build this)

### Task 2.1: Create the branch

```bash
git checkout main
git pull origin main
git checkout -b feature/add-todo
```

---

### Task 2.2: Implement the Add Todo feature

**Step 1: Add a route to `app.py`** for handling the form submission

Add this after the `index()` function:
```python
@app.route('/add', methods=['POST'])
def add_todo():
    global next_id
    text = request.form.get('text', '').strip()
    if text:
        todos.append({
            "id": next_id,
            "text": text,
            "completed": False
        })
        next_id += 1
    return redirect(url_for('index'))
```

> **What is `global next_id`?** Since `next_id` is defined outside the function, we need `global` to modify it inside the function.
>
> **`request.form.get('text')`** reads the value the user typed into the form.
>
> **`redirect(url_for('index'))`** sends the user back to the homepage after adding.

**Step 2: Add the form to `templates/index.html`**

Add this before the `</body>` tag:
```html
    <form action="/add" method="POST">
        <input
            type="text"
            name="text"
            placeholder="What needs to be done?"
            required
        >
        <button type="submit">Add Todo</button>
    </form>
```

**Step 3: Add form styling to `static/style.css`**

```css
form {
    display: flex;
    gap: 10px;
    margin-top: 20px;
}

form input[type="text"] {
    flex: 1;
    padding: 8px;
    font-size: 16px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

button {
    padding: 8px 16px;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

button:hover {
    background: #45a049;
}
```

**Step 4: Test it**

```bash
python3 app.py
```

Open `http://localhost:5000`, type a todo in the box, and click "Add Todo". The todo should appear in the list.

Press `Ctrl+C` to stop.

---

### Task 2.3: Commit, push, open PR, and merge

Follow the same steps as Task 1.3–1.5:

```bash
git add .
git commit -m "feat: add todo form and POST /add route"
git push origin feature/add-todo
```

Then open a PR on GitHub, merge it, and sync:
```bash
git checkout main
git pull origin main
```

---

## Phase 3: Collaborator Adds Two Features ("Alex" simulates PRs)

> **What's happening here:** Your collaborator "Alex" has been working in parallel. They built the Delete and Mark Complete features. You'll now see their branches on GitHub and merge their PRs.
>
> **Claude will simulate this** by creating the branches, writing the code, and creating the PRs on your behalf. Your job is to REVIEW their code and MERGE it.

### Task 3.1: Alex adds the Delete Todo feature

**Claude (as Alex) will:**
1. Create branch `feature/delete-todo`
2. Add the delete route and button
3. Push and open a PR with description

**Code Alex wrote:**

In `app.py`, add:
```python
@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return redirect(url_for('index'))
```

In `templates/index.html`, update the `<li>` inside the loop:
```html
        <li class="{{ 'completed' if todo.completed else '' }}">
            {{ todo.text }}
            <form action="/delete/{{ todo.id }}" method="POST" style="display:inline">
                <button type="submit" class="btn-delete">Delete</button>
            </form>
        </li>
```

In `static/style.css`, add:
```css
.btn-delete {
    background: #e74c3c;
    padding: 4px 8px;
    font-size: 12px;
    margin-left: 10px;
}

.btn-delete:hover {
    background: #c0392b;
}
```

**Your job:** Review Alex's PR on GitHub and merge it.

> **How to review a PR:**
> 1. Go to your repo on GitHub
> 2. Click the "Pull requests" tab
> 3. Click on Alex's PR
> 4. Click "Files changed" tab — review the code
> 5. If it looks good, click "Merge pull request"

After merging:
```bash
git checkout main
git pull origin main
```

---

### Task 3.2: Alex adds the Mark Complete feature

**Code Alex wrote:**

In `app.py`, add:
```python
@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            break
    return redirect(url_for('index'))
```

In `templates/index.html`, update the `<li>` to add a checkbox:
```html
        <li class="{{ 'completed' if todo.completed else '' }}">
            <form action="/toggle/{{ todo.id }}" method="POST" style="display:inline">
                <button type="submit" class="btn-toggle">
                    {{ '✓' if todo.completed else '○' }}
                </button>
            </form>
            {{ todo.text }}
            <form action="/delete/{{ todo.id }}" method="POST" style="display:inline">
                <button type="submit" class="btn-delete">Delete</button>
            </form>
        </li>
```

In `static/style.css`, add:
```css
.btn-toggle {
    background: #3498db;
    padding: 4px 8px;
    font-size: 12px;
}

.btn-toggle:hover {
    background: #2980b9;
}
```

**Your job:** Review and merge Alex's PR.

```bash
git checkout main
git pull origin main
```

---

## Phase 4: Feature 5 — Filter by Status (YOU build this)

### Task 4.1: Create the branch

```bash
git checkout main
git pull origin main
git checkout -b feature/filter-todos
```

---

### Task 4.2: Implement filtering

**Step 1: Update the `index` route in `app.py`** to accept a filter parameter

Replace the existing `index()` function with:
```python
@app.route('/')
def index():
    filter_status = request.args.get('filter', 'all')

    if filter_status == 'active':
        filtered_todos = [t for t in todos if not t['completed']]
    elif filter_status == 'completed':
        filtered_todos = [t for t in todos if t['completed']]
    else:
        filtered_todos = todos

    return render_template('index.html', todos=filtered_todos, current_filter=filter_status)
```

> **`request.args.get('filter', 'all')`** reads the `?filter=active` part of the URL. If nothing is there, it defaults to `'all'`.

**Step 2: Add filter buttons to `templates/index.html`**

Add this between the `<h1>` and the `<ul>`:
```html
    <div class="filters">
        <a href="/?filter=all" class="{{ 'active' if current_filter == 'all' else '' }}">All</a>
        <a href="/?filter=active" class="{{ 'active' if current_filter == 'active' else '' }}">Active</a>
        <a href="/?filter=completed" class="{{ 'active' if current_filter == 'completed' else '' }}">Completed</a>
    </div>
```

**Step 3: Style the filters in `static/style.css`**

```css
.filters {
    display: flex;
    gap: 10px;
    margin: 20px 0;
}

.filters a {
    padding: 6px 12px;
    text-decoration: none;
    color: #333;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.filters a.active {
    background: #333;
    color: white;
}
```

**Step 4: Test all filters**

```bash
python3 app.py
```

1. Add a few todos
2. Mark some as complete
3. Test the All / Active / Completed filter buttons

Press `Ctrl+C` to stop.

---

### Task 4.3: Commit, push, open PR, and merge

```bash
git add .
git commit -m "feat: add filter by status (all/active/completed)"
git push origin feature/filter-todos
```

Open PR on GitHub, merge it, sync:
```bash
git checkout main
git pull origin main
```

---

## Phase 5: Bonus — Experience a Merge Conflict

> **What is a merge conflict?** When two branches change the SAME line of code, Git doesn't know which version to keep. It asks YOU to decide. This happens constantly in real teams.

### Task 5.1: Create a conflict on purpose

**Step 1: Create two branches from main**

```bash
git checkout main
git checkout -b conflict-branch-a
```

**Step 2: Change the `<h1>` title in branch A**

In `templates/index.html`, change:
```html
<h1>My Todo List</h1>
```
to:
```html
<h1>My Awesome Todo List</h1>
```

```bash
git add .
git commit -m "change: update page title to Awesome"
```

**Step 3: Switch to a new branch B from main**

```bash
git checkout main
git checkout -b conflict-branch-b
```

**Step 4: Change the SAME line differently in branch B**

In `templates/index.html`, change:
```html
<h1>My Todo List</h1>
```
to:
```html
<h1>My Super Todo List</h1>
```

```bash
git add .
git commit -m "change: update page title to Super"
```

**Step 5: Merge branch A into main first**

```bash
git checkout main
git merge conflict-branch-a
git push origin main
```

**Step 6: Try to merge branch B — this will CONFLICT**

```bash
git merge conflict-branch-b
```

Expected: Git will say "CONFLICT — Merge conflict in templates/index.html"

**Step 7: Open the conflicting file**

In `templates/index.html`, you'll see:
```html
<<<<<<< HEAD
<h1>My Awesome Todo List</h1>
=======
<h1>My Super Todo List</h1>
>>>>>>> conflict-branch-b
```

> **Reading a conflict:**
> - Everything between `<<<<<<< HEAD` and `=======` is what's in main
> - Everything between `=======` and `>>>>>>>` is what's in your branch
> - You need to pick one (or combine them)

**Step 8: Resolve the conflict**

Delete the conflict markers and pick a final version:
```html
<h1>My Todo List</h1>
```

**Step 9: Finish the merge**

```bash
git add templates/index.html
git commit -m "merge: resolve title conflict, keep original title"
git push origin main
```

You've resolved your first merge conflict!

---

## Phase 6: Final Verification

### Task 6.1: Test the complete app

```bash
git checkout main
git pull origin main
python3 app.py
```

Test all 5 features:
- [ ] Page loads and shows "No todos yet"
- [ ] Can add a new todo
- [ ] Todo appears in the list
- [ ] Can mark a todo as complete (gets strikethrough)
- [ ] Can delete a todo
- [ ] All / Active / Completed filters work correctly

---

### Task 6.2: Review what you learned

Open your GitHub repo and explore:

1. **Commits tab** — click "X commits" to see every commit ever made
2. **Network graph** — go to Insights → Network to see the branch history visually
3. **Pull Requests (closed)** — see all the PRs that were merged

You have now practiced:
- [ ] Creating a GitHub repo
- [ ] Cloning/initializing a local repo
- [ ] Creating feature branches
- [ ] Making commits with descriptive messages
- [ ] Pushing branches to GitHub
- [ ] Opening Pull Requests
- [ ] Reviewing someone else's PR
- [ ] Merging PRs
- [ ] Resolving a merge conflict
- [ ] Keeping your local `main` in sync

---

## Quick Reference — Commands You'll Use Most

```bash
# Start a new feature
git checkout main
git pull origin main
git checkout -b feature/my-feature

# Save your work
git add .
git commit -m "descriptive message"

# Send to GitHub
git push origin feature/my-feature

# After your PR is merged
git checkout main
git pull origin main

# Check your current state
git status
git branch          # which branch am I on?
git log --oneline   # what commits exist?
```
