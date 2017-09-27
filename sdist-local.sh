#!/bin/bash

echo ''
echo 'Removing ggps from local PyPi server cache:'
rm /Users/cjoakim/pypi-packages/ggps*

echo 'Creating sdist, uploading to local PyPi server:'
python setup.py sdist upload -r local

echo ''
echo 'Listing local PyPi server packages:'
ls -al /Users/cjoakim/pypi-packages

# python setup.py sdist
# python setup.py sdist upload
