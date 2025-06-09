Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> years = int(input("Enter the number of years: "))
Enter the number of years: 20
>>> days_in_year = 365
>>> hours_in_day = 24
>>> minutes_in_hour = 60
>>> minutes_in_year = days_in_year * hours_in_day * minutes_in_hour
>>> total_minutes = years * minutes_in_year
>>> print("Total number of minutes:", total_minutes)
Total number of minutes: 10512000
