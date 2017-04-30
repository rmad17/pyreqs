#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

from setuptools import setup

setup(
    name='pipin',
    version='0.0.1',
    description='Better manage python requirements file',
    author='Sourav Basu',
    author_email='souravbasu17@gmail.com',
    url='https://github.com/rmad17/pipin',
    py_modules=['pipin'],
    install_requires=[
        'click', 'sh'
    ],
    entry_points='''
        [console_scripts]
        pipin=pipin:pipin
    ''',
)
