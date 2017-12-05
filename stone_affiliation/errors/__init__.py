# -*- coding: utf-8 -*-

"""
Pacote contendo erros encapsulados pela biblioteca
"""
from .error import Error
from .internal_server_error import InternalServerError
from .bad_request import BadRequest
from .failed_validation import FailedValidation
from .unauthorized import Unauthorized
from . import factory
