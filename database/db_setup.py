import sqlite3

def initialize_database():
    connection = sqlite3.connect('/home/natan/Desktop/contrat/SampleInformationSystem/database/university.db')
    cursor = connection.cursor()

  
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK (role IN ('student', 'staff', 'admin', 'visitor'))
        )
    ''')

   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            message TEXT NOT NULL,
            recipient_role TEXT NOT NULL CHECK (recipient_role IN ('student', 'staff', 'visitor'))
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exam_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_name TEXT NOT NULL,
            midterm INTEGER CHECK(midterm >= 0 AND midterm <= 30),
            assignment INTEGER CHECK(assignment >= 0 AND assignment <= 20),
            final_exam INTEGER CHECK(final_exam >= 0 AND final_exam <= 50),
            FOREIGN KEY(student_id) REFERENCES users(id)
        )
    ''')

   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT UNIQUE NOT NULL
        )
    ''')
    courses = [
        ('Mathematics',), ('Physics',), ('Chemistry',),
        ('Biology',), ('Computer Science',), ('English',), ('History',)
    ]
    cursor.executemany('INSERT OR IGNORE INTO courses (course_name) VALUES (?)', courses)

  
    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password, role) 
        VALUES ('admin', 'admin123', 'admin')
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    initialize_database()