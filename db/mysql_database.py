from .database import Database
import mysql.connector
from typing import Any, Sequence, Tuple


class MySQLDatabase(Database):
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.db = None

    def connect(
        self, host: str, user: str, password: str, db: str
    ) -> None:
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()
        self.db = db

    def execute_sql_file(self, file: str) -> None:
        with open(file) as f:
            sql = f.read()
            statements = sql.split(";")
            for stmt in statements:
                self.cursor.execute(stmt)

    def setup_db(self) -> None:
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db}")
        self.cursor.execute(f"USE {self.db}")

        self.execute_sql_file("rooms_schema.sql")
        self.execute_sql_file("students_schema.sql")

        self.conn.commit()

    def execute_query(self, query: str) -> Any:
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_many(self, query: str, data: Sequence[Tuple[Any, ...]]) -> None:
        self.cursor.executemany(query, data)
        self.conn.commit()

    def close(self) -> None:
        self.cursor.close()
