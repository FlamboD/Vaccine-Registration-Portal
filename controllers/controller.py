from flask import Flask, render_template, make_response, request, redirect
from modules import dataValidation
from modules import models


class Controller:
    @staticmethod
    def page0():
        warning_phrase = ["Tap the box above to make a choice","This field must be selected"]
        if request.args.get("isOver18") == "YES":
            return redirect("/1")
        resp = make_response(render_template("0.html", **request.args))
        resp.set_cookie('page', "0")
        return resp

    @staticmethod
    def page1():
        req = request.args
        if req.get("id")=="true":
            return redirect("/2")
        elif req.get("passport")=="true":
            pass
        elif req.get("asylum")=="true":
            pass
        elif req.get("back")=="true":
            return redirect("/0")
        else:
            pass
        resp = make_response(render_template("1.html",**request.args))
        resp.set_cookie('page',"1")
        return resp

    @staticmethod
    def page2():
        ID = name = surname = dob = confID = passport = ""
        checksum = True
        if request.method == "POST":
            ID = request.form["IDNumber"]
            name = request.form["firstname"]
            dob = request.form["dob"]
            passport = request.form["passport"]
            confID = request.form["confIDNum"]
            surname = request.form["surname"]
            gender = request.form["gender"]
            checksum = dataValidation.validateChecksum(ID)
            id_match = dataValidation.id_match(ID, confID)
            if checksum:
                PDetails = models.personal_details(ID, passport, surname, name, dob, gender)
                models.db.session.add(PDetails)
                models.db.session.commit()
                return redirect("/3")
            else:
                pass

    @staticmethod
    def page3():
        if request.args.get('next') == "true":
            return redirect("/4")
        elif request.args.get("back") == "true":
            return redirect("/2")
        else:
            pass

        resp = make_response(render_template("3.html", **request.args))
        resp.set_cookie('page', "3")
        return resp

    @staticmethod
    def page4():
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
