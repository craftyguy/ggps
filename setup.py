
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# see http://peterdowns.com/posts/first-time-with-pypi.html
# see 

# # Get the long description from the README file
# here = path.abspath(path.dirname(__file__))
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#     long_description = f.read()

def description():
    return 'ggps is a python library for parsing Garmin gpx and tcx files'

def readme():
    with open("README.rst", encoding='utf-8') as f:
        return f.read()

setup(
    name='ggps',
    version='0.1.8',
    description=description(),
    long_description = readme(),
    url='https://github.com/cjoakim/ggps',
    author='Christopher Joakim',
    author_email='christopher.joakim@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='garmin gps gpx tcx parsing utilities m26',

    # You can just specify the packages manually here if your project is simple.
    # Or you can use find_packages().
    # packages=find_packages(exclude=['bin', 'contrib', 'coverage', 'data', 'docs', 'tests*']),
    packages=['ggps'],

    test_suite = 'tests',

    # Run-time dependencies; these will be installed by pip when the project is installed.
    # See https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'arrow', 
        'm26',
    ],

    # Dev and Test dependencies, install like this: $ pip install -e .[dev,test]
    extras_require={
        'dev':  ['check-manifest', 'flake8', 'rstcheck', 'Sphinx'],
        'test': ['coverage', 'cov-core', 'nose2'],
    }
)
