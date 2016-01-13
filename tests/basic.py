#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from os import path
import unittest

from click.testing import CliRunner
from tldr import cli
import mock


ROOT = path.dirname(path.realpath(__file__))


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.repo_dir = path.join(ROOT, 'mock_tldr')
        self.config_path = path.join(self.repo_dir, '.tldrrc')
        os.environ['TLDR_CONFIG_DIR'] = self.repo_dir
        self.runner = CliRunner()
        self.call_init_command()

    def tearDown(self):
        if path.exists(self.config_path):
            os.remove(self.config_path)

    def call_init_command(self, repo_dir=path.join(ROOT, 'mock_tldr'),
                          platform='linux'):
        with mock.patch('click.prompt', side_effect=[repo_dir, platform]):
            result = self.runner.invoke(cli.init)
        return result

    def call_update_command(self):
        with mock.patch('tldr.cli.build_index', return_value=None):
            result = self.runner.invoke(cli.update)
        return result

    def call_find_command(self, command_name):
        result = self.runner.invoke(cli.find, [command_name])
        return result

    def call_reindex_command(self):
        result = self.runner.invoke(cli.reindex)
        return result

    def call_locate_command(self, command_name):
        result = self.runner.invoke(cli.locate, [command_name])
        return result
