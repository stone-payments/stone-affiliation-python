# -*- coding: utf-8 -*-

import logging
from stone_affiliation.services.service import Service, CONTEXTS
from stone_affiliation.models.operator import Comparison

LOGGER = logging.getLogger(__name__)

BASE_PATH = "{}/merchant".format(CONTEXTS["merchant"])

ENDPOINTS = {
    "list": "GetSettlementBankAccount"
}

URLS = {
    "list": "{}/{}/".format(BASE_PATH, ENDPOINTS["list"])
}


class BankAccount(Service):
    """
    BankAccount implementa um serviço de operações CRUD de 
    contas bancárias de clientes
    """

    def list(self, stonecode):
        LOGGER.info("Listing bank accounts of merchant %s", stonecode)

        data = self._base_data(ENDPOINTS["list"])
        data["StoneCode"] = stonecode

        return self._request(self.build_url(URLS["list"]), data)
