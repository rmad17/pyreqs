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

from sh import grep as sh_grep
from sh import mv as sh_mv
from sh import pip as sh_pip
from sh import rm as sh_rm


@click.group()
@click.version_option()
def pyreqs():
    """
    Entry point for pyreqs
    """
    pass


@pyreqs.command()
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
    print('Installing ', packagename)
    print(sh_pip.install(packagename))
    if not filename:
        filename = get_filename(save, save_dev, save_test)
    try:
        add_requirements(packagename, filename)
    except AssertionError:
        print('Package already pinned in ', filename)


@pyreqs.command()
@click.argument('packagename')
@click.option('--save', is_flag=True, help='remove package from requirements')
@click.option('--save-dev', is_flag=True,
              help='remove package from dev-requirements')
@click.option('--save-test', is_flag=True,
              help='remove package from test-requirements')
@click.argument('filename', required=False)
def remove(packagename, save, save_dev, save_test, filename):
    """
    Uninstall the package and remove it from requirements file.
    """
    print(sh_pip.uninstall(packagename, "-y"))
    if not filename:
        filename = get_filename(save, save_dev, save_test)
    remove_requirements(packagename, filename)


def add_requirements(packagename, filename):
    output = sh_pip.freeze
    packages = output.split('\n')
    try:
        with open(filename, 'rb+') as f0:
            current_requirements = f0.readlines()
        versioned_packagename = sh_grep(
            sh_pip.freeze(_iter=True), packagename, _iter=True)
        byted_packagename = str(versioned_packagename).encode('utf-8')
        assert byted_packagename not in current_requirements
    except FileNotFoundError:
        pass
    for req in packages:
        if not req:
            continue
        if packagename in req:
            with open(filename, 'ab+') as f:
                f.write(req.encode('utf-8'))
    order_requirements(filename)
    print('Updated', str(filename) + '!')


def remove_requirements(packagename, filename):
    with open(filename, 'rb+') as f0:
        for line in f0.readlines():
            if packagename not in str(line):
                with open(filename + '.tmp', 'wb+') as f1:
                    f1.write(line)
    sh_rm(filename, "-f")
    sh_mv(filename + '.tmp', filename)
    print('Updated', str(filename) + '!')


def get_filename(save=False, save_dev=False, save_test=False):
    if save_dev:
        return 'dev-requirements.txt'
    if save_test:
        return 'test-requirements.txt'
    return 'requirements.txt'


def order_requirements(filename):
    with open(filename, 'rb+') as f0:
        packages = f0.readlines()
        packages.sort()
    with open(filename + '.tmp', 'ab+') as f1:
        for package in packages:
            f1.write(package)
    sh_rm(filename, "-f")
    sh_mv(filename + '.tmp', filename)


if __name__ == '__main__':
    pyreqs()
