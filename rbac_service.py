from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def rbac_home():
    return {"message": "RBAC working"}

@router.get("/roles")
def get_roles():
    return {"roles": ["admin", "user"]}
