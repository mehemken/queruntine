#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'queruntine',
    version = '0.2',
    description = 'Python asks Rust to query a database concurrently.',
    long_description=long_description,
    author = 'Marco Hemken',
    author_email = 'mehemken@gmail.com',
    url = 'https://github.com/mehemken/queruntine',
    packages = find_packages(exclude=['contrib', 'docs', 'tests'])
)
