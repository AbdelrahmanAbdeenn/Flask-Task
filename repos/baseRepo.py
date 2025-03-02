from typing import Any, Dict, Generic, Type, TypeVar

from entities.Entities import BaseEntity

E = TypeVar('E', bound='BaseEntity')

items: Dict[str, Dict[int, Any]] = {}


class baseRepo(Generic[E]):

    name: str
    entity_type: Type[E]

    def __init__(self, entity_type: Type[E], name: str) -> None:
        self.entity_type = entity_type
        self.name = name

    def get_all(self) -> list[E]:
        return list(items[self.name].values())

    def get_by_id(self, id: int) -> Any:
        if self.name not in items:
            return None
        if id not in items[self.name]:
            return None
        result = items[self.name][id]
        return result

    def insert(self, entity: E) -> E:
        if self.name not in items:
            items[self.name] = {}
        items[self.name][entity.id] = entity
        return entity

    def update(self, id: int, data: Dict[str, Any]) -> bool:
        item = items[self.name][id]
        if item:
            for key, value in data.items():
                setattr(item, key, value)
            return True
        return False

    def delete(self, id: int) -> None:
        items[self.name].pop(id)
