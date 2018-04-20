# -*- coding: utf-8 -*-

"""
Módulo contendo serviço que retorna terminais do lojista em diferentes contextos
"""
import logging
from stone_affiliation.services.service import Service, CONTEXTS
from stone_affiliation.models.operator import Comparison

LOGGER = logging.getLogger(__name__)

BASE_PATH = "{}/merchant".format(CONTEXTS["merchant"])

ENDPOINTS = {
    "terminal_devices": "ListTerminalDevices",
    "paged_terminal_devices": "ListPagedTerminalDevices"
}

URLS = {
    "terminal_devices": "{}/{}/".format(BASE_PATH, ENDPOINTS["terminal_devices"]),
    "paged_terminal_devices": "{}/{}/".format(BASE_PATH, ENDPOINTS["paged_terminal_devices"])
}

DEFAULT_LIMIT_PAGE = 100
DEFAULT_PAGE = 1


class Terminal(Service):
    """
    Terminal implementa um serviço de operações de listagem de terminais
    """

    def get_by_merchant_id(self, merchant_id):
        LOGGER.info("Listing all terminals from merchant %s", merchant_id)

        data = self._base_data(ENDPOINTS["terminal_devices"])
        data["MerchantId"] = merchant_id

        return self._request(self.build_url(URLS["terminal_devices"]), data)

    def get_by_stonecode(self, stonecode, page=DEFAULT_PAGE, limit=DEFAULT_LIMIT_PAGE):
        LOGGER.info("Listing all terminals from stonecode %s", stonecode)

        query = [
            self.build_condition("StoneCode", stonecode, Comparison.EQUALS)
        ]

        data = self._base_data(ENDPOINTS["paged_terminal_devices"])
        data["QueryExpression"] = {
            "ConditionList": query or [],
            "PageNumber": page,
            "RowsPerPage": limit
        }

        return self._request(self.build_url(URLS["paged_terminal_devices"]), data)
