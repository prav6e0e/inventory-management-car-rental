# Routes
from fastapi import APIRouter,Depends
from . schemas import UserRead,UserCreate
from database.db import get_db
from sqlalchemy.orm import Session
from . import views

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

# http://localhost:8000/users/get-users/

#GET all  products
@router.get("/get-products", response_model=list[UserRead])
async def read_products(db:Session=Depends(get_db)):
    products = views.get_products(db)
    return products

#CREATE 
@router.post("/create-product", response_model=UserRead)
async def create_product(product:UserCreate,db:Session=Depends(get_db)):
    
    return views.create_product(db,product)

#UPDATE PRODUCT
@router.put("/update-product/{product_id}",
response_model=UserRead)
async def update_product(product_id:int,product:UserCreate,db:Session=Depends(get_db)):
    return views.update_product(db,product_id,product)


#DELETE 
@router.delete("/delete-product/{product_id}")
async def delete_product(product_id:int,db:Session=Depends(get_db)):
    return views.delete_product(db,product_id)