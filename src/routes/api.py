from flask import Blueprint, request

from ..services.users.user import get_user_by_short_id, upsert_user
from ..services.auth.token import check_token
from ..services.lineNotify.notify import send_notification

api_app = Blueprint("api", __name__)


@api_app.route("/status/<short_id>", methods=["GET", "POST", "DELETE"])
def status(short_id):
    token_state = check_token(request.get_data("token"), request.args.get("token"))
    if not token_state:
        return {"status": "invalid token"}

    param_method = request.args.get("method")
    request_method = request.method

    if request_method == "GET" and param_method != None:
        if param_method.upper() == "POST" or param_method.upper() == "DELETE":
            request_method = param_method.upper()

    if request_method == "GET":
        return {"status": "invalid method"}

    user = get_user_by_short_id(short_id)
    if user == None:
        return {"status": "user not found"}

    upsert_user(
        user_id=user["id"],
        name=user["name"],
        email=user["email"],
        profile_img=user["profile_img"],
        short_id=user["short_id"],
        status=(request_method == "POST"),
        notify_token=user["notify_token"],
    )
    return {"status": "ok"}


@api_app.route("/notify/<short_id>", methods=["GET", "POST"])
def notify(short_id):
    token_state = check_token(request.get_data("token"), request.args.get("token"))
    if not token_state:
        return {"status": "invalid token"}

    param_msg = request.args.get("message")
    msg = request.get_data("message")

    if not param_msg and not msg:
        return {"status": "invalid message"}

    if not msg:
        msg = param_msg

    user = get_user_by_short_id(short_id)
    if user == None:
        return {"status": "user not found"}

    res = send_notification(user["notify_token"], msg)
    return res.text
