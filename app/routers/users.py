from fastapi import APIRouter, Depends
from .. import models
from ..dependencies import get_current_user

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"], response_model=models.User)
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    # In a real app, you'd fetch the user from the DB based on current_user.username
    # For this example, we'll just return a mock user object.
    return {
        "username": current_user.username,
        "email": "test@example.com",
        "full_name": "Test User",
        "disabled": False,
    }


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
