### **3. Using `Poetry` for Packaging and Dependency Management**

**Project structure:**

```
flask_tic_tac_toe/
│
├── flask_tic_tac_toe/
│   └──__init__.py
│   └── app.py
│   └── templates/
|       └── index.html
│   └── static/
|       └── style.css
└── pyproject.toml
```

**`pyproject.toml` (after running `poetry init`):**

1. make sure to create & activate your virtual environment

We can use:

```
poetry shell
```

```toml
[tool.poetry]
name = "flask_tic_tac_toe"
version = "0.1.0"
description = "Tic-Tac-Toe game using Flask."
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"
flask = "^2.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

#### **Complete the Steps**

Install the dependencies and build the project:
**If you command arent recognised you may need to add python -m at the beginning to force python to use the current environment**

1. Install pip then the dependencies using:

   ```
   python -m pip install poetry (or pip only)

   poetry install
   ```

2. Build the project:

   ```
   poetry build
   ```

3. Install your depenedencies using poetry **(see : https://python-poetry.org/docs/cli/#install)**

   ```
   poetry install

   ```

#### **`README.md` for Students**

1. Install dependencies using `poetry install`.
2. Run the Flask app with:

   ```
   poetry run    flask --app flask_tic_tac_toe/app.py run
   ```

3. Build the package using `poetry build`.

   - Used for publishing to PyPI or internal repos.
   - Can be installed via `pip install dist/*.whl` or `pip install dist/*.tar.gz`.

   ```
   dist/
   ├── your_package-0.1.0.tar.gz   ← Source distribution
   └── your_package-0.1.0-py3-none-any.whl ← Wheel distribution
   ```
