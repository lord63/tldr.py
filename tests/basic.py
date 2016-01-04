#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from os import path
import unittest

from click.testing import CliRunner
from tldr import cli
import mock


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.repo_dir = path.join(path.dirname(path.realpath(__file__)),
                                  'mock_tldr')
        self.config_path = path.join(self.repo_dir, '.tldrrc')

        self.runner = CliRunner()
        with mock.patch('click.prompt', side_effect=[self.repo_dir, 'linux']):
            with mock.patch('os.path.expanduser', return_value=self.repo_dir):
                self.runner.invoke(cli.init)

    def tearDown(self):
        if path.exists(self.config_path):
            os.remove(self.config_path)
