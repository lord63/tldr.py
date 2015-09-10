#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click

from tldr.config import get_config


def parse_page(page):
    """Parse the command man page."""
    colors = get_config()['colors']
    with open(page) as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('#'):
            continue
        elif line.startswith('>'):
            click.secho(line.replace('>', ' '), fg=colors['description'],
                        nl=False)
        elif line.startswith('-'):
            click.secho(line, fg=colors['usage'], nl=False)
        elif line.startswith('`'):
            click.secho('  ' + line.replace('`', ''), fg=colors['command'],
                        nl=False)
        else:
            click.secho(line, nl=False)
