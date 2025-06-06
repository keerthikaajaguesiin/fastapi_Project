from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):  # This is what was missing!
    id: int

    class Config:
        from_attributes = True  # Pydantic v2
