# -*- coding: utf-8 -*-

from tests.suite import TestSuite
from stone_affiliation.errors import FailedValidation


class TestFailedValidation(TestSuite):
    """
    TestFailedValidation testa unitariamente a classe 
    agregadora de serviços FailedValidation
    """

    def test_init(self):
        total_errors = 4
        mock_data = {"MessageList": []}
        expected = ""

        for i in range(0, total_errors):
            message = "Error{}".format(i)
            mock_data["MessageList"].append({
                "Message": message
            })
            expected += "{}\n".format(message)

        actual = FailedValidation(mock_data)
        self.assertEqual(str(actual), expected)
