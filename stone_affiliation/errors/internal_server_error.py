# -*- coding: utf-8 -*-

"""
Módulo de erro interno do servidor
"""
from stone_affiliation.errors.error import Error


class InternalServerError(Error):
    """
    InternalServerError encapsula erros internos do servidor
    """

    def __init__(self, data=None):
        message = "Internal server error"

        if data:
            message = data.get("Status", {}).get("Message", message)

        super().__init__(message)
