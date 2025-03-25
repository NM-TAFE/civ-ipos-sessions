## **Build, package, and distribute a Flask app using modern tools and a fast workflow with [`uv`](https://github.com/astral-sh/uv).**

## **Project Structure**

```
flask_tic_tac_toe/
│
├── flask_tic_tac_toe/
│   ├── __init__.py
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
├── pyproject.toml
├── setup.py
├── MANIFEST.in
└── README.md
```

---

### Step 1: Set Up Environment with `uv`

1. **Install `uv` globally (once)**

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

2. **Create a new isolated environment:**

```bash
uv venv
source .venv/bin/activate
# or .venv\Scripts\activate on Windows
```

3. **Install dependencies:**

```bash
uv pip install flask
```

---

### Step 2: Package Metadata with `setup.py` & `pyproject.toml`

#### **setup.py**

```python
from setuptools import setup, find_packages

setup(
    name='flask_tic_tac_toe',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['flask'],
)
```

#### **pyproject.toml**

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

#### **MANIFEST.in**

```text
recursive-include flask_tic_tac_toe/templates *
recursive-include flask_tic_tac_toe/static *
```

---

### Step 3: Build a `.whl` File

1. Ensure build tools are available:

```bash
uv pip install build
```

2. Build the package:

```bash
python -m build
```

This creates both `.whl` and `.tar.gz` files in `dist/`.

---

### Step 4: Install the Wheel in Another Project

```bash
mkdir ../new_env
cd ../new_env
uv venv
source .venv/bin/activate

uv pip install ../flask_tic_tac_toe/dist/flask_tic_tac_toe-0.1.0-py3-none-any.whl
```

Verify:

```bash
uv pip list
```

---

### Step 5: Run the Flask App

Set the Flask app explicitly:

```bash
flask --app flask_tic_tac_toe/app.py run
```

---

### Step 6: Create a Standalone Binary with PyInstaller

1. Install PyInstaller:

```bash
uv pip install pyinstaller
```

2. Package the app (with templates/static):

**Linux/macOS**

```bash
pyinstaller --onefile app.py --add-data "templates:templates" --add-data "static:static"
```

**Windows**

```bash
pyinstaller --onefile app.py --add-data "templates;templates" --add-data "static;static"
```

3. Run the binary:

```bash
cd dist
./app       # Linux/macOS
app.exe     # Windows
```

---

#### Optional: Export `requirements.txt` (for legacy tools)

```bash
uv pip freeze > requirements.txt
```

---
