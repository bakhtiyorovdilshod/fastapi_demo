# import sqlalchemy
from fastapi import FastAPI
from src.models.contact import contacts
from db import metadata, sqlalchemy
from sqlalchemy.orm import relationship



users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("phone_number", sqlalchemy.String),
    sqlalchemy.Column("address", sqlalchemy.String),
    sqlalchemy.Column("gender", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.Integer),
    sqlalchemy.Column("is_provider", sqlalchemy.Boolean),
    sqlalchemy.Column("contact", sqlalchemy.Integer, sqlalchemy.ForeignKey('contacts.id'))           
)

