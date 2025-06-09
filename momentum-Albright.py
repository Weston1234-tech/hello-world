Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> mass = float(input("Enter the object's mass in kilograms: "))
Enter the object's mass in kilograms: 50
>>> velocity = float(input("Enter the object's velocity in meters per second: "))
Enter the object's velocity in meters per second: 3
>>> momentum = mass * velocity
>>> kinetic_energy = 0.5 * mass * velocity**2
>>> print("The object's momentum is:", momentum, "kg*m/s")
>>> print("The object's kinetic energy is:", kinetic_energy, "Joules")
