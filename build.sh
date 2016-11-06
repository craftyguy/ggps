#!/bin/bash

source bin/activate

# echo 'building/merging the codebase...'
# python build.py

echo 'checking the merged source code with flake8...'
flake8 ggps/*.py

rm coverage/*.*

echo 'executing unit tests...'
python -m unittest -v

echo 'creating code coverage report...'
nose2 --with-coverage --coverage-report html

echo 'done'
