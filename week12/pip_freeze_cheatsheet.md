# common pip freeze commands

## List Installed Packages: Lists all installed packages and their versions.

pip freeze

## Save Installed Packages to a Requirements File: Saves all installed packages to a requirements.txt file.

pip freeze > requirements.txt

## Show Dependencies of a Specific Package: Shows only the dependencies of a specific package.

pip freeze | grep package_name

## Show Only Top-Level Packages: Shows only the top-level packages (no dependencies). show all lines that do not start with a hyphen.

pip freeze | grep -v -e '^\-'

## Show Specific Package Version: Shows the version of a specific package.

pip freeze | grep package_name

## Check for Outdated Packages: Lists installed packages and shows if there are updates available.

pip list --outdated

## Show Detailed Infor## mation: Shows additional information about installed packages (e.g., location, dependencies).

pip show package_name

## Check Installed Package Locations: Shows the installation locations of all packages.

pip freeze | xargs pip show -f | grep Location

## Display in JSON Format: Displays the list of installed packages in JSON format.

pip freeze --json

## Filter Out Specific Packages: Excludes specific packages from the output.

pip freeze | grep -v package_name
