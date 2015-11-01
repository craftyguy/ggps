#!/bin/bash

# Shell script to install or upgrade python packages for this pyvenv.
# Chris Joakim, 2015/11/01

source bin/activate

echo 'upgrading pip and libraries used by this project...'

pip install --upgrade pip

pip3 --version
python3 --version

pip install --upgrade arrow
pip install --upgrade check-manifest
pip install --upgrade coverage
pip install --upgrade flake8
pip install --upgrade nose

pip list   > pip_list.txt
pip freeze > requirements.txt

echo 'done'
