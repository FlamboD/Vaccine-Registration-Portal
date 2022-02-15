import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flaskext.couchdb import CouchDBManager

from controllers.controller import Controller
from controllers.database_controller import DatabaseController
from modules import models

manager = CouchDBManager()
load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = str.format(os.getenv("DATABASE_URI"), dir=os.getcwd())
app.config["SESSION_TYPE"] = 'filesystem'
app.config['FLASK_DEBUG'] = 1
app.secret_key = "secret"
models.db.init_app(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/")
def home_():
    return Controller.page0()
    
@app.route("/0")
def home():
    return Controller.page0()


@app.route("/1")
def step1():
    return Controller.page1()


@app.route("/2", methods=["GET", "POST"])
def step2():
    return Controller.page2()


@app.route("/3")
def step3():
    return Controller.page3()


@app.route("/4")
def step4():
    return Controller.page4()


@app.route("/5")
def step5():
    return Controller.page5()


@app.route("/6")
def step6():
    return Controller.page6()


@app.route("/6a")
def step6a():
    return Controller.page6a()


@app.route("/7")
def step7():
    return Controller.page7()


@app.route("/8")
def step8():
    return Controller.page8()


if __name__ == "__main__":
    DatabaseController.create()

    with app.app_context():
        # engine = models.db.get_engine()
        models.db.create_all()
        models.setup_defaults()
    manager.setup(app)
    app.run(debug=True)

