from db import Database
from models import Room, Student


class DataHandler:
    def __init__(self, db: Database):
        self.db = db

    def insert_rooms(self, rooms: list[Room]) -> None:
        self.db.execute_query("DELETE FROM rooms")
        data = [(room.id, room.name) for room in rooms]
        self.db.execute_many(
            "INSERT INTO rooms (id, name) VALUES (%s, %s)",
            data
        )

    def insert_students(self, students: list[Student]) -> None:
        self.db.execute_query("DELeTE FROM students")
        data = [
            (
                student.id,
                student.name,
                student.birthday,
                student.sex,
                student.room_id
            )
            for student in students
        ]

        self.db.execute_many(
            """
            INSERT INTO students (id, name, birthday, sex, room_id)
            VALUES (%s, %s, %s, %s, %s)
            """,
            data
        )
