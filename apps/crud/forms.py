from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length

#Class for user creation and update
class UserForm(FlaskForm):
    username = StringField(
        "User name",
        validators=[
            DataRequired(message="User name is required."),
            length(max=30, message="Enter name within 30 charactors."),
        ],
    )

    email = StringField(
        "Email Address",
        validators=[
            DataRequired(message="Email address is required."),
            Email(message="Enter as Email format.")
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required.")
        ]
    )

    submit = SubmitField("Create")