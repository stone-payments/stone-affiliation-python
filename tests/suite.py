from unittest import TestCase
from os import environ


class TestSuite(TestCase):
    def get_config(self):
        try:
            self.config = {
                "api_url": environ["API_URL"],
                "app_key": environ["APP_KEY"],
                "secret_key": environ["SECRET_KEY"],
            }
        except KeyError as e:
            print("Please, provide api configurations. Expecting: {}".format(e))
            exit(1)
