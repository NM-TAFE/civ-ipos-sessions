### **1. Creating a Basic Package with `setup.py`**

**Project structure:**

```
project_directory/
│
├── flask_tic_tac_toe/
│   ├── __init__.py
│   └── app.py
│   └── templates/
│     └── index.html
└── setup.py
```

**`flask_tic_tac_toe/__init__.py`:**

```python
from .app import app
```

**`setup.py`:**

```python
from setuptools import setup, find_packages

setup(
    name='flask_tic_tac_toe',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
```

---

### `MANIFEST.in`

```
recursive include flask_tic_tac_toe/templates *
recursive-include flask_tic_tac_toe/static *
```

#### **Complete the steps**

1. Create a virtual environment and activate it.

```python
python -m venv myenv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

Same as above, with the following additions:

2. Build and package the app:

   ```python
   python -m pip install --upgrade setuptools
   ```

   ```python
   python -m setup.py sdist
   ```

3. Install it in a virtual environment:
   ```python
   pip install .
   ```

#### **Notes**

1. Try running the Flask app using:
   ```python
   python -m flask --app flask_tic_tac_toe run
   ```
2. Any dist issue cleanup and start again
   ```python
   rm -rf dist/ build/ flask_tic_tac_toe.egg-info
   python setup.py sdist
   pip install dist/*.tar.gz
   ```

---
