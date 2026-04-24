from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def subscription_home():
    return {"message": "Subscription working"}

@router.get("/plans")
def get_plans():
    return {"plans": ["basic", "premium"]}