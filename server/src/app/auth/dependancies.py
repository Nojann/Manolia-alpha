from src.app.config import settings

from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from argon2 import PasswordHasher
from argon2 import PasswordHasher
import jwt
from jwt.exceptions import InvalidTokenError

from src.app.models.user import User
from src.app.data.user import get_user
from .schemas import TokenData
from .security import verify_password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")
password_hasher = PasswordHasher()

def authenticate_user(username: str, password: str):
    user: User = get_user(username)
    if not user:
        # Add timing to prevent attack
        password_hasher.hash(password)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try: 
        payload = jwt.decode(token, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


