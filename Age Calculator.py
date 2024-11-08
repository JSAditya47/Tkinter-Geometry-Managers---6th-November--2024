import tkinter as tk
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()
root.title("Age Calculator")
root.geometry("600x400")

def calculate_age():
    try:

        birth_year = int(entry_year.get())
        birth_month = int(entry_month.get())
        birth_day = int(entry_day.get())

        today = datetime.today()

        birthdate = datetime(birth_year, birth_month, birth_day)
        age = today.year - birthdate.year
        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
            age -= 1

        messagebox.showinfo("Age", f"Your age is: {age} years")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for year, month, and date.")

label_year = tk.Label(root, text="Year of Birth:")
label_year.pack(pady=10)

entry_year = tk.Entry(root)
entry_year.pack(pady=5)

label_month = tk.Label(root, text="Month of Birth:")
label_month.pack(pady=10)

entry_month = tk.Entry(root)
entry_month.pack(pady=5)

label_day = tk.Label(root, text="Day of Birth:")
label_day.pack(pady=10)

entry_day = tk.Entry(root)
entry_day.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=20)

root.mainloop()


