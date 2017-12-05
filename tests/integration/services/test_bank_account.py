# -*- coding: utf-8 -*-

from tests.integration.services.suite import TestSuite
from stone_affiliation.services import BankAccount


class TestBankAccount(TestSuite):
    """
    TestBankAccount testa a integração da classe de serviço BankAccount
    com a API de credenciamento
    """

    def setUp(self):
        super().setUp()
        self.service = BankAccount(**self.get_config())

    def test_list(self):
        resp = self.service.list(self.merchant["StoneCode"])
        self.assertEquals(
            resp["SettlementBankAccount"]["AffiliationCode"],
            self.merchant["StoneCode"])
