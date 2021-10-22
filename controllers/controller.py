from flask import render_template, make_response, request, redirect, session
from VaccineRegistration import VaccineRegistration
from modules.decoders import vaccineRegistrationDecoder
from modules import dataValidation
from modules import models
from uuid import uuid4
import json


class Controller:
    @staticmethod
    def page0():
        if not session.get("id"):
            session["id"] = uuid4()
            session["user"] = VaccineRegistration().__dict__

        warning_phrase = ["Tap the box above to make a choice","This field must be selected"]
        if request.args.get("isOver18") == "YES":
            return redirect("/1")
        resp = make_response(render_template("0.html", **request.args))
        return resp

    @staticmethod
    def page1():
        if not session.get("user") or not session.get("user")["is_over_18"]:
            return redirect("0")
        req = request.args
        if req.get("id") == "true":
            return redirect("/2")
        elif req.get("passport") == "true":
            pass
        elif req.get("asylum") == "true":
            pass
        elif req.get("back") == "true":
            return redirect("/0")
        else:
            pass
        resp = make_response(render_template("1.html", **request.args))
        return resp

    @staticmethod
    def page2():
        if not session.get("user") or not session.get("user")["is_over_18"]:
            return redirect("0")
        if request.method == "POST":
            ID = request.form["IDNumber"]
            confID = request.form["confIDNum"]
            id_match = dataValidation.id_match(ID, confID)
            checksum = dataValidation.validateChecksum(ID)
            if checksum and id_match:
                user = vaccineRegistrationDecoder(session["user"])
                user.id_number = ID
                user.first_names = request.form["firstname"]
                user.last_name = request.form["surname"]
                user.date_of_birth = request.form["dob"]
                user.passport_number = request.form["passport"]
                user.gender = request.form["gender"]
                session["user"] = user.__dict__
                # PDetails = models.User(
                #     id_number=ID, passport_number=passport, surname, name, dob, gender)
                # models.db.session.add(PDetails)
                # models.db.session.commit()
                return redirect("/3")
            else:
                pass
        resp = make_response(render_template("2.html", **request.args))
        return resp

    @staticmethod
    def page3():
        if not session.get("user") or not session.get("user")["is_over_18"]:
            return redirect("0")
        print(session["user"])
        print(vaccineRegistrationDecoder(session["user"]))
        if request.args.get('next') == "true":
            return redirect("/4")
        elif request.args.get("back") == "true":
            return redirect("/2")
        else:
            pass

        resp = make_response(render_template("3.html", **request.args))
        return resp

    @staticmethod
    def page4():
        if not session.get("user") or not session.get("user")["is_over_18"]:
            return redirect("0")
        if request.args.get("return") == "true":
            return redirect("3")

        if request.args.get("submit") == "true":
            return redirect("5")

        provinces = [
            ("Eastern Cape", "EC"),
            ("Free State", "FS"),
            ("Gauteng", "GT"),
            ("KwaZulu-Natal", "KZN"),
            ("Limpopo", "LPO"),
            ("Mpumalanga", "MPU"),
            ("North West", "NW"),
            ("Northern Cape", "NC"),
            ("Western Cape", "WC"),
        ]
        municipalities = {
                "EC": [
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
                "FS": [
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
                "GT": [
                    "Emfuleni",
                    "Lesedi",
                    "Merafong City",
                    "Midvaal",
                    "Mogale City",
                    "Rand West City",
                ],
                "KZN": [
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
                "LPO": [
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
                "MPU": [
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
                "NW": [
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
                "NC": [
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
                "WC": [
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
        resp = make_response(render_template("4.html", **request.args, provinces=provinces, municipalities=municipalities))
        resp.set_cookie('page', "4")
        return resp

    @staticmethod
    def page5():
        if request.args.get("return") == "true":
            return redirect("4")

        if request.args.get("submit") == "true":
            return redirect("6")

        resp = make_response(render_template("5.html", **request.args))
        resp.set_cookie('page', "5")
        return resp

    @staticmethod
    def page6():
        if request.args.get("return") == "true":
            return redirect("5")

        if request.args.get("medical-aid") == "yes":
            return redirect("6a")

        elif request.args.get("medical-aid") == "no":
            return redirect("8")

        resp = make_response(render_template("6.html", **request.args))
        resp.set_cookie('page', "6")
        return resp

    @staticmethod
    def page6a():
        if request.args.get("return") == "true":
            return redirect("6")

        resp = make_response(render_template("6a.html", **request.args))
        resp.set_cookie('page', "6a")
        return resp

    @staticmethod
    def page7():
        if request.args.get("return") == "true":
            return redirect("6")

        resp = make_response(render_template("7.html", **request.args))
        resp.set_cookie('page', "7")
        return resp

    @staticmethod
    def page8():
        resp = make_response(render_template("8.html", **request.args))
        resp.set_cookie('page', "8")
        return resp
