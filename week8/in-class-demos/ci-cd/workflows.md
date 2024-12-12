name: Run Tests and Coverage

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Install dependencies
        run: python -m pip install coverage

      - name: Run tests with coverage
        run: |
          coverage run -m unittest discover -s . -p 'test_*.py'
          coverage report -m