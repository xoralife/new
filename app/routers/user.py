from fastapi import APIRouter
from app.schemas.user import UserSchema
from app.models.user import User
from app.database import SessionLocal
from dependencies import get_db
router = APIRouter(
    prefix="/users",
)
@router.post("")
def store(request: UserSchema,db = depends(get_db())):
    print("inside store")

    user = User(
        name =request.name,
        email=request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user