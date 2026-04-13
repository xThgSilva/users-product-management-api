from models.product.product_model import Product
from fastapi import HTTPException

def create_product(product, db):
    new_product = Product(name=product.name, 
                          description=product.description,
                          price=product.price,
                          quantity=product.quantity)
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

def get_all_products(db):
    return db.query(Product).all()

def get_product_by_id(id, db):
    product_found = db.query(Product).filter(Product.id == id).first()

    if product_found:
        return product_found
    else:
        raise HTTPException(status_code=404, detail= f"Product with Id {id} not found.")
    
def delete_product_by_id(id, db):
    product_to_delete = db.query(Product).filter(Product.id == id).first()

    if product_to_delete:
        db.delete(product_to_delete)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail= f"Product with Id {id} not delete.")