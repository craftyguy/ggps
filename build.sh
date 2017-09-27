#!/bin/bash

source bin/activate

echo 'removing previous *.pyc files ...'
rm ggps/*.pyc
rm ggps/__pycache__/*.pyc
rm tests/__pycache__/*.pyc

echo 'removing the output files ...'
rm coverage/*.*

echo 'checking the source code with flake8 ...'
flake8 src --ignore F401

echo 'executing unit tests ...'
rm -rf coverage/
pytest -v --cov=ggps/ --cov-report html tests/

echo 'done'

# pre-deployment steps:
# python setup.py develop

# deployment steps:
# check-manifest
#   -> lists of files in version control and sdist match
# python setup.py sdist
# python setup.py sdist upload

# python setup.py sdist upload -r local
# ls -al /Users/cjoakim/pypi-packages

# https://pypi.python.org/pypi (current)
# https://pypi.org  (new)
# https://packaging.python.org
# https://setuptools.readthedocs.io/en/latest/setuptools.html
# https://glyph.twistedmatrix.com/2016/08/python-packaging.html
