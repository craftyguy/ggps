
import os

from setuptools import setup, find_packages

NAME = 'ggps'
VERSION = '0.2.1'
DESCRIPTION = 'ggps is a python library for parsing and enhancing Garmin gpx and tcx files'
URL = 'https://github.com/cjoakim/ggps'
AUTHOR = 'Christopher Joakim'
EMAIL = 'christopher.joakim@gmail.com'
LICENSE = 'MIT'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    packages=['ggps'],
    install_requires=[
        'arrow',
        'm26'
    ],
    test_suite="tests",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
