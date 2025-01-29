### **3. Using `Poetry` for Packaging and Dependency Management**

**Project structure:**

```
flask_tic_tac_toe/
│
├── flask_tic_tac_toe/
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
requires = ["poetry>=1.0"]
build-backend = "poetry.masonry.api"
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

3. Export dependencies to `requirements.txt`: (pycharm may offer a link to install the packages)

   ```
   poetry export -f requirements.txt > requirements.txt (this can also be done with pip freeze)

   ```

#### **`README.md` for Students**

1. Install dependencies using `poetry install`.
2. Run the Flask app with:

   ```
   poetry run flask run
   ```

   **Note** you may need:

   ```
   flask --app flask_tic_tac_toe/app.py run
   ```

3. Build the package using `poetry build`.
