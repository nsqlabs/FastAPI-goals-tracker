from fastapi import APIRouter

router = APIRouter()


@router.get("/categories/", tags=["categories"])
async def read_categories():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/categories/me", tags=["categories"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/categories/{username}", tags=["categories"])
async def read_user(username: str):
    return {"username": username}