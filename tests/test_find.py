#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from os import path
import unittest

from click.testing import CliRunner
import mock

from tldr import cli


class TestFind(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        with mock.patch('click.prompt', side_effect=['/tmp/tldr', 'linux']):
            runner = CliRunner()
            result = runner.invoke(cli.init)

    def test_find_tldr_in_common(self):
        result = self.runner.invoke(cli.find, ['tldr'])
        assert result.output == (
            '\n  Simplified man pages\n\n- get typical usages of a command '
            '(hint: this is how you got here!)\n\n  tldr {{command}}\n'
        )

    def test_find_tcpflow_in_linux(self):
        result = self.runner.invoke(cli.find, ['tcpflow'])
        assert result.output == (
            '\n  Capture TCP traffic for debugging and analysis\n\n- Show all '
            'data on the given interface and port\n\n  tcpflow -c -i {{eth0}} '
            'port {{80}}\n'
        )

    def test_can_not_find_something(self):
        result = self.runner.invoke(cli.find, ['yoooooooooooooo'])
        assert result.output == (
            "Sorry, we don't support command: yoooooooooooooo right now.\nYou "
            "can file an issue or send a PR on github:\n    https://github.com"
            "/tldr-pages/tldr\n"
        )

    def test_find_command_do_not_support_your_platform(self):
        result = self.runner.invoke(cli.find, ['airport'])
        assert result.output == (
            'Sorry, command airport is not supported on your platform.\nYou '
            'can file an issue or send a PR on github:\n    https://github.'
            'com/tldr-pages/tldr\n'
        )
