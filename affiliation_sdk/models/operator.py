from enum import Enum


class Comparison(Enum):
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
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
