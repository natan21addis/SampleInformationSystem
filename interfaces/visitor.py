import tkinter as tk

class VisitorPage:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.frame = tk.Frame(root)
        self.frame.pack(fill='both', expand=True)

        tk.Label(self.frame, text=f"Welcome, {username} (Visitor)").pack(pady=10)
        tk.Button(self.frame, text="View Campus Map", command=self.view_campus_map).pack(pady=5)
        tk.Button(self.frame, text="Logout", command=self.logout).pack(pady=5)

    def view_campus_map(self):
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