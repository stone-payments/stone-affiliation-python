# -*- coding: utf-8 -*-

import hashlib
from mock import patch
from tests.suite import TestSuite
from stone_affiliation.processors import encrypt


class TestEncrypt(TestSuite):
    """
    TestEncrypt testa unitariamente processadores de criptografia
    """

    @patch("hmac.new")
    def test_encrypt(self, mock_crypt):
        actual = encrypt("my_key", "my_message")
        mock_crypt.assert_called_once_with(b"my_key", b"my_message",
                                           hashlib.sha512)
        self.assertEqual(actual, mock_crypt().hexdigest())
