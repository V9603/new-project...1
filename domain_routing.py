from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def domain_home():
    return {"message": "Domain routing working"}