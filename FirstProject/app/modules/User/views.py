from sqlalchemy.orm import Session
from modules.User.models import User
from modules.User.schemas import UserCreate

#get all products list
def get_products(db:Session):
    products=db.query(User).all()
    return products
    

#create products
def create_product(db:Session,product:UserCreate):
    new_product=User(name=product.name,
                    price=product.price,
                    quantity=product.quantity,
                    description=product.description,
                
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


#UPDATE 
def update_product(db:Session,product_id:int,product:UserCreate):
    existing_product=db.query(User).filter(User.id==product_id).first()

    if existing_product:
            existing_product.name=product.name
            existing_product.price=product.price
            existing_product.quantity=product.quantity
            existing_product.description=product.description

            db.commit()
            db.refresh(existing_product)

    return existing_product

#DELETE

def delete_product(db:Session,product_id:int):
    product=db.query(User).filter(User.id==product_id).first()

    if product:
            db.delete(product)
            db.commit()
    return product
