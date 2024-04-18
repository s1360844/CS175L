# CS 175 L
# Jared Mishen
# Expenses Pie Chart Assignment


import matplotlib.pyplot as plt

def read_expenses(filename):
    expenses = {}
    try:
        with open(r'/Users/jaredmishen/Desktop/expenses.txt') as file:
            for line in file:
                label, value = line.strip().split('\t')
                try:
                    expenses[label] = int(value)
                except ValueError:
                    print(f"Error: Invalid data for {label}. Skipping...")
    except IOError:
        print("Error: Unable to open the file.")
    return expenses

def plot_pie_chart(expenses):
    labels = expenses.keys()
    values = expenses.values()

    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Expenses Pie Chart')
    plt.axis('equal')  
    plt.show()

def main():
    filename = 'expenses.txt'
    expenses = read_expenses(filename)
    if expenses:
        plot_pie_chart(expenses)

if __name__ == "__main__":
    main()
