from typing import Any, Dict, Generic, List, Type, TypeVar

from sqlalchemy import Table, delete, insert, select, update
from sqlalchemy.orm import Session

from src.domain.entities import BaseEntity

E = TypeVar('E', bound='BaseEntity')


class BaseRepo(Generic[E]):
    name: str
    entity_type: Type[E]
    table: Table

    def __init__(self, entity_type: Type[E], name: str, table: Table) -> None:
        self.entity_type = entity_type
        self.name = name
        self.table = table

    def get_all(self, session: Session) -> List[E]:
        statement = select(self.table)
        result = session.execute(statement).fetchall()
        entities = []
        for row in result:
            row_dict = dict(row._mapping)
            entity = self.entity_type(**row_dict)
            entities.append(entity)
        return entities

    def get_by_id(self, session: Session, id: int) -> E | None:
        statement = select(self.table).where(self.table.c.id == id)
        result = session.execute(statement).fetchone()
        if result:
            row_dict = dict(result._mapping)
            entity: E = self.entity_type(**row_dict)
            return entity
        return None

    def insert(self, session: Session, entity: E) -> E:
        stmt = insert(self.table).values(vars(entity))
        session.execute(stmt)
        return entity

    def update(self, session: Session, id: int, data: Dict[str, Any]) -> bool:
        stmt = update(self.table).where(self.table.c.id == id).values(data)
        result = session.execute(stmt)
        r: bool = result.rowcount > 0
        return r

    def delete(self, session: Session, id: int) -> bool:
        stmt = delete(self.table).where(self.table.c.id == id)
        result = session.execute(stmt)
        r: bool = result.rowcount > 0
        return r
