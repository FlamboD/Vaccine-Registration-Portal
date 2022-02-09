from flask_sqlalchemy import SQLAlchemy
import uuid

from VaccineRegistration import VaccineRegistration

db = SQLAlchemy()


LOCATIONS = {
    "Eastern Cape": [
        "Amahlathi",
        "Blue Crane Route",
        "Dr Beyers Naudé",
        "Elundini",
        "Emalahleni",
        "Engcobo",
        "Enoch Mgijima",
        "Great Kei",
        "Ingquza Hill",
        "Intsika Yethu",
        "Inxuba Yethemba",
        "King Sabata Dalindyebo",
        "Kouga",
        "Koukamma",
        "Makana",
        "Matatiele",
        "Mbhashe",
        "Mhlontlo",
        "Mnquma",
        "Ndlambe",
        "Ngqushwa",
        "Ntabankulu",
        "Nyandeni",
        "Port St Johns",
        "Raymond Mhlaba",
        "Sakhisizwe",
        "Senqu",
        "Sundays River Valley",
        "Umzimvubu",
        "Walter Sisulu",
        "Winnie Madikizela-Mandela"],
    "Free State": [
        "Dihlabeng",
        "Kopanong",
        "Letsemeng",
        "Mafube",
        "Maluti-A-Phofung",
        "Mantsopa",
        "Masilonyana",
        "Matjhabeng",
        "Metsimaholo",
        "Mohokare",
        "Moqhaka",
        "Nala",
        "Ngwathe",
        "Nketoana",
        "Phumelela",
        "Setsoto",
        "Tokologo",
        "Tswelopele",
    ],
    "Gauteng": [
        "Emfuleni",
        "Lesedi",
        "Merafong City",
        "Midvaal",
        "Mogale City",
        "Rand West City",
    ],
    "KwaZulu-Natal": [
        "AbaQulusi",
        "Alfred Duma",
        "Big 5 Hlabisa",
        "City of uMhlathuze",
        "Dannhauser",
        "Dr Nkosazana Dlamini Zuma",
        "eDumbe",
        "eMadlangeni",
        "Endumeni",
        "Greater Kokstad",
        "Impendle",
        "Inkosi Langalibalele",
        "Jozini",
        "KwaDukuza",
        "Mandeni",
        "Maphumulo",
        "Mkhambathini",
        "Mpofana",
        "Msunduzi",
        "Mthonjaneni",
        "Mtubatuba",
        "Ndwedwe",
        "Newcastle",
        "Nkandla",
        "Nongoma",
        "Nquthu",
        "Okhahlamba",
        "Ray Nkonyeni",
        "Richmond",
        "Ubuhlebezwe",
        "Ulundi",
        "Umdoni",
        "uMfolozi",
        "uMhlabuyalingana",
        "uMlalazi",
        "uMngeni",
        "uMshwathi",
        "uMsinga",
        "Umuziwabantu",
        "Umvoti",
        "uMzimkhulu",
        "Umzumbe",
        "uPhongolo",
    ],
    "Limpopo": [
        "Ba-Phalaborwa",
        "Bela-Bela",
        "Blouberg",
        "Collins Chabane",
        "Elias Motsoaledi",
        "Ephraim Mogale",
        "Fetakgomo Tubatse",
        "Greater Giyani",
        "Greater Letaba",
        "Greater Tzaneen",
        "Lepelle-Nkumpi",
        "Lephalale",
        "Makhado",
        "Makhuduthamaga",
        "Maruleng",
        "Modimolle-Mookgophong",
        "Mogalakwena",
        "Molemole",
        "Musina",
        "Polokwane",
        "Thabazimbi",
        "Thulamela",
    ],
    "Mpumalanga": [
        "Bushbuckridge",
        "Chief Albert Luthuli",
        "City of Mbombela",
        "Dipaleseng",
        "Dr JS Moroka",
        "Dr Pixley Ka Isaka Seme",
        "Emakhazeni",
        "Emalahleni",
        "Govan Mbeki",
        "Lekwa",
        "Mkhondo",
        "Msukaligwa",
        "Nkomazi",
        "Steve Tshwete",
        "Thaba Chweu",
        "Thembisile Hani",
        "Victor Khanye",
    ],
    "North West": [
        "City of Matlosana",
        "Ditsobotla",
        "Greater Taung",
        "JB Marks",
        "Kagisano-Molopo",
        "Kgetlengrivier",
        "Lekwa-Teemane",
        "Madibeng",
        "Mahikeng",
        "Mamusa",
        "Maquassi Hills",
        "Moretele",
        "Moses Kotane",
        "Naledi",
        "Ramotshere Moiloa",
        "Ratlou",
        "Rustenburg",
        "Tswaing",
    ],
    "Northern Cape": [
        "!Kheis",
        "Dawid Kruiper",
        "Dikgatlong",
        "Emthanjeni",
        "Ga-Segonyana",
        "Gamagara",
        "Hantam",
        "Joe Morolong",
        "Kai !Garib",
        "Kamiesberg",
        "Kareeberg",
        "Karoo Hoogland",
        "Kgatelopele",
        "Khai-Ma",
        "Magareng",
        "Nama Khoi",
        "Phokwane",
        "Renosterberg",
        "Richtersveld",
        "Siyancuma",
        "Siyathemba",
        "Sol Plaatje",
        "Thembelihle",
        "Tsantsabane",
        "Ubuntu",
        "Umsobomvu",
    ],
    "Western Cape": [
        "Beaufort West",
        "Bergrivier",
        "Bitou",
        "Breede Valley",
        "Cape Agulhas",
        "Cederberg",
        "Drakenstein",
        "George",
        "Hessequa",
        "Kannaland",
        "Knysna",
        "Laingsburg",
        "Langeberg",
        "Matzikama",
        "Mossel Bay",
        "Oudtshoorn",
        "Overstrand",
        "Prince Albert",
        "Saldanha Bay",
        "Stellenbosch",
        "Swartland",
        "Swellendam",
        "Theewaterskloof",
        "Witzenberg",
    ]
}

