# -*- coding: utf-8 -*-

"""
Módulo contendo serviço que lida com operações de cliente
"""
import logging
from stone_affiliation.services.service import Service, CONTEXTS

LOGGER = logging.getLogger(__name__)

BASE_PATH = "{}/merchant".format(CONTEXTS["merchant"])

ENDPOINTS = {
    "basic": "GetBasicMerchant"
}

URLS = {
    "basic": "{}/{}/".format(BASE_PATH, ENDPOINTS["basic"])
}

class BasicMerchant(Service):
    """
    Merchant implementa um serviço de operações CRUD de clientes
    """
    
    def get_by_stonecode(self, stonecode):
        """
        get_by_stonecode retorna dados do lojista baseado no stonecode baseado
        """
        LOGGER.info("Get merchant based on stonecode: %s", stonecode)

        data = self._base_data(ENDPOINTS["basic"])
        data["StoneCode"] = stonecode
        
        return self._request(self.build_url(URLS["basic"]), data)

    def get_by_merchant_id(self, merchant_id):
        """
        get_by_merchant_id retorna dados do lojista baseado no merchant_id baseado
        """
        LOGGER.info("Get merchant based on merchant_id: %s", merchant_id)

        data = self._base_data(ENDPOINTS["basic"])
        data["MerchantId"] = merchant_id
        
        return self._request(self.build_url(URLS["basic"]), data)
