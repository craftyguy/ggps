#!/bin/bash

source bin/activate

echo 'removing previous *.pyc files ...'
rm ggps/*.pyc
rm ggps/__pycache__/*.pyc
rm tests/__pycache__/*.pyc

echo 'removing the output files ...'
rm coverage/*.*

# echo 'creating/merging file ggps/__init__.py ...'
# python build.py

# echo 'merging the codebase ...'
# python build.py

echo 'checking the merged source code with flake8 ...'
flake8 ggps/__init__.py

echo 'executing unit tests ...'
python -m nose2 -v

echo 'creating code coverage report ...'
nose2 --with-coverage --coverage-report html

echo 'done'

# pre-deployment steps:
# python setup.py develop

# deployment steps:
# check-manifest
#   -> lists of files in version control and sdist match
# python setup.py sdist
# python setup.py sdist upload

# https://pypi.python.org/pypi (current)
# https://pypi.org  (new)
# https://packaging.python.org
# https://setuptools.readthedocs.io/en/latest/setuptools.html
# https://glyph.twistedmatrix.com/2016/08/python-packaging.html
