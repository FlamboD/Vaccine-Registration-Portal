from VaccineRegistration import VaccineRegistration


def validateChecksum(id_number: str):
    if not id_number.isdigit or len(id_number) != 13: return False

    total = 0

    for i in range(13):
        _ = int(id_number[i]) * (i % 2 + 1)
        if _ > 9: _ = int(str(_)[0]) + int(str(_)[1])
        total += _

    return not total % 10

    # sum = 0
    # miniSum = 0
    # current_digit = 0
    # checksum = None
    # if ((id_number.isdigit()) & (len(id_number)==13)):
    #     for i in range(0,12):
    #         current_digit = int(id_number[i])
    #         if not(i%2==0):
    #             product = current_digit*2
    #             if product>9:
    #                 miniSum = int(str(product)[0])+ int(str(product)[1])
    #                 sum +=miniSum
    #             else:
    #                 sum +=product
    #         else:
    #             sum += current_digit
    # checksum = 10-(sum%10)
    #
    # if checksum>9:
    #     checksum = 0
    # if checksum==int(id_number[12]):
    #     return True
    # else:
    #     return False


def id_match(id_number: str, conf_id: str):
    return str(id_number) == str(conf_id)


def access_page(page: int, vrp: VaccineRegistration):
    print(vrp.__dict__)

    def inner():
        if not vrp or not vrp.older_than_18:
            return 0
        if not vrp.id_number:
            return 2
        if not vrp.mobile_number:
            return 3
        if not vrp.province:
            return 4
        if -1 in (vrp.morning, vrp.weekday):
            return 5
        if page == 6 and not vrp.medical_aid:
            return 6
        return page

    print(inner(), page)
    return min(inner(), page)
