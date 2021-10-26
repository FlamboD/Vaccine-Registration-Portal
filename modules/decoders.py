from VaccineRegistration import VaccineRegistration


def VRDecoder(obj) -> VaccineRegistration:
    return VaccineRegistration(**obj)


def VREncoder(obj):
    return obj.__dict__
