from .data_loader import DataLoader
import json
import sys
from typing import Any


class JSONLoader(DataLoader):
    def load(self, file: str, model: Any):
        try:
            with open(file) as f:
                data = json.load(f)

                return [model.from_dict(item) for item in data]
        except FileNotFoundError:
            print(f"File not found: {file}")
            sys.exit(1)
