from flask import Blueprint, request
from flask_login import login_required, current_user, login_user, logout_user
from sqlalchemy.exc import IntegrityError
from app.forms import SignupForm
from app.models import db, User


bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("",  methods=["POST"])
def signup():
    try:
        if current_user.is_authenticated:
            return 'User has logged in'
        form = SignupForm()
        # form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            data = form.data
            user = User(
                display_name=data['display_name'],
                email=data['email'],
                password=data['password']
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return user.to_dict()
    except IntegrityError:
        return "Failed to sign up"
