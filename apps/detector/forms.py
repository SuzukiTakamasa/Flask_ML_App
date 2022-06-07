from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField

class UploadImageForm(FlaskForm):
    image = FileField(
        validators=[
            FileRequired("Select image files."),
            FileAllowed(["png", "jpg", "jpeg"],
            "Unsupported image type")
        ]
    )

    submit = SubmitField("Upload")

class DetectorForm(FlaskForm):
    submit = SubmitField("Verification")