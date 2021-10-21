from flask_sqlalchemy import SQLAlchemy
from random import randint

db = SQLAlchemy()


def random_key() -> int:
    _min = 100
    _max = 9999999999
    return randint(_min, _max)


class Gender(db.Model):
    gender = db.Column(db.String, primary_key=True)


class ContactDetails(db.Model):
    ID = db.Column(db.INT, default=random_key, primary_key=True)
    email = db.Column(db.String)
    phone_number = db.Column(db.String)


class Location(db.Model):
    ID = db.Column(db.INT, default=random_key, primary_key=True)
    province = db.Column(db.String)
    municipality = db.Column(db.String)
    address = db.Column(db.String)



# class PersonalDetails(db.Model):
#     # __tablename__ = 'Personal_Details'
#
#     id = db.Column(db.String(13), primary_key=True)
#     passport = db.Column(db.String())
#     surname = db.Column(db.String())
#     name = db.Column(db.String())
#     dob = db.Column(db.String())
#     gender = db.Column(db.String())
#
#     def __init__(self, id, passport, surname, name, dob, gender):
#         self.id = id
#         self.passport = passport
#         self.surname = surname
#         self.name = name
#         self.dob = dob
#         self.gender = gender

