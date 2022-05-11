from email_validator import validate_email, EmailNotValidError
from flask import (
    Flask,
    render_template,
    url_for,
    current_app,
    g,
    request,
    redirect,
    flash,
)
import logging

app = Flask(__name__)
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"
app.logger.setLevel(logging.DEBUG)

#TOP(index)画面
@app.route("/")
def index():
    return render_template("index.html", name="Piraruku")

#一覧画面
@app.route("/data_lists/<string:name>", methods=["GET", "POST"], endpoint="data_lists_endpoint")
def data_lists(name):
    return "Here is some data, {}".format(name)

#お問い合わせフォーム画面
@app.route("/contact")
def contact():
    return render_template("contact.html")

#お問い合わせ完了画面
@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        is_valid = True

        if not username:
            flash("User Name is required.")
            is_valid = False
        
        if not email:
            flash("Email Address is required.")
            is_valid = False
        
        try:
            validate_email(email)
        except:
            flash("Enter as email format.")
            is_valid = False
        
        if not description:
            flash("Contact Content is required.")
            is_valid = False
        
        if not is_valid:
            return redirect(url_for("contact"))

        #Send Email
        flash("Thank you for your contact.")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")