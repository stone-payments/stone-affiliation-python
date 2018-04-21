# -*- coding: utf-8 -*-

from mock import patch
from tests.suite import TestSuite
from stone_affiliation.services import Terminal


class TestTerminal(TestSuite):
    """
    TestTerminal testa unitariamente a classe de serviço Terminal
    """

    def setUp(self):
        self.service = Terminal("api_url", "app_key", "secret_key",
                                "source_ip", "user_email")

    @patch("stone_affiliation.services.service.Service._base_data", return_value={})
    @patch("stone_affiliation.services.service.Service.build_url", return_value="url_builded")
    @patch("stone_affiliation.services.service.Service._request", return_value="response")
    def test_get_list_paged_terminal_devices_by_stonecode(self, mock_requester, mock_url_builder, mock_data_builder):
        actual = self.service.get_by_stonecode("919243797")

        mock_data_builder.assert_called_once_with("ListPagedTerminalDevices")
        mock_url_builder.assert_called_once_with("/Merchant/MerchantService.svc/merchant/ListPagedTerminalDevices/")
        self.assertEqual(actual, 'response')

    @patch("stone_affiliation.services.service.Service._base_data", return_value={})
    @patch("stone_affiliation.services.service.Service.build_url", return_value="url_builded")
    @patch("stone_affiliation.services.service.Service._request", return_value="response")
    def test_get_list_terminal_devices_by_merchant_id(self, mock_requester, mock_url_builder, mock_data_builder):
        actual = self.service.get_by_merchant_id("516165165")

        mock_data_builder.assert_called_once_with("ListTerminalDevices")
        mock_url_builder.assert_called_once_with("/Merchant/MerchantService.svc/merchant/ListTerminalDevices/")
        mock_requester.assert_called_once_with("url_builded", {
            "MerchantId": "516165165"
        })
        self.assertEqual(actual, 'response')

    @patch("stone_affiliation.services.service.Service._base_data", return_value={})
    @patch("stone_affiliation.services.service.Service.build_url", return_value="url_builded")
    @patch("stone_affiliation.services.service.Service._request", return_value="response")
    def test_get_list_paged_terminal_devices_by_query(self, mock_requester, mock_url_builder,
                  mock_data_builder):
        actual = self.service.list(30, 1000, "query")

        mock_data_builder.assert_called_once_with("ListPagedTerminalDevices")
        mock_url_builder.assert_called_once_with(
            "/Merchant/MerchantService.svc/merchant/ListPagedTerminalDevices/")
        mock_requester.assert_called_once_with("url_builded", {
            "DisableTerminalRentControlService": True,
            "QueryExpression": {
                "ConditionList": "query",
                "PageNumber": 30,
                "RowsPerPage": 1000
            }
        })
        self.assertEqual(actual, 'response')

