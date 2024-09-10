from fastapi import FastAPI
from app.api.v1.endpoints import auth, users

app = FastAPI()

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])


@app.get("/health-check")
def health_check():
    return {"status": "OK"}
