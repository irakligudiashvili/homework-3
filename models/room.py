from dataclasses import dataclass
from typing import Self


@dataclass
class Room:
    id: int
    name: str

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(**data)
