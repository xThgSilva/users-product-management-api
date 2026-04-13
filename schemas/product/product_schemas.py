from pydantic import BaseModel
from typing import Optional, List

class ProductRequest(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

    class Config:
        from_attributes = True

class ProductResponseBase(BaseModel):
    message: str
    product: ProductResponse

class ProductListResponse(BaseModel):
    message: str
    products: List[ProductResponse]
    