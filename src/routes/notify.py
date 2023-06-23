from flask import Blueprint, redirect, request

from ..services.lineNotify import auth as lineNotifyAuth

notify_app = Blueprint("notify", __name__)


@notify_app.route("/auth")
def auth():
    # TODO: ユーザーIDをセッションから取得する
    url = lineNotifyAuth.get_redirect_auth_url("USER_ID")
    return redirect(url)


@notify_app.route("/callback", methods=["POST"])
def callback():
    code = request.form["code"]
    state = request.form["state"]

    # TODO: ユーザーIDをセッションから取得する
    if not lineNotifyAuth.check_state(state, "USER_ID"):
        return redirect("/", code=400)

    access_token = lineNotifyAuth.get_access_token(code)
    return access_token