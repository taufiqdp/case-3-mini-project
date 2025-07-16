from enum import Enum
from typing import List

from pydantic import BaseModel, Field, field_validator


class Gender(str, Enum):
    male = "male"
    female = "female"


class PersonInfo(BaseModel):
    gender: Gender
    age: int
    symptoms: List[str]

    @field_validator("age")
    def validate_age_range(cls, value):
        if value < 0 or value > 130:
            raise ValueError("Age must be between 0 and 120.")
        return value


class Recommendation(BaseModel):
    recommended_department: str = Field(
        description="The recommended medical department for the patient's initial consultation."
    )
