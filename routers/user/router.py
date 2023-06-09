from fastapi import APIRouter

from schemes.user.schema import UserCreateSchema, UserUpdateSchema
from services.user.UserService import UserService


router = APIRouter(prefix="/users")


@router.post("/create")
async def create_user(user: UserCreateSchema):
    UserService.create(user.name, user.number)
    return {"status": "created"}


@router.get("/all")
async def read_all_users():
    users = UserService.read_all()
    return {"users": users}


@router.get("/{user_id}")
async def read_user_by_id(user_id: int):
    user = UserService.read_by_id(user_id)
    return {"user": user}


@router.post("/update")
async def update_user_by_id(user: UserUpdateSchema):
    UserService.update_by_id(user.id, user.new_name, user.new_number)
    return {"status": "updated"}


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    UserService.delete_by_id(user_id)
    return {"status": "deleted"}
