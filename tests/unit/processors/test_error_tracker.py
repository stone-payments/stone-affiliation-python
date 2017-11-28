# -*- coding: utf-8 -*-

from mock import Mock, patch
from tests.suite import TestSuite
from stone_affiliation import errors
from stone_affiliation.processors import track_error


class MockException(Exception):
    pass


class TestErrorTracker(TestSuite):
    """
    TestErrorTracker testa unitariamente processadores de tracking de erro
    """

    def setUp(self):
        self.response = Mock()
        self.response.json.return_value = {
            "Message": "Unauthorized",
            "Status": {
                "Code": "FAILED_STATUS"
            },
            "MessageList": [
                "messages"
            ]
        }

    def test_track_error_bad_request(self):
        self.response.status_code = 400
        with self.assertRaises(errors.BadRequest):
            track_error(self.response)

    def test_track_error_internal_server(self):
        self.response.status_code = 500
        with self.assertRaises(errors.InternalServerError):
            track_error(self.response)

    def test_track_error_unauthorized(self):
        self.response.status_code = 401
        with self.assertRaises(errors.Unauthorized):
            track_error(self.response)

    @patch.dict("stone_affiliation.errors.factory.STATUS",
                {"FAILED_STATUS": MockException}, clear=True)
    def test_track_error_failed_status(self):
        for i in range(200, 400):
            self.response.status_code = i
            with self.assertRaises(MockException):
                track_error(self.response)

    def test_track_error_status_untracked(self):
        for i in range(200, 400):
            self.response.status_code = i
            with self.assertRaises(errors.Error):
                track_error(self.response)
