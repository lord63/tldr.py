#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click

from tldr import __version__


@click.group(context_settings={'help_option_names': ('-h', '--help')})
@click.version_option(__version__, '-V', '--version', message='%(version)s')
def cli():
    """A python client for tldr: simplified and community-driven man pages."""
    pass


@cli.command()
def update():
    """Update to the latest pages."""
    pass


@cli.command()
def init():
    """Init config file and download the man pages."""
    pass
