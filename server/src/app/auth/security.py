from src.app.config import settings
from typing import Optional, Sequence
from src.app.models.user import User
from datetime import timedelta, datetime, timezone
from argon2 import PasswordHasher
from argon2.exceptions import (
    VerifyMismatchError,
    VerificationError,
    InvalidHashError,
)
import jwt
from jwt.exceptions import InvalidTokenError
from src.app.data.user import get_users

password_hasher = PasswordHasher()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return password_hasher.verify(hashed_password, plain_password)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        return False
    
def hash_password(password: str) -> str:
    return password_hasher.hash(password)

def create_access_token(data: dict):
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = data.copy()
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

def verify_token(token: str, token_type: str = "access") -> Optional[dict]:
    try:
        payload = jwt.decode(jwt = token, key = settings.SECRET_KEY, algorithms = [settings.ALGORITHM])
        return payload
    except InvalidTokenError:
        return None

def verify_beyond_user_limit() -> bool:
    users: Sequence[User] = get_users()
    if (len(users) > settings.USER_LIMIT):
        return True
    else:
        return False
    
#def create_refresh_token(data: dict) -> str: