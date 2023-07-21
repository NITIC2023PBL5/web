from db.db import MongoDB
from flask_login import UserMixin

usersDb = MongoDB("data", "users")


class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id: str):
        user = usersDb.find_one({"id": user_id})
        if not user:
            return None

        user = User(
            id_=user["id"],
            name=user["name"],
            email=user["email"],
            profile_pic=user["profile_img"],
        )
        return user

    @staticmethod
    def create(user_id: str, name: str, email: str, profile_img: str):
        usersDb.insert_one(
            {"id": user_id, "name": name, "email": email, "profile_img": profile_img},
        )
