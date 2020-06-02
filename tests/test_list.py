#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from basic import BasicTestCase


class Testlist(BasicTestCase):
    def test_list_command(self):
        result = self.call_list_command('')
        assert result.output == 'du\ntcpflow\ntldr\n'

    def test_list_command_with_platform(self):
        result = self.call_list_command('osx')
        assert result.output == 'airport\ndu\ntldr\n'
