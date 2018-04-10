# -*- coding: utf-8 -*-

from mock import patch
from tests.suite import TestSuite
from stone_affiliation import StoneAffiliation
from stone_affiliation.services import (Merchant, BankAccount, BasicMerchant,
                                        ListPagedTerminalDevices, ListTerminalDevices)

MOCK_CONFIG = {
    "api_url": "api_url",
    "app_key": "app_key",
    "secret_key": "secret_key"
}
MOCK_USER = {
    "user_email": "user_email",
    "source_ip ": "source_ip"
}


class TestStoneAffiliation(TestSuite):
    """
    TestStoneAffiliation testa unitariamente a classe
    agregadora de serviços StoneAffiliation
    """

    def setUp(self):
        self.client = StoneAffiliation(**MOCK_CONFIG)

    def test_merchant_service(self):
        actual = self.client.merchant_service("user_email", "source_ip")
        self.assertTrue(isinstance(actual, Merchant))

    def test_bank_account_service(self):
        actual = self.client.bank_account_service("user_email", "source_ip")
        self.assertTrue(isinstance(actual, BankAccount))

    def test_basic_merchant_service(self):
        actual = self.client.basic_merchant_service("user_email", "source_ip")
        self.assertTrue(isinstance(actual, BasicMerchant))

    def test_list_paged_terminal_service(self):
        actual = self.client.list_paged_terminal_devices("user_email", "source_ip")
        self.assertTrue(isinstance(actual, ListPagedTerminalDevices))

    def test_list_terminal_service(self):
        actual = self.client.list_terminal_devices("user_email", "source_ip")
        self.assertTrue(isinstance(actual, ListTerminalDevices))
