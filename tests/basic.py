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
        self.runner = CliRunner()
        self.call_init_command()

    def tearDown(self):
        if path.exists(self.config_path):
            os.remove(self.config_path)

    def call_init_command(self, repo_dir=path.join(ROOT, 'mock_tldr'),
                          platform='linux'):
        with mock.patch('click.prompt', side_effect=[repo_dir, platform]):
            with mock.patch('os.path.expanduser', return_value=self.repo_dir):
                result = self.runner.invoke(cli.init)
        return result

    def call_update_command(self):
        with mock.patch('os.path.expanduser', return_value=self.repo_dir):
            with mock.patch('tldr.cli.build_index', return_value=None):
                result = self.runner.invoke(cli.update)
        return result

    def call_find_command(self, command_name):
        with mock.patch('os.path.expanduser', return_value=self.repo_dir):
            result = self.runner.invoke(cli.find, [command_name])
        return result

    def call_reindex_command(self):
        with mock.patch('os.path.expanduser', return_value=self.repo_dir):
            result = self.runner.invoke(cli.reindex)
        return result
