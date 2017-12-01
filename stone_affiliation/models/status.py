# -*- coding: utf-8 -*-

"""
Módulo com enums de statuses da API
"""
from enum import Enum


class Status(Enum):
    """
    Status é um enum com tipos de status da API
    """
    OK = "OK"
    VALIDATION_ERROR = "VALIDATION_ERRORS"
    INTERNAL_ERROR = "INTERNAL_ERROR"
