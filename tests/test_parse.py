#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import unittest

import mock

from tldr.parser import parse_page


class TestParse(unittest.TestCase):
    def test_parse_page(self):
        mock_config = {
            'colors': {
                'command': 'cyan',
                'description': 'blue',
                'usage': 'green'
            },
            'platform': 'linux',
            'repo_directory': '/tmp/tldr'
        }
        with mock.patch('tldr.parser.get_config', return_value=mock_config):
            result = parse_page('/tmp/tldr/pages/sunos/prctl.md')
            assert ''.join(result) == (
                '\n\x1b[0m\x1b[34m  Get or set the resource controls of '
                'running processes,\n\x1b[0m\x1b[34m  tasks, and projects\n'
                '\x1b[0m\n\x1b[0m\x1b[32m- examine process limits and '
                'permissions\n\x1b[0m\n\x1b[0m\x1b[36m  prctl {{PID}}\n\x1b'
                '[0m\n\x1b[0m\x1b[32m- examine process limits and permissions '
                'in machine parseable format\n\x1b[0m\n\x1b[0m\x1b[36m  prctl '
                '-P {{PID}}\n\x1b[0m\n\x1b[0m\x1b[32m- Get specific limit for '
                'a running process\n\x1b[0m\n\x1b[0m\x1b[36m  prctl -n '
                'process.max-file-descriptor {{PID}}\x1b[0m'
            )
