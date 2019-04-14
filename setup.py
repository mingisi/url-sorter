#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This code is distributed under the terms and conditions
# from the Apache License, Version 2.0
#
# http://opensource.org/licenses/apache2.0.php

"""
Run with:
python ./setup.py install
"""

import os
import io
import subprocess

import setuptools.command.develop
from distutils.core import setup


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(path, encoding='utf8').read()


class SetupDevelop(setuptools.command.develop.develop):
    """Docstring is overwritten."""

    def run(self):
        """
        Prepare environment for development.
        - Ensures 'nose' and 'coverage.py' are installed for testing.
        - Call super()'s run method.
        """
        subprocess.check_call(('pip', 'install', 'pytest', 'coverage'))

        # Call super() (except develop is an old-style class, so we must call
        # directly). The effect is that the development egg-link is installed.
        setuptools.command.develop.develop.run(self)

SetupDevelop.__doc__ = setuptools.command.develop.develop.__doc__


setup(
    name='urlsorter',
    version='1.0.0',
    description='grouping sorting urls hostnames',
    long_description=read('README.md'),

    py_modules=['sqlitedict'],

    author='Salim Muthalib',
    author_email="salim.muthalib@outlook.com",
    maintainer='Salim Muthalib',
    maintainer_email='salim.muthalib@outlook.com',

    url='https://github.com/mingisi/url-sorter',

    keywords='url sorter',

    license='Apache 2.0',
    platforms='any',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Database :: Front-Ends',
    ],
    cmdclass={'develop': SetupDevelop},
)
