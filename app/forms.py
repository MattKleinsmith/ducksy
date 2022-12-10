from flask_wtf import FlaskForm
from wtforms.fields import StringField, FloatField, TextAreaField, SubmitField, URLField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, URL, NumberRange


def validation_errors_formatter(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = {
        field: error
        for field in validation_errors
        for error in validation_errors[field]
    }
    return errorMessages


class LoginForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class SignupForm(FlaskForm):
    display_name = StringField(
        "Display Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    profile_picture_url = URLField(
        "Profile Picture URL",
        default="https://d23.com/app/uploads/2017/10/1180w-600h_101717_donald-nephews-anniversary_v3-780x440.jpg",
        validators=[URL()]
    )
    submit = SubmitField("Sign up")


class ProductForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    price = FloatField("Price", validators=[
                       DataRequired(), NumberRange(min=0)])
    description = TextAreaField("Description")

    submit = SubmitField("List product")
