# Build, package, and distribute a Flask app using modern tools and a fast workflow with [`uv`](https://github.com/astral-sh/uv)

## Project Structure

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

## Step 1: Set Up Environment with `uv`

1. Install `uv` globally (once):

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

2. Create a new isolated environment:

```bash
uv venv
source .venv/bin/activate
# or .venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
uv pip install flask
```

## Step 2: Package Metadata with `setup.py` & `pyproject.toml`

### setup.py

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

### pyproject.toml

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"
```

### MANIFEST.in

```text
graft flask_tic_tac_toe/templates
graft flask_tic_tac_toe/static
include README.md
```

## Step 3: Build a .whl File

1. Ensure build tools are available:

```bash
uv pip install build
```

2. Build the package:

```bash
python -m build
```

This creates both `.whl` and `.tar.gz` files in `dist/`.

## Step 4: Install the Wheel in Another Project

```bash
mkdir ../new_env
cd ../new_env
uv venv
source .venv/bin/activate

uv pip install ../flask_tic_tac_toe/dist/flask_tic_tac_toe-0.1.0-py3-none-any.whl
```

Verify the install:

```bash
uv pip list
```

## Step 5: Run the Flask App

If `__init__.py` contains `from .app import app`, you can run:

```bash
flask --app flask_tic_tac_toe run
```

## Step 6: Create a Standalone Binary with PyInstaller

1. Create `main.py`:

```python
from flask_tic_tac_toe.app import app

if __name__ == "__main__":
    app.run()
```

2. Install PyInstaller:

```bash
uv pip install pyinstaller
```

3. Package the app (with templates and static files):

On Linux/macOS:

```bash
pyinstaller --onefile main.py --add-data "flask_tic_tac_toe/templates:flask_tic_tac_toe/templates" --add-data "flask_tic_tac_toe/static:flask_tic_tac_toe/static"
```

On Windows:

```bash
pyinstaller --onefile main.py --add-data "flask_tic_tac_toe/templates;flask_tic_tac_toe/templates" --add-data "flask_tic_tac_toe/static;flask_tic_tac_toe/static"
```

4. Run the binary:

```bash
cd dist
./main       # Linux/macOS
main.exe     # Windows
```

## Optional: Export requirements.txt

```bash
uv pip freeze > requirements.txt
```
