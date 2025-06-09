starting_salary = float(input("Enter the starting salary: "))
annual_increase_percent = float(input("Enter the annual % increase: "))
num_years = int(input("Enter the number of years: "))

annual_increase = annual_increase_percent / 100

salary = starting_salary

print("n\\Year\tSalary")
print("----------------------")

for year in range(1, num_years + 1):
    print(f"{year}\t${salary:,.2f}")

    salary += salary * annual_increase
