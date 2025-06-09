Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> initial_height = float(input("Height from which the ball dropped: "))
Height from which the ball dropped: 10
>>> num_bounces = int(input("Enter the number of times the ball bounced: "))
Enter the number of times the ball bounced: 4
>>> total_distance = initial_height
>>> current_height = initial_height
>>> for i in range(num_bounces):
...     bounce_distance = current_height * (1+0.6)
...     total_distance += bounce_distance
...     current_height *=0.6
... 
...     
>>> print("Total distance traveled is:", total_distance, "units.")
Total distance traveled is: 44.816 units.
