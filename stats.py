def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    if not numbers:
        return 0
    frequency ={}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]

    if len(modes) == len(frequency):
        return 0
    return modes[0] if len(modes) == 1 else modes

def main():
    user_input = input("Enter your numbers, and seperate them by commas: ")
    try:
        sample_data = [float(num.strip()) for num in user_input.split(',')]
    except ValueError:
        print("Invalid Number. Please enter numbers with commas for seperation.")
        return
    print("Sample Data:", sample_data)
    print("Mean:", mean(sample_data))
    print("Median:", median(sample_data))
    print("Mode:", mode(sample_data))

if __name__ == "__main__":
    main()
