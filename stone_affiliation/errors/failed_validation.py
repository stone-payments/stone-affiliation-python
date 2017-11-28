from stone_affiliation.errors.error import Error


class FailedValidation(Error):
    def __init__(self, errors):
        message = ""

        for error in errors:
            message += "{}\n".format(error.get("Message"))

        super().__init__(message)
