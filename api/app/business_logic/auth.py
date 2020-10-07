from models.teams import TeamUser
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
)
import bcrypt
import typing as tp


def auth(login: str, password: str) -> tp.Optional[tp.Tuple[str, str]]:
    """Login by password and receive JWT token."""

    user = TeamUser.objects.filter(login=login).first()
    if not user:
        return None

    if user and bcrypt.checkpw(password.encode("utf8"), user.hashpw.encode("utf8")):
        current_user = str(user.id)
        new_token = create_access_token(identity=current_user, expires_delta=False)
        new_refresh = create_refresh_token(identity=current_user, expires_delta=False)
        return new_token, new_refresh
    return None
