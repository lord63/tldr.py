#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from os import path
import unittest

from click.testing import CliRunner
from tldr import cli
import mock
import pytest


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.repo_dir = path.join(path.dirname(path.realpath(__file__)),
                                  'mock_tldr')
        self.config_path = path.join(self.repo_dir, '.tldrrc')

        self.runner = CliRunner()
        with mock.patch('click.prompt', side_effect=[self.repo_dir, 'linux']):
            self.call_init_command()

    def tearDown(self):
        if path.exists(self.config_path):
            os.remove(self.config_path)

    def call_init_command(self):
        with mock.patch('os.path.expanduser', return_value=self.repo_dir):
            result = self.runner.invoke(cli.init)
        return result

    def call_update_command(self):
        with mock.patch('os.path.expanduser', return_value=self.repo_dir):
            result = self.runner.invoke(cli.update)
        return result

    def call_find_command(self, command_name):
        with mock.patch('os.path.expanduser', return_value=self.repo_dir):
            result = self.runner.invoke(cli.find, [command_name])
        return result
