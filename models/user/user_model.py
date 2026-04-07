from sqlalchemy import Column, Integer, String
from database.connection import Base

class Users(Base):
    __tablename__ = "tb_users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
