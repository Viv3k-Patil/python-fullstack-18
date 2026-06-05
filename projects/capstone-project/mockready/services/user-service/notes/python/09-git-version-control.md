# 📚 Presentation

# Git & GitHub — Introduction, Setup & Hands-On

---

# Slide 1 — Title Slide

# Git & GitHub

### Version Control for Developers

---

# Slide 2 — What Problem Are We Solving?

Before Git existed, developers worked like this:

```
project/
   final_code/
   final_code_new/
   final_code_latest/
   final_code_latest_v2/
   final_code_latest_final/
   final_code_latest_final_REAL/
```

Problems:

❌ Many copies of same project
❌ Don't know which is correct
❌ If code breaks, cannot go back
❌ Team members overwrite each other's code
❌ No history of changes

This created **confusion and chaos**.

---

# Slide 3 — Real Life Example

Imagine writing a **Word document**.

You make versions:

```
resume.doc
resume_new.doc
resume_final.doc
resume_final_latest.doc
resume_final_latest_real.doc
```

After some time:

❓ Which one is correct?
❓ What changed between versions?
❓ If something breaks, how do we restore?

Developers faced the **same problem with code**.

---

# Slide 4 — Solution: Version Control

To solve this problem, we use **Version Control System (VCS)**.

A Version Control System:

✔ tracks code changes
✔ stores history
✔ allows restoring previous versions
✔ supports teamwork

This means:

```
Every change is recorded
```

---

# Slide 5 — What is Git?

**Git** is a Version Control System.

It helps developers:

✔ Track code changes
✔ Maintain history
✔ Work safely with teams
✔ Undo mistakes

Git was created by:

👨‍💻 **Linus Torvalds (creator of Linux)**

---

# Slide 6 — What Git Actually Does

Git keeps **snapshots of your code**.

Example:

```
Version 1 → Initial Code
Version 2 → Added Login
Version 3 → Fixed Bug
Version 4 → Added Payment Feature
```

Git stores:

```
who changed
what changed
when it changed
```

---

# Slide 7 — Why Developers Love Git

Advantages:

✔ Track history
✔ Restore old versions
✔ Work in teams
✔ Experiment safely
✔ Backup code

Git is used by:

🏢 Google
🏢 Amazon
🏢 Netflix
🏢 Microsoft

Basically **every tech company**.

---

# Slide 8 — Local vs Remote Code

There are two places where code lives.

### 1️⃣ Local Repository

Code on your computer.

Example:

```
C:/projects/my-app
```

---

### 2️⃣ Remote Repository

Code stored on internet.

Example:

```
GitHub
GitLab
Bitbucket
```

---

# Slide 9 — What is GitHub?

GitHub is a **cloud platform for Git repositories**.

Think of it as:

```
Google Drive for code
```

GitHub allows:

✔ store code online
✔ collaborate with team
✔ share projects
✔ backup code

Website:

```
https://github.com
```

---

# Slide 10 — Git vs GitHub

| Git                    | GitHub        |
| ---------------------- | ------------- |
| Tool                   | Platform      |
| Version control system | Cloud hosting |
| Works locally          | Works online  |

Simple understanding:

```
Git = Engine
GitHub = Parking Garage
```

---

# Slide 11 — Git Workflow (Important)

Typical Git workflow:

```
Write Code
   ↓
Add changes
   ↓
Commit changes
   ↓
Push to GitHub
```

Flow:

```
Working Directory
        ↓
      Stage
        ↓
      Commit
        ↓
      GitHub
```

---

# Slide 12 — Key Git Concepts

Important terms:

### Repository

Project folder managed by Git.

---

### Commit

Saved version of code.

---

### Branch

Parallel version of project.

---

### Push

Upload code to GitHub.

---

### Pull

Download latest code.

---

# Slide 13 — Git Basic Architecture

```
Working Directory
       ↓
Staging Area
       ↓
Repository
       ↓
GitHub
```

Explanation:

