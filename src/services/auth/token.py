import os
from dotenv import load_dotenv

load_dotenv()
TOKEN_LIST = os.getenv("TOKEN").split(",")


def check_token(token1: str | None, token2: str | None) -> bool:
    if not token1 and not token2:
        return False

    token = token1 if token1 else token2
    return token in TOKEN_LIST
