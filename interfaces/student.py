import tkinter as tk
from tkinter import messagebox
import sqlite3

class StudentPage:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.frame = tk.Frame(root)
        self.frame.pack(fill='both', expand=True)

        tk.Label(self.frame, text=f"Welcome, {username} (Student)").pack(pady=10)
        tk.Button(self.frame, text="View Notifications", command=self.view_notifications).pack(pady=5)
        tk.Button(self.frame, text="View Exam Results", command=self.view_exam_results).pack(pady=5)
        tk.Button(self.frame, text="View Campus Map", command=self.view_campus_map).pack(pady=5)
        tk.Button(self.frame, text="Logout", command=self.logout).pack(pady=5)

    def view_notifications(self):
        connection = sqlite3.connect('database/university.db')
        cursor = connection.cursor()
        cursor.execute('SELECT title, message FROM notifications WHERE recipient_role = "student"')
        notifications = cursor.fetchall()
        connection.close()

        if notifications:
            messages = "\n".join([f"{title}: {message}" for title, message in notifications])
            messagebox.showinfo("Notifications", messages)
        else:
            messagebox.showinfo("Notifications", "No notifications available.")

    def view_exam_results(self):
        connection = sqlite3.connect('database/university.db')
        cursor = connection.cursor()

        # Fetch student ID
        cursor.execute('SELECT id FROM users WHERE username = ?', (self.username,))
        student_id = cursor.fetchone()
        if not student_id:
            messagebox.showerror("Error", "Student not found.")
            return
        student_id = student_id[0]

        # Fetch exam results
        cursor.execute('''
            SELECT course_name, midterm, assignment, final_exam 
            FROM exam_results WHERE student_id = ?
        ''', (student_id,))
        results = cursor.fetchall()
        connection.close()

        if results:
            result_text = "\n".join([f"{course}: Midterm: {midterm}, Assignment: {assignment}, Final: {final_exam}" 
                                     for course, midterm, assignment, final_exam in results])
            messagebox.showinfo("Exam Results", result_text)
        else:
            messagebox.showinfo("Exam Results", "No results available.")

    def view_campus_map(self):
        # Show campus map (assumes a file named `campus_map.png`)
        top = tk.Toplevel(self.root)
        top.title("Campus Map")
        map_image = tk.PhotoImage(file="assets/campus_map.png")
        map_label = tk.Label(top, image=map_image)
        map_label.image = map_image
        map_label.pack()

    def logout(self):
        self.frame.destroy()
        from interfaces.login import LoginPage
        LoginPage(self.root)