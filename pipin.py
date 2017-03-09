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


@click.group()
@click.version_option()
def pipin():
    """
    Entry point for pipin
    """
    pass


@pipin.command()
@click.argument('packagename')
@click.option('--save', is_flag=True, help='pin package to requirements')
@click.option('--save-dev', is_flag=True,
              help='pin package to dev-requirements')
@click.option('--save-test', is_flag=True,
              help='pin package to test-requirements')
@click.argument('filename', required=False)
def install(packagename, save, save_dev, save_test, filename):
    """
    Install the package via pip, pin the package only to requirements file.
    Use option to decide which file the package will be pinned to.
    """
    delegator.run('pip install ' + packagename)
    print('Installing ', packagename)
    if not filename:
        filename = get_filename(save, save_dev, save_test)
    update_requirements(packagename, filename)


@pipin.command()
@click.argument('packagename')
@click.argument('filename', required=False)
def remove(packagename, filename):
    delegator.run('pip uninstall ' + packagename)
    if not filename:
        filename = get_filename()
    update_requirements(packagename, filename, True)


def update_requirements(packagename, filename, uninstall=False):
    output = delegator.run('pip freeze').out

    for req in output.split('\n'):
        if not req:
            continue
        if packagename in req and not uninstall:
            with open(filename, 'ab+') as f:
                f.write(req.encode('utf-8'))
        if uninstall and packagename not in req:
            with open(filename, 'wb') as f:
                f.write(req.encode('utf-8'))

    print('Updated', str(filename) + '!')


def get_filename(save=False, save_dev=False, save_test=False):
    if save_dev:
        return 'dev-requirements.txt'
    if save_test:
        return 'test-requirements.txt'
    return 'requirements.txt'


if __name__ == '__main__':
    pipin()
