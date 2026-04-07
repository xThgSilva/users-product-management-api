from sqlalchemy import Column, Integer, String, Numeric
from database.connection import Base

class Product(Base):
    __tablename__ = "tb_products"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(150), nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False)
