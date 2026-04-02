from fastapi import APIRouter
from backend.app.services.onboarding_service import *

onboarding_router = APIRouter(prefix="/onboarding", tags=["Onboarding"])


@onboarding_router.post("/register-school")
def register_school_api(data: dict):
    return register_school(data)


@onboarding_router.post("/create-admin")
def create_admin_api(data: dict):
    return create_admin(data)


@onboarding_router.post("/complete-profile")
def complete_profile_api(data: dict):
    return complete_profile(data)


@onboarding_router.post("/setup-branding")
def setup_branding_api(data: dict):
    return setup_branding(data)


@onboarding_router.post("/setup-academics")
def setup_academics_api(data: dict):
    return setup_academics(data)


@onboarding_router.post("/activate-features")
def activate_features_api(data: dict):
    return activate_features(data)


@onboarding_router.post("/complete-onboarding")
def complete_onboarding_api(data: dict):
    return complete_onboarding(data)


@onboarding_router.get("/status/{school_id}")
def onboarding_status_api(school_id: int):
    return get_onboarding_status(school_id)


@onboarding_router.post("/admin-override")
def admin_override_api(data: dict):
    return admin_override(data)