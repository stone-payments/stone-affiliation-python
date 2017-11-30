from stone_affiliation.services import (Merchant, BankAccount)


class StoneAffiliation(object):
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
