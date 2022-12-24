from enum import Enum
from src.baseclasses.pyenum import PyEnum


class Genders(Enum):
    female = 'female'
    male = 'male'


class Statuses(PyEnum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    DELETED = 'DELETED'
    BANNED = 'BANNED'


class UserErrors(Enum):
    WRONG_EMAIL = 'Email does not have @'


print(Statuses.list())
