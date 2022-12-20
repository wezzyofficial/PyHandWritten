import uuid


def new_hex() -> str:
    return uuid.uuid4().hex