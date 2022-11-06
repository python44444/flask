from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return "What the fuckkkkkkkkkkkkkkkkkk!!!!!!!!!"


@app.route("/abcde")
def hello2():
    return "ABCDE"


@app.route("/user/age/<age>")
def heyName(age):
    return age


@app.route("/html")
def html():
    # return "<h1>Hello HTML</h1>"
    return render_template("index.html")


@app.route("/html/<shit>")
def htmlShit(shit):
    # return "<h1>Hello HTML</h1>"
    return render_template("shit.html", name=shit)


@app.route("/query")
def query():
    search_text = request.args.get("search_text")
    if search_text is not None:
        return search_text
    else:
        return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
