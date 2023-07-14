from ...db.db import MongoDB

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
