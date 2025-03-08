from sqlalchemy import Column, Integer, String, Table

from src.database.db import engine, metadata

students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String,),
    Column('age', Integer),
    Column('grade', String),
)
metadata.create_all(engine)
