# -*- coding: utf-8 -*-

from tests.suite import TestSuite
from stone_affiliation.processors import encrypt


class TestEncrypt(TestSuite):
    """
    TestEncrypt testa processadores de criptografia
    """

    def test_encrypt(self):
        actual = encrypt("my_key", "my_message")
        self.assertEqual(
            actual, '5fdd070e8947b9c4233dc5a193315a8e7d827a2081a6b309131c6ce6d921f7171625c6eb883ba3855f8c7a02a2d06e47a50ce53280da959ef5288f6065b361f3')
