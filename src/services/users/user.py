from db.db import MongoDB
from flask_login import UserMixin

usersDb = MongoDB("data", "users")


def get_user(user_id: str):
    return usersDb.find_one({"id": user_id})


def get_user_by_short_id(short_id: str):
    return usersDb.find_one({"short_id": short_id})


def upsert_user(
    user_id: str,
    name: str,
    email: str,
    profile_img: str,
    short_id: str | None,
    status: bool,
    notify_token: str | None,
):
    return usersDb.update_one(
        {"id": user_id},
        {
            "id": user_id,
            "name": name,
            "email": email,
            "profile_img": profile_img,
            "short_id": short_id,
            "status": status,
            "notify_token": notify_token,
        },
    )


class User(UserMixin):
    def __init__(
        self,
        id_: str,
        name: str,
        email: str,
        profile_img: str,
        short_id: str | None,
        status: bool,
        notify_token: str | None,
    ):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_img
        self.short_id = short_id
        self.status = status
        self.notify_token = notify_token

    @staticmethod
    def get(user_id: str):
        user = usersDb.find_one({"id": user_id})
        if not user:
            return None

        return User(
            id_=user["id"],
            name=user["name"],
            email=user["email"],
            profile_img=user["profile_img"],
            short_id=user["short_id"],
            status=user["status"],
            notify_token=user["notify_token"],
        )

    @staticmethod
    def create(
        user_id: str,
        name: str,
        email: str,
        profile_img: str,
        short_id: str | None,
        status: bool,
        notify_token: str | None,
    ):
        usersDb.update_one(
            {"id": user_id},
            {
                "id": user_id,
                "name": name,
                "email": email,
                "profile_img": profile_img,
                "short_id": short_id,
                "status": status,
                "notify_token": notify_token,
            },
        )
