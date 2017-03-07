#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import click

import delegator


@click.command()
@click.argument('packagename')
@click.option('--save', default='requirements.txt',
              help='main/prod requirements file name')
@click.option('--save-dev', default='dev-requirements.txt',
              help='dev requirements file name')
@click.option('--save-test', default='test-requirements.txt',
              help='test requirements file')
def pipin(packagename, save, save_dev, save_test):
    delegator.run('pip install ' + packagename)
    output = delegator.run('pip freeze').out

    for option in [save, save_dev, save_test]:
        print(option)
        if option:
            file_name = option
    for req in output.decode().split('\n'):
        if not req:
            continue
        if packagename in req:
            with(file_name, 'ab+') as f:
                f.write(req)
