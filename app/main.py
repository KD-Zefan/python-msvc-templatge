from fastapi import FastAPI
from app.api.v1.endpoints import auth, users

app = FastAPI()

# Include routers


@app.get("/health-check")
def health_check():
    return {"status": "OK"}
