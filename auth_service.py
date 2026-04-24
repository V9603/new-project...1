from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def auth_home():
    return {"message": "Auth working"}

@router.post("/login")
def login():
    return {"message": "Login success"}
