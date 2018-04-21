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
        stonecode = "192489630"
        serial_number = "11188CT30467867"

        stonecode_condition = {
            "Field": "StoneCode",
            "Value": stonecode,
            "LogicalOperator": Logical.AND,
            "ComparisonOperator": Comparison.EQUALS
        }

        serial_number_condition = {
            "Field": "SerialNumber",
            "Value": serial_number,
            "LogicalOperator": Logical.AND,
            "ComparisonOperator": Comparison.EQUALS
        }

        query = [
            self.service.build_condition(field=stonecode_condition['Field'],
                                         value=stonecode_condition["Value"],
                                         comparison_operator=stonecode_condition["ComparisonOperator"],
                                         logical_operator=stonecode_condition['LogicalOperator']),

            self.service.build_condition(field=serial_number_condition['Field'],
                                         value=serial_number_condition["Value"],
                                         comparison_operator=serial_number_condition["ComparisonOperator"],
                                         logical_operator=serial_number_condition['LogicalOperator'])
        ]

        resp = self.service.list(query=query)
        self.assertEqual(resp["ListedTerminalDevices"][0]['StoneCode'], stonecode)
        self.assertEqual(resp["ListedTerminalDevices"][0]['SerialNumber'], serial_number)

