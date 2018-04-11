# -*- coding: utf-8 -*-

from tests.integration.services.suite import TestSuite
from stone_affiliation.services import Merchant


class TestMerchant(TestSuite):
    """
    TestMerchant testa a integração da classe de serviço Merchant
    com a API de credenciamento
    """

    def setUp(self):
        super().setUp()
        self.service = Merchant(**self.get_config())

    def test_get_by_id(self):
        resp = self.service.get_by_id(self.merchant["Id"])
        self.assertDictEqual(resp["ListedMerchants"][0], self.merchant)

    def test_get_by_stonecode(self):
        resp = self.service.get_by_stonecode(self.merchant["StoneCode"])
        self.assertDictEqual(resp["ListedMerchants"][0], self.merchant)

    def test_get_by_ids(self):
        resp = self.service.get_by_ids(
            [merchant["Id"] for merchant in self.merchants])
        self.assertEqual(len(resp["ListedMerchants"]), len(self.merchants))

    def test_get_by_stonecodes(self):
        resp = self.service.get_by_stonecodes(
            [merchant["StoneCode"] for merchant in self.merchants])
        self.assertEqual(len(resp["ListedMerchants"]), len(self.merchants))

    def test_get_list_paged_terminal_devices_by_stonecode(self):
        resp = self.service.get_list_paged_terminal_devices_by_stonecode(self.merchant["StoneCode"])
        terminal_list = resp["ListedTerminalDevices"]
        min_terminal = 0
        self.assertTrue(len(terminal_list) > min_terminal)

    def test_get_list_terminal_devices_by_merchant_id(self):
        merchant_id = 10168
        min_terminal_device = 0
        resp = self.service.get_list_terminal_devices_by_merchant_id(merchant_id)
        self.assertTrue(len(resp["TerminalList"]) > min_terminal_device)
