from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

Base = declarative_base()

class TestTable(Base):
    __tablename__ = 'test_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Role(Base):
	__tablename__ = "roles"
	
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, unique=True, nullable=False)
	description = Column(String, nullable=True)
	user = relationship("User", back_populates="role")



class User(Base):
	__tablename__ = "users"
	
	
	id = Column(Integer, primary_key =True, index=True)
	username = Column(String, unique=True, index=True)
	email = Column(String, unique=True, index=True)
	hashed_password = Column(String)
	full_name = Column(String, index=True)
	is_active = Column(Boolean, default=True)

	role_id = Column(Integer, ForeignKey("roles.id"))
	role = relationship("Role", back_populates="users")
	

	in_active = Column(Integer, default=1)
