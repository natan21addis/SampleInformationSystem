import tkinter as tk
from tkinter import ttk  # For better styling
from interfaces.login import LoginPage
from interfaces.signup import SignUpPage  # New SignUpPage
from interfaces.admin import AdminPage
from interfaces.staff import StaffPage
from interfaces.student import StudentPage
from interfaces.visitor import VisitorPage

def show_interface(interface_class, username):
    """Clear the current frame and show a new interface."""
    for widget in root.winfo_children():
        widget.destroy()
    
    # Create the new interface
    interface_class(root, username)

def choose_role():
    """Display buttons for role selection."""
    for widget in root.winfo_children():
        widget.destroy()
        
    title_label = tk.Label(
        root, 
        text="Select Your Role", 
        font=('Arial', 24), 
        bg='#E8F0F2', 
        fg='#2C3E50'
    )
    title_label.pack(pady=20)

    button_frame = tk.Frame(root, bg='#E8F0F2')
    button_frame.pack(pady=20)

    # Create buttons for each role
    roles = {
        "Admin": AdminPage,
        "Staff": StaffPage,
        "Student": StudentPage,
        "Visitor": VisitorPage
    }

    for role, interface_class in roles.items():
        button = ttk.Button(button_frame, text=role, command=lambda r=role, c=interface_class: show_login(r, c))
        button.pack(side=tk.LEFT, padx=10, pady=10)
        button.configure(width=15, style='TButton')

    # Sign Up button (excluding Admin)
    signup_button = ttk.Button(button_frame, text="Sign Up", command=lambda: show_signup())
    signup_button.pack(side=tk.LEFT, padx=10, pady=10)
    signup_button.configure(width=15, style='TButton')

def show_login(role, interface_class):
    """Display the login page for the selected role."""
    for widget in root.winfo_children():
        widget.destroy()
    
    # Initialize the login page with the role and interface class
    LoginPage(root, role, interface_class)

def show_signup():
    """Display the sign-up page."""
    for widget in root.winfo_children():
        widget.destroy()
    
    SignUpPage(root)  # Initialize the sign-up page

def main():
    """Main function to initialize the application."""
    global root
    root = tk.Tk()
    root.title("University Information Desk")
    root.geometry("800x600")
    
    # Set a colorful background
    root.configure(bg='#E8F0F2')

    # Show role selection when the app starts
    choose_role()

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == '__main__':
    main()