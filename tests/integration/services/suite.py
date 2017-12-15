# -*- coding: utf-8 -*-

from tests import suite
from stone_affiliation.services import Merchant


class TestSuite(suite.TestSuite):
    def setUp(self):
        self.merchants = self.get_merchants()
        self.merchant = self.merchants[0]

    def get_merchants(self):
        service = Merchant(**self.get_config())
        try:
            resp = service.list(limit=3)

            if not resp.get("ListedMerchants"):
                self.fail("No merchant found")

            return resp.get("ListedMerchants")
        except Exception as e:
            self.fail("Fail on fetch merchants. Exception: " + str(e))
