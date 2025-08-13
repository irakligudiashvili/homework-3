from models import Room, Student
from .data_loader import DataLoader
import json
import sys
from typing import Any, Type
from datetime import datetime


class JSONLoader(DataLoader):
    def load(self, file: str, model: Type[Any]) -> list[Any]:
        try:
            with open(file) as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"File not found: {file}")
            sys.exit(1)

        if model:
            if model == Student:
                return [
                    model(
                        id=s["id"],
                        name=s["name"],
                        birthday=datetime.fromisoformat(s["birthday"]),
                        sex=s["sex"],
                        room_id=s["room"]
                    )
                    for s in data
                ]
            else:
                return [model(**item) for item in data]

        return data
