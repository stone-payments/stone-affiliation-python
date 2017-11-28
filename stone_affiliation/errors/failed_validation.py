# -*- coding: utf-8 -*-

from stone_affiliation.errors.error import Error


class FailedValidation(Error):
    """
    FailedValidation encapsula erros de falha de validação
    """

    def __init__(self, errors):
        message = ""

        for error in errors:
            message += "{}\n".format(error.get("Message"))

        super().__init__(message)
