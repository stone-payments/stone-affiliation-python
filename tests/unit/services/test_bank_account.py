# -*- coding: utf-8 -*-

from random import randint
from mock import patch
from tests.suite import TestSuite
from stone_affiliation.services import BankAccount
from stone_affiliation.models.operator import Comparison


class TestBankAccount(TestSuite):
    """
    TestBankAccount testa unitariamente a classe de serviço BankAccount
    """

    def setUp(self):
        self.service = BankAccount("api_url", "app_key", "secret_key",
                                   "source_ip", "user_email")

    @patch("stone_affiliation.services.service.Service._base_data",
           return_value={})
    @patch("stone_affiliation.services.service.Service.build_url",
           return_value="url_builded")
    @patch("stone_affiliation.services.service.Service._request",
           return_value="response")
    def test_list(self, mock_requester, mock_url_builder,
                  mock_data_builder):
        stonecode = randint(0, 100)
        actual = self.service.list(stonecode)

        mock_data_builder.assert_called_once_with("GetSettlementBankAccount")
        mock_url_builder.assert_called_once_with(
            "/Merchant/MerchantService.svc/merchant/GetSettlementBankAccount/")
        mock_requester.assert_called_once_with("url_builded", {
            "StoneCode": stonecode
        })
        self.assertEqual(actual, 'response')
