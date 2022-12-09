from flask import Blueprint
from flask_login import login_required, current_user, login_user, logout_user
from sqlalchemy.exc import IntegrityError
from app.user_form import SignupForm
from app.models import db, User
from . import products


bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("",  methods=["GET", "POST"])
def signup():
    try:
        if current_user.is_authenticated:
            return 'User has logged in'
        form = SignupForm()
        if form.validate_on_submit():
            data = form.data
            print(form.data)
            # print(data)
            # user = User(
            #     **data
            # )
            # db.session.add(user)
            # db.session.commit()
            # return user.to_dict()
            return "hi"
    except IntegrityError:
        return "Failed to sign up"
