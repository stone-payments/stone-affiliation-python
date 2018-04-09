# -*- coding: utf-8 -*-

from mock import patch
from tests.suite import TestSuite
from stone_affiliation.services import ListTerminalDevices


class TestListTerminalDevices(TestSuite):
    """
    TestListTerminalDevices testa unitariamente a classe de serviço ListTerminalDevices
    """

    def setUp(self):
        self.service = ListTerminalDevices("api_url", "app_key", "secret_key",
                                           "source_ip", "user_email")

    @patch("stone_affiliation.services.service.Service._base_data", return_value={})
    @patch("stone_affiliation.services.service.Service.build_url", return_value="url_builded")
    @patch("stone_affiliation.services.service.Service._request", return_value="response")
    def test_get_by_merchant_id(self, mock_requester, mock_url_builder, mock_data_builder):
        actual = self.service.get_by_merchant_id("516165165")

        mock_data_builder.assert_called_once_with("ListTerminalDevices")
        mock_url_builder.assert_called_once_with("/Merchant/MerchantService.svc/merchant/ListTerminalDevices/")
        mock_requester.assert_called_once_with("url_builded", {
            "MerchantId": "516165165"
        })
        self.assertEqual(actual, 'response')
