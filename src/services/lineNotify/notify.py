import requests


def send_notification(token: str, message: str):
    res = requests.post(
        "https://notify-api.line.me/api/notify",
        headers={"Authorization": f"Bearer {token}"},
        data={"message": message},
    )

    return res
