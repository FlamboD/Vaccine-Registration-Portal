import os

from flask import Flask, render_template, request
from controllers.controller import Controller
from controllers.database_controller import DatabaseController
from dotenv import load_dotenv
from modules import models

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
models.db.init_app(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/0")
def home():
    print({**request.cookies})
    print(bool(request.cookies))
    return Controller.page0()


@app.route("/1")
def step1():
    print({**request.cookies})
    print(bool(request.cookies))
    return Controller.page1()


@app.route("/2")
def step2():
    print({**request.cookies})
    print(bool(request.cookies))
    return Controller.page2()


@app.route("/3")
def step3():
    print({**request.cookies})
    print(bool(request.cookies))
    return Controller.page3()


@app.route("/4")
def step4():
    print({**request.args})
    return Controller.page4()


@app.route("/5")
def step5():
    print({**request.args})
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
    # DatabaseController.create()

    with app.app_context():
        models.db.create_all()
    app.run(debug=True)

