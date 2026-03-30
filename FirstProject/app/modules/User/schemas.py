from pydantic import BaseModel

# Response schema GET request
class UserRead(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    description: str 

    class Config:
        orm_mode = True

# Product Create Schema POST request ke liye 
class UserCreate(BaseModel):

    name: str
    price: float
    quantity: int
    description: str

    class Config:
        orm_mode = True