MEDICAL_AID_SCHEMES = [
    "AECI MEDICAL AID SOCIETY",
    "ALLIANCE-MIDMED MEDICAL SCHEME",
    "ANGLO MEDICAL SCHEME",
    "ANGLOVAAL GROUP MEDICAL SCHEME",
    "BANKMED",
    "BARLOWORLD MEDICAL SCHEME",
    "BESTMED MEDICAL SCHEME",
    "BMW EMPLOYEES MEDICAL AID SOCIETY",
    "BONITAS MEDICAL FUND",
    "BP MEDICAL AID SOCIETY",
    "BUILDING & CONSTRUCTION INDUSTRY MEDICAL AID FUND",
    "CAPE MEDICAL PLAN",
    "CHARTERED ACCOUNTANTS (SA) MEDICAL AID FUND (CAMAF)",
    "COMPCARE WELLNESS MEDICAL SCHEME",
    "DE BEERS BENEFIT SOCIETY",
    "DISCOVERY HEALTH MEDICAL SCHEME",
    "ENGEN MEDICAL BENEFIT FUND",
    "FEDHEALTH MEDICAL SCHEME",
    "FISHING INDUSTRY MEDICAL SCHEME (FISH-MED)",
    "FOODMED MEDICAL SCHEME",
    "GENESIS MEDICAL SCHEME",
    "GLENCORE MEDICAL SCHEME",
    "GOLDEN ARROWS EMPLOYEES' MEDICAL BENEFIT FUND",
    "GOVERNMENT EMPLOYEES MEDICAL SCHEME (GEMS)",
    "HEALTH SQUARED MEDICAL SCHEME",
    "HORIZON MEDICAL SCHEME",
    "HOSMED MEDICAL AID SCHEME",
    "IMPALA MEDICAL PLAN",
    "IMPERIAL AND MOTUS MEDICAL AID",
    "KEYHEALTH",
    "LA-HEALTH MEDICAL SCHEME",
    "LIBCARE MEDICAL SCHEME",
    "LONMIN MEDICAL SCHEME",
    "MAKOTI MEDICAL SCHEME",
    "MALCOR MEDICAL SCHEME",
    "MASSMART HEALTH PLAN",
    "MBMED MEDICAL AID FUND",
    "MEDIHELP",
    "MEDIMED MEDICAL SCHEME",
    "MEDIPOS MEDICAL SCHEME",
    "MEDSHIELD MEDICAL SCHEME",
    "MOMENTUM MEDICAL SCHEME",
    "MOTOHEALTH CARE",
    "MULTICHOICE MEDICAL AID SCHEME",
    "NEDGROUP MEDICAL AID SCHEME",
    "NETCARE MEDICAL SCHEME",
    "OLD MUTUAL STAFF MEDICAL AID FUND",
    "PARMED MEDICAL AID SCHEME",
    "PG GROUP MEDICAL SCHEME",
    "PICK N PAY MEDICAL SCHEME",
    "PLATINUM HEALTH",
    "PROFMED",
    "QUANTUM MEDICAL AID SOCIETY",
    "RAND WATER MEDICAL SCHEME",
    "REMEDI MEDICAL AID SCHEME",
    "RETAIL MEDICAL SCHEME",
    "RHODES UNIVERSITY MEDICAL SCHEME",
    "SABC MEDICAL AID SCHEME",
    "SAMWUMED",
    "SASOLMED",
    "SEDMED",
    "SISONKE HEALTH MEDICAL SCHEME",
    "SIZWE MEDICAL FUND",
    "SOUTH AFRICAN BREWERIES MEDICAL SCHEME",
    "SOUTH AFRICAN POLICE SERVICE MEDICAL SCHEME (POLMED)",
    "SUREMED HEALTH",
    "TFG MEDICAL AID SCHEME",
    "THEBEMED",
    "TIGER BRANDS MEDICAL SCHEME",
    "TRANSMED MEDICAL FUND",
    "TSOGO SUN GROUP MEDICAL SCHEME",
    "UMVUZO HEALTH MEDICAL SCHEME",
    "UNIVERSITY OF KWA-ZULU NATAL MEDICAL SCHEME",
    "WITBANK COALFIELDS MEDICAL AID SCHEME",
    "WOOLTRU HEALTHCARE FUND"
]


