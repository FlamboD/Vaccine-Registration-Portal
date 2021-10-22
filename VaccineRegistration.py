import typing


class VaccineRegistration:
    def __init__(
            self,
            *args,
            older_than_18: typing.Optional[bool] = None,
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
            weekday: bool = typing.Optional[None],
            morning: bool = typing.Optional[None],
            medical_aid: bool = None,
            medical_aid_scheme_name: str = None,
            medical_aid_number: str = None,
            **kwargs
    ):
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
        self.weekday: typing.Optional[bool] = weekday
        self.morning: typing.Optional[bool] = morning
        self.medical_aid: bool = medical_aid
        self.medical_aid_scheme_name: str = medical_aid_scheme_name
        self.medical_aid_number: str = medical_aid_number
