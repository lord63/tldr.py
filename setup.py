#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import tldr


with open('README.rst') as f:
    long_description = f.read()

setup(
    name='tldr.py',
    version=tldr.__version__,
    description='A python client for tldr: simplified and community-driven man pages.',
    long_description=long_description,
    url='https://github.com/lord63/tldr.py',
    author='lord63',
    author_email='lord63.j@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='tldr cli man command usage',
    packages=['tldr'],
    install_requires=[
        'click>=5.0',
        'PyYAML>=3.11',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'tldr=tldr.cli:cli']
    }
)
