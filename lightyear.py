Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> speed_of_light = 3e8
>>> years = float(input("Enter the number of years: "))
Enter the number of years: 5
>>> days_in_year = 365
>>> hours_in_day = 24
>>> minutes_in_hour = 60
>>> seconds_in_minute = 60
>>> seconds_in_year = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
>>> distance = speed_of_light * seconds_in_year * years
>>> print("Distance traveled in", years, "years:", distance, "meters")
Distance traveled in 5.0 years: 4.7304e+16 meters
