# CS175L
# Jared Mishen
# Temperature Conversions

def convert_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def convert_to_centigrade(fahrenheit):
    centigrade = (fahrenheit - 32) * 5/9
    return centigrade

def do_conversion(fahrenheit):
    kelvin = convert_to_kelvin(fahrenheit)
    centigrade = convert_to_centigrade(fahrenheit)
    print(f'Fahrenheit: {fahrenheit} Kelvin: {kelvin:.2f} Centigrade: {centigrade:.2f}')

def repeat_conversions():
    num_conversions = int(input('How many conversions would you like to do this time? '))

    for _ in range(num_conversions):
        fahrenheit = get_fahrenheit()
        do_conversion(fahrenheit)

def control_loop():
    while True:
        user_input = input('Do you want to do some conversions? (Yes or No): ').lower()

        if user_input == 'yes':
            repeat_conversions()
        elif user_input == 'no':
            break
        else:
            print('Invalid input. Please enter "Yes" or "No".')

def get_fahrenheit():
    while True:
        try:
            fahrenheit = float(input('Enter Fahrenheit temperature (must be -50 to 130): '))
            if -50 <= fahrenheit <= 130:
                return fahrenheit
            else:
                print('Temperature must be within the range -50 to 130. Please re-enter.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')

def main():
    control_loop()


if __name__ == '__main__':
    main()
