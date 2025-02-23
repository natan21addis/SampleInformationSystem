import tkinter as tk
from tkinter import messagebox, ttk

class AdminPage:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.frame = tk.Frame(root, bg='#E8F0F2')
        self.frame.pack(fill='both', expand=True)

        # Title label
        tk.Label(self.frame, text=f"Welcome, {username} (Admin)", font=('Arial', 24), bg='#E8F0F2', fg='#2C3E50').pack(pady=10)

        # Buttons
        tk.Button(self.frame, text="Send Notification", command=self.send_notification, width=20, style='TButton').pack(pady=5)
        tk.Button(self.frame, text="Add Exam Results", command=self.add_exam_results, width=20, style='TButton').pack(pady=5)
        tk.Button(self.frame, text="Logout", command=self.logout, width=20, style='TButton').pack(pady=5)

        # Button styling
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 14), padding=10, background='#3498DB', foreground='white')
        style.map('TButton', background=[('active', '#2980B9')], foreground=[('active', 'white')])

    def send_notification(self):
        # Function to send notifications
        pass

    def add_exam_results(self):
        # Function to add exam results
        pass

    def logout(self):
        # Function to handle logout
        pass