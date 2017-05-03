#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from basic import BasicTestCase


class TestFind(BasicTestCase):
    def test_find_tldr_in_common(self):
        self._assert_command_output(
            'tldr',
            ('\n  Simplified man pages\n\n- get typical usages of a command '
             '(hint: this is how you got here!)\n\n  tldr {{command}}\n\n')
        )

    def test_find_tcpflow_in_linux(self):
        self._assert_command_output(
            'tcpflow',
            ('\n  Capture TCP traffic for debugging and analysis\n\n'
             '- Show all data on the given interface and port\n\n'
             '  tcpflow -c -i {{eth0}} port {{80}}\n\n')
        )

    def test_find_airport_on_maxos(self):
        self._assert_command_output(
            'airport',
            ('\n  Wireless network configuration utility.\n\n'
             '- Show current wireless status information:\n\n'
             '  airport -I\n\n'
             '- Sniff wireless traffic on channel 1:\n\n'
             '  airport sniff {{1}}\n\n'
             '- Scan for available wireless networks:\n\n'
             '  airport -s\n\n'
             '- Disassociate from current airport network:\n\n'
             '  sudo airport -z\n\n'),
            'osx'
        )

    def test_can_not_find_something(self):
        self._assert_command_output(
            'yoooooooooooooo',
            ("Sorry, we don't support command: yoooooooooooooo right now.\n"
             "You can file an issue or send a PR on github:\n"
             "    https://github.com/tldr-pages/tldr\n")
        )

    def test_find_command_do_not_support_your_platform(self):
        self._assert_command_output(
            'airport',
            ('Sorry, command airport is not supported on your platform.\n'
             'You can file an issue or send a PR on github:\n'
             '    https://github.com/tldr-pages/tldr\n')
        )

    def _assert_command_output(self, command_name, expected_output,
                               platform=''):
        result = self.call_find_command(command_name, platform)
        assert result.output == expected_output
