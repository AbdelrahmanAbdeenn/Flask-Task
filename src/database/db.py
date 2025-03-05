from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import text

DATABASE_URL = "postgresql://abdelrahman:079@localhost:5432/mydatabase"
engine = create_engine(DATABASE_URL)
metadata = MetaData()


