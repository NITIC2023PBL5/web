from ...db.db import MongoDB

usersDb = MongoDB("data", "users")


def get_user(user_id: str):
    return usersDb.find_one({"id": user_id})


def upsert_user(user_id: str, name: str, email: str, profile_img: str):
    usersDb.update_one(
        {"id": user_id},
        {"id": user_id, "name": name, "email": email, "profile_img": profile_img},
    )
