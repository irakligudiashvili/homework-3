from abc import ABC, abstractmethod
from typing import Any, Sequence, Tuple


class Database(ABC):
    @abstractmethod
    def connect(
        self, host: str, user: str, password: str, db: str
    ) -> None:
        pass

    @abstractmethod
    def execute_sql_file(self, file: str) -> None:
        pass

    @abstractmethod
    def setup_db(self) -> None:
        pass

    @abstractmethod
    def execute_query(self, query: str) -> Any:
        pass

    @abstractmethod
    def execute_many(self, query: str, data: Sequence[Tuple[Any, ...]]) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
