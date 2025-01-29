### **Steps to Install the Wheel in a New Environment**

You need:

- A different project environment.
- A new virtual environment.

### 1. **Create a New Directory and Set Up a Virtual Environment**

To install the project in a fresh environment, it's a good idea to create a new directory and set up a virtual environment to keep things isolated.

#### For a new directory:

```bash
mkdir new_project_directory
cd new_project_directory
```

#### Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 2. **Install the Wheel File**

If the wheel file is located in a different directory (e.g., `dist/`), you can specify the path to the wheel file:

```bash
pip install /path/to/flask_tic_tac_toe-0.1.0-py3-none-any.whl
```

Alternatively, if you copied the wheel file into your new directory, just install it directly:

```bash
pip install flask_tic_tac_toe-0.1.0-py3-none-any.whl
```

### 3. **Verify the Installation**

Verify the installation by checking if the package is listed in the installed packages:

```bash
pip list
```

You should see `flask_tic_tac_toe` (or the package name in the wheel) listed.

### 4. **Run the Project**

You can now run it from this new environment.

```bash
flask run
```

Make sure you have set the appropriate `FLASK_APP` environment variable or use the `--app` option as needed.

### **Installing the Wheel Globally**

If you want to install the project globally (i.e., not inside a virtual environment), you can simply use `pip install` with administrative or root privileges:

On Linux/macOS:

```bash
sudo pip install /path/to/flask_tic_tac_toe-0.1.0-py3-none-any.whl
```

On Windows (run Command Prompt or PowerShell as administrator):

```bash
pip install /path/to/flask_tic_tac_toe-0.1.0-py3-none-any.whl
```
