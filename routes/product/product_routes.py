from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.product.product_schemas import ProductRequest, ProductResponseBase, ProductListResponse
from typing import List
from services.product.product_service import create_product, get_all_products, get_product_by_id, delete_product_by_id

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/register", status_code=201, response_model=ProductResponseBase)
def register_product(product: ProductRequest, db: Session = Depends(get_db)):
    new_product = create_product(product, db)

    return {
        "message": "Product created.",
        "product": new_product
    }

@router.get("/all", response_model=ProductListResponse)
def list_all_products(db: Session = Depends(get_db)):
    products = get_all_products(db)
    return {
        "message": "Products list.",
        "products": products
    }