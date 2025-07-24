def main():
    filename = input("Enter your file name here: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File was not found. Did you spell it right, AND is it in the same directory as this script?")
        return

    num_lines = len(lines)
    print(f"\nThe file has {num_lines} lines.\n")

    while True:
        try:
            line_number = int(input(f"Enter a line number between 1 and {num_lines} (or 0 to quit out): "))
        except ValueError:
            print("Invalid input. I need a real number.")
            continue

        if line_number == 0:
            print("Exiting, glad I could help!")
            break
        elif 1 <= line_number <= num_lines:
            print(f"Line {line_number}: {lines[line_number - 1].rstrip()}")
        else:
            print(f"Invalid line number. Please enter a number between 1 and {num_lines}.")

if __name__ == "__main__":
    main()
