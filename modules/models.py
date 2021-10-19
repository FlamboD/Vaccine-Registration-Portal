from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class personal_details(db.Model):
    __tablename__ = 'Personal_Details'
 
    id = db.Column(db.String(13), primary_key = True)
    passport = db.Column(db.String())
    surname =  db.Column(db.String())
    name = db.Column(db.String())
    dob = db.Column(db.String())
    gender = db.Column(db.String())
 
    def __init__(self,id, passport,surname,name,dob,gender):
        self.id = id
        self.passport =passport
        self.surname = surname
        self.name = name
        self.dob = dob
        self.gender = gender

class contact_details(db.Model):
    __tablename__ = 'Contact_Details'
    id = db.Column(db.String(13), foreign_key = True)
    cellphone_number =  db.Column(db.String(10))
    email_address = db.Column(db.String())

    def __init__(self,id, cellphone_number,email_address):
        self.id = id
        self.cellphone_number = cellphone_number
        self.email_address = email_address