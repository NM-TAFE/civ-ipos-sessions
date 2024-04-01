# Git/GitHub Workflow

## Concepts and Terminology

- **Issue**: A report or proposal for work to be done
- **Branch**: A version control mechanism to isolate changes
- **PR (Pull Request)**: A request to merge changes from one branch to another
- **Autoclose**: Automatically close an issue when a PR is merged
- **Test Case**: Code written to test a feature or fix
- **Local Testing**: Running tests on your local machine
- **Branch Naming**: Conventional names for better management

| Task                          | Description                                               | Syntax/Command                                                |
|-------------------------------|-----------------------------------------------------------|---------------------------------------------------------------|
| Opening an Issue              | Create a new GitHub issue                                 | `GitHub UI: Issues -> New Issue`                              |
| Creating a Branch             | Make a new branch in your repo                            | `git checkout -b feature/new-feature`                         |
| Creating a Test Case          | Add a new test case within your branch                    | `// Add test in tests/ directory using unittest`              |
| Opening a PR                  | Create a PR to propose changes                            | `GitHub UI: Pull requests -> New Pull Request`                |
| Autoclose Issue               | Annotate PR to close the issue when merged                | `// In PR description, write 'Closes #issue-number'`          |
| Passing Test Case Locally     | Run tests locally to ensure they pass                     | `python -m unittest discover`                                 |
| Updating the PR               | Add more commits to the existing PR                       | `git add .; git commit; git push origin feature/new-feature`  |
| Merging PR                    | Merge the pull request into the target branch             | `GitHub UI: Pull Request -> Merge Pull Request`               |

## Examples

### Opening an Issue

1. Go to the GitHub repo page.
2. Navigate to `Issues` tab.
3. Click on `New Issue`.

### Creating a Branch

```bash
git checkout -b feature/add-feature
```

- **Benefit of Naming Convention**: Enhances branch management and easily identifies the purpose (e.g., `feature/`, `bugfix/`).

### Creating a Test Case

- Add a class in a test file under the `tests/` folder using Python's `unittest` framework.

  ```python
  import unittest
  from your_module import your_function

  class TestNewFeature(unittest.TestCase):
      def test_feature(self):
          self.assertEqual(your_function('input'), 'expected_output')
  ```

### Opening a PR

1. Push the branch to GitHub.
2. Go to `Pull Requests` tab on GitHub.
3. Click `New Pull Request`.

### Autoclose Issue

- In the PR description, include:

  ```
  Closes #1
  ```

- **Benefit**: Using terms like `Closes`, `Resolves`, or `Fixes` followed by issue numbers automates issue closure and links PR to the relevant issue for tracking.

### Passing Test Case Locally

- Run `unittest` in the project directory

  ```bash
  python -m unittest discover
  ```

### Updating the PR

```bash
git add .
git commit -m "Address review feedback"
git push origin feature/add-feature
```

### Merging PR

1. Ensure all tests pass.
2. Review code.
3. Click `Merge Pull Request` on GitHub.

