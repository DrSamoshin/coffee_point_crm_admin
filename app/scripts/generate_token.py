from typing import Union
import jwt
import logging
from datetime import datetime, timedelta, timezone
from app.core.configs import settings

POINT_TYPE = "point"
ADMIN_TYPE = "admin"

def create_access_token(subject: str, token_type: str = POINT_TYPE, expires_delta: Union[timedelta, None] = None):
    to_encode = {"sub": subject}
    if expires_delta:
        to_encode["exp"] = datetime.now(timezone.utc) + expires_delta
    secret = None
    if token_type == POINT_TYPE:
        secret = settings.jwt_token.JWT_POINT_SECRET_KEY
    elif token_type == ADMIN_TYPE:
        secret = settings.jwt_token.JWT_ADMIN_SECRET_KEY
    logging.info(f"secret: {secret}")
    try:
        encoded_jwt = jwt.encode(
            payload=to_encode,
            key=secret,
            algorithm=settings.jwt_token.ALGORITHM,
        )
    except Exception as error:
        logging.error(error)
    else:
        return encoded_jwt


if __name__ == "__main__":
    user_id = input("user_id: ")
    token_type = input(f"token_type [{ADMIN_TYPE}, {POINT_TYPE}]: ")

    token = create_access_token(subject=user_id, token_type=token_type.strip())
    logging.info(f"token: {token}")
