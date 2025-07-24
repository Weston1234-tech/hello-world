"""
File: testinputfunctions.py

Defines a function for robust input of ints.
"""

def inputInt(prompt):
    """Guarantees that the user inputs an integer,
    using the given prompt. Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            print("Error: the input must consist only of digits")

def inputFloat(prompt):
    """Guarantees that the user inputs a floating number, using the given prompt, then returns float."""
    while True:
        theString = input(prompt)
        if theString.count('.') <= 1 and all(ch.isdigit() or ch == '.' for ch in theString) and theString != '.':
            try:
                return float(theString)
            except ValueError:
                print("Error: Invalid floating number")
        else:
            print("Error: Invalid floating number")

def main():
    n = inputInt("Please enter a number: ")
    print("You entered the number", n)

    f = inputFloat("Please enter a Floating Number: ")
    print("You entered the float:", f)

if __name__ == "__main__":
    main()
