import tkinter as tk
from tkinter import messagebox
import sqlite3

class SignUpPage:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root, bg='#E8F0F2')
        self.frame.pack(fill='both', expand=True)

        # Title label
        tk.Label(self.frame, text="Sign Up", font=('Arial', 24), bg='#E8F0F2', fg='#2C3E50').pack(pady=20)

        # Username and password input
        tk.Label(self.frame, text="Username", bg='#E8F0F2').pack(pady=5)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.frame, text="Password", bg='#E8F0F2').pack(pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack(pady=5)

        tk.Label(self.frame, text="Role", bg='#E8F0F2').pack(pady=5)
        self.role_var = tk.StringVar(value="student")  # Default role
        roles = ["staff", "student", "visitor"]
        for role in roles:
            tk.Radiobutton(self.frame, text=role.capitalize(), variable=self.role_var, value=role, bg='#E8F0F2').pack(anchor=tk.W)

        # Sign Up button
        tk.Button(self.frame, text="Sign Up", command=self.signup, width=10, bg='#3498DB', fg='white').pack(pady=10)

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()

        # Password length validation
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long.")
            return

        connection = sqlite3.connect('database/university.db')
        cursor = connection.cursor()

        try:
            cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
            connection.commit()
            messagebox.showinfo("Success", "Account created successfully")
            self.root.destroy()  # Close the sign-up page
            # Optionally, redirect to the login page
            from main import main
            main()  # Restart the main application
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")
        finally:
            connection.close()