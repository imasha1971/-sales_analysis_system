import tkinter as tk
from tkinter import filedialog, messagebox
from analysis import generate_chart

# Global variable to store selected file path
selected_file_path = None

def open_dashboard():
    global chart_frame

    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("1000x900")
    dashboard.configure(bg="white")

    # Dashboard Title
    title_label = tk.Label(dashboard, text="Dashboard", font=("Arial", 24, "bold"), bg="white")
    title_label.place(x=400, y=23)

    # Select Data File Button
    select_file_btn = tk.Button(dashboard, text="Select Data File", font=("Arial", 13, "bold"),
                                bg="blue", fg="white", width=27, height=2, command=select_data_file)
    select_file_btn.place(x=50, y=20)

    # Chart Display Area
    chart_frame = tk.Frame(dashboard, bg="white", width=950, height=400)
    chart_frame.place(x=50, y=240)

    # Button Style
    button_style = {
        "font": ("Arial", 13, "bold"),
        "bg": "gray",
        "fg": "black",
        "width": 27,
        "height": 2
    }

    # Top Row Buttons
    btn1 = tk.Button(dashboard, text="Monthly Sales Analysis", **button_style,
                     command=lambda: show_branch_buttons("Monthly Sales Analysis"))
    btn1.place(x=50, y=90)

    btn2 = tk.Button(dashboard, text="Price Analysis of Each Product", **button_style,
                     command=lambda: show_branch_buttons("Price Analysis of Each Product"))
    btn2.place(x=350, y=90)

    btn3 = tk.Button(dashboard, text="Weekly Sales Analysis", **button_style,
                     command=lambda: show_branch_buttons("Weekly Sales Analysis"))
    btn3.place(x=650, y=90)

    # Bottom Row Buttons
    btn4 = tk.Button(dashboard, text="Product Preference Analysis", **button_style,
                     command=lambda: show_branch_buttons("Product Preference Analysis"))
    btn4.place(x=200, y=160)

    btn5 = tk.Button(dashboard, text="Sales Amount Distribution", **button_style,
                     command=lambda: show_branch_buttons("Sales Amount Distribution"))
    btn5.place(x=550, y=160)

    # Exit Button
    exit_btn = tk.Button(dashboard, text="Exit", font=("Arial", 14, "bold"),
                         bg="red", fg="white", width=10, command=dashboard.destroy)
    exit_btn.place(x=800, y=710)
    dashboard.mainloop()

def select_data_file():
    global selected_file_path
    file_path = filedialog.askopenfilename(
        title="Select Excel Data File",
        filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
    )
    if file_path:
        selected_file_path = file_path
        messagebox.showinfo("File Selected", f"Data file loaded:\n{file_path}")
    else:
        messagebox.showwarning("No File", "No file was selected.")

def show_branch_buttons(analysis_type):
    global selected_file_path
    if not selected_file_path:
        messagebox.showerror("Error", "Please select a data file first.")
        return

    for widget in chart_frame.winfo_children():
        widget.destroy()

    branches = ["Matara", "Galle", "Badulla"]
    for branch in branches:
        tk.Button(chart_frame, text=branch,
                  command=lambda b=branch: generate_chart(b, analysis_type, chart_frame, selected_file_path),
                  font=("Arial", 12)).pack(pady=5)
import tkinter as tk
from tkinter import filedialog, messagebox
from analysis import generate_chart

# Global variable to store selected file path
selected_file_path = None

def open_dashboard():
    global chart_frame

    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("1000x900")
    dashboard.configure(bg="white")

    # Dashboard Title
    title_label = tk.Label(dashboard, text="Dashboard", font=("Arial", 24, "bold"), bg="white")
    title_label.place(x=400, y=23)

    # Select Data File Button
    select_file_btn = tk.Button(dashboard, text="Select Data File", font=("Arial", 13, "bold"),
                                bg="blue", fg="white", width=27, height=2, command=select_data_file)
    select_file_btn.place(x=50, y=20)

    # Chart Display Area
    chart_frame = tk.Frame(dashboard, bg="white", width=950, height=400)
    chart_frame.place(x=50, y=240)

    # Button Style
    button_style = {
        "font": ("Arial", 13, "bold"),
        "bg": "gray",
        "fg": "black",
        "width": 27,
        "height": 2
    }

    # Top Row Buttons
    btn1 = tk.Button(dashboard, text="Monthly Sales Analysis", **button_style,
                     command=lambda: show_branch_buttons("Monthly Sales Analysis"))
    btn1.place(x=50, y=90)

    btn2 = tk.Button(dashboard, text="Price Analysis of Each Product", **button_style,
                     command=lambda: show_branch_buttons("Price Analysis of Each Product"))
    btn2.place(x=350, y=90)

    btn3 = tk.Button(dashboard, text="Weekly Sales Analysis", **button_style,
                     command=lambda: show_branch_buttons("Weekly Sales Analysis"))
    btn3.place(x=650, y=90)

    # Bottom Row Buttons
    btn4 = tk.Button(dashboard, text="Product Preference Analysis", **button_style,
                     command=lambda: show_branch_buttons("Product Preference Analysis"))
    btn4.place(x=200, y=160)

    btn5 = tk.Button(dashboard, text="Sales Amount Distribution", **button_style,
                     command=lambda: show_branch_buttons("Sales Amount Distribution"))
    btn5.place(x=550, y=160)

    # Exit Button
    exit_btn = tk.Button(dashboard, text="Exit", font=("Arial", 14, "bold"),
                         bg="red", fg="white", width=10, command=dashboard.destroy)
    exit_btn.place(x=800, y=710)
    dashboard.mainloop()

def select_data_file():
    global selected_file_path
    file_path = filedialog.askopenfilename(
        title="Select Excel Data File",
        filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
    )
    if file_path:
        selected_file_path = file_path
        messagebox.showinfo("File Selected", f"Data file loaded:\n{file_path}")
    else:
        messagebox.showwarning("No File", "No file was selected.")

def show_branch_buttons(analysis_type):
    global selected_file_path
    if not selected_file_path:
        messagebox.showerror("Error", "Please select a data file first.")
        return

    for widget in chart_frame.winfo_children():
        widget.destroy()

    branches = ["Matara", "Galle", "Badulla"]
    for branch in branches:
        tk.Button(chart_frame, text=branch,
                  command=lambda b=branch: generate_chart(b, analysis_type, chart_frame, selected_file_path),
                  font=("Arial", 12)).pack(pady=5)
