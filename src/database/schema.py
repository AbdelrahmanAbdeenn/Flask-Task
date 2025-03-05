from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from database.db import metadata, engine

students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String,),
    Column('age', Integer),
    Column('grade', String),
)   
metadata.create_all(engine)