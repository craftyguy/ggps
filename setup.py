
import os
from setuptools import setup

def description():
    return 'ggps is a python library for parsing Garmin gpx and tcx files'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def readme():
    return read('README.rst')

setup(
    name='ggps',
    version='0.1.12',
    description='ggps is a python library for parsing Garmin gpx and tcx files',
    long_description='ggps is a python library for parsing Garmin gpx and tcx files',
    url='https://github.com/cjoakim/ggps',
    author='Christopher Joakim',
    author_email='christopher.joakim@gmail.com',
    license='MIT',
    packages=['ggps'],
    install_requires=[
        'arrow',
        'm26'
    ],
    test_suite="tests",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
