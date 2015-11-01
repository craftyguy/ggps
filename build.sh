#!/bin/bash

source bin/activate

echo 'building/merging the codebase...'
python build.py

echo 'checking the merged source code with flake8...'
flake8 ggps/__init__.py

echo 'running all tests with nose and code coverage...'
nosetests --with-coverage --cover-html --cover-html-dir=coverage --cover-package=ggps
