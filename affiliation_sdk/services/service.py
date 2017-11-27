
import hashlib
import hmac
from collections import OrderedDict
from requests import codes
from affiliation_sdk import request
from affiliation_sdk import errors
from affiliation_sdk.models.status import Status

CONTEXTS = {
    "merchant": "/Merchant/MerchantService.svc"
}


class Service(object):
    def __init__(self, api_url, user_id, secret_key,
                 source_ip="", user_email=""):

        self.api_url = api_url
        self.user_id = user_id
        self.secret_key = secret_key
        self.source_ip = source_ip
        self.user_email = user_email

    def _request(self, url, data):
        return self._process_response(request.post(url, json=data))

    def _process_response(self, response):
        import pdb
        pdb.set_trace()
        if response.status_code == codes.BAD:
            raise errors.BadRequest()

        elif response.status_code == codes.INTERNAL_SERVER_ERROR:
            raise errors.InternalServerError()

        else:
            data = response.json()
            status = data.get("Status", {}).get("Code", "")

            if response.status_code == codes.UNAUTHORIZED:
                raise errors.Unauthorized(data.get("Message"))

            elif response.status_code in range(codes.OK, codes.BAD)\
                    and status != Status.OK.value:

                error = errors.factory.STATUS.get(status)

                if error:
                    raise error(data["MessageList"])

                raise errors.Error(
                    "Could not track error from response {}".format(str(data)))

        return response

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
            "UserId": self.user_id
        }

    def _build_signature(self, message):
        digester = hmac.new(bytes(self.secret_key, "utf-8"),
                            bytes(message, "utf-8"),
                            hashlib.sha512)

        return digester.hexdigest()
