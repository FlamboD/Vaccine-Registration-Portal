from flask_sqlalchemy import SQLAlchemy
import uuid

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
    ID = db.Column(db.String, primary_key=True, default=random_key)
    gender = db.Column(db.String)

    def __init__(self, *, gender):
        self.ID = random_key()
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


class MedicalAid(db.Model):
    ID = db.Column(db.String, primary_key=True, default=random_key)
    scheme_name = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)

    def __init__(self, *, scheme_name, number):
        self.ID = random_key()
        self.scheme_name = scheme_name
        self.number = number


class User(db.Model):
    id_number = db.Column(db.String, primary_key=True)
    first_names = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    passport_number = db.Column(db.String)
    gender = db.Column(db.String, db.ForeignKey(Gender.ID), nullable=False)
    contact_details = db.Column(db.String, db.ForeignKey(ContactDetails.ID), nullable=False)
    location = db.Column(db.String, db.ForeignKey(Location.ID), nullable=False)
    vaccine_time_preference = db.Column(db.String, db.ForeignKey(VaccineTimePreference.ID), nullable=False)
    medical_aid = db.Column(db.String, db.ForeignKey(MedicalAid.ID))

    def __init__(
            self,
            *,
            id_number,
            first_names,
            last_name,
            passport_number=None,
            gender,
            contact_details,
            location,
            vaccine_time_preference,
            medical_aid=None
    ):
        self.id_number = id_number
        self.first_names = first_names
        self.last_name = last_name
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

    if not db.session.query(Province).count():
        Municipality.query.delete()
        for province in LOCATIONS:
            _p = Province(name=province)
            db.session.add(_p)
            _LOCATIONS[_p.ID] = LOCATIONS[province]

    if not db.session.query(Municipality).count() and _LOCATIONS:
        for province in _LOCATIONS:
            for municipality in _LOCATIONS[province]:
                db.session.add(Municipality(province=province, name=municipality))

    db.session.commit()
