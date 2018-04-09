# -*- coding: utf-8 -*-

from tests.integration.services.suite import TestSuite
from stone_affiliation.services import ListTerminalDevices


class TestListTerminalDevices(TestSuite):
    """
    ListTerminalDevices testa a integração da classe de serviço ListTerminalDevices
    com a API de credenciamento
    """

    def setUp(self):
        super().setUp()
        self.service = ListTerminalDevices(**self.get_config())

    def test_message_ok(self):
        resp = self.service.get_by_merchant_id("192489630")
        status_message_ok = "OK"
        self.assertEquals(resp["Status"]["Message"], status_message_ok)

    def test_get_list_terminal_by_merchant_id(self):
        resp = self.service.get_by_merchant_id(10168)
        self.assertTrue(len(resp["TerminalList"]) > 0)
