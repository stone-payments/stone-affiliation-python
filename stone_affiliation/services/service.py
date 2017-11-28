# -*- coding: utf-8 -*-

from collections import OrderedDict
from stone_affiliation import (request, processors)
from stone_affiliation.models.operator import Comparison


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
        return self._process_response(request.post(url, json=data))

    def _process_response(self, response):
        return processors.track_error(response).json()

    def build_condition(self, field, value, comparison_operator):
        if not isinstance(comparison_operator, Comparison):
            raise TypeError(
                "comparison_operator should be an Comparator Enum")

        return OrderedDict([
            ("__type", CONDITION_TYPE),
            ("ComparisonOperator", comparison_operator.value),
            ("Field", field),
            ("Value", value)
        ])

    def build_url(self, resource_path):
        return "{}{}".format(self.api_url, resource_path)

    def _base_data(self, endpoint):
        return {
            "UserCredential": self._build_credentials(endpoint)
        }

    def _build_credentials(self, endpoint):
        return {
            "EffectiveUserId": self.user_email,
            "Signature": self._build_signature(endpoint),
            "SourceIp": self.source_ip,
            "UserId": self.app_key
        }

    def _build_signature(self, message):
        return processors.encrypt(self.secret_key, message)
