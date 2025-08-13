from db import Database
from typing import Any


class QueryHandler:
    def __init__(self, db: Database):
        self.db = db

    def rooms_with_student_count(self) -> Any:
        return self.db.execute_query("""
            SELECT r.name, COUNT(s.id) AS student_count
            FROM rooms r
            LEFT JOIN students s ON r.id = s.room_id
            GROUP BY r.id
        """)

    def top_5_smallest_avg_age(self) -> Any:
        return self.db.execute_query("""
            SELECT
                r.name,
                AVG(TIMESTAMPDIFF(YEAR, s.birthday, CURDATE())) AS avg_age
            FROM rooms r
            LEFT JOIN students s ON r.id = s.room_id
            GROUP BY r.id
            ORDER BY avg_age ASC
            LIMIT 5
        """)

    def top_5_largest_age_diff(self) -> Any:
        return self.db.execute_query("""
            SELECT
                name,
                youngest,
                oldest,
                oldest - youngest AS age_diff
            FROM (
                SELECT
                    r.name,
                    MAX(TIMESTAMPDIFF(YEAR, s.birthday, CURDATE())) AS oldest,
                    MIN(TIMESTAMPDIFF(YEAR, s.birthday, CURDATE())) AS youngest
                FROM rooms r
                LEFT JOIN students s on r.id = s.room_id
                GROUP BY r.id
            ) AS room_ages
            ORDER BY age_diff DESC
            LIMIT 5
        """)

    def mixed_sex_rooms(self) -> Any:
        return self.db.execute_query("""
            SELECT r.name
            FROM rooms r
            LEFT JOIN students s ON r.id = s.room_id
            GROUP BY r.id
            HAVING COUNT(DISTINCT s.sex) > 1
        """)
