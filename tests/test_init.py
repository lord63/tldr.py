#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from os import path
import unittest

from click.testing import CliRunner
import mock
import yaml

from tldr import cli


class TestInit(unittest.TestCase):
    def setUp(self):
        self.config_path = path.join(path.expanduser('~'), '.tldrrc')
        if path.exists(self.config_path):
            os.remove(self.config_path)

    def tearDown(self):
        if path.exists(self.config_path):
            os.remove(self.config_path)

    def test_init(self):
        with mock.patch('click.prompt', side_effect=['/tmp/tldr', 'linux']):
            runner = CliRunner()
            result = runner.invoke(cli.init)
        assert result.output == 'Initializing the config file at ~/.tldrrc\n'
        assert path.exists(self.config_path)

        expected_config = {
            'colors': {
                'command': 'cyan',
                'description': 'blue',
                'usage': 'green'
            },
            'platform': 'linux',
            'repo_directory': '/tmp/tldr'
        }
        with open(self.config_path) as f:
            config = yaml.safe_load(f)
        assert expected_config == config
