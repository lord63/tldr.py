#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from os import path
import shutil

from basic import BasicTestCase


class Testlist(BasicTestCase):
    def setUp(self):
        super(Testlist, self).setUp()

        # Add a new page.
        self.page_path = path.join(self.repo_dir, 'pages')

        # Backup the index.json.
        shutil.copy(path.join(self.page_path, 'index.json'),
                    path.join(self.page_path, 'index_bak.json'))
        self.call_reindex_command()

    def tearDown(self):
        super(Testlist, self).tearDown()
        # Restore the index.json.
        if path.exists(path.join(self.page_path, 'index_bak.json')):
            shutil.move(path.join(self.page_path, 'index_bak.json'),
                        path.join(self.page_path, 'index.json'))

    def test_common_command(self):
        self._assert_command_output(
            '',
            'airport du tcpflow tldr\n'
        )

    def _assert_command_output(self, command_name, expected_output,
                               platform=''):
        result = self.call_list_command(command_name, platform)
        assert result.output == expected_output
