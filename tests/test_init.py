#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import io
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
            'repo_directory': self.repe_dir
        }
        with io.open(self.config_path) as f:
            config = yaml.safe_load(f)
        assert expected_config == config
