# -*- coding: utf-8 -*-

"""
Módulo de erro de falha de validação
"""
from stone_affiliation.errors.error import Error


class FailedValidation(Error):
    """
    FailedValidation encapsula erros de falha de validação
    """

    def __init__(self, data):
        message = ""

        default_message = {
            "Message": "Request validation failed"
        }

        errors = data.get("MessageList") or [default_message]

        for error in errors:
            message += "{}\n".format(error.get("Message"))

        super().__init__(message)
