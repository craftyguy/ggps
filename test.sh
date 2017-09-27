#!/bin/bash

source bin/activate

echo 'removing previous *.pyc files ...'
rm ggps/*.pyc
rm ggps/__pycache__/*.pyc
rm tests/__pycache__/*.pyc

echo 'checking the source code with flake8 ...'
flake8 ggps --ignore F401

echo 'executing unit tests with code coverage ...'
rm -rf coverage/
pytest -v --cov=ggps/ --cov-report html tests/

echo 'done'

# For sdist deployment to PyPi, or local PyPi server:
# python setup.py sdist
# python setup.py sdist upload
# python setup.py sdist upload -r local
# ls -al /Users/cjoakim/pypi-packages
# rm /Users/cjoakim/pypi-packages/ggps*
