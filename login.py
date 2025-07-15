import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from dashboard import open_dashboard

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("1000x656")

        # Background Image
        self.bg = Image.open("assets/login_background.jpg")
        self.bg = self.bg.resize((1000, 656))
        self.bg_image = ImageTk.PhotoImage(self.bg)
        self.bg_label = tk.Label(master, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # LOGIN Title
        self.title_label = tk.Label(master, text="LOGIN", font=("Arial", 36, "bold"), fg="black")
        self.title_label.place(x=650, y=40)

        # Email Label and Entry
        self.email_label = tk.Label(master, text="Email:", font=("Arial", 18, "bold"), fg="black")
        self.email_label.place(x=550, y=230)
        self.email_entry = tk.Entry(master, font=("Arial", 16), width=23)
        self.email_entry.place(x=690, y=230)

        # Password Label and Entry
        self.pass_label = tk.Label(master, text="Password:", font=("Arial", 18, "bold"), fg="black")
        self.pass_label.place(x=550, y=340)
        self.pass_entry = tk.Entry(master, font=("Arial", 16), width=23, show="*")
        self.pass_entry.place(x=690, y=340)

        # Login Button
        self.login_btn = tk.Button(master, text="Login", font=("Arial", 16, "bold"),
                                   bg="green", fg="white", width=16, command=self.check_login)
        self.login_btn.place(x=650, y=450)

        # Exit Button
        self.exit_btn = tk.Button(master, text="Exit", font=("Arial", 16, "bold"),
                                  bg="red", fg="white", width=16, command=self.master.quit)
        self.exit_btn.place(x=650, y=580)

    def check_login(self):
        email = self.email_entry.get()
        password = self.pass_entry.get()

        # Check credentials
        if email == "ashi@" and password == "123":
            messagebox.showinfo("Success", "Login successful")

            # Show welcome message
            messagebox.showinfo("Welcome", "Welcome to Sampath Food City Sale System")

            # Open dashboard
            self.master.destroy()
            open_dashboard()
        else:
            messagebox.showerror("Error", "Login failed. Incorrect email or password.")
