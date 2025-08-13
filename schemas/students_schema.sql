CREATE TABLE IF NOT EXISTS students(
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthday DATE NOT NULL,
    sex ENUM('M', 'F') NOT NULL,
    room_id INT,
    FOREIGN KEY (room_id) REFERENCES rooms(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_students_room_id ON students (room_id);
CREATE INDEX IF NOT EXISTS idx_students_room_sex ON students (room_id, sex);
CREATE INDEX IF NOT EXISTS idx_students_birthday ON students (birthday);