# -*- coding: utf-8 -*-

from tests import suite
from stone_affiliation.services import Merchant


class TestSuite(suite.TestSuite):
    def setUp(self):
        self.merchant = self.get_merchant()

    def get_merchant(self):
        service = Merchant(**self.get_config())
        try:
            resp = service.list(limit=1)
            return resp.get("ListedMerchants")[0]
        except Exception as e:
            self.fail("Fail on fetch merchants. Exception: " + str(e))
