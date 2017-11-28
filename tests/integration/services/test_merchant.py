from tests.suite import TestSuite
from stone_affiliation.services import Merchant


class TestMerchant(TestSuite):
    def setUp(self):
        self.service = Merchant(**self.get_config())
        self.merchant = self.get_merchant()

    def get_merchant(self):
        try:
            resp = self.service.list(limit=1)
            return resp.get("ListedMerchants")[0]
        except Exception as e:
            self.fail("Fail on fetch merchants. Exception: " + str(e))

    def test_get_by_id(self):
        resp = self.service.get_by_id(self.merchant["Id"])
        self.assertDictEqual(resp["ListedMerchants"][0], self.merchant)

    def test_get_by_stonecode(self):
        resp = self.service.get_by_stonecode(self.merchant["StoneCode"])
        self.assertDictEqual(resp["ListedMerchants"][0], self.merchant)
