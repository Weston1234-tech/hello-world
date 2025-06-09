Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> total_minutes_of_arc = 90 * 60
>>> distance_in_km = 10000
>>> total_nautical_miles = total_minutes_of_arc
>>> km_per_nautical_mile = distance_in_km / total_nautical_miles
>>> kilometers = float(input("Enter the number of kilometers: "))
Enter the number of kilometers: 30
>>> nautical_miles = kilometers / km_per_nautical_mile
>>> print("Nautical miles:", nautical_miles)
Nautical miles: 16.2
