#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import io
import os
from os import path
import sys

import yaml


def get_config():
    """Get the configurations from .tldrrc and return it as a dict."""
    config_path = path.join(
        (os.environ.get('TLDR_CONFIG_DIR') or path.expanduser('~')),
        '.tldrrc')
    if not path.exists(config_path):
        sys.exit("Can't find config file at: {0}. You may use `tldr init` "
                 "to init the config file.".format(config_path))

    with io.open(config_path, encoding='utf-8') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.scanner.ScannerError:
            sys.exit("The config file is not a valid YAML file.")

    supported_colors = ['black', 'red', 'green', 'yellow', 'blue',
                        'magenta', 'cyan', 'white']
    if not set(config['colors'].values()).issubset(set(supported_colors)):
        sys.exit("Unsupported colors in config file: {0}.".format(
            ', '.join(set(config['colors'].values()) - set(supported_colors))))
    if not path.exists(config['repo_directory']):
        sys.exit("Can't find the tldr repo, check the `repo_directory` "
                 "setting in config file.")

    return config
