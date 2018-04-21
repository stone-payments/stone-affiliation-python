# -*- coding: utf-8 -*-

"""
Módulo contendo serviço base para outros serviços
"""
import logging
from collections import OrderedDict
from stone_affiliation import (request, processors)
from stone_affiliation.models.operator import Comparison, Logical

LOGGER = logging.getLogger(__name__)

CONTEXTS = {
    "merchant": "/Merchant/MerchantService.svc"
}

CONDITION_TYPE = "Condition:#Stone.ServiceLayer.Affiliation.DataContracts"


class Service(object):
    """
    Service abstrai um servico
    """

    def __init__(self, api_url, app_key, secret_key,
                 user_email=None, source_ip=None):

        self.api_url = api_url
        self.app_key = app_key
        self.secret_key = secret_key
        self.source_ip = source_ip or ""
        self.user_email = user_email or ""

    def _request(self, url, data):
        LOGGER.info("Requesting to %s", url)

        return self._process_response(request.post(url, json=data))

    @classmethod
    def _process_response(cls, response):
        LOGGER.debug("Processing response")

        return processors.track_error(response).json()

    @classmethod
    def build_condition(cls, field, value, comparison_operator, logical_operator=None):
        """
        build_condition recebe valores para construir condição
        para endpoints de listagem
        """
        LOGGER.info("Building condition to Field: %s; Value: %s", field, value)

        if not isinstance(comparison_operator, Comparison):
            LOGGER.info("Invalid comparison sent: %s", comparison_operator)

            raise TypeError(
                "comparison_operator should be an Comparator Enum")

        if logical_operator and not isinstance(logical_operator, Logical):
            LOGGER.info("Invalid logical operator sent: %s", logical_operator)

            raise TypeError(
                "logical_operator should be an Logical Enum")

        if isinstance(value, list):
            value = ",".join([str(item) for item in value])

        return OrderedDict([
            ("__type", CONDITION_TYPE),
            ("LogicalOperator", logical_operator.value if logical_operator else logical_operator),
            ("ComparisonOperator", comparison_operator.value),
            ("Field", field),
            ("Value", value)
        ])

    def build_url(self, resource_path):
        LOGGER.debug("Building url to resource %s", resource_path)

        return "{}{}".format(self.api_url, resource_path)

    def _base_data(self, endpoint):
        LOGGER.debug("Building base data to endpoint %s", endpoint)

        return {
            "UserCredential": self._build_credentials(endpoint)
        }

    def _build_credentials(self, endpoint):
        LOGGER.debug("Building credentials to endpoint %s", endpoint)

        return {
            "EffectiveUserId": self.user_email,
            "Signature": self._build_signature(endpoint),
            "SourceIp": self.source_ip,
            "UserId": self.app_key
        }

    def _build_signature(self, message):
        return processors.encrypt(self.secret_key, message)
