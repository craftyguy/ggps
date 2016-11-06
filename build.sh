#!/bin/bash

source bin/activate

# echo 'building/merging the codebase...'
# python build.py

echo 'checking the merged source code with flake8...'
flake8 ggps/__init__.py

rm htmlcov/*.*

echo 'executing unit tests...'
python -m unittest -v

echo 'creating code coverage report...'
coverage html

echo 'done'
