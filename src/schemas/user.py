from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Status, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Status

    @validator('email')
    def check_dog_in_email(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
