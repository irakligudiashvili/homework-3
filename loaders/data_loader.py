from abc import ABC, abstractmethod
from typing import Any, Type


class DataLoader(ABC):
    @abstractmethod
    def load(self, file: str, model: Type[Any]) -> list[Any]:
        pass
