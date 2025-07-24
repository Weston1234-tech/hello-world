import tkinter as tk

def fahrenheit_to_celsius():
    try:
        f = float(fahrenheit_var.get())
        c = (f - 32) * 5 / 9
        celsius_var.set(f"{c:.2f}")
    except ValueError:
        celsius_var.set("Error")

def celsius_to_fahrenheit():
    try:
        c = float(celsius_var.get())
        f = (c * 9 / 5) + 32
        fahrenheit_var.set(f"{f:.2f}")
    except ValueError:
        fahrenheit_var.set("Error")

root = tk.Tk()
root.title("Temprature Converter")

fahrenheit_var = tk.StringVar(value="32.0")
celsius_var = tk.StringVar(value="0.0")

tk.Label(root, text="Fahrenheit").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Celsius").grid(row=0, column=1, padx=10, pady=5)

tk.Entry(root, textvariable=fahrenheit_var, width=16).grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=celsius_var, width=16).grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text=">>>>", command=fahrenheit_to_celsius).grid(row=2, column=0, pady=10)
tk.Button(root, text="<<<<", command=celsius_to_fahrenheit).grid(row=2, column=1, pady=10)

root.mainloop()
