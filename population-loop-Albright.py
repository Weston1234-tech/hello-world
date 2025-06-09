Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def predict_population_with_loop(initial_population, growth_rate, growth_time, total_time, time_interval=1):
...  current_population = initial_population
...  elapsed_time = 0
...  while elapsed_time < total_time:
...      time_step = min(time_interval, total_time - elapsed_time)
...      growth_factor = growth_rate ** (time_step / growth_time)
...      current_population *= growth_factor
...      elapsed_time += time_step
...      print(f"Time: {elapsed_time}, Population: {current_population:.2f}")
...  return current_population
... 
>>> initial_population = float(input("Enter the initial number of organisms: "))
Enter the initial number of organisms: 500
>>> growth_rate = float(input("Enter the growth rate: "))
Enter the growth rate: 2
>>> growth_time = float(input("Enter the number of hours it takes to achieve this rate: "))
Enter the number of hours it takes to achieve this rate: 6
>>> total_time = float(input("Enter the number of hours during which the population grows: "))
Enter the number of hours during which the population grows: 12
>>> final_population = predict_population_with_loop(initial_population, growth_rate, growth_time, total_time)
Time: 1, Population: 561.23
Time: 2, Population: 629.96
Time: 3, Population: 707.11
Time: 4, Population: 793.70
Time: 5, Population: 890.90
Time: 6, Population: 1000.00
Time: 7, Population: 1122.46
Time: 8, Population: 1259.92
Time: 9, Population: 1414.21
Time: 10, Population: 1587.40
Time: 11, Population: 1781.80
Time: 12, Population: 2000.00
