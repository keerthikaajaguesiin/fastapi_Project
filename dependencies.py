from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from fastapi import Security
from dotenv import load_dotenv
load_dotenv()
import os


# JWT settings
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")  #token endpoint

#schema for data in token

class TokenData(BaseModel):
	email: str
	role: str

#Dependency to get current user from JWT token

def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
	try:
	    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
	    email: str = payload.get("sub")
	    role: str = payload.get("role")
	    if email is None or role is None:
	        raise HTTPException(status_code=401, detail="Invalid token")
	    return TokenData(email=email, role=role)
	except JWTError:
	    raise HTTPException(status_code=401, detail="Invalid token")
		
