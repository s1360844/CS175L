# CS 175L
# Jared Mishen
# AverageFromInput

def main():
    total = 0
    count = 0

    with open('/Users/jaredmishen/Desktop/numbers.txt', 'r') as file:
        for line in file:
            number = int(line)
            count += 1
            total += number
            print(f"I read in {count} number(s) Current number is: {number} Total is: {total}")

    if count > 0:
        average = total / count
        print(f"Average: {average}")
    else:
        print("No numbers found in the file.")

if __name__ == "__main__":
    main()
