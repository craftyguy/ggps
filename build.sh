#!/bin/bash

source bin/activate

echo 'removing the output files ...'
rm ggps/__init__.py
rm coverage/*.*

echo 'creating/merging file ggps/__init__.py ...'
python build.py

echo 'checking the merged source code with flake8 ...'
flake8 ggps/*.py

echo 'executing unit tests ...'
python -m nose2 -v

echo 'creating code coverage report ...'
nose2 --with-coverage --coverage-report html

echo 'done'

# deployment steps:
# check-manifest
#   -> lists of files in version control and sdist match
# python setup.py sdist
# python setup.py sdist upload
