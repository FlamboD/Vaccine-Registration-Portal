import typing
from datetime import date
from enum import Enum


class Gender(Enum):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"


class VaccineRegistration:
    def __init__(self):
        # self.older_than_18: bool
        self.id_number: str
        self.passport_number: typing.Optional[str]
        self.date_of_birth: date
        self.first_names: str
        self.surname: str
        self.gender: Gender
        self.mobile_number: str
        self.email: str
        self.province: str
        self.municipality: str
        self.address: typing.Optional[str]
        self.preferred_vaccination_day: str
        self.preferred_vaccination_time: str
        self.medical_aid: bool
        self.medical_aid_scheme_name: str
        self.medical_aid_scheme_number: str


