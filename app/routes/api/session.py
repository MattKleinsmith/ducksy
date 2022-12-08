from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from app.forms import LoginForm
from app.models import User

bp = Blueprint("session", __name__, url_prefix="/session")


@bp.route("/")
def already_logged_in():
    if current_user.is_authenticated:
        return redirect(url_for("success"))
    return render_template("login.html", form=LoginForm())


@bp.route("/", methods=["POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if not user or not user.check_password(form.password.data):
            return redirect(url_for(".login"))
        login_user(user)
        return redirect(url_for("success"))


@bp.route("/", methods=["DELETE"])
def logout():
    logout_user()
    return redirect(url_for('.login'))
