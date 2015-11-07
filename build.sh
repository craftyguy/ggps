#!/bin/bash

source bin/activate

echo 'building/merging the codebase...'
python build.py

echo 'checking the merged source code with flake8...'
flake8 ggps/__init__.py

python ggps/gpx_handler.py data/twin_cities_marathon.gpx > tmp/twin_cities_marathon_gpx.out
python ggps/tcx_handler.py data/twin_cities_marathon.tcx > tmp/twin_cities_marathon_tcx.out

echo 'running all tests with nose and code coverage...'
nosetests --with-coverage --cover-html --cover-html-dir=coverage --cover-package=ggps
