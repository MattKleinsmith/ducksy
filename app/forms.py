from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.fields import StringField, FloatField, TextAreaField, SubmitField, URLField, EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, URL, NumberRange, Length


def validation_errors_formatter(form, validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = {
        form[field].label.text: error
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
        "Display name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    profile_picture_url = URLField(
        "Profile picture URL",
        default="https://d23.com/app/uploads/2017/10/1180w-600h_101717_donald-nephews-anniversary_v3-780x440.jpg",
        validators=[URL()]
    )
    submit = SubmitField("Sign up")


class ProductForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=140)])
    price = FloatField("Price", validators=[
                       DataRequired(), NumberRange(min=0)])
    description = TextAreaField("Description")

    submit = SubmitField("List product")


def require_image_or_url(form, field):
    return form.url.data or form.image.data


class ProductImageForm(FlaskForm):
    url = URLField()
    image = FileField()
    preview = BooleanField(default=False)
    submit = SubmitField()


class ReviewForm(FlaskForm):
    rating = StringField("Star rating", validators=[DataRequired()])
    review = TextAreaField("Review text", validators=[DataRequired()])
    submit = SubmitField()
