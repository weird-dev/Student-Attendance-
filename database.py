import sqlite3

# Function to create a table in the database if it doesn't exist
def create_table():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY, name TEXT, matric_number TEXT, department TEXT)''')
    conn.commit()
    conn.close()

# Function to add a new student to the database
def add_student(name, matric_number, department):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''INSERT INTO students (name, matric_number, department)
                 VALUES (?, ?, ?)''', (name, matric_number, department))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()

# Function to fetch all students from the database
def get_students():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    conn.close()
    return students

def get_student_by_id(student_id):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = c.fetchone()
    conn.close()
    return student

def update_student(student_id, name, matric_number, department):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("UPDATE students SET name=?, matric_number=?, department=? WHERE id=?", (name, matric_number, department, student_id))
    conn.commit()
    conn.close()