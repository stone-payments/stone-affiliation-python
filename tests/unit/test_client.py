# -*- coding: utf-8 -*-

from tests.suite import TestSuite
from stone_affiliation import StoneAffiliation
from stone_affiliation.services import (Merchant, BankAccount, BasicMerchant, Terminal)

MOCK_CONFIG = {
    "api_url": "api_url",
    "app_key": "app_key",
    "secret_key": "secret_key"
}
MOCK_USER = {
    "user_email": "user_email",
    "source_ip ": "source_ip"
}

TEST_MAIL = "test@mail.com"
SOURCE_IP = "68.142.102.212"


class TestStoneAffiliation(TestSuite):
    """
    TestStoneAffiliation testa unitariamente a classe
    agregadora de serviços StoneAffiliation
    """

    def setUp(self):
        self.client = StoneAffiliation(**MOCK_CONFIG)

    def test_merchant_service(self):
        actual = self.client.merchant_service(TEST_MAIL, SOURCE_IP)
        self.assertTrue(isinstance(actual, Merchant))
        self.assertEqual(actual.user_email, TEST_MAIL)
        self.assertEqual(actual.source_ip, SOURCE_IP)

    def test_bank_account_service(self):
        actual = self.client.bank_account_service(TEST_MAIL, SOURCE_IP)
        self.assertTrue(isinstance(actual, BankAccount))
        self.assertEqual(actual.user_email, TEST_MAIL)
        self.assertEqual(actual.source_ip, SOURCE_IP)

    def test_basic_merchant_service(self):
        actual = self.client.basic_merchant_service(TEST_MAIL, SOURCE_IP)
        self.assertTrue(isinstance(actual, BasicMerchant))
        self.assertEqual(actual.user_email, TEST_MAIL)
        self.assertEqual(actual.source_ip, SOURCE_IP)

    def test_terminal_service(self):
        actual = self.client.terminal_service(TEST_MAIL, SOURCE_IP)
        self.assertTrue(isinstance(actual, Terminal))
        self.assertEqual(actual.user_email, TEST_MAIL)
        self.assertEqual(actual.source_ip, SOURCE_IP)
