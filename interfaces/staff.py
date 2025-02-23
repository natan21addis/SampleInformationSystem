import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class StaffPage:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.frame = tk.Frame(root)
        self.frame.pack(fill='both', expand=True)

        tk.Label(self.frame, text=f"Welcome, {username} (Staff)").pack(pady=10)
        tk.Button(self.frame, text="Add Exam Results", command=self.add_exam_results).pack(pady=5)
        tk.Button(self.frame, text="View Submitted Results", command=self.view_results).pack(pady=5)
        tk.Button(self.frame, text="Logout", command=self.logout).pack(pady=5)

    def add_exam_results(self):
        def submit_results():
            student = student_var.get()
            course = course_var.get()
            midterm = int(midterm_entry.get())
            assignment = int(assignment_entry.get())
            final_exam = int(final_exam_entry.get())

            connection = sqlite3.connect('database/university.db')
            cursor = connection.cursor()

            # Fetch student ID
            cursor.execute('SELECT id FROM users WHERE username = ?', (student,))
            student_id = cursor.fetchone()
            if not student_id:
                messagebox.showerror("Error", "Student not found.")
                return
            student_id = student_id[0]

            # Insert results
            cursor.execute('''
                INSERT INTO exam_results (student_id, course_name, midterm, assignment, final_exam) 
                VALUES (?, ?, ?, ?, ?)
            ''', (student_id, course, midterm, assignment, final_exam))
            connection.commit()
            connection.close()

            messagebox.showinfo("Success", "Exam results submitted successfully.")
            add_result_window.destroy()

        add_result_window = tk.Toplevel(self.root)
        add_result_window.title("Add Exam Results")

        # Fetch registered students and courses
        connection = sqlite3.connect('database/university.db')
        cursor = connection.cursor()
        cursor.execute('SELECT username FROM users WHERE role = "student"')
        students = [row[0] for row in cursor.fetchall()]
        cursor.execute('SELECT course_name FROM courses')
        courses = [row[0] for row in cursor.fetchall()]
        connection.close()

        # Student dropdown
        tk.Label(add_result_window, text="Select Student").pack(pady=5)
        student_var = tk.StringVar()
        student_dropdown = ttk.Combobox(add_result_window, textvariable=student_var, values=students)
        student_dropdown.pack(pady=5)

        # Course dropdown
        tk.Label(add_result_window, text="Select Course").pack(pady=5)
        course_var = tk.StringVar()
        course_dropdown = ttk.Combobox(add_result_window, textvariable=course_var, values=courses)
        course_dropdown.pack(pady=5)

        # Midterm, Assignment, Final Exam
        tk.Label(add_result_window, text="Midterm (30%)").pack(pady=5)
        midterm_entry = tk.Entry(add_result_window)
        midterm_entry.pack(pady=5)

        tk.Label(add_result_window, text="Assignment (20%)").pack(pady=5)
        assignment_entry = tk.Entry(add_result_window)
        assignment_entry.pack(pady=5)

        tk.Label(add_result_window, text="Final Exam (50%)").pack(pady=5)
        final_exam_entry = tk.Entry(add_result_window)
        final_exam_entry.pack(pady=5)

        tk.Button(add_result_window, text="Submit", command=submit_results).pack(pady=10)

    def view_results(self):
        view_results_window = tk.Toplevel(self.root)
        view_results_window.title("View Submitted Results")

        # Results table
        results_tree = ttk.Treeview(view_results_window, columns=("Student", "Course", "Midterm", "Assignment", "Final"), show="headings")
        results_tree.heading("Student", text="Student")
        results_tree.heading("Course", text="Course")
        results_tree.heading("Midterm", text="Midterm")
        results_tree.heading("Assignment", text="Assignment")
        results_tree.heading("Final", text="Final")
        results_tree.pack(fill="both", expand=True)

        # Fetch results from database
        connection = sqlite3.connect('database/university.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT u.username, e.course_name, e.midterm, e.assignment, e.final_exam 
            FROM exam_results e
            INNER JOIN users u ON e.student_id = u.id
        ''')
        results = cursor.fetchall()
        connection.close()

        for row in results:
            results_tree.insert("", "end", values=row)

    def logout(self):
        self.frame.destroy()
        from interfaces.login import LoginPage
        LoginPage(self.root)