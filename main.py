from fastapi import FastAPI
from backend.app.routes.onboarding_routes import onboarding_router

app = FastAPI()

app.include_router(onboarding_router)
from fastapi import FastAPI
from backend.app.database import engine, Base
from backend.app.models.onboarding_status_model import OnboardingStatus
from backend.app.routes.onboarding_routes import onboarding_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(onboarding_router)