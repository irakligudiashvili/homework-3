from dataclasses import dataclass
from datetime import datetime
from typing import Self


@dataclass
class Student:
    id: int
    name: str
    birthday: datetime
    sex: str
    room_id: int

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(
            id=data["id"],
            name=data["name"],
            birthday=datetime.fromisoformat(data["birthday"]),
            sex=data["sex"],
            room_id=data["room"]
        )
