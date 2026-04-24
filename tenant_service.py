from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def tenant_home():
    return {"message": "Tenant working"}

@router.get("/list")
def get_tenants():
    return {"tenants": ["tenant1", "tenant2"]}