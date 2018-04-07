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

    def test_get_by_stonecode(self):
        resp = self.service.get_by_stonecode("192489630")
        status_message_ok = "OK"
        self.
        self.assertTrue(len(resp["TerminalList"]) > 0)

# {'MessageList': [], 'Status': {'Code': 'OK', 'Message': 'OK', 'MessageRefCode': 'TXT_OK'}, 'TerminalList': []}