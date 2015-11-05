#!/bin/bash

# Shell script to install or upgrade python packages for this pyvenv.
# Chris Joakim, 2015/11/05

source bin/activate

pip3 install --upgrade pip
pip3 install --upgrade pip-tools

pip-compile requirements.in
pip3 install -r requirements.txt
pip-sync

pip3 list > pip_list.txt

echo 'done'
