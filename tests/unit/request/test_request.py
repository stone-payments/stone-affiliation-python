# -*- coding: utf-8 -*-

from mock import patch
from tests.suite import TestSuite
from stone_affiliation.request import request


class TestRequest(TestSuite):
    """
    TestRequest testa unitariamente http requester
    """

    @patch("stone_affiliation.request.request._request",
           return_value="response")
    def test_post(self, mock_processor):
        kwargs = {
            "my_arg": "value"
        }
        actual = request.post("url", "data", "json", **kwargs)
        mock_processor.assert_called_once_with(
            "post", "url", data="data", json="json", my_arg="value")
        self.assertEqual(actual, "response")

    @patch("requests.post",
           return_value="response")
    def test_request(self, mock_processor):
        actual = request._request("post", "url", my_arg="value")
        mock_processor.assert_called_once_with("url", my_arg="value")
        self.assertEqual(actual, "response")
