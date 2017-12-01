# -*- coding: utf-8 -*-

"""
Módulo com processadores de tracking de erro
"""
from requests import codes
from stone_affiliation import errors
from stone_affiliation.models.status import Status


def track_error(response):
    """
    track_error rastreia o erro através da response da API
    """
    if response.status_code == codes["BAD"]:
        raise errors.BadRequest()

    elif response.status_code == codes["INTERNAL_SERVER_ERROR"]:
        raise errors.InternalServerError()

    else:
        data = response.json()
        status = data.get("Status", {}).get("Code", "")

        if response.status_code == codes["UNAUTHORIZED"]:
            raise errors.Unauthorized(data.get("Message"))

        elif response.status_code in range(codes["OK"], codes["BAD"])\
                and status != Status.OK.value:

            error = errors.factory.STATUS.get(status)

            if error:
                raise error(data)

            raise errors.Error(
                "Could not track error from response {}".format(str(data)))

    return response
