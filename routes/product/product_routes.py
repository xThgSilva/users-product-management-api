from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.product.product_schemas import ProductRequest, ProductResponseBase, ProductListResponse
from typing import List
from services.product.product_service import create_product, get_all_products, get_product_by_id, delete_product_by_id, update_product_by_id
from auth.get_user import get_current_user
from models.user.user_model import Users

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
def list_all_products(db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    products = get_all_products(db)
    return {
        "message": "Products list.",
        "products": products
    }

@router.get("product/{id}", response_model=ProductResponseBase)
def get_product(id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(id, db)

    return {
        "message": "Product found",
        "product": product
    }

@router.delete("/delete/{id}", status_code=204)
def delete_product(id: int, db: Session = Depends(get_db)):
    delete_product_by_id(id, db)

@router.put("update/{id}", response_model=ProductResponseBase)
def update_product(id: int, product: ProductRequest, db: Session = Depends(get_db)):
    product_updated = update_product_by_id(id, product, db)

    return {
        "message": "Product updated.",
        "product": product_updated
    }
