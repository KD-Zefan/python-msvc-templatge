from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import verify_token
from app.db.models import User

router = APIRouter()


@router.get("/profile")
async def get_profile(
    token: str = Depends(verify_token), db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == token).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"email": user.email, "role": user.role, "created_at": user.created_at}
