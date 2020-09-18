from pydantic import BaseModel
from src.models.contact import  contacts


class Contact(BaseModel):
    id: int
    phone_number : str
    name: str

class ContactIn(BaseModel):
    phone_number : str
    name:str


class ForContact(BaseModel):
    id: int


class UserIn(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    address: str
    gender: str
    age: int
    is_provider: bool
    contact: int 
  


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_number: str
    address: str
    gender: str
    age: int
    is_provider: bool
    contact: int 





