from typing import Any, Dict, Generic, Type, TypeVar, List
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert, update, delete
from domain.entities import BaseEntity
from database.db import engine, metadata

E = TypeVar('E', bound='BaseEntity')

class baseRepo(Generic[E]):
    name: str
    entity_type: Type[E]
    table: Table

    def __init__(self, entity_type: Type[E], name: str, table: Table) -> None:
        self.entity_type = entity_type
        self.name = name
        self.table = table

    def get_all(self) -> List[E]:
        """Fetch all rows from the table and return a list of entity instances."""
        with engine.connect() as connection:
            statement = select(self.table)
            result = connection.execute(statement).fetchall()
            
            entities = []
            for row in result:
                row_dict = dict(row._mapping)  
                entity = self.entity_type(**row_dict)  
                entities.append(entity)
            
            return entities

    def get_by_id(self, id: int) -> E | None:
        """Fetch a single row by ID."""
        with engine.connect() as connection:
            statement = select(self.table).where(self.table.c.id == id)
            result = connection.execute(statement).fetchone()
            if result:
                row_dict = dict(result._mapping)
                entity : E = self.entity_type(**row_dict)
                return entity
            return None

    def insert(self, entity: E) -> E:
        """Insert a new entity into the table."""
        with engine.connect() as connection:
            stmt = insert(self.table).values(entity.to_dict()) 
            connection.execute(stmt)
            connection.commit() 
            
        return entity

    def update(self, id: int, data: Dict[str, Any]) -> bool:
        """Update an existing entity in the table."""
        with engine.connect() as connection:
            stmt = update(self.table).where(self.table.c.id == id).values(data) 
            result = connection.execute(stmt) 
            connection.commit()  
            r : bool = result.rowcount > 0
            return r

    def delete(self, id: int) -> bool:
        """Delete an entity from the table."""
        with engine.connect() as connection:
            stmt = delete(self.table).where(self.table.c.id == id)  
            result = connection.execute(stmt)  
            connection.commit()  
            r : bool = result.rowcount > 0
            return r
