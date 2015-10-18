#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from os import path
import unittest

from click.testing import CliRunner
import mock

from tldr.config import get_config
from tldr import cli


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config_path = path.join(path.expanduser('~'), '.tldrrc')
        if path.exists(self.config_path):
            os.remove(self.config_path)

        self.runner = CliRunner()
        with mock.patch('click.prompt', side_effect=['/tmp/tldr', 'linux']):
            self.runner.invoke(cli.init)

    def tearDown(self):
        if path.exists(self.config_path):
            os.remove(self.config_path)

    def test_config_not_exist(self):
        with mock.patch('os.path.exists', side_effect=[False, True]):
            with self.assertRaises(SystemExit) as error:
                get_config()
            assert error.exception.message == (
                ("Can't find config file at: {0}. You may use `tldr init` to "
                 "init the config file.").format(self.config_path)
            )

    def test_invalid_yaml_file(self):
        with mock.patch('io.open',
                        mock.mock_open(read_data="%YAML:1.0\nname:jhon")):
            with self.assertRaises(SystemExit) as error:
                get_config()
            assert error.exception.message == (
                "The config file is not a valid YAML file."
            )

    def test_unsupported_color_in_config(self):
        mock_config = {
            'colors': {
                'command': 'indigo',
                'description': 'orange',
                'usage': 'green'
            },
            'platform': 'linux',
            'repo_directory': '/tmp/tldr'
        }
        with mock.patch('yaml.safe_load', return_value=mock_config):
            with self.assertRaises(SystemExit) as error:
                get_config()
            assert error.exception.message == (
                "Unsupported colors in config file: orange, indigo."
            )

    def test_repo_directory_not_exist(self):
        with mock.patch('os.path.exists', side_effect=[True, False]):
            with self.assertRaises(SystemExit) as error:
                get_config()
            assert error.exception.message == (
                "Can't find the tldr repo, check the `repo_direcotry` "
                "setting in config file."
            )
