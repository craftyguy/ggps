#!/bin/bash

# Shell script to install or upgrade python packages for this pyvenv.
# Chris Joakim, 2016/11/06

source bin/activate

pip3 install --upgrade pip
pip3 install --upgrade pip-tools

pip-compile requirements.in
pip3 install -r requirements.txt
pip-sync

pip3 list --format=legacy > pip_list.txt

echo 'done'
