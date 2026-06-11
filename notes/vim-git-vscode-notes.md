Vim Summary Notes

---

1. What Is Vim

* Vim is a terminal-based text editor used for writing and editing files.
* It works using keyboard commands instead of mouse control.
* It is commonly used in Linux systems and Git workflows.

Vim is powerful but works differently because it uses modes instead of normal typing.

---

2. Vim Modes and Their Meaning

Normal Mode (Default Mode)s

* Used for navigation and editing commands such as delete, copy, and paste.
* You cannot directly type text in this mode.

Example:

* Press Esc to enter Normal Mode
* Use h, j, k, l to move the cursor

---

Insert Mode (Typing Mode)

* Used for inserting or editing text.

Example:

* Press i to enter Insert Mode
* Type text such as “Hello World”
* Press Esc to return to Normal Mode

---

Visual Mode (Selection Mode)

* Used to select text for copying, deleting, or modifying.

Example:

* Press v to start selection
* Move cursor to highlight text
* Press y to copy selected text
* Press d to delete selected text

---

Command Mode (Save / Exit Mode)

* Used for saving files, quitting Vim, and executing commands.
* Activated by pressing :

Example:

* Type :wq to save and exit
* Type :q to quit without saving
* Type :q! to force quit without saving changes

---

3. Why Does Vim Open

* Vim opens when a command requires text input but no input is provided.
* The most common case is running git commit without -m.

In such cases, Git opens Vim to allow writing a commit message.

---

4. Basic Vim Commands

Navigation

* h → Move left
* j → Move down
* k → Move up
* l → Move right
* w → Move to next word
* b → Move to previous word
* 0 → Move to start of line
* $ → Move to end of line
* gg → Move to top of file
* G → Move to bottom of file

---

Editing

* x → Delete character
* dd → Delete entire line
* dw → Delete word
* yy → Copy line
* p → Paste

---

Undo and Redo

* u → Undo last action
* Ctrl + r → Redo action

---

Search

* /text → Search for text
* n → Next match
* N → Previous match

---

5. How to Exit Vim

* :wq → Save changes and exit
* :q → Quit without saving
* :q! → Force quit without saving changes

Always press Esc before entering these commands.

---

6. How to Avoid Accidentally Opening Vim

* Use git commit -m "message" instead of git commit
* This directly adds the commit message and prevents Vim from opening

---

7. Why Git Opens Vim

* If git commit is used without -m, Git requires a commit message
* Since no message is provided, Git opens the default editor (usually Vim)

---

8. What Does -m Mean

* -m stands for “message”
* It allows writing the commit message directly in the command line

Example:

* git commit -m "fix login issue"

This skips Vim and commits immediately

---

9. Making VS Code Default Editor for Git

git config --global core.editor "code --wait"

* git config --global core.editor → checks current editor setting

After configuration:

* Git opens VS Code instead of Vim for commit messages
* Works in PowerShell, Bash, CMD, and VS Code terminal

---

10. VS Code Commands

* code . → Opens current folder in VS Code
* code --diff file1 file2 → Opens side-by-side comparison of two files
