smaller = int(input(f"Enter the smaller number: "))
larger = int(input(f"Enter the larger number: "))
print(f"Think of a number between {smaller} and {larger}, and I'll try to guess it.")
low = smaller
high = larger
count = 0
while True:
    count += 1
    computer_guess = (low + high) // 2
    print(f"My guess is: {computer_guess}")
    feedback = input("Too high (H), too low (L), or correct (C)? ").upper()
    if feedback == 'C':
        print(f"I got it in {count} tries!")
        break
    elif feedback == 'H':
        high = computer_guess - 1
    elif feedback == 'L':
        low = computer_guess + 1
    else:
        print(f"Invalid input. Please enter 'H', 'L', or 'C'.")
