import tkinter as tk
from tkinter import messagebox
import sqlite3

class StudentPage:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.frame = tk.Frame(root, bg='#E8F0F2')
        self.frame.pack(fill='both', expand=True)

        # Welcome message
        tk.Label(self.frame, text=f"Welcome, {username} (Student)", font=('Arial', 24), bg='#E8F0F2', fg='#2C3E50').pack(pady=10)

        # Action buttons
        tk.Button(self.frame, text="View Notifications", command=self.view_notifications, width=20).pack(pady=5)
        tk.Button(self.frame, text="View Exam Results", command=self.view_exam_results, width=20).pack(pady=5)
        tk.Button(self.frame, text="View Campus Map", command=self.view_campus_map, width=20).pack(pady=5)
        tk.Button(self.frame, text="Logout", command=self.logout, width=20).pack(pady=5)

    def view_notifications(self):
        """Fetch and display notifications for the student."""
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
        """Fetch and display exam results for the student."""
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
            result_text = "\n".join([
                f"{course}: Midterm: {midterm}, Assignment: {assignment}, Final: {final_exam}" 
                for course, midterm, assignment, final_exam in results
            ])
            messagebox.showinfo("Exam Results", result_text)
        else:
            messagebox.showinfo("Exam Results", "No results available.")

    def view_campus_map(self):
        """Display the campus map in a new window."""
        top = tk.Toplevel(self.root)
        top.title("Campus Map")
        top.geometry("800x600")  # Set a size for the campus map window

        # Load and display the campus map image
        try:
            map_image = tk.PhotoImage(file="assets/campus_map.png")  # Adjust path as necessary
            map_label = tk.Label(top, image=map_image)
            map_label.image = map_image  # Keep a reference to avoid garbage collection
            map_label.pack(fill='both', expand=True)
        except tk.TclError:
            messagebox.showerror("Error", "Campus map image not found.")

    def logout(self):
        """Handle user logout and return to the login page."""
        self.frame.destroy()
        from interfaces.login import LoginPage
        # Specify the role and interface_class to pass to LoginPage
        LoginPage(self.root, "Student", LoginPage)  # Adjust if needed to match your implementation