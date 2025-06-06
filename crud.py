from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models
import schemas
from models import User
from schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
	return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
	hashed_password = pwd_context.hash(user.password)
	db_user = models.User(email=user.email, hashed_password=hashed_password)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user