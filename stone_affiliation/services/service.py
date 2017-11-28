# -*- coding: utf-8 -*-

import logging
from collections import OrderedDict
from stone_affiliation import (request, processors)
from stone_affiliation.models.operator import Comparison

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
                 source_ip=None, user_email=None):

        self.api_url = api_url
        self.app_key = app_key
        self.secret_key = secret_key
        self.source_ip = source_ip or ""
        self.user_email = user_email or ""

    def _request(self, url, data):
        LOGGER.info("Requesting to %s", url)
        
        return self._process_response(request.post(url, json=data))

    def _process_response(self, response):
        LOGGER.debug("Processing response")
        
        return processors.track_error(response).json()

    def build_condition(self, field, value, comparison_operator):
        LOGGER.info("Building condition to Field: %s; Value: %s", field, value)
        
        if not isinstance(comparison_operator, Comparison):
            LOGGER.info("Invalid comparison sent: {}".format(comparison_operator))
            
            raise TypeError(
                "comparison_operator should be an Comparator Enum")

        return OrderedDict([
            ("__type", CONDITION_TYPE),
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
