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
