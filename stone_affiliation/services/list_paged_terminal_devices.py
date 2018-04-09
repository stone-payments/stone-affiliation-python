"""
Módulo para listar os terminais de um cliente pelo stonecode
"""
import logging
from stone_affiliation.services.service import Service, CONTEXTS
from stone_affiliation.models.operator import Comparison

LOGGER = logging.getLogger(__name__)

BASE_PATH = "{}/merchant".format(CONTEXTS["merchant"])

ENDPOINTS = {
    "list_paged_terminal_devices": "ListPagedTerminalDevices"
}

URLS = {
    "list_paged_terminal_devices": "{}/{}/".format(BASE_PATH, ENDPOINTS["list_paged_terminal_devices"])
}

DEFAULT_LIMIT_PAGE = 100
DEFAULT_PAGE = 1


class ListPagedTerminalDevices(Service):
    """
    ListPagedTerminalDevices é uma interface de comunicação
    com o endpoint /merchant/ListPagedTerminalDevices/
    """

    def get_by_stonecode(self, stonecode, page=DEFAULT_PAGE, limit=DEFAULT_LIMIT_PAGE):
        LOGGER.info("Listing all terminals from merchant %s", stonecode)

        query = [
            self.build_condition("StoneCode", stonecode, Comparison.EQUALS)
        ]

        data = self._base_data(ENDPOINTS["list_paged_terminal_devices"])
        data["QueryExpression"] = {
            "ConditionList": query or [],
            "PageNumber": page,
            "RowsPerPage": limit
        }

        return self._request(self.build_url(URLS["list_paged_terminal_devices"]), data)
