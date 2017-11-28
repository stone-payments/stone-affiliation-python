
from collections import OrderedDict
from requests import codes
from affiliation_sdk import (request, errors, processors)
from affiliation_sdk.models.status import Status

CONTEXTS = {
    "merchant": "/Merchant/MerchantService.svc"
}


class Service(object):
    def __init__(self, api_url, app_key, secret_key,
                 source_ip="", user_email=""):

        self.api_url = api_url
        self.app_key = app_key
        self.secret_key = secret_key
        self.source_ip = source_ip
        self.user_email = user_email

    def _request(self, url, data):
        return self._process_response(request.post(url, json=data))

    def _process_response(self, response):
        return processors.track_error(response)

    def build_condition(self, field, value, comparison_operator=None):
        return OrderedDict([
            ("__type", "Condition:#Stone.ServiceLayer.Affiliation.DataContracts"),
            ("ComparisonOperator", comparison_operator or ""),
            ("Field", field),
            ("Value", value)
        ])

    def build_url(self, resource_path):
        return "{}/{}".format(self.api_url, resource_path)

    def _base_data(self, endpoint):
        return {
            "UserCredential": self._credentials(endpoint)
        }

    def _credentials(self, endpoint):
        return {
            "EffectiveUserId": self.user_email,
            "Signature": self._build_signature(endpoint),
            "SourceIp": self.source_ip,
            "UserId": self.app_key
        }

    def _build_signature(self, message):
        return processors.encrypt(self.secret_key, message)
