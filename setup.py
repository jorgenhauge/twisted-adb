#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages
from os.path import dirname, join

THIS_DIR = dirname(__file__)


def get_requirements(path):
    with open(path) as f:
        return f.readlines()


install_requires = get_requirements(join(THIS_DIR, 'requirements.txt'))

setup(
    name='twistedadb',
    version='1.0',
    description='Implementation of Android Debug Bridge (ADB) protocol in Python Twisted',
    author='Geir Sporsheim',
    author_email='gksporsh@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 2.7'],
    keywords='adb twisted',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['twistedadb = twistedadb:main'],
        }
)
