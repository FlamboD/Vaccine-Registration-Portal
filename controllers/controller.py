from collections import defaultdict

from flask import render_template, make_response, request, redirect, session
from VaccineRegistration import VaccineRegistration
from modules.decoders import VRDecoder, VREncoder
from modules import dataValidation
from modules import models
from uuid import uuid4
import json

from modules.models import submit


class Controller:
    @staticmethod
    def page0():
        print(0)

        if not session.get("user"):
            session["user"] = VREncoder(VaccineRegistration())

        warning_phrase = ["Tap the box above to make a choice","This field must be selected"]
        if request.args.get("isOver18") == "YES":
            user = VRDecoder(session.get("user"))
            user.older_than_18 = True
            session["user"] = VREncoder(user)
            return redirect("/1")
        resp = make_response(render_template("0.html", **request.args))
        return resp

    @staticmethod
    def page1():
        print(1)

        _ = dataValidation.access_page(1, VRDecoder(session.get("user")))
        if _ != 1: return redirect(str(_))

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
        print(2)

        _ = dataValidation.access_page(2, VRDecoder(session.get("user")))
        if _ != 2: return redirect(str(_))

        if not session.get("user") or not session.get("user")["older_than_18"]:
            return redirect("0")
        if request.method == "POST":
            ID = request.form["IDNumber"]
            confID = request.form["confIDNum"]
            id_match = dataValidation.id_match(ID, confID)
            checksum = dataValidation.validateChecksum(ID)
            if checksum and id_match:
                user = VRDecoder(session["user"])
                user.id_number = ID
                user.first_names = request.form["firstname"]
                user.surname = request.form["surname"]
                user.date_of_birth = request.form["dob"]
                user.passport_number = request.form["passport"]
                user.gender = request.form["gender"]
                session["user"] = user.__dict__

                return redirect("/3")
            else:
                pass

        user = VRDecoder(session["user"])
        resp = make_response(render_template("2.html", **request.args, genders=models.Gender.query.all(), user=user))
        return resp

    @staticmethod
    def page3():
        print(3)

        _ = dataValidation.access_page(3, VRDecoder(session.get("user")))
        if _ != 3: return redirect(str(_))

        if request.args.get('next') == "true":

            user = VRDecoder(session.get("user"))
            user.mobile_number = request.args.get("mobile-number")
            user.email = request.args.get("email")
            session["user"] = VREncoder(user)

            return redirect("/4")
        elif request.args.get("back") == "true":
            return redirect("/2")
        else:
            pass

        user = VRDecoder(session.get("user"))
        resp = make_response(render_template("3.html", **request.args, user=user))
        return resp

    @staticmethod
    def page4():
        print(4)

        _ = dataValidation.access_page(4, VRDecoder(session.get("user")))
        if _ != 4: return redirect(str(_))

        if request.args.get("return") == "true":
            return redirect("3")

        if request.args.get("submit") == "true":

            user = VRDecoder(session.get("user"))
            user.province = request.args.get("province")
            user.municipality = request.args.get("municipality")
            user.address = request.args.get("address")
            session["user"] = VREncoder(user)

            return redirect("5")

        groups = defaultdict(list)
        for _m in models.Municipality.query.all():
            groups[_m.province].append((_m.name, _m.ID))

        provinces = [(_.name, _.ID) for _ in models.Province.query.all()]
        municipalities = dict(groups)

        user = VRDecoder(session.get("user"))
        resp = make_response(render_template("4.html", **request.args, provinces=provinces, municipalities=municipalities, user=user))
        return resp

    @staticmethod
    def page5():
        print(5)

        _ = dataValidation.access_page(5, VRDecoder(session.get("user")))
        if _ != 5: return redirect(str(_))

        if request.args.get("return") == "true":
            return redirect("4")

        if request.args.get("submit") == "true":

            user = VRDecoder(session.get("user"))
            user.weekday = 1 if request.args.get("week") == "weekday" else 0
            user.morning = 1 if request.args.get("day") == "morning" else 0
            session["user"] = VREncoder(user)

            return redirect("6")

        user = VRDecoder(session.get("user"))
        resp = make_response(render_template("5.html", **request.args, user=user))
        return resp

    @staticmethod
    def page6():
        print(6)

        _ = dataValidation.access_page(6, VRDecoder(session.get("user")))
        if _ != 6: return redirect(str(_))

        if request.args.get("return") == "true":
            return redirect("5")

        if request.args.get("medical-aid") == "yes":
            return redirect("6a")

        elif request.args.get("medical-aid") == "no":
            return redirect("7")

        user = VRDecoder(session.get("user"))
        resp = make_response(render_template("6.html", **request.args, user=user))
        return resp

    @staticmethod
    def page6a():
        print("6a")

        _ = dataValidation.access_page(6, VRDecoder(session.get("user")))
        if _ != 6: return redirect(str(_))

        if request.args.get("return") == "true":
            return redirect("6")

        if request.args.get("submit") == "true":

            user = VRDecoder(session.get("user"))
            user.medical_aid_scheme = request.args.get("medical-scheme-name")
            user.medical_aid_number = request.args.get("medical-scheme-number")
            session["user"] = VREncoder(user)

            return redirect("7")

        user = VRDecoder(session.get("user"))
        resp = make_response(render_template("6a.html", **request.args, schemes=models.MedicalAidScheme.query.all(), user=user))
        return resp

    @staticmethod
    def page7():
        if request.args.get("return") == "true":
            return redirect("6")

        user = VRDecoder(session.get("user"))
        resp = make_response(render_template("7.html", **request.args, user=user))
        return resp

    @staticmethod
    def page8():

        user = VRDecoder(session.get("user"))
        models.submit(user)

        resp = make_response(render_template("8.html", **request.args))
        return resp
