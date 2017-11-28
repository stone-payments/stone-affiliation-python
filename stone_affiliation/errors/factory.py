from stone_affiliation.models.status import Status
from stone_affiliation.errors import FailedValidation

STATUS = {
    Status.VALIDATION_ERROR: FailedValidation
}
