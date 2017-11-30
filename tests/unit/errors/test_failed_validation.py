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
        mock_errors = []
        expected = ""

        for i in range(0, total_errors):
            message = "Error{}".format(i)
            mock_errors.append({
                "Message": message
            })
            expected += "{}\n".format(message)

        actual = FailedValidation(mock_errors)
        self.assertEqual(str(actual), expected)
