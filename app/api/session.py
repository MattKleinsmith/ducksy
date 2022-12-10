from flask import Blueprint, request
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm
from app.models import User

bp = Blueprint("session", __name__, url_prefix="/session")


@bp.route("")
def restore():
    if current_user.is_authenticated:
        return current_user.to_dict()
    else:
        return {"message": "Not logged in"}, 400


@bp.route("", methods=["POST"])
def login():
    if current_user.is_authenticated:
        return {"message": "Already logged in"}, 400

    form = LoginForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if not user or not user.check_password(form.password.data):
            return {"message": "Failed to log in"}, 400
        login_user(user)
        return user.to_dict()
    return {"message": "Failed to log in"}, 400


@bp.route("", methods=["DELETE"])
@login_required
def logout():
    logout_user()
    return {"message": "Logged out"}


@bp.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