def random_key() -> str:
    return str(uuid.uuid4())


class Province(db.Model):
    ID = db.Column(db.String, primary_key=True, default=random_key)
    name = db.Column(db.String)

    def __init__(self, *, name):
        self.ID = random_key()
        self.name = name


class Municipality(db.Model):
    ID = db.Column(db.String, primary_key=True, default=random_key)
    province = db.Column(db.String, db.ForeignKey("province.ID"))
    name = db.Column(db.String)

    def __init__(self, *, province, name):
        self.ID = random_key()
        self.province = province
        self.name = name


class Gender(db.Model):
    # ID = db.Column(db.String, primary_key=True, default=random_key)
    gender = db.Column(db.String, primary_key=True)

    def __init__(self, *, gender):
        # self.ID = random_key()
        self.gender = gender


class ContactDetails(db.Model):
    ID = db.Column(db.String, primary_key=True, default=random_key)
    email = db.Column(db.String)
    phone_number = db.Column(db.String)

    def __init__(self, *, email, phone_number):
        self.ID = random_key()
        self.email = email
        self.phone_number = phone_number


class Location(db.Model):
    ID = db.Column(db.String, primary_key=True, default=random_key)
    province = db.Column(db.String, db.ForeignKey(Province.ID), nullable=False)
    municipality = db.Column(db.String, db.ForeignKey(Municipality.ID), nullable=False)
    address = db.Column(db.String)

    def __init__(self, *, province, municipality, address=None):
        self.ID = random_key()
        self.province = province
        self.municipality = municipality
        self.address = address


