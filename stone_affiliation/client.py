# -*- coding: utf-8 -*-

"""
Módulo do client principal
"""
from stone_affiliation.services import (Merchant, BankAccount, BasicMerchant, ListTerminalDevices)


class StoneAffiliation(object):
    """
    StoneAffiliation agrupa todos os serviços que se comunicam
    com a API de Credenciamento
    """

    def __init__(self, api_url, app_key, secret_key):
        self.config = {
            "api_url": api_url,
            "app_key": app_key,
            "secret_key": secret_key
        }

    def merchant_service(self, user_email=None, source_ip=None):
        return Merchant(user_email=user_email,
                        source_ip=source_ip,
                        **self.config)

    def bank_account_service(self, user_email=None, source_ip=None):
        return BankAccount(user_email=user_email,
                           source_ip=source_ip,
                           **self.config)

    def basic_merchant_service(self, user_email=None, source_ip=None):
        return BasicMerchant(user_email=user_email,
                             source_ip=source_ip,
                             **self.config)

    def list_terminal_devices(self, user_email=None, source_ip=None):
        return ListTerminalDevices(user_email=user_email,
                                   source_ip=source_ip,
                                   **self.config)
