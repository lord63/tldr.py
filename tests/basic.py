#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from os import path
import unittest


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.config_path = path.join(path.expanduser('~'), '.tldrrc')
        self.repe_dir = path.dirname(path.realpath(__file__))
        if path.exists(self.config_path):
            os.remove(self.config_path)

    def tearDown(self):
        if path.exists(self.config_path):
            os.remove(self.config_path)
