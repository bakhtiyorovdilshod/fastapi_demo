import databases
import sqlalchemy
from db import metadata


contacts = sqlalchemy.Table(
    "contacts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("phone_number", sqlalchemy.String),
    sqlalchemy.Column("name", sqlalchemy.String)
    
)
