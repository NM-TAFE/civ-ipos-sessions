## Keeping Your Branch Up to Date with the Original Repository

When you're working on a GitHub project from a **fork**, you need to make sure your branch stays updated with the latest changes from the original (upstream) repository.

Here's how to do that **without overwriting your own work**.

---

## Step 1: Fork the Repository

1. Go to the GitHub repository provided by your instructor.
2. Click **"Fork"** (top-right corner).
3. Clone **your fork** to your computer:

```bash
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME
```

---

## Step 2: Set the Upstream Remote

The upstream is the **original repository** you forked from (e.g., your instructor's or the class repo).

```bash
git remote add upstream https://github.com/NM-TAFE/dip-web-application-development-classes.git
```

You can check that both remotes are set correctly:

```bash
git remote -v
```

Expected output:

```
origin    https://github.com/YOUR_USERNAME/REPO_NAME.git (fetch)
origin    https://github.com/YOUR_USERNAME/REPO_NAME.git (push)
upstream  https://github.com/NM-TAFE/dip-web-application-development-classes.git (fetch)
upstream  https://github.com/NM-TAFE/dip-web-application-development-classes.git (push)
```

---

## Step 3: Pull Updates from Upstream

To get the latest changes from the `main` branch of the original repo into **your own branch**, follow either **merge** or **rebase** instructions below.

---

### Option 1: **Merge** `upstream/main` into your branch

This is safer and easier for beginners.

1. Switch to the branch you're working on:

   ```bash
   git checkout your-branch-name
   ```

2. Fetch the latest changes from upstream:

   ```bash
   git fetch upstream
   ```

3. Merge those changes into your branch:

   ```bash
   git merge upstream/main
   ```

4. If you see conflicts, Git will guide you to resolve them. Open the conflicting files, fix them, then:

   ```bash
   git add <file>
   git commit
   ```

---

### Option 2: **Rebase** your branch onto `upstream/main`

This keeps your history cleaner, but should only be used **before pushing your branch** to GitHub.

1. Checkout your working branch:

   ```bash
   git checkout your-branch-name
   ```

2. Fetch latest updates from upstream:

   ```bash
   git fetch upstream
   ```

3. Rebase your branch onto upstream/main:

   ```bash
   git rebase upstream/main
   ```

4. If there are conflicts:

   - Fix them in the file(s)
   - Then run:

   ```bash
   git add <file>
   git rebase --continue
   ```

5. If you already pushed this branch to GitHub, you need to **force push**:

   ```bash
   git push --force-with-lease
   ```

---

## Merge vs Rebase – Which Should You Use?

| Merge                            | Rebase                                          |
| -------------------------------- | ----------------------------------------------- |
| Easier, especially for beginners | Cleaner commit history                          |
| Creates a merge commit           | Rewrites commit history                         |
| Keeps record of when you merged  | Avoids extra merge commits                      |
| Safe for shared branches         | Should only be done before pushing or with care |
