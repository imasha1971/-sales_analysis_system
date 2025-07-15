import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_chart(branch, analysis_type, parent_frame, file_path):
    df = pd.read_excel(file_path)
    df_branch = df[df["Branch"] == branch]
    fig, ax = plt.subplots(figsize=(7, 5))

    if "Monthly Sales" in analysis_type:
        monthly_sales = df_branch.groupby("Date")["Total"].sum()
        monthly_sales.plot(kind='line', ax=ax, title=f"{branch} - Monthly Sales")

    elif "Price Analysis" in analysis_type:
        avg_prices = df_branch.groupby("Product Name")["Price"].mean()
        avg_prices.plot(kind='bar', ax=ax, title="Average Price per Product")

    elif "Weekly Sales" in analysis_type:
        weekly = df_branch.groupby("Week Number")["Total"].sum()
        weekly.plot(kind='bar', ax=ax, title=f"{branch} - Weekly Sales")

    elif "Product Preference" in analysis_type:
        products = df_branch.groupby("Product Name")["Quantity"].sum()
        products.plot(kind='pie', ax=ax, autopct='%1.1f%%', title="Product Preference")

    elif "Distribution" in analysis_type:
        df_branch["Total"].plot(kind='hist', ax=ax, bins=10, title="Sales Amount Distribution")

    for widget in parent_frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

