from sqlalchemy import MetaData, create_engine

DATABASE_URL = "postgresql://abdelrahman:079@localhost:5432/mydatabase"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
