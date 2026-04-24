
# from fastapi import FastAPI

# # Import routers from each service (make sure each file defines router = APIRouter())
# import tenant_service
# # import onboarding_service
# import subscription_service
# import domain_routing
# import rbac_service
# import auth_service

# # For the new project folder: Python cannot import from a folder with dots in its name.
# # Rename the folder in VS Code Explorer from "new-project..1" to "new_project_1"
# # so Python can import it cleanly.
# # import new_project_1.main as new_project

# app = FastAPI()

# # Include routers from each service
# app.include_router(tenant_service.router, prefix="/tenant")
# # app.include_router(onboarding_service.router, prefix="/onboarding")
# app.include_router(subscription_service.router, prefix="/subscription")
# app.include_router(domain_routing.router, prefix="/domain")
# app.include_router(rbac_service.router, prefix="/rbac")
# app.include_router(auth_service.router, prefix="/auth")
# # app.include_router(new_project.router, prefix="/new-project")

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "API is working 🚀"}


# from fastapi import FastAPI

# # Import routers
# import tenant_service
# import subscription_service
# import domain_routing
# import rbac_service
# import auth_service

# app = FastAPI()

# # Include routers
# app.include_router(tenant_service.router, prefix="/tenant")
# app.include_router(subscription_service.router, prefix="/subscription")
# app.include_router(domain_routing.router, prefix="/domain")
# app.include_router(rbac_service.router, prefix="/rbac")
# app.include_router(auth_service.router, prefix="/auth")

# # Home route
# @app.get("/")
# def home():
#     return {"message": "API is working 🚀"}
# =======
# from fastapi import FastAPI
# from backend.app.routes.onboarding_routes import onboarding_router

# app = FastAPI()

# app.include_router(onboarding_router)
# from fastapi import FastAPI
# from backend.app.database import engine, Base
# from backend.app.models.onboarding_status_model import OnboardingStatus
# from backend.app.routes.onboarding_routes import onboarding_router

# app = FastAPI()

# Base.metadata.create_all(bind=engine)

# app.include_router(onboarding_router)

from fastapi import FastAPI
import tenant_service
import subscription_service
import domain_routing
import rbac_service
import auth_service

app = FastAPI()

app.include_router(tenant_service.router, prefix="/tenant")
app.include_router(subscription_service.router, prefix="/subscription")
app.include_router(domain_routing.router, prefix="/domain")
app.include_router(rbac_service.router, prefix="/rbac")
app.include_router(auth_service.router, prefix="/auth")

@app.get("/")
def home():
    return {"message": "API is working 🚀"}