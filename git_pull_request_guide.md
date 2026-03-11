# 🚀 How to Merge Pull Requests & Resolve Conflicts

Follow these steps when a teammate (like Anuska) sends you a Pull Request (PR) and you want to merge it into your `main` branch.

## 1. Prepare your local Environment
Before starting, make sure your own local `main` branch is clean and updated.
```bash
git checkout main
git pull origin main
```

## 2. Fetch the "Incoming" Changes
Find the **Pull Request Number** on GitHub (it's the number next to the title, like #9). Run this command to bring their code into a temporary branch:
```bash
# Replace 'ID' with the PR number (e.g., 9)
git fetch origin pull/ID/head:incoming-changes
```

## 3. Try the Merge
Now, attempt to merge that temporary branch into your `main` branch:
```bash
git merge incoming-changes
```
*If there are **no conflicts**, you are done! If there are **conflicts**, proceed to Step 4.*

## 4. Manually Resolve Conflicts (Keeping Both)
Open any file that Git says has a "Conflict" (like `home.py`). 

1. **Locate the markers**: Look for `<<<<<<< HEAD`, `=======`, and `>>>>>>>`.
2. **Edit**: Delete those three marker lines.
3. **Organize**: Make sure the code from both sections flows correctly (put Task 2 before Task 3, etc.).
4. **Save**: Save the file in your editor.

## 5. Finish and Upload
Tell Git that you have fixed the mess:
```bash
# 1. Mark as resolved
git add home.py

# 2. Finish the merge with a commit
git commit -m "Merge PR and resolve conflicts by keeping both sets of changes"

# 3. Synchronize with GitHub
git push origin main
```

---

### 💡 Pro-Tips
*   **Panic Button**: If you get confused mid-merge and want to start over, type: `git merge --abort`.
*   **Check Status**: Type `git status` anytime to see which files still need fixing.