class VaccineTimePreference(db.Model):
    ID = db.Column(db.String, primary_key=True, default=random_key)
    weekday = db.Column(db.Boolean, nullable=False)
    morning = db.Column(db.Boolean, nullable=False)

    def __init__(self, *, weekday, morning):
        self.ID = random_key()
        self.weekday = weekday
        self.morning = morning


class MedicalAidScheme(db.Model):
    ID = db.Column(db.String, primary_key=True, default=random_key)
    scheme_name = db.Column(db.String, nullable=False)

    def __init__(self, *, scheme_name):
        self.ID = random_key()
        self.scheme_name = scheme_name


class MedicalAid(db.Model):
    ID = db.Column(db.String, primary_key=True, default=random_key)
    scheme = db.Column(db.String, db.ForeignKey(MedicalAidScheme.ID), nullable=False)
    number = db.Column(db.String, nullable=False)

    def __init__(self, *, scheme, number):
        self.ID = random_key()
        self.scheme = scheme
        self.number = number


class User(db.Model):
    id_number = db.Column(db.String, primary_key=True)
    first_names = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    passport_number = db.Column(db.String)
    gender = db.Column(db.String, db.ForeignKey(Gender.gender), nullable=False)
    contact_details = db.Column(db.String, db.ForeignKey(ContactDetails.ID), nullable=False)
    location = db.Column(db.String, db.ForeignKey(Location.ID), nullable=False)
    vaccine_time_preference = db.Column(db.String, db.ForeignKey(VaccineTimePreference.ID), nullable=False)
    medical_aid = db.Column(db.String, db.ForeignKey(MedicalAid.ID))

    def __init__(
            self,
            *,
            id_number,
            first_names,
            surname,
            passport_number=None,
            gender,
            contact_details,
            location,
            vaccine_time_preference,
            medical_aid=None
    ):
        self.id_number = id_number
        self.first_names = first_names
        self.surname = surname
        self.passport_number = passport_number
        self.gender = gender
        self.contact_details = contact_details
        self.location = location
        self.vaccine_time_preference = vaccine_time_preference
        self.medical_aid = medical_aid


def setup_defaults():
    _LOCATIONS = {}

    if not Gender.query.count():
        for gender in ("Male", "Female", "Other"):
            db.session.add(Gender(gender=gender))

    if not Province.query.count():
        Municipality.query.delete()
        for province in LOCATIONS:
            _p = Province(name=province)
            db.session.add(_p)
            _LOCATIONS[_p.ID] = LOCATIONS[province]

    if not Municipality.query.count() and _LOCATIONS:
        for province in _LOCATIONS:
            for municipality in _LOCATIONS[province]:
                db.session.add(Municipality(province=province, name=municipality))

    if not MedicalAidScheme.query.count():
        for scheme_name in MEDICAL_AID_SCHEMES:
            db.session.add(MedicalAidScheme(scheme_name=scheme_name))

    db.session.commit()


def submit(user: VaccineRegistration):
    exists = User.query.get(user.id_number)
    if not exists:
        contact_details = ContactDetails(email=user.email, phone_number=user.mobile_number)
        db.session.add(contact_details)
        location = Location(province=user.province, municipality=user.municipality, address=user.address)
        db.session.add(location)
        medical_aid = MedicalAid(scheme=user.medical_aid_scheme, number=user.medical_aid_number)
        if user.medical_aid:
            db.session.add(medical_aid)
        time_pref = VaccineTimePreference(weekday=user.weekday == 1, morning=user.morning == 1)
        db.session.add(time_pref)

        db.session.commit()

        _user = User(
            id_number=user.id_number,
            first_names=user.first_names,
            surname=user.surname,
            passport_number=user.passport_number,
            gender=user.gender,
            contact_details=contact_details.ID,
            location=location.ID,
            vaccine_time_preference=time_pref.ID,
            medical_aid=medical_aid.ID if user.medical_aid else None)
        db.session.add(_user)

        db.session.commit()
    print("NOT IMPLEMENTED")
