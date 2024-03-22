# CS 175L
# Jared Mishen
# Chapter 6 Average from Input File with Exception Handling 

def read_numbers_from_file(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                number = float(line.strip())
                numbers.append(number)
                print(f"I read in {len(numbers)} number(s) Current number is: {number} Total is: {sum(numbers)}")
    except IOError as e:
        print(f"SystemExit: File not found: numbers.txt - exiting")
        raise SystemExit
    except ValueError as e:
        print(f"Bad data: {line.strip()} skipping")

    return numbers

def calculate_average(numbers):
    if numbers:
        average = sum(numbers) / len(numbers)
        return average
    else:
        return None

def main():
    file_path = '/Users/jaredmishen/Desktop/numbers.txt'

    numbers = read_numbers_from_file(file_path)
    average = calculate_average(numbers)

    if average is not None:
        print(f"Average: {average}")
    else:
        print("No valid numbers found in the file.")

if __name__ == "__main__":
    main()
