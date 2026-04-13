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
        raise HTTPException(status_code=404, detail= f"Product with Id {id} not found to delete.")
    
def update_product_by_id(id, product, db):
    product_to_update = db.query(Product).filter(Product.id == id).first()

    if product_to_update:
        product_to_update.name = product.name
        product_to_update.description = product.description
        product_to_update.price = product.price
        product_to_update.quantity = product.quantity

        db.commit()
        db.refresh(product_to_update)

        return product_to_update
    else:
        raise HTTPException(status_code=404, detail= f"Product with Id {id} not found to update.")

