### **1. Creating a Basic Package with `setup.py`**

**Project structure:**

```
flask_tic_tac_toe/
│
├── flask_tic_tac_toe/
│   ├── __init__.py
│   └── app.py
├── templates/
│   └── index.html
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

#### **Complete the steps**

Same as above, with the following additions:

1. Build and package the app:

   ```
   python setup.py sdist
   ```

   ```
   python -m pip install --upgrade setuptools
   ```

2. Install it in a virtual environment:
   ```
   pip install .
   ```

#### **Notes**

1. Create a virtual environment and activate it.

```
python -m venv myenv
source myenv/bin/activate  # On Windows, use: myenv\Scripts\activate
```

2. Run `python setup.py sdist` to create the distribution.
3. Install the package using `pip install .`. (`python -m pip install .`)
4. Run the Flask app using:
   ```
   flask run
   python -m flask run
   ```

---
