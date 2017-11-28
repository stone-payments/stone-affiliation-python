# -*- coding: utf-8 -*-

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
    """
    Merchant implementa um serviço de operações CRUD de clientes
    """

    def get_by_id(self, identifier):
        query = [
            self.build_condition("Id", identifier,
                                 Comparison.EQUALS)
        ]
        return self.list(query=query)

    def get_by_stonecode(self, stonecode):
        query = [
            self.build_condition("StoneCode", stonecode,
                                 Comparison.EQUALS)
        ]
        return self.list(query=query)

    def list(self, page=1, limit=100, query=None):
        data = self._base_data(ENDPOINTS["list"])
        data["ListComplementaryData"] = True
        data["QueryExpression"] = {
            "ConditionList": query or [],
            "PageNumber": page,
            "RowsPerPage": limit
        }
        return self._request(self.build_url(URLS["list"]), data)
