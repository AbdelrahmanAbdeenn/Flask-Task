from typing import Any, Dict, Generic, TypeVar

from flask import jsonify

from src.database.unit_of_work import UnitOfWork
from src.domain.entities import BaseEntity
from src.repos.base_repo import BaseRepo

E = TypeVar('E', bound='BaseEntity')


class BaseService(Generic[E]):
    def __init__(self, repo: BaseRepo[E], uow: UnitOfWork) -> None:
        self.repo = repo
        self.uow = uow

    def get(self, id: int | None) -> Any:
        try:
            with self.uow:
                session = self.uow.get_session()
                if id is None:
                    entities = self.repo.get_all(session)
                    return jsonify([vars(entity) for entity in entities])
                else:
                    entity = self.repo.get_by_id(session, id)
                    if entity is None:
                        return jsonify("Entity not found"), 404
                    return jsonify(vars(entity))
        except Exception as e:
            return jsonify(str(e))

    def create(self, data: Any) -> Any:
        try:
            with self.uow:
                session = self.uow.get_session()
                entity: E = self.repo.entity_type(**data)
                if not entity:
                    return jsonify("Entity creation failed"), 400
                if self.repo.get_by_id(session, entity.id):
                    return jsonify("Entity with this ID already exists"), 400
                self.repo.insert(session, entity)
                return jsonify(vars(entity))
        except Exception as e:
            return jsonify(str(e))

    def update(self, id: int, data: Dict[str, Any]) -> Any:
        try:
            with self.uow:
                session = self.uow.get_session()
                entity = self.repo.get_by_id(session, id)
                if entity is None:
                    return jsonify("Entity not found"), 404

                if 'id' in data:
                    del data['id']

                updated = self.repo.update(session, id, data)
                newEntity = self.repo.get_by_id(session, id)
                if not updated:
                    return jsonify("Failed to update entity"), 400
                return jsonify(vars(newEntity))
        except Exception as e:
            return jsonify(str(e))

    def delete(self, id: int) -> Any:
        try:
            with self.uow:
                session = self.uow.get_session()
                entity = self.repo.get_by_id(session, id)
                if entity is None:
                    return jsonify("Entity not found"), 404
                deleted = self.repo.delete(session, id)
                if not deleted:
                    return jsonify("Failed to delete entity"), 400
                return jsonify("Entity deleted")
        except Exception as e:
            return jsonify(str(e))
