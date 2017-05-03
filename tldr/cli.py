#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import io
import json
from operator import itemgetter
import os
from os import path
import subprocess
import sys

import click
import yaml

from tldr import __version__
from tldr.config import get_config
from tldr.parser import parse_page


def parse_man_page(command, platform):
    """Parse the man page and return the parsed lines."""
    page_path = find_page_location(command, platform)
    output_lines = parse_page(page_path)
    return output_lines


def find_page_location(command, specified_platform):
    """Find the command man page in the pages directory."""
    repo_directory = get_config()['repo_directory']
    default_platform = get_config()['platform']
    command_platform = (
        specified_platform if specified_platform else default_platform)

    with io.open(path.join(repo_directory, 'pages/index.json'),
                 encoding='utf-8') as f:
        index = json.load(f)
    command_list = [item['name'] for item in index['commands']]
    if command not in command_list:
        sys.exit(
            ("Sorry, we don't support command: {0} right now.\n"
             "You can file an issue or send a PR on github:\n"
             "    https://github.com/tldr-pages/tldr").format(command))

    supported_platforms = index['commands'][
        command_list.index(command)]['platform']
    if command_platform in supported_platforms:
        platform = command_platform
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
    return page_path


def build_index():
    repo_directory = get_config()['repo_directory']
    index_path = path.join(repo_directory, 'pages', 'index.json')
    page_path = path.join(repo_directory, 'pages')

    tree_generator = os.walk(page_path)
    folders = next(tree_generator)[1]
    commands, new_index = {}, {}
    for folder in folders:
        pages = next(tree_generator)[2]
        for page in pages:
            command_name = path.splitext(page)[0]
            if command_name not in commands:
                commands[command_name] = {'name': command_name,
                                          'platform': [folder]}
            else:
                commands[command_name]['platform'].append(folder)
    command_list = [item[1] for item in
                    sorted(commands.items(), key=itemgetter(0))]
    new_index['commands'] = command_list

    with open(index_path, mode='w') as f:
        json.dump(new_index, f)


@click.group(context_settings={'help_option_names': ('-h', '--help')})
@click.version_option(__version__, '-V', '--version', message='%(version)s')
def cli():
    """A python client for tldr: simplified and community-driven man pages."""
    pass  # pragma: no cover


@cli.command()
@click.argument('command')
@click.option('--on', type=click.Choice(['linux', 'osx', 'sunos']),
              help='the specified platform.')
def find(command, on):
    """Find the command usage."""
    output_lines = parse_man_page(command, on)
    click.echo(''.join(output_lines))


@cli.command()
def update():
    """Update to the latest pages."""
    repo_directory = get_config()['repo_directory']
    os.chdir(repo_directory)
    click.echo("Check for updates...")

    local = subprocess.check_output('git rev-parse master'.split()).strip()
    remote = subprocess.check_output(
        'git ls-remote https://github.com/tldr-pages/tldr/ HEAD'.split()
    ).split()[0]
    if local != remote:
        click.echo("Updating...")
        subprocess.check_call('git checkout master'.split())
        subprocess.check_call('git pull --rebase'.split())
        build_index()
        click.echo("Update to the latest and rebuild the index.")
    else:
        click.echo("No need for updates.")


@cli.command()
def init():
    """Init config file."""
    default_config_path = path.join(
        (os.environ.get('TLDR_CONFIG_DIR') or path.expanduser('~')),
        '.tldrrc')
    if path.exists(default_config_path):
        click.echo("There is already a config file exists, "
                   "skip initializing it.")
    else:
        repo_path = click.prompt("Input the tldr repo path(absolute path)")
        if not path.exists(repo_path):
            sys.exit("Repo path not exist, clone it first.")

        platform = click.prompt("Input your platform(linux, osx or sunos)")
        if platform not in ['linux', 'osx', 'sunos']:
            sys.exit("Platform should be in linux, osx or sunos.")

        colors = {
            "description": "blue",
            "usage": "green",
            "command": "cyan"
        }

        config = {
            "repo_directory": repo_path,
            "colors": colors,
            "platform": platform
        }
        with open(default_config_path, 'w') as f:
            f.write(yaml.safe_dump(config, default_flow_style=False))

        click.echo("Initializing the config file at {0}".format(
            default_config_path))


@cli.command()
def reindex():
    """Rebuild the index."""
    build_index()
    click.echo('Rebuild the index.')


@cli.command()
@click.argument('command')
@click.option('--on', type=click.Choice(['linux', 'osx', 'sunos']),
              help='the specified platform.')
def locate(command, on):
    """Locate the command's man page."""
    location = find_page_location(command, on)
    click.echo(location)
