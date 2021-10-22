from VaccineRegistration import VaccineRegistration


def vaccineRegistrationDecoder(obj) -> VaccineRegistration:
    return VaccineRegistration(**obj)