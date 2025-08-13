from dataclasses import dataclass
from datetime import date


@dataclass
class Student:
    id: int
    name: str
    birthday: date
    sex: str
    room_id: int
