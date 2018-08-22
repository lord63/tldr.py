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
            output_lines.append(process_headline(line, colors))
        elif is_description(line):
            output_lines.append(process_description_line(line, colors))
        elif is_old_usage(line):
            output_lines.append(process_usage_line(line, colors))
        elif is_code_example(line):
            output_lines.append(process_command_line(line, colors))
        elif is_line_break(line):
            output_lines.append(line)
        else:
            output_lines.append(process_usage_line('- ' + line, colors))
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


def _color_text_block(line,
                      start_marker,
                      end_marker,
                      color_in,
                      color_out,
                      preserve_marker=False):
    """Color the block of text between start_marker and end_marker.

    with color_in
    """
    color_reset_text = click.style('', fg='reset')
    replace_open = color_reset_text + click.style('',
                                                  fg=color_in, reset=False)
    replace_close = color_reset_text + click.style('',
                                                   fg=color_out, reset=False)

    if preserve_marker:
        replace_open = start_marker + replace_open
        replace_close = replace_close + end_marker

    line = line.replace(start_marker, replace_open)
    line = line.replace(end_marker, replace_close)

    return line


def _color_command_option(line, color_in, color_out):
    """Color the command options given in usage or desription inside []."""
    line = _color_text_block(line,
                             '[',
                             ']',
                             color_in,
                             color_out,
                             preserve_marker=True)

    return line


def _color_command_parameter(line, color_in, color_out):
    """Color the parameters in code examples."""
    line = _color_text_block(line,
                             '{{',
                             '}}',
                             color_in,
                             color_out,
                             preserve_marker=False)

    return line


def _color_inline_command(line, color_in, color_out):
    """Color the inline commands in usage or description."""
    line = _color_text_block(line,
                             '`',
                             '`',
                             color_in,
                             color_out,
                             preserve_marker=True)

    return line


def process_command_line(line, colors):
    """Color the example command lines."""
    default_color = colors['command']
    line = line.rstrip()
    line = '    ' + line[1:] if line.startswith('`') else line[2:]
    line = line[:-1] if line.endswith('`') else line

    line = _color_command_parameter(line, colors['parameter'], default_color)
    line = click.style(line, fg=default_color)

    return line + '\n'


def process_usage_line(line, colors):
    """Color the usage line."""
    default_color = colors['usage']
    line = line.rstrip()

    line = _color_command_option(line, colors['command'], default_color)
    line = _color_inline_command(line, colors['command'], default_color)
    line = click.style(line, fg=default_color)

    return line + '\n'


def process_description_line(line, colors):
    """Color the description line."""
    default_color = colors['description']
    line = line.rstrip()
    if line[0] == '>' or line[:2] == ' >':
        line = line.replace('>', ' ', 1)

    line = _color_command_option(line, colors['command'], default_color)
    line = _color_inline_command(line, colors['command'], default_color)
    line = click.style(line, fg=default_color)

    return line + '\n'


def process_headline(line, colors):
    """Color the headline."""
    line_p = line.split(' ', 1)
    line_p[0] = click.style(line_p[0], fg='black')
    line_p[1] = click.style(line_p[1], fg=colors['headline'], bold=True)

    return ' '.join(line_p)
