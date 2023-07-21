import random

from ...db.db import MongoDB

short_id_db = MongoDB("data", "short_id")


def get_all_short_id():
    return short_id_db.find_one({"type": "short_id"})


def generate_short_id():
    short_id = get_all_short_id()
    all_id = list(short_id["short_id"])

    while True:
        short_id = str(random.randint(0, 99))
        if short_id not in all_id:
            all_id.append(short_id)
            short_id_db.update_one(
                {"type": "short_id"},
                {"type": "short_id", "short_id": all_id},
            )
            return short_id
