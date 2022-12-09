from flask import Blueprint, redirect
from flask_login import login_required, current_user, login_user, logout_user
from app.user_form import LoginForm
from app.models import User

bp = Blueprint("session", __name__, url_prefix="/session")


@bp.route("", methods=["POST"])
def login():
    # flask_login.current_user
    if current_user.is_authenticated:
        return "User has logged in."
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter(User.email == data["email"]).first()
        if not user or not user.check_password(data["password"]):
            return redirect("login")
        login_user(user)
        return user.to_dict()
    return "Login page error"


@bp.route("", methods=["DELETE"])
@login_required
def logout():
    # flask_login.current_user.logout()
    logout_user()
    return "Log out successfully"
