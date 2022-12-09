from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    class Meta:
        csrf = False  # TODO: Turn this off once we have a frontend

    email = EmailField(
        "Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class SignupForm(FlaskForm):
    class Meta:
        csrf = False  # TODO: Turn this off once we have a frontend
    display_name = StringField(
        "Display Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    profile_picture_url = URLField("Profile Picture URL")
    submit = SubmitField("Sign up")
