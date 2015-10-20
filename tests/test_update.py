#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import mock

from tldr import cli
from basic import BasicTestCase


class TestUpdate(BasicTestCase):
    def test_update_available(self):
        mock_different_sha1 = [
            '8f82e7445fef6cc83c2e02b82df5f92fe0a909c6',
            'a4013ab1b14812624bbddf96feb1bfa2b03564f6'
        ]
        self._assert_update_info(mock_different_sha1, 'Updating...')

    def test_no_need_for_update(self):
        mock_same_sha1 = [
            '8f82e7445fef6cc83c2e02b82df5f92fe0a909c6',
            '8f82e7445fef6cc83c2e02b82df5f92fe0a909c6'
        ]
        self._assert_update_info(mock_same_sha1, 'No need for updates.')

    def _assert_update_info(self, mock_sha1, expected_message):
        with mock.patch('subprocess.check_output', side_effect=mock_sha1):
            with mock.patch('subprocess.check_call', side_effect=[0, 0]):
                result = self.runner.invoke(cli.update)
        assert expected_message in result.output
