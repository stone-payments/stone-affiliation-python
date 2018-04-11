# -*- coding: utf-8 -*-

from mock import patch
from tests.suite import TestSuite
from stone_affiliation.services import BasicMerchant


class TestBasicMerchant(TestSuite):
    """
    TestBasicMerchant testa unitariamente a classe de serviço Merchant
    """

    def setUp(self):
        self.service = BasicMerchant("api_url", "app_key", "secret_key",
                                "source_ip", "user_email")

    @patch("stone_affiliation.services.service.Service._base_data",
           return_value={})
    @patch("stone_affiliation.services.service.Service.build_url",
           return_value="url_builded")
    @patch("stone_affiliation.services.service.Service._request",
           return_value="response")
    def test_get_by_stonecode(self, mock_requester, mock_url_builder,
                  mock_data_builder):
        actual = self.service.get_by_stonecode("516165165")

        mock_data_builder.assert_called_once_with("GetBasicMerchant")
        mock_url_builder.assert_called_once_with(
            "/Merchant/MerchantService.svc/merchant/GetBasicMerchant/")
        mock_requester.assert_called_once_with("url_builded", {
            "StoneCode": "516165165"            
        })
        self.assertEqual(actual, 'response')

        
    @patch("stone_affiliation.services.service.Service._base_data",
           return_value={})
    @patch("stone_affiliation.services.service.Service.build_url",
           return_value="url_builded")
    @patch("stone_affiliation.services.service.Service._request",
           return_value="response")
    def test_get_by_stonecode(self, mock_requester, mock_url_builder,
                  mock_data_builder):
        actual = self.service.get_by_merchant_id("5569")

        mock_data_builder.assert_called_once_with("GetBasicMerchant")
        mock_url_builder.assert_called_once_with(
            "/Merchant/MerchantService.svc/merchant/GetBasicMerchant/")
        mock_requester.assert_called_once_with("url_builded", {
            "MerchantId": "5569"            
        })
        self.assertEqual(actual, 'response')

