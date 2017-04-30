#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

from setuptools import setup

setup(
    name='pipinstall',
    version='0.0.2',
    description='Better manage python requirements file',
    author='Sourav Basu',
    author_email='souravbasu17@gmail.com',
    url='https://github.com/rmad17/pipinstall',
    py_modules=['pipinstall'],
    install_requires=[
        'click', 'sh'
    ],
    entry_points='''
        [console_scripts]
        pipinstall=pipinstall:pipinstall
    ''',
)
