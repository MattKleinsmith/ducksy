from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, EmailField, URLField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    class Meta:
        csrf = False  # TODO: Turn this off once we have a frontend

    email = StringField(
        "Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class SignupForm(FlaskForm):
    display_name = StringField(
        "Display Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    profile_picture = URLField("Profile Picture")
    submit = SubmitField("Sign up")
