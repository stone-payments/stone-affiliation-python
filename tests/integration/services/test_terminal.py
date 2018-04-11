# -*- coding: utf-8 -*-

from tests.integration.services.suite import TestSuite
from stone_affiliation.services import Terminal


class TestTerminal(TestSuite):
    """
    TestTerminal testa a integração da classe de serviço Terminal
    com a API de credenciamento
    """

    def setUp(self):
        super().setUp()
        self.service = Terminal(**self.get_config())

    def test_get_list_paged_terminal_devices_by_stonecode(self):
        resp = self.service.get_by_stonecode(self.merchant["StoneCode"])
        terminal_list = resp["ListedTerminalDevices"]
        min_terminal = 0
        self.assertTrue(len(terminal_list) > min_terminal)

    def test_get_list_terminal_devices_by_merchant_id(self):
        merchant_id = 10168
        min_terminal_device = 0
        resp = self.service.get_by_merchant_id(merchant_id)
        self.assertTrue(len(resp["TerminalList"]) > min_terminal_device)
