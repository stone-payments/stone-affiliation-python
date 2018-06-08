# -*- coding: utf-8 -*-

from mock import patch
from tests.suite import TestSuite
from stone_affiliation.services import EnvironmentAvailability


class TestEnvironmentAvailability(TestSuite):
    """
    TestTerminal testa unitariamente a classe de serviço Terminal
    """

    def setUp(self):
        self.service = EnvironmentAvailability("api_url", "app_key", "secret_key",
                                               "source_ip", "user_email")

    @patch("stone_affiliation.services.service.Service._base_data",
           return_value={})
    @patch("stone_affiliation.services.service.Service.build_url",
           return_value="url_builded")
    @patch("stone_affiliation.services.service.Service._request",
           return_value="response")
    def test_check(self, mock_requester, mock_url_builder,
                   mock_data_builder):
        actual = self.service.check()

        mock_data_builder.assert_called_once_with("TestEnvironmentAvailability")
        mock_url_builder.assert_called_once_with(
            "/Merchant/MerchantService.svc/test/TestEnvironmentAvailability/")
        mock_requester.assert_called_once_with("url_builded", mock_data_builder.return_value)
        self.assertEqual(actual, 'response')
