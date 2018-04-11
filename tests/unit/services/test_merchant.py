# -*- coding: utf-8 -*-

from random import randint
from mock import patch
from tests.suite import TestSuite
from stone_affiliation.services import Merchant
from stone_affiliation.models.operator import Comparison


class TestMerchant(TestSuite):
    """
    TestMerchant testa unitariamente a classe de serviço Merchant
    """

    def setUp(self):
        self.service = Merchant("api_url", "app_key", "secret_key",
                                "source_ip", "user_email")

    @patch("stone_affiliation.services.service.Service.build_condition",
           return_value="condition")
    @patch("stone_affiliation.services.Merchant.list")
    def test_get_by_id(self, mock_requester, mock_builder):
        identifier = randint(0, 1000)
        actual = self.service.get_by_id(identifier)

        mock_builder.assert_called_once_with(
            "Id", identifier, Comparison.EQUALS)

        mock_requester.assert_called_once_with(query=["condition"])

    @patch("stone_affiliation.services.service.Service.build_condition",
           return_value="condition")
    @patch("stone_affiliation.services.Merchant.list")
    def test_get_by_stonecode(self, mock_requester, mock_builder):
        stonecode = randint(0, 1000)
        actual = self.service.get_by_stonecode(stonecode)

        mock_builder.assert_called_once_with(
            "StoneCode", stonecode, Comparison.EQUALS)

        mock_requester.assert_called_once_with(query=["condition"])

    @patch("stone_affiliation.services.service.Service.build_condition",
           return_value="condition")
    @patch("stone_affiliation.services.Merchant.list")
    def test_get_by_stonecodes(self, mock_requester, mock_builder):
        stonecodes = []

        for _ in range(0, 10):
            stonecodes.append(randint(0, 1000))

        actual = self.service.get_by_stonecodes(stonecodes, 2)

        mock_builder.assert_called_once_with(
            "StoneCode", stonecodes, Comparison.IN)

        mock_requester.assert_called_once_with(query=["condition"], page=2)

    @patch("stone_affiliation.services.service.Service.build_condition",
           return_value="condition")
    @patch("stone_affiliation.services.Merchant.list")
    def test_get_by_ids(self, mock_requester, mock_builder):
        identifiers = []

        for _ in range(0, 10):
            identifiers.append(randint(0, 1000))

        actual = self.service.get_by_ids(identifiers, 2)

        mock_builder.assert_called_once_with("Id", identifiers, Comparison.IN)

        mock_requester.assert_called_once_with(query=["condition"], page=2)

    @patch("stone_affiliation.services.service.Service._base_data",
           return_value={})
    @patch("stone_affiliation.services.service.Service.build_url",
           return_value="url_builded")
    @patch("stone_affiliation.services.service.Service._request",
           return_value="response")
    def test_list(self, mock_requester, mock_url_builder,
                  mock_data_builder):
        actual = self.service.list(30, 1000, "my_query")

        mock_data_builder.assert_called_once_with("ListMerchants")
        mock_url_builder.assert_called_once_with(
            "/Merchant/MerchantService.svc/merchant/ListMerchants/")
        mock_requester.assert_called_once_with("url_builded", {
            "ListComplementaryData": True,
            "QueryExpression": {
                "ConditionList": "my_query",
                "PageNumber": 30,
                "RowsPerPage": 1000
            }
        })
        self.assertEqual(actual, 'response')

    @patch("stone_affiliation.services.service.Service._base_data", return_value={})
    @patch("stone_affiliation.services.service.Service.build_url", return_value="url_builded")
    @patch("stone_affiliation.services.service.Service._request", return_value="response")
    def test_get_list_paged_terminal_devices_by_stonecode(self, mock_requester, mock_url_builder, mock_data_builder):
        actual = self.service.get_list_paged_terminal_devices_by_stonecode("919243797")

        mock_data_builder.assert_called_once_with("ListPagedTerminalDevices")
        mock_url_builder.assert_called_once_with("/Merchant/MerchantService.svc/merchant/ListPagedTerminalDevices/")
        self.assertEqual(actual, 'response')

    @patch("stone_affiliation.services.service.Service._base_data", return_value={})
    @patch("stone_affiliation.services.service.Service.build_url", return_value="url_builded")
    @patch("stone_affiliation.services.service.Service._request", return_value="response")
    def test_get_list_terminal_devices_by_merchant_id(self, mock_requester, mock_url_builder, mock_data_builder):
        actual = self.service.get_list_terminal_devices_by_merchant_id("516165165")

        mock_data_builder.assert_called_once_with("ListTerminalDevices")
        mock_url_builder.assert_called_once_with("/Merchant/MerchantService.svc/merchant/ListTerminalDevices/")
        mock_requester.assert_called_once_with("url_builded", {
            "MerchantId": "516165165"
        })
        self.assertEqual(actual, 'response')
