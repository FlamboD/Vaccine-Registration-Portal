import typing


class VaccineRegistration:
    def __init__(
            self,
            *args,
            older_than_18: bool = False,
            id_number: str = None,
            passport_number: str = None,
            date_of_birth: str = None,
            first_names: str = None,
            surname: str = None,
            gender: str = None,
            mobile_number: str = None,
            email: str = None,
            province: str = None,
            municipality: str = None,
            address: str = None,
            weekday: int = -1,
            morning: int = -1,
            medical_aid: bool = False,
            medical_aid_scheme: str = None,
            medical_aid_number: str = None,
            **kwargs
    ):
        self.older_than_18: bool = older_than_18
        self.id_number: str = id_number
        self.passport_number: typing.Optional[str] = passport_number
        self.date_of_birth: str = date_of_birth
        self.first_names: str = first_names
        self.surname: str = surname
        self.gender: str = gender
        self.mobile_number: str = mobile_number
        self.email: str = email
        self.province: str = province
        self.municipality: str = municipality
        self.address: str = address
        self.weekday: int = weekday
        self.morning: int = morning
        self.medical_aid: bool = medical_aid
        self.medical_aid_scheme: str = medical_aid_scheme
        self.medical_aid_number: str = medical_aid_number
