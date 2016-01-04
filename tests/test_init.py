#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import io
import os
from os import path

import yaml
import mock

from tldr import cli
from basic import BasicTestCase


class TestInit(BasicTestCase):
    def test_init(self):
        assert path.exists(self.config_path)

        expected_config = {
            'colors': {
                'command': 'cyan',
                'description': 'blue',
                'usage': 'green'
            },
            'platform': 'linux',
            'repo_directory': self.repo_dir
        }
        with io.open(self.config_path, encoding='utf-8') as f:
            config = yaml.safe_load(f)
        assert expected_config == config

    def test_wrong_platform_input(self):
        with mock.patch('click.prompt', side_effect=[self.repo_dir, 'linux']):
            with mock.patch('os.path.expanduser', return_value=self.repo_dir):
                result = self.runner.invoke(cli.init)
        assert result.output == (
            "There is already a config file exists, skip initializing it.\n"
        )

    def test_bad_repo_location(self):
        os.remove(self.config_path)
        with mock.patch('click.prompt', side_effect=['/notexist', 'linux']):
            with mock.patch('os.path.expanduser', return_value=self.repo_dir):
                result = self.runner.invoke(cli.init)
        assert result.exception.args[0] == (
            "Repo path not exist, clone it first."
        )

    def test_back_platform_input(self):
        os.remove(self.config_path)
        with mock.patch('click.prompt', side_effect=[self.repo_dir, 'myos']):
            with mock.patch('os.path.expanduser', return_value=self.repo_dir):
                result = self.runner.invoke(cli.init)
        assert result.exception.args[0] == (
            "Platform should be in linux, osx or sunos."
        )
