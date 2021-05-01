from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class SubmitForm(FlaskForm):
    name = StringField("Task name", validators = [DataRequired(), Length(1, 64)])
    task = TextAreaField("Task", validators = [DataRequired()])
    submit = SubmitField("Submit")

    email = StringField("Enter email to receive confirmation")


