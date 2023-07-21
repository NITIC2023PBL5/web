from flask import Blueprint, redirect, request, url_for
from flask_login import login_required, current_user

from ..services.lineNotify.auth import (
    get_redirect_auth_url,
    check_state,
    get_access_token,
)
from ..services.users.user import add_notify_token

notify_app = Blueprint("notify", __name__)


@login_required
@notify_app.route("/auth")
def auth():
    user = vars(current_user)
    if not "id" in user:
        return redirect(url_for("login"))

    url = get_redirect_auth_url(user["id"])
    return redirect(url)


@notify_app.route("/callback", methods=["POST"])
def callback():
    code = request.form["code"]
    state = request.form["state"]

    user = vars(current_user)
    if not "id" in user:
        return redirect(url_for("login"))

    if not check_state(state, user["id"]):
        return redirect(url_for("index"))

    access_token = get_access_token(code)
    add_notify_token(user["id"], access_token)
    return redirect(url_for("index"))
