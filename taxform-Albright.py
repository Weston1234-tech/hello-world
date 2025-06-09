Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def calculate_tax(price, tax_rate):
...     tax_amount = price * tax_rate
...     rounded_tax_amount = round(tax_amount, 2)
...     return rounded_tax_amount
... 
>>> price = float(input("Enter the price: "))
Enter the price: 5.00
>>> tax_rate = float(input("Enter the tax rate (e.g., 0.07 for 7%): "))
Enter the tax rate (e.g., 0.07 for 7%): 0.08
>>> tax = calculate_tax(price, tax_rate)
>>> print("Tax Amount:", tax)
Tax Amount: 0.4
