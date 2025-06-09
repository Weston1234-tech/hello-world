Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> hourly_wage = float(input("Enter the hourly wage: "))
Enter the hourly wage: 7.50
>>> regular_hours = float(input("Enter the total regular hours: "))
Enter the total regular hours: 40
>>> overtime_hours = float(input("Enter the total overtime hours: "))
Enter the total overtime hours: 5
>>> regular_pay = hourly_wage * regular_hours
>>> overtime_pay = overtime_hours * 1.5 * hourly_wage
>>> total_weekly_pay = regular_pay + overtime_pay
>>> print("Total weekly pay: $", total_weekly_pay)
Total weekly pay: $ 356.25
