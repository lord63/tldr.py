#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from os import path

from basic import BasicTestCase


class TestLocate(BasicTestCase):
    def test_common_command(self):
        assert (self.call_locate_command('tldr').output.strip() ==
                path.join(self.repo_dir, 'pages', 'common', 'tldr.md'))
