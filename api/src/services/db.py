import datetime

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from config import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD
import databases

DB_USER = DB_USER
DB_PASSWORD = DB_PASSWORD
DB_HOST = DB_HOST
DB_NAME = DB_NAME
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base = declarative_base()
metadata = sqlalchemy.MetaData()

usage = sqlalchemy.Table(
    "usage",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("city", sqlalchemy.String(100)),
    sqlalchemy.Column("currency", sqlalchemy.Text()),
)

metadata.create_all(engine)


async def insert_data(city, currency):
    query = (
        usage.insert()
        .values(city=city, currency=currency, created_at=datetime.datetime.now())
    )
    await database.fetch_one(query)
