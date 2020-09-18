from typing import List
from fastapi import FastAPI
from db import db
from src.models.database import UserIn, User, Contact, ContactIn
from src.models.user import users
from src.models.contact import contacts
from sqlalchemy.sql import select
from sqlalchemy.orm import Session


app = FastAPI()

@app.on_event("startup")
async def startup():
	await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
	contact_id = user.contact
	check_id = select([contacts.c.id]).where(contacts.c.id==contact_id)
	fetch_data = await db.fetch_one(check_id)
	get_cantact_id = x[0]
	query = users.insert().values(first_name=user.first_name, last_name=user.last_name, phone_number=user.phone_number, address=user.address, gender=user.gender, age=user.age, is_provider=user.is_provider, contact=get_cantact_id)
	last_record_id = await db.execute(query)
	return {**user.dict(), "id": last_record_id}


@app.get("/notes/", response_model=List[User])
async def read_notes():
    query = users.select()
    return await db.fetch_all(query)


@app.post("/create/contact", response_model=Contact)
async def create_contact(contact: ContactIn):
	query = contacts.insert().values(phone_number=contact.phone_number, name=contact.name)
	last_record_id = await db.execute(query)
	return {**contact.dict(), "id":last_record_id }

@app.get("/")
