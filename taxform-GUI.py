import tkinter as tk
from tkinter import messagebox

def calculate_tax():
    try:
        income = float(entry_income.get())
        dependents = int(entry_dependents.get())

        if income < 0:
            raise ValueError("Income can't be negative.")
        if dependents < 0:
            raise ValueError("Number of Dependents can't be negative.")
        deduction_per_dependent = 2000
        taxable_income = income - (dependents * deduction_per_dependent)
        taxable_income = max(taxable_income, 0)
        if income <= 10000:
            tax = 0
        elif income <= 50000:
            tax = (income - 10000) * 0.1
        elif income <=10000:
            tax = 4000 + (income - 50000) * 0.2
        else:
            tax = 14000 + (income - 100000) * 0.3

        label_result.config(text=f"Calculated Tax: ${tax:,.2f}")
    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid Input: {ve}")

window = tk.Tk()
window.title("Tax Calculator with Dependents")
window.geometry("400x300")

label_title = tk.Label(window, text="Tax Calculator", font=("Arial", 16))
label_title.pack(pady=10)

frame_input = tk.Frame(window)
frame_input.pack()

label_income = tk.Label(frame_input, text="Enter your income: $")
label_income.pack(side=tk.LEFT)

entry_income = tk.Entry(frame_input)
entry_income.pack(side=tk.LEFT)

frame_dependents = tk.Frame(window)
frame_dependents.pack(pady=5)

label_dependents = tk.Label(frame_dependents, text="Number of dependents:")
label_dependents.pack(pady=5)

entry_dependents = tk.Entry(frame_dependents)
entry_dependents.pack(side=tk.LEFT)

btn_calculate = tk.Button(window, text="Calculate Tax", command=calculate_tax)
btn_calculate.pack(pady=10)

label_result = tk.Label(window, text="Calculated Tax: $0.00", font=("Arial", 12))
label_result.pack(pady=10)

window.mainloop()
