## **Quick Command to List Merge Commits**

This shows only merge commits in your `main` branch:

```bash
git log --merges --oneline
```

### Example output:

```
f1a2b3c (HEAD -> main) Merge pull request #42 from feature/quiz-logic
3c4d5e6 Merge branch 'feature/auth'
```

- Each line starts with a **commit hash** (e.g., `f1a2b3c`)
- The message will typically start with `Merge` – this confirms it's a merge commit

---

## Visualise Git History with Graph\*\*

This helps you understand merge structure:

```bash
git log --graph --oneline --decorate
```

### Example:

```
*  f1a2b3c (HEAD -> main) Merge pull request #42 from feature/dateutil
|\
| * b7c8d9e (feature/dateutil) Add quiz evaluation
* | 3c4d5e6 Merge branch 'feature/addtask'
|/
* 1234567 Initial commit
```

The commits with multiple parents (merge points) will show branching lines.

---

## **Option 1: Use `git revert` (SAFE, keeps history)**

This is the **recommended and safest** way, especially for **shared or public repositories**.

### To undo a merge commit on `main`:

```bash
# First, identify the commit hash to revert (a merge commit)
git log --oneline

# Then revert the merge commit using the -m flag (choose the mainline parent, usually 1)
git revert -m 1 <merge_commit_hash>
```

Repeat for each merge commit if needed. This will create a new "undo" commit without erasing history.

---

## **Option 2: Reset to a Previous Commit (REWRITES HISTORY!)**

Use this **only if the branch is not public** or you are the only contributor, or you coordinate with the team.

### Step-by-step:

1. **View previous commits**:

   ```bash
   git log --oneline
   ```

2. **Reset local main branch**:

   ```bash
   git checkout main
   git reset --hard <last_known_good_commit>
   ```

3. **Force push to GitHub** (dangerous!):
   ```bash
   git push origin main --force
   ```

**This rewrites history. Use if you're the sole developer.**

---

## **Option 3: Create a Revert Branch (SAFE & COLLABORATIVE)**

If unsure, create a new branch and revert changes safely.

### Create a revert branch:

```bash
git checkout -b revert-to-good-state <last_known_good_commit>
git push origin revert-to-good-state
```

Then open a pull request on GitHub to restore the codebase.

---

## Tag commits for rollback safety

```bash
git tag before-bad-merge
```

You can always return to it later:

```bash
git checkout before-bad-merge
```
