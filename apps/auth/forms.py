from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(FlaskForm):
    username = StringField(
        "User Name",
        validators=[
            DataRequired("User Name is required."),
            Length(1, 30, "Enter within 30 characters."),
        ],
    )

    email = StringField(
        "Email Address",
        validators=[
            DataRequired("Email Address is required."),
            Email("Enter as Email format"),
        ],
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired("Password is required.")
        ],
    )

    submit = SubmitField("Create User")