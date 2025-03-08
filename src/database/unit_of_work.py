from sqlalchemy.orm import sessionmaker
from src.database.db import engine
from sqlalchemy.orm import Session
from typing import Optional , Type
from types import TracebackType


class UnitOfWork:
    def __init__(self) -> None:
        self.session = sessionmaker(bind=engine)()  

    def __enter__(self) -> 'UnitOfWork':
        self.start()
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]) -> None:
        if exc_type is None:
            self.commit()
        else:
            self.rollback()

    def start(self) -> None:
        self.session.begin()  

    def commit(self) -> None:
        try:
            self.session.commit()  
        except Exception as e:
            self.session.rollback()  
            raise e  

    def rollback(self) -> None:
        self.session.rollback()  

    def get_session(self) -> Session:
        return self.session