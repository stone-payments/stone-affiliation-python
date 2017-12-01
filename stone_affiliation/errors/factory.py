# -*- coding: utf-8 -*-
"""
Este módulo contém fabricas de erros por contexto
"""
from stone_affiliation.models.status import Status
from stone_affiliation.errors import (InternalServerError,
                                      FailedValidation)

STATUS = {
    Status.VALIDATION_ERROR.value: FailedValidation,
    Status.INTERNAL_ERROR.value: InternalServerError
}