Working Directory → where you edit files
Staging Area → select files for commit
Repository → saved version
GitHub → remote backup

---

# Slide 14 — Installing Git

Download Git:

```
https://git-scm.com
```

Install normally.

Check installation:

```
git --version
```

Example output:

```
git version 2.42
```

---

# Slide 15 — Configure Git (First Time Setup)

Git needs your identity.

Run:

```
git config --global user.name "Your Name"
```

Example:

```
git config --global user.name "Vivek"
```

Now email:

```
git config --global user.email "vivek@email.com"
```

Check configuration:

```
git config --list
```

---

# Slide 16 — Create First Git Project

Create a folder:

```
mkdir git-demo
```

Go inside:

```
cd git-demo
```

Initialize git:

```
git init
```

Output:

```
Initialized empty Git repository
```

Now your project is a **Git repository**.

---

# Slide 17 — What `git init` Does

When we run:

```
git init
```

Git creates a hidden folder:

```
.git
```

Inside `.git` Git stores:

✔ history
✔ commits
✔ branches

This is the **brain of Git**.

---

# Slide 18 — Check File Status

Create file:

```
hello.txt
```

Add some text.

Now run:

```
git status
```

Output:

```
Untracked file: hello.txt
```

Meaning:

Git sees the file but **not tracking yet**.

---

# Slide 19 — Add File to Staging

Command:

```
git add hello.txt
```

Now check status again:

```
git status
```

Output:

```
Changes to be committed
```

File is now in **Staging Area**.

---

# Slide 20 — Commit Changes

Commit means **saving a version**.

Command:

```
git commit -m "first commit"
```

Explanation:

```
-m = message
```

Example message:

```
git commit -m "Added hello file"
```

Now Git has saved a **version of your project**.

---

# Slide 21 — View Commit History

Command:

```
git log
```

Example output:

```
commit a7c3f2
Author: Vivek
Message: first commit
```

This shows:

✔ who committed
✔ when
✔ commit message

---

# Slide 22 — Create GitHub Account

Go to:

```
https://github.com
```

Sign up.

Create new repository:

```
git-demo
```

Choose:

```
Public or Private
```

Do NOT add README yet.

---

# Slide 23 — Connect Local Git to GitHub

Copy repository URL.

Example:

```
https://github.com/vivek/git-demo.git
```

Now run:

```
git remote add origin <repo-url>
```

Example:

```
git remote add origin https://github.com/vivek/git-demo.git
```

---

# Slide 24 — Push Code to GitHub

Command:

```
git push -u origin main
```

Explanation:

```
push → upload code
origin → GitHub repo
main → branch name
```

Now code is uploaded to **GitHub**.

---

# Slide 25 — Full Git Workflow Recap

Daily workflow:

```
Edit code
   ↓
git add .
   ↓
git commit -m "message"
   ↓
git push
```

---

# Slide 26 — Hands-On Exercise

Students must perform:

1️⃣ Install Git
2️⃣ Create folder
3️⃣ Initialize Git
4️⃣ Create file
5️⃣ Add file
6️⃣ Commit file
7️⃣ Create GitHub repo
8️⃣ Push code

Commands summary:

```
git init
git status
git add .
git commit -m "first commit"
git remote add origin URL
git push -u origin main
```

---

# Slide 27 — Mini Challenge

Students task:

Create project:

```
student-profile
```

Inside create:

```
profile.txt
```

Add your:

```
Name
City
Favorite programming language
```

Then push to GitHub.

---

# Slide 28 — Common Beginner Mistakes

Mistake 1:

Forgetting commit message.

---

Mistake 2:

Pushing before committing.

---

Mistake 3:

Wrong repository URL.

---

Mistake 4:

Not configuring Git username/email.

---

# Slide 29 — Key Takeaways

Today we learned:

✔ Problem before Git
✔ Version control concept
✔ Git basics
✔ GitHub introduction
✔ Setup Git
✔ First commit
✔ Push to GitHub

---
