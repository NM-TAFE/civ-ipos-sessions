### **4. `.whl` Archives**

**Project structure:**

```
flask_tic_tac_toe/
│
├── flask_tic_tac_toe/
│   └──__init__.py
│   └── app.py
│   └── templates/
|       └── index.html
├── templates/
│   └── index.html
└── setup.py
```

#### **Complete the Steps**

**Activate your venv as you have previously done**

1. Generate the wheel:
   ** The command below may need you to install setuptools**

   ```
   pip install setuptools wheel
   python setup.py bdist_wheel
   ```

2. Install the `.whl` file locally:

   ```
   pip install dist/flask_tic_tac_toe-0.1.0-py3-none-any.whl
   ```

3. Create the `.whl` file using `python setup.py bdist_wheel`.
4. Install it using `pip install <your_wheel>.whl`.
5. Run the app with `flask run`.

### **Steps to Include `app.py` and `templates` in the Wheel**

#### **1. Using `setuptools` (via `setup.py`)**

If you’re using `setuptools` with a `setup.py` file, you’ll need to do two things:

1. Ensure the Python files like `app.py` are included.
2. Explicitly specify non-Python files like the `templates/` directory.

#### a. **Include Non-Python Files Using `MANIFEST.in`**

To include the `templates` directory (or other non-code files like `static/`), create a `MANIFEST.in` file at the root of your project.

**Example `MANIFEST.in`:**

```text
recursive-include flask_tic_tac_toe/templates *
```

This line tells `setuptools` to include everything inside the `templates/` directory in the package.

#### b. **Modify `setup.py` to Include Package Data**

Make sure your `setup.py` includes `include_package_data=True` and points to the correct package directory (e.g., `flask_tic_tac_toe`).

**Example `setup.py`:**

```python
from setuptools import setup, find_packages

setup(
    name='flask_tic_tac_toe',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,  # This ensures non-code files are included
    install_requires=[
        'flask',
    ],
)
```

#### **3. Project Structure**

Here’s an example of how your project structure should look:

```
flask_tic_tac_toe/
│
├── flask_tic_tac_toe/
│   ├── app.py                 # Flask app code
│   ├── __init__.py            # __init__.py if your package is a module
│   └── templates/             # Template files
│       └── index.html
├── setup.py                   # Only for setuptools
├── pyproject.toml              # Only for Poetry
├── MANIFEST.in                 # For including non-code files with setuptools
└── README.md
```

### **4. Ways to Build the Wheel**

Once you've set up either `setup.py` or `pyproject.toml` correctly, you can build the wheel again.

- **For setuptools:**

  ```bash
  python setup.py bdist_wheel
  ```

- **For Poetry:**
  ```bash
  poetry build
  ```
- **For PDM:**
  ```bash
  pdm build
  ```

### **5. Verify the Wheel Contents**

You can verify that your `app.py` and `templates/` directory have been included in the wheel by inspecting the contents of the `.whl` file.

1. **Extract the contents of the wheel:**
   ```bash
   unzip flask_tic_tac_toe-0.1.0-py3-none-any.whl -d wheel_content/
   ```
