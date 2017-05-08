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
    for line in lines[1:]:
        if is_headline(line):
            continue
        elif is_description(line):
            output_lines.append(click.style(line.replace('>', ' '),
                                            fg=colors['description']))
        elif is_old_usage(line):
            output_lines.append(click.style(line, fg=colors['usage']))
        elif is_code_example(line):
            line = '  ' + line if line.startswith('`') else line[2:]
            output_lines.append(click.style(line.replace('`', ''),
                                            fg=colors['command']))
        elif is_line_break(line):
            output_lines.append(click.style(line))
        else:
            output_lines.append(click.style('- ' + line, fg=colors['usage']))
    return output_lines


def is_headline(line):
    return line.startswith(('#', '='))


def is_description(line):
    return line.startswith('>')


def is_old_usage(line):
    return line.startswith('-')


def is_code_example(line):
    return line.startswith(('`', '    '))


def is_line_break(line):
    return line.startswith("\n")
