from src.app.config import settings
from datetime import timedelta, datetime, timezone
from argon2 import PasswordHasher
from argon2.exceptions import (
    VerifyMismatchError,
    VerificationError,
    InvalidHashError,
)
import jwt
from jwt.exceptions import InvalidTokenError


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

#def create_refresh_token(data: dict) -> str:

#def verify_token(token: str, token_type: str = "access") -> Optional[dict]: