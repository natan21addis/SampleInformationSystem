import tkinter as tk
from tkinter import messagebox
import sqlite3

class LoginPage:
    def __init__(self, root, role, interface_class):
        self.root = root
        self.role = role
        self.interface_class = interface_class
        self.frame = tk.Frame(root, bg='#E8F0F2')
        self.frame.pack(fill='both', expand=True)

        # Role label
        tk.Label(self.frame, text=f"Login as: {role}", font=('Arial', 24), bg='#E8F0F2', fg='#2C3E50').pack(pady=20)

        # Username and password input
        tk.Label(self.frame, text="Username", bg='#E8F0F2').pack(pady=5)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.frame, text="Password", bg='#E8F0F2').pack(pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack(pady=5)

        # Login button
        tk.Button(self.frame, text="Login", command=self.login, width=10, bg='#3498DB', fg='white').pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate input based on role
        if self.role == "Admin":
            if username == "admin" and password == "123456":
                self.frame.destroy()
                self.interface_class(self.root, username)
            else:
                messagebox.showerror("Error", "Invalid admin credentials.")
        else:
            # Connect to the database for other roles
            connection = sqlite3.connect('database/university.db')
            cursor = connection.cursor()
            cursor.execute('SELECT role FROM users WHERE username=? AND password=?', (username, password))
            result = cursor.fetchone()

            if result:
                role = result[0]
                self.frame.destroy()
                self.interface_class(self.root, username)
            else:
                messagebox.showerror("Error", "Invalid username or password.")

            connection.close()