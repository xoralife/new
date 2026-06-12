from pydantic import BaseModel , Field

class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    @Field_validator("email")
    @classmethod 
    def check_email(cls,value , db = Depends(get_db)):
        user = db.query(User).filter(
            User.email == value).first(
                User.email == value
            ).first()
        if user:
            raise ValueError("Email already exists")
        return value

