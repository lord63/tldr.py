#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import io
import click

from tldr.config import get_config


def parse_page(page):
    """Parse the command man page."""
    colors = get_config()['colors']
    with io.open(page, encoding='utf-8') as f:
        lines = f.readlines()
    output_lines = []
    for line in lines:
        if line.startswith('#'):
            continue
        elif line.startswith('>'):
            output_lines.append(click.style(line.replace('>', ' '),
                                            fg=colors['description']))
        elif line.startswith('-'):
            output_lines.append(click.style(line, fg=colors['usage']))
        elif line.startswith('`'):
            output_lines.append(click.style('  ' + line.replace('`', ''),
                                            fg=colors['command']))
        else:
            output_lines.append(click.style(line))
    return output_lines
