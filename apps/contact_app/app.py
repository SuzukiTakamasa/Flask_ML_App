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
    make_response,
    session,
)
import logging
import os
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message

app = Flask(__name__)
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"
app.logger.setLevel(logging.DEBUG)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)

app.config["MAIL_SERVER"] = os.environ["MAIL_SERVER"]
app.config["MAIL_PORT"] = os.environ["MAIL_PORT"]
app.config["MAIL_USE_TLS"] = os.environ["MAIL_USE_TLS"]
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
app.config["MAIL_DEFAULT_SENDER"] = os.environ["MAIL_DEFAULT_SENDER"]

mail = Mail(app)

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
    response =  make_response(render_template("contact.html"))
    response.set_cookie("flask_app key", "flask_app value")
    session["username"] = "Suzuki"
    return response

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
        def send_email(to, subject, template, **kwargs):
            msg = Message(subject, recipients=[to])
            msg.body = render_template(template + ".txt", **kwargs)
            msg.html = render_template(template + ".html", **kwargs)
            mail.send(msg)

        send_email(email,"Thank you for your contact", "contact_mail", username=username, description=description)
        flash("Thank you for your contact.")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")
