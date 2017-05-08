#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import unittest

import mock

from tldr.parser import parse_page


class TestParse(unittest.TestCase):
    def test_parse_page(self):
        mock_page = (
            '#node\n\n'
            '> Main node command\n\n'
            '- Call an interactive node shell\n\n'
            '`node`\n\n'
            '- Execute node on a JS file\n\n'
            '`node {{FILENAME}}.js`\n\n'
        )
        self._assert_mock_read(mock_page)

    def test_parse_new_syntax_page(self):
        mock_page = (
            'node\n'
            '====\n\n'
            '> Main node command\n\n'
            'Call an interactive node shell\n\n'
            '    node\n\n'
            'Execute node on a JS file\n\n'
            '    node {{FILENAME}}.js\n\n'
        )
        self._assert_mock_read(mock_page)

    def _assert_mock_read(self, page_content):
        mock_config = {
            'colors': {
                'command': 'cyan',
                'description': 'blue',
                'usage': 'green'
            },
            'platform': 'linux',
            'repo_directory': '/tmp/tldr'
        }
        expected_result = (
            '\n'
            '\x1b[0m\x1b[34m  Main node command\n'
            '\x1b[0m\n\x1b[0m\x1b[32m- Call an interactive node shell'
            '\n\x1b[0m\n\x1b[0m\x1b[36m  node\n'
            '\x1b[0m\n\x1b[0m\x1b[32m- Execute node on a JS file\n'
            '\x1b[0m\n\x1b[0m\x1b[36m  node {{FILENAME}}.js\n'
            '\x1b[0m\n\x1b[0m'
        )
        with mock.patch('tldr.parser.get_config', return_value=mock_config):
            with mock.patch('io.open', mock.mock_open(read_data=page_content)):
                result = parse_page('/repo_directory/pages/common/node.md')
                assert ''.join(result) == expected_result
