from enum import Enum


class Status(Enum):
    OK = "OK"
    VALIDATION_ERROR = "VALIDATION_ERRORS"
    INTERNAL_ERROR = "INTERNAL_ERROR"
