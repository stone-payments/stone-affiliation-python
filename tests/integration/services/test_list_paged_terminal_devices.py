# -*- coding: utf-8 -*-

from tests.integration.services.suite import TestSuite
from stone_affiliation.services import ListPagedTerminalDevices


class TestListPagedTerminalDevices(TestSuite):
    """
    ListTerminalDevices testa a integração da classe de serviço ListTerminalDevices
    com a API de credenciamento
    """

    def setUp(self):
        super().setUp()
        self.service = ListPagedTerminalDevices(**self.get_config())

    def test_message_ok(self):
        resp = self.service.get_by_stonecode("192489630")
        status_message_ok = "OK"
        self.assertEquals(resp["Status"]["Message"], status_message_ok)

    def test_get_list_terminal_by_stonecode(self):
        resp = self.service.get_by_stonecode("919243797")
        terminal_list = resp["ListedTerminalDevices"]
        min_terminal = 0
        self.assertTrue(len(terminal_list) > min_terminal)
