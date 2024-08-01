# Activity notes
> provides supplementary  notes for [CI activity](https://coderefinery.github.io/testing/continuous-integration/)

- When creating the repo on **GitHub**, also select add `.gitignore` 
- In the `.gitignore`, uncomment `.idea/`


To install `pytest` (not part of Python standard library):

```bash
python -m pip install pytest
```
> **Note**: if you are doing this in **PyCharm** ensure your `venv` is active:
```->(venv)<- C:\Users\...```

Try and make the necessary tweaks to the `.yml` using the instructions, but 
if you get stuck, the following is a complete `.yml` with the required tweaks:

```yml
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read
  pull-requests: write

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest pytest-cov
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest and calculate coverage
      run: |
        pytest --cov-report "xml:coverage.xml"  --cov=.
    - name: Create Coverage 
      if: ${{ github.event_name == 'pull_request' }}
      uses: orgoro/coverage@v3.1
      with:
          coverageFile: coverage.xml
          token: ${{ secrets.GITHUB_TOKEN }}
```
