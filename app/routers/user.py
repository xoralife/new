from fastapi import APIRouter
from app.schemas.user import UserSchema
from app.models.user import User
from app.database import SessionLocal
from dependencies import get_db
router = APIRouter(
    prefix="/users",
)

@router.get("")
def search(name : str="",db = depends(get_db())):
    users = db.query(User).filter(User.name.ilike(f"%.com")).all()
    return users
@router.post("")
def store(request: UserSchema,db = depends(get_db())):
    user = db.query(User).filter(User.email == request.email).first()
    if user:
        return user
    



    print("inside store")

    user = User(
        name =request.name,
        email=request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user