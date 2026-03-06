from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.app.models.user import User, UserCreate
from src.app.data.user import create_user, get_user_by_username

from src.app.auth.dependancies import get_current_user, authenticate_user
from src.app.auth.security import hash_password, create_access_token, verify_beyond_user_limit
from src.app.auth.schemas import Token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
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

@router.get("/me")
async def user(current_user: Annotated[str, Depends(get_current_user)]):
    return current_user

@router.post("/register")
async def create(user_data: UserCreate):
    if(verify_beyond_user_limit()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user limit has been reached."
        )
    if get_user_by_username(user_data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    hashed_password = hash_password(user_data.plain_password)
    user = User(username = user_data.username, hashed_password = hashed_password)
    created_user = create_user(user)
    return created_user