#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import json
from os import path
import sys

import click

from tldr import __version__
from tldr.config import get_config
from tldr.parser import parse_page


def find_page(command):
    """Find the command man page in the pages directory."""
    repo_directory = get_config()['repo_directory']
    default_platform = get_config()['platform']

    with open(path.join(repo_directory, 'pages/index.json')) as f:
        index = json.load(f)
    command_list = [item['name'] for item in index['commands']]
    if command not in command_list:
        sys.exit(
            ("Sorry, we don't support command: {0} right now.\n"
             "You can file an issue or send a PR on github:\n"
             "    https://github.com/tldr-pages/tldr").format(command))

    supported_platforms = index['commands'][
        command_list.index(command)]['platform']
    if default_platform in supported_platforms:
        platform = default_platform
    elif 'common' in supported_platforms:
        platform = 'common'
    else:
        platform = ''
    if not platform:
        sys.exit(
            ("Sorry, command {0} is not supported on your platform.\n"
             "You can file an issue or send a PR on github:\n"
             "    https://github.com/tldr-pages/tldr").format(command))

    page_path = path.join(path.join(repo_directory, 'pages'),
                          path.join(platform, command + '.md'))
    parse_page(page_path)


@click.group(context_settings={'help_option_names': ('-h', '--help')})
@click.version_option(__version__, '-V', '--version', message='%(version)s')
def cli():
    """A python client for tldr: simplified and community-driven man pages."""
    pass


@cli.command()
@click.argument('command')
def find(command):
    """Find the command usage."""
    find_page(command)


@cli.command()
def update():
    """Update to the latest pages."""
    pass


@cli.command()
def init():
    """Init config file and download the man pages."""
    pass
