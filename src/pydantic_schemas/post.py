from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(ls=32)
    title: str

    # @validator('id')
    # def check_that_id_less_n(cls, v):
    #     if v > 2:
    #         raise ValueError('id is not less two')
    #     else:
    #         return v
