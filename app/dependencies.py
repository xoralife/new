from app.database import SessionLocal





def get_db():
    db = SessionLocal()
    print("before yield")
    yield db
    print("after yield")
    db.close