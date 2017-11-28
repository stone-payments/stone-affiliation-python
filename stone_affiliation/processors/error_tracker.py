from requests import codes
from stone_affiliation import errors


def track_error(response):
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
