from unittest import TestCase
from os import environ


class TestSuite(TestCase):
    def get_config(self):
        try:
            return {
                "api_url": environ["API_URL"],
                "app_key": environ["APP_KEY"],
                "secret_key": environ["SECRET_KEY"],
            }
        except KeyError as e:
            self.fail(
                "Please, provide api configurations. Expecting: {}".format(e))
