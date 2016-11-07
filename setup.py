
import codecs
import os

from setuptools import setup

def description():
    return 'ggps is a python library for parsing Garmin gpx and tcx files'

def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)

def readme():
    filename = fpath('README.rst')
    with codecs.open(filename, encoding='utf-8') as f:
        return f.read()

setup(
    name='ggps',
    version='0.1.9',
    description='ggps is a python library for parsing Garmin gpx and tcx files',
    long_description=readme(),
    url='https://github.com/cjoakim/ggps',
    author='Christopher Joakim',
    author_email='christopher.joakim@gmail.com',
    license='MIT',
    packages=['ggps'],
    zip_safe=False,
    install_requires=['arrow','m26'],
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
