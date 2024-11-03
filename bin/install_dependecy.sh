#!/bin/sh

# get package name

echo "Enter the name of the Python package to install:"
read package_name

# install dependency with pip
pip install "$package_name"
if [ $? -eq 0 ]; then
    # if installation is successful, run pip freeze > requrirements.txt
    echo "Package '$package_name' successfully installed"
    pip freeze > requirements.txt
else
    # if installation is unsuccessful, print error
    echo "Error: Package '$package_name' could not be installed"
fi

# exit
exit 0
