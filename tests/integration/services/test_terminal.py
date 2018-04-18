# -*- coding: utf-8 -*-

from tests.integration.services.suite import TestSuite
from stone_affiliation.services import Terminal
from stone_affiliation.models.operator import Comparison, Logical


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

        self.assertEqual(terminal_list[0]["StoneCode"], self.merchant["StoneCode"])

    def test_get_list_terminal_devices_by_merchant_id(self):
        resp = self.service.get_by_merchant_id(self.merchant["Id"])
        terminal_list = resp["TerminalList"]

        self.assertTrue(terminal_list[0]["Id"] > 0)

    def test_get_list_paged_terminal_devices_by_query(self):
        terminal_model_id = 27

        query = [
            self.service.build_condition(field="StoneCode", value=self.merchant["StoneCode"],
                                         comparison_operator=Comparison.EQUALS),
            self.service.build_condition(logical_operator=Logical.AND, field="TerminalModelId",
                                         value=terminal_model_id, comparison_operator=Comparison.EQUALS)]

        resp = self.service.list(query=query)
        self.assertEqual(resp["ListedTerminalDevices"][0]['TerminalModel']['Id'], terminal_model_id)
