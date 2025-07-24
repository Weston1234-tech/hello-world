from functools import reduce

def calculate_average_from_file():
    """Prompte the user for a file, then calculates the average of the numbers in the file."""
    file_name = input("Enter the name of your file, such as numbers.txt: ")
    try:
        with open(file_name, 'r') as file:
            all_words = file.read().replace(',', ' ').split()
            def is_number(s):
                try:
                    float(s)
                    return True
                except ValueError:
                    return False

            valid_numbers = list(map(float, filter(is_number, all_words)))

            if not valid_numbers:
                print("No valid numbers found in the file.")
                return

            total = reduce(lambda x, y: x + y, valid_numbers)
            average = total / len(valid_numbers)

            print(f"The average of the numbers in '{file_name}' is: {average:.2f}")
            print(f"The Sum: {total:.2f}")
            print(f"The Minimum: {min(valid_numbers):.2f}")
            print(f"The Maximum: {max(valid_numbers):.2f}")

    except FileNotFoundError:
        print("Error: File not found. Did you spell it right, and is it in the same directory as this program?")

    except Exception as e:
         print(f"An Unknown Error Has Occured.")


if __name__ == "__main__":
    calculate_average_from_file()
