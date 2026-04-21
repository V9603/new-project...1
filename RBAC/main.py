from fastapi import FastAPI
from routes.role_routers import router

app = FastAPI()

app.include_router(router,prefix="/roles")

@app.get("/")
def home():
    return {"message": "RBAC API running"}