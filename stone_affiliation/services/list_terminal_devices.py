"""
Módulo para listar os terminais de um cliente pelo stonecode
"""
import logging
from stone_affiliation.services.service import Service, CONTEXTS

LOGGER = logging.getLogger(__name__)

BASE_PATH = "{}/merchant".format(CONTEXTS["merchant"])

ENDPOINTS = {
    "terminal_devices": "ListTerminalDevices"
}

URLS = {
    "terminal_devices": "{}/{}/".format(BASE_PATH, ENDPOINTS["terminal_devices"])
}


class ListTerminalDevices(Service):
    """
    ListTerminalDevices é uma interface de comunicação
    com o endpoint /merchant/ListTerminalDevices/
    """

    def get_by_merchant_id(self, merchant_id):
        LOGGER.info("Listing all terminals from merchant %s", merchant_id)

        data = self._base_data(ENDPOINTS["terminal_devices"])
        data["MerchantId"] = merchant_id

        return self._request(self.build_url(URLS["terminal_devices"]), data)
