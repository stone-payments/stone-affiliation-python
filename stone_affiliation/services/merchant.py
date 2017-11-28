from stone_affiliation.services.service import Service, CONTEXTS
from stone_affiliation.models.operator import Comparison


BASE_PATH = "{}/merchant".format(CONTEXTS["merchant"])

ENDPOINTS = {
    "get": "GetBasicMerchant",
    "list": "ListMerchants"
}

URLS = {
    "get": "{}/{}/".format(BASE_PATH, ENDPOINTS["get"]),
    "list": "{}/{}/".format(BASE_PATH, ENDPOINTS["list"])
}


class Merchant(Service):
    def get_by_stonecode(self, stonecode):
        query = {
            "ConditionList": [
                self.build_condition("StoneCode", stonecode,
                                     Comparison.EQUALS.value)
            ]
        }
        return self.list(query)

    def list(self, query=None):
        data = self._base_data(ENDPOINTS["list"])
        data["QueryExpression"] = query
        return self._request(self.build_url(URLS["list"]), data)
