import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT UNIQUE NOT NULL,
    age INTEGER NOT NULL,
    DBMS INTEGER NOT NULL,
    PYTHON INTEGER NOT NULL,
    JAVA INTEGER NOT NULL,
    WEB INTEGER NOT NULL
)
""")
cursor.execute("DELETE FROM students")
cursor.executemany("""
INSERT INTO students (name, age, DBMS, PYTHON, JAVA, WEB)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    ("Prem", 18, 85, 90, 80, 95),
    ("Kasthuri", 19, 87, 97, 90, 80),
    ("Thanuj", 21, 90, 95, 85, 90),
    ("Mithun", 23, 100, 90, 100, 87),
    ("Thanmaye", 20, 95, 100, 90, 95),
    ("Manoj", 22, 95, 80, 70, 85)
   
])

connection.commit()
connection.close()

print("Database created successfully!")