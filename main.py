from fastapi import FastAPI, FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db         #  your database session getter
from schemas import UserCreate, UserOut
import crud                         #The file you created above
from users import router as user_router
import models
from database import engine

app = FastAPI()

@app.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
	db_user = crud.get_user_by_email(db, email=user.email)
	if db_user:
		raise HTTPException(status_code=400, detail="Email already registres")
	new_user = crud.create_user(db, user=user)
	return new_user

#create database tables
models.Base.metadata.create_all(bind=engine)

app.include_router(user_router)

@app.get("/")
def read_root():
	return{"message": "Welcome to FastAPI"}
