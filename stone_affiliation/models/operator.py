# -*- coding: utf-8 -*-

"""
Módulo com enums de operações
"""
from enum import Enum


class Comparison(Enum):
    """
    Comparison é um enum com operações de comparação
    """
    EQUALS = "Equals"
    NOT_EQUAL_TO = "NotEqualTo"
    GREATER_THAN = "GreaterThan"
    LESS_THAN = "LessThan"
    GREATER_THAN_OR_EQUAL_TO = "GreaterThanOrEqualTo"
    LESS_THAN_OR_EQUAL_TO = "LessThanOrEqualTo"
    IN = "In"
    NOT_IN = "NotIn"
    LIKE = "Like"
    IS_NULL = "IsNull"
    IS_NOT_NULL = "IsNotNull"


class Logical(Enum):
    """
    Logical é um enum com operações de lógica
    """
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
