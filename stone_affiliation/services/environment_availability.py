# -*- coding: utf-8 -*-

"""
Módulo contendo serviço que retorna disponibilidade da API
"""
import logging
from stone_affiliation.services.service import Service, CONTEXTS

LOGGER = logging.getLogger(__name__)

BASE_PATH = "{}/test".format(CONTEXTS["merchant"])

ENDPOINTS = {
    "test": "TestEnvironmentAvailability",
}

URLS = {
    "test": "{}/{}/".format(BASE_PATH, ENDPOINTS["test"]),
}

DEFAULT_LIMIT_PAGE = 100
DEFAULT_PAGE = 1


class EnvironmentAvailability(Service):
    """
    EnvironmentAvailability implementa o check de disponibilidade do ambiente
    """
    def check(self):
        """
        check retorna o status da API
        """
        data = self._base_data(ENDPOINTS["test"])
        return self._request(self.build_url(URLS["test"]), data)

