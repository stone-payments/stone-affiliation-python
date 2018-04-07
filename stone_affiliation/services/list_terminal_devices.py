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

    def get_by_stonecode(self, stonecode):
        LOGGER.info("Listing all terminals from merchant %s", stonecode)

        data = self._base_data(ENDPOINTS["terminal_devices"])
        data["StoneCode"] = stonecode

        return self._request(self.build_url(URLS["terminal_devices"]), data)
