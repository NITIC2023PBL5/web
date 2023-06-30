import os
import hashlib
from dotenv import load_dotenv
import requests

load_dotenv()

CLIENT_ID = os.environ["LINE_NOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["LINE_NOTIFY_CLIENT_SECRET"]
REDIRECT_URI = os.environ["LINE_NOTIFY_REDIRECT_URI"]


def get_redirect_params(user_id: str):
    return {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "notify",
        "state": hashlib.sha256(user_id.encode()).hexdigest(),
        "response_mode": "form_post",
    }


def get_redirect_auth_url(user_id: str):
    params = get_redirect_params(user_id)
    url = "https://notify-bot.line.me/oauth/authorize?"
    for key, value in params.items():
        url += f"{key}={value}&"
    return url


def check_state(state: str, user_id: str):
    return state == hashlib.sha256(user_id.encode()).hexdigest()


def get_access_token(code: str):
    res = requests.post(
        "https://notify-bot.line.me/oauth/token",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    if res.status_code == 200:
        d = res.json()
        return d["access_token"]
