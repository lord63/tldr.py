#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from os import path
import shutil

from basic import BasicTestCase


class TestReindex(BasicTestCase):
    def setUp(self):
        super(TestReindex, self).setUp()

        # Add a new page.
        self.page_path = path.join(self.repo_dir, 'pages')
        self.new_page = path.join(self.page_path, 'linux', 'blabla.md')
        shutil.copy(path.join(self.page_path, 'linux', 'tcpflow.md'),
                    self.new_page)

        # Backup the index.json.
        shutil.copy(path.join(self.page_path, 'index.json'),
                    path.join(self.page_path, 'index_bak.json'))

    def tearDown(self):
        super(TestReindex, self).tearDown()
        if path.exists(self.new_page):
            os.remove(self.new_page)
        # Restore the index.json.
        if path.exists(path.join(self.page_path, 'index_bak.json')):
            shutil.move(path.join(self.page_path, 'index_bak.json'),
                        path.join(self.page_path, 'index.json'))

    def test_reindex(self):
        before_reindex = self.call_find_command('blabla', platform='')
        assert 'Sorry' in before_reindex.output
        self.call_reindex_command()
        after_reindex = self.call_find_command('blabla', platform='')
        assert 'tcpflow' in after_reindex.output
