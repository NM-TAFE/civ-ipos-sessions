# common pip install commands:

## Install a Package: Installs a package from PyPI (Python Package Index).

pip install package_name

## Install a Specific Version: Installs a specific version of a package.

pip install package_name==1.2.3

## Upgrade a Package: Upgrades a package to the latest version.

pip install --upgrade package_name

## bInstall from a Requirements File: Installs all packages listed in a requirements.txt file.

pip install -r requirements.txt

## Install Packages to User Directory: Installs packages for the current user only.

pip install --user package_name

## Install Packages in Editable Mode: Installs packages in editable mode, useful for development.

pip install -e .

## Install Packages with Specific Index: Installs packages from a specific index URL.

pip install --index-url https://example.com/simple/ package_name

## Install Packages with Extra Features: Installs a package with extra features (if available).

pip install package_name[extra_feature]

## Install Packages without Dependencies: Installs a package without its dependencies.

pip install --no-deps package_name

## Install Development Dependencies: Installs development dependencies listed in requirements-dev.txt.

pip install -r requirements-dev.txt

## Install from a Specific Source: Installs a package from a specific source (e.g., Git).

pip install git+https://github.com/user/repo.git

## Install Packages with a Specific Python Version: Installs packages for a specific Python version.

python3 -m pip install package_name
