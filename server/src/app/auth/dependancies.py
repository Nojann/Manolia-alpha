from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from argon2 import PasswordHasher
from argon2 import PasswordHasher

from src.app.models.user import User
from src.app.data.user import get_user_by_username
from .schemas import TokenData
from .security import verify_password, verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
password_hasher = PasswordHasher()

def authenticate_user(username: str, password: str):
    user: User = get_user_by_username(username)
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
    payload = verify_token(token, token_type="access")
    if payload is None:
        raise credentials_exception
    
    username = payload.get("sub")
    if username is None:
        raise credentials_exception
    token_data = TokenData(username=username)
    
    user = get_user_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    
    return user


