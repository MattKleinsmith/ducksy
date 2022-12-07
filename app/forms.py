from flask_wtf import FlaskForm

from wtforms.fields import StringField, FloatField, TextAreaField, SubmitField

from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    class Meta:
        csrf = False  # TODO: Turn this off once we have a frontend

    name = StringField("Name", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    description = TextAreaField("Description")

    submit = SubmitField("List product")
