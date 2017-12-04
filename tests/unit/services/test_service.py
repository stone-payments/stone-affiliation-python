# -*- coding: utf-8 -*-

from mock import patch, Mock
from stone_affiliation.services.service import Service, CONDITION_TYPE
from stone_affiliation.models.operator import Comparison
from tests.suite import TestSuite


class TestService(TestSuite):
    """
    TestService testa unitariamente a classe base Service
    """

    def setUp(self):
        self.service = Service("api_url", "app_key", "secret_key",
                               "source_ip", "user_email")

    @patch("stone_affiliation.request.post",
           return_value="raw_response")
    @patch("stone_affiliation.services.service.Service._process_response",
           return_value="response_processed")
    def test_request(self, mock_processor, mock_requester):
        actual = self.service._request("my_url", "data")

        mock_requester.assert_called_once_with("my_url", json="data")
        mock_processor.assert_called_once_with("raw_response")
        self.assertEqual(actual, "response_processed")

    @patch("stone_affiliation.processors.track_error")
    def test_process_response(self, mock_processor):
        expected = Mock()
        mock_processor.return_value = expected
        actual = self.service._process_response("raw_response")

        mock_processor.assert_called_once_with("raw_response")
        self.assertEqual(actual, expected.json())

    def test_build_condition(self):
        with self.assertRaises(TypeError):
            self.service.build_condition("FIELD", "VALUE", "")

        actual = self.service.build_condition(
            "FIELD", "VALUE", Comparison.EQUALS)

        self.assertEqual(actual["__type"], CONDITION_TYPE)
        self.assertEqual(actual["ComparisonOperator"], Comparison.EQUALS.value)
        self.assertEqual(actual["Field"], "FIELD")
        self.assertEqual(actual["Value"], "VALUE")

    def test_build_url(self):
        actual = self.service.build_url("/my_resource")

        self.assertEqual(actual, "api_url/my_resource")

    @patch("stone_affiliation.services.service.Service._build_credentials",
           return_value="credentials")
    def test_base_data(self, mock_builder):
        actual = self.service._base_data("endpoint")

        mock_builder.assert_called_once_with("endpoint")
        self.assertEqual(actual, {"UserCredential": "credentials"})

    @patch("stone_affiliation.services.service.Service._build_signature",
           return_value="signature")
    def test_build_credentials(self, mock_builder):
        actual = self.service._build_credentials("endpoint")

        mock_builder.assert_called_once_with("endpoint")
        self.assertEqual(actual, {
            "EffectiveUserId": self.service.user_email,
            "Signature": "signature",
            "SourceIp": self.service.source_ip,
            "UserId": self.service.app_key
        })

    @patch("stone_affiliation.processors.encrypt",
           return_value="hash")
    def test_build_signature(self, mock_processor):
        actual = self.service._build_signature("message")

        self.assertEqual(actual, "hash")
        mock_processor.assert_called_once_with(
            self.service.secret_key, "message")
