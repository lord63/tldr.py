#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click


def parse_page(page):
    """Parse the command man page."""
    with open(page) as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('#'):
            continue
        elif line.startswith('>'):
            click.secho(line.replace('>', ' '), fg='blue', nl=False)
        elif line.startswith('-'):
            click.secho(line, fg='green', nl=False)
        elif line.startswith('`'):
            click.secho('  ' + line.replace('`', ''), fg='cyan', nl=False)
        else:
            click.secho(line, nl=False)
