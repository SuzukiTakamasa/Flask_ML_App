from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name="Piraruku")

@app.route("/data_lists/<string:name>",
          methods=["GET", "POST"],
          endpoint="data_lists_endpoint")
def data_lists(name):
    return "Here is some data, {}".format(name)

with app.test_request_context():
    print(url_for("index"))
    print(url_for("data_lists_endpoint", name="Piraruku", page=1))
