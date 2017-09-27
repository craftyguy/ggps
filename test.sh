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
# python setup.py sdist upload -r pypilegacy
# ls -al /Users/cjoakim/pypi-packages
# rm /Users/cjoakim/pypi-packages/ggps*

# Submitting dist/ggps-0.2.0.tar.gz to https://pypi.python.org/pypi
# Upload failed (410): Gone (This API has been deprecated and removed from legacy PyPI in favor of using the APIs available in the new PyPI.org implementation of PyPI (located at https://pypi.org/). For more information about migrating your use of this API to PyPI.org, please see https://packaging.python.org/guides/migrating-to-pypi-org/#uploading. For more information about the sunsetting of this API, please see https://mail.python.org/pipermail/distutils-sig/2017-June/030766.html)
# error: Upload failed (410): Gone (This API has been deprecated and removed from legacy PyPI in favor of using the APIs available in the new PyPI.org implementation of PyPI (located at https://pypi.org/). For more information about migrating your use of this API to PyPI.org, please see https://packaging.python.org/guides/migrating-to-pypi-org/#uploading. For more information about the sunsetting of this API, please see https://mail.python.org/pipermail/distutils-sig/2017-June/030766.html)
