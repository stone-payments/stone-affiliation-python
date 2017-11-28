# -*- coding: utf-8 -*-

import logging
from stone_affiliation.services.service import Service, CONTEXTS
from stone_affiliation.models.operator import Comparison

LOGGER = logging.getLogger(__name__)

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
        LOGGER.info("Getting merchant with id %d", identifier)
        
        query = [
            self.build_condition("Id", identifier,
                                 Comparison.EQUALS)
        ]
        return self.list(query=query)

    def get_by_stonecode(self, stonecode):
        LOGGER.info("Getting merchant with stonecode %s", stonecode)
        
        query = [
            self.build_condition("StoneCode", stonecode,
                                 Comparison.EQUALS)
        ]
        return self.list(query=query)

    def list(self, page=1, limit=100, query=None):
        LOGGER.info("Listing merchants. Page: %d; Limit: %d", page, limit)

        data = self._base_data(ENDPOINTS["list"])
        data["ListComplementaryData"] = True
        data["QueryExpression"] = {
            "ConditionList": query or [],
            "PageNumber": page,
            "RowsPerPage": limit
        }
        return self._request(self.build_url(URLS["list"]), data)
