# Working with pip and PyPI

## Concepts and Terminology

- **pip**: Python's package manager to install libraries and manage dependencies
- **PyPI**: Python Package Index, the repository for Python packages
- **`requirements.txt`**: A text file that lists project dependencies
- **`pip freeze`**: Command to list all installed packages and versions

| Task                      | Description                                               | Syntax/Command                                     |
|---------------------------|-----------------------------------------------------------|----------------------------------------------------|
| Install Package           | Install a Python package from PyPI                        | `pip install package_name`                         |
| Uninstall Package         | Remove a Python package                                   | `pip uninstall package_name`                       |
| Upgrade Package           | Upgrade a package to the latest version                   | `pip install --upgrade package_name`               |
| List Packages             | List installed packages                                   | `pip list`                                         |
| Freeze Requirements       | Generate a list of installed packages                     | `pip freeze > requirements.txt`                    |
| Install from Requirements | Install packages from a `requirements.txt` file           | `pip install -r requirements.txt`                  |


## Examples

### Installing a Package

To install a package called `requests` from PyPI:

```bash
pip install requests
```

### Uninstalling a Package

To uninstall the `requests` package:

```bash
pip uninstall requests
```

### Upgrading a Package

To upgrade the `requests` package to the latest version:

```bash
pip install --upgrade requests
```

### List Installed Packages

To list all installed packages:

```bash
pip list
```

### Freezing Requirements

To generate a `requirements.txt` file listing all installed packages and versions:

```bash
pip freeze > requirements.txt
```

### Installing from Requirements

To install packages listed in a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Search for Packages
> **DEPRECATED**: Use [PyPI search](www.pypi.org) instead.

To search for a package called `requests` on PyPI:

```bash
pip search requests
```

## Basic Introduction to PyPI

- **What is PyPI**: Usually pronounced "Pie P.I.", the Python Package Index (PyPI) is a repository for Python software packages. It enables package discovery, installation, and dependency management. Anyone can add packages to PyPI.
- **Usage**: Utilized in tandem with pip, PyPI provides a centralized platform for sharing Python libraries and utilities, making it easier to distribute and manage Python libraries.
