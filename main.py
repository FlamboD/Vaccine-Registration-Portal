from flask import Flask, render_template, request
from routes.routes import page0, page1, page2, page3, page4, page5, page6, page6a, page8

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/0")
def home():
    print({**request.cookies})
    print(bool(request.cookies))
    return page0()


@app.route("/1")
def step1():
    print({**request.cookies})
    print(bool(request.cookies))
    return page1()


@app.route("/2")
def step2():
    print({**request.cookies})
    print(bool(request.cookies))
    return page2()


@app.route("/3")
def step3():
    print({**request.cookies})
    print(bool(request.cookies))
    return page3()


@app.route("/4")
def step4():
    print({**request.args})
    return page4()


@app.route("/5")
def step5():
    print({**request.args})
    return page5()


@app.route("/6")
def step6():
    return page6()


@app.route("/6a")
def step6a():
    return page6a()


@app.route("/8")
def step8():
    return page8()


if __name__ == "__main__":
    app.run(debug=True)
