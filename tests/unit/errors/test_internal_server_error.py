# -*- coding: utf-8 -*-

from tests.suite import TestSuite
from stone_affiliation.errors import InternalServerError


class TestInternalServerError(TestSuite):
    """
    TestInternalServerError testa unitariamente a classe 
    agregadora de serviços InternalServerError
    """

    def test_init(self):
        expected = "Internal Error"
        mock_data = {"Status": {"Message": expected}}

        actual = InternalServerError(mock_data)
        self.assertEqual(str(actual), expected)
