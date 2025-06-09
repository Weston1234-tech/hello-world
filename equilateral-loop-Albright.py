Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> while True:
...     print("Check if a triangle is equilateral: ")
...     side1 = float(input("Enter the first side: "))
...     side2 = float(input("Enter the second side: "))
...     side3 = float(input("Enter the third side: "))
...     if side1 == side2 == side3:
...         print("This triangle is equilateral.")
...     else:
...         print("This triangle is not equilateral.")
...     again = input("Do you want to test another triantle? (yes/no): ")
...     if again.lower() != "yes":
...         print("Goodbye!")
...         break
... 
...     
Check if a triangle is equilateral: 
Enter the first side: 20
Enter the second side: 20
Enter the third side: 20
This triangle is equilateral.
Do you want to test another triantle? (yes/no): yes
Check if a triangle is equilateral: 
Enter the first side: 10
Enter the second side: 15
Enter the third side: 20
This triangle is not equilateral.
Do you want to test another triantle? (yes/no): no
Goodbye!
