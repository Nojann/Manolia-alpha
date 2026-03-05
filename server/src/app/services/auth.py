import os
from dotenv import load_dotenv

from datetime import timedelta, datetime, timezone
from typing import Annotated
from pydantic import BaseModel


import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from argon2 import PasswordHasher

from src.app.models.user import User
from src.app.crud.crud_user import get_user


load_dotenv()
secret_key = os.environ.get("SECRET")
algorithm = "HS256"
access_token_expire_minutes = 10080
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")
password_hasher = PasswordHasher()

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

def authenticate_user(username: str, password: str):
    user: User = get_user(username)
    if not user:
        verify_password(password, user.hashed_password)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def verify_password(plain_password: str, hashed_password: str) -> bool:
    isValidated: bool = False
    try:
        isValidated = password_hasher.verify(hashed_password, plain_password)
    except:
        isValidated = False
    return isValidated

def create_access_token(data: dict):
        expire = datetime.now(timezone.utc) + timedelta(minutes=access_token_expire_minutes)
        to_encode = data.copy()
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
        return encoded_jwt

async def hash_password(password: str) -> str:
    return password_hasher.hash(password)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try: 
        payload = jwt.decode(token, secret_key, algorithm)
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


