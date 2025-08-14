from handlers import DataHandler
from loaders import JSONLoader
from handlers import QueryHandler
from typing import Any
from db import Database
from models import Room, Student
from config import Config


class App:
    def __init__(self, db: Database):
        self.host = Config.db_host
        self.user = Config.db_user
        self.password = Config.db_password
        self.database = Config.db_name

        self.db = db
        self.loader = JSONLoader()
        self.data_handler = DataHandler(self.db)
        self.query_handler = QueryHandler(self.db)

    def run(self) -> Any:
        self.db.connect(self.host, self.user, self.password, self.database)
        print("Connection established")

        self.db.setup_db()
        print("Database has been setup")

        self.data_handler.clean_tables()
        print("Tables cleaned")

        rooms = self.loader.load("data/rooms.json", model=Room)
        self.data_handler.insert_rooms(rooms)
        print("Rooms have been added")

        students = self.loader.load("data/students.json", model=Student)
        self.data_handler.insert_students(students)
        print("Students have been added")

        print("""
        ==========================
        Rooms and student count
        ==========================
        """)
        for row in self.query_handler.rooms_with_student_count():
            print(row)

        print("""
        ==========================
        Top 5 smallest average age
        ==========================
        """)
        for row in self.query_handler.top_5_smallest_avg_age():
            print(row)

        print("""
        ==========================
        Top 5 largest average age
        ==========================
        """)
        for row in self.query_handler.top_5_largest_age_diff():
            print(row)

        print("""
        ==========================
        Rooms with mixed sexes
        ==========================
        """)
        for row in self.query_handler.mixed_sex_rooms():
            print(row)

        self.db.close()
