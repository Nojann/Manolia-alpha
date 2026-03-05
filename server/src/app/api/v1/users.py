from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta

from src.app.models.user import User
from src.app.data.user import create_user
from src.app.services.auth import get_current_user, authenticate_user, create_access_token, hash_password, Token

router = APIRouter(tags=["users"])

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
    )
    access_token = create_access_token(data={"sub": user.username})
    return Token(access_token=access_token, token_type="bearer")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/token")

@router.get("/user")
async def user(current_user: Annotated[str, Depends(get_current_user)]):
    return current_user

@router.post("/user")
async def create(username, password):
    hashed_password = await hash_password(password)
    user = User(username = username, hashed_password = hashed_password)
    created_user = create_user(user)
    return created_user