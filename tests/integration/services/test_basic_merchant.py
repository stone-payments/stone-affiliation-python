# -*- coding: utf-8 -*-

from tests.integration.services.suite import TestSuite
from stone_affiliation.services import BasicMerchant


class TestBasicMerchant(TestSuite):
    """
    TestBasicMerchant testa a integração da classe de serviço BasicMerchant
    com a API de credenciamento
    """

    def setUp(self):
        super().setUp()
        self.service = BasicMerchant(**self.get_config())

    def test_get_by_stonecode(self):
        resp = self.service.get_by_stonecode(self.merchant["StoneCode"])
        self.assertEquals(
            resp["Merchant"]["AffiliationCode"],
            self.merchant["StoneCode"])

    def test_get_by_merchant_id(self):
        resp = self.service.get_by_merchant_id(self.merchant["Id"])
        self.assertEquals(
            resp["Merchant"]["Id"],
            self.merchant["Id"])
