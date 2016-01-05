#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import io
import os
from os import path

import yaml

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
        result = self.call_init_command()
        assert result.output == (
            "There is already a config file exists, skip initializing it.\n"
        )

    def test_bad_repo_location(self):
        os.remove(self.config_path)
        result = self.call_init_command(repo_dir='/notexist')
        assert result.exception.args[0] == (
            "Repo path not exist, clone it first."
        )

    def test_back_platform_input(self):
        os.remove(self.config_path)
        result = self.call_init_command(platform='myos')
        assert result.exception.args[0] == (
            "Platform should be in linux, osx or sunos."
        )
