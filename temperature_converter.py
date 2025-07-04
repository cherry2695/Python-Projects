def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def display_menu():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            temp = float(input("Enter temperature in Celsius: "))
            print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")

        elif choice == '2':
            temp = float(input("Enter temperature in Fahrenheit: "))
            print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")

        elif choice == '3':
            temp = float(input("Enter temperature in Celsius: "))
            print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")

        elif choice == '4':
            temp = float(input("Enter temperature in Kelvin: "))
            print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")

        elif choice == '5':
            temp = float(input("Enter temperature in Fahrenheit: "))
            print(f"{temp}°F = {fahrenheit_to_kelvin(temp):.2f}K")

        elif choice == '6':
            temp = float(input("Enter temperature in Kelvin: "))
            print(f"{temp}K = {kelvin_to_fahrenheit(temp):.2f}°F")

        elif choice == '7':
            print("Thank you for using the Temperature Converter.")
            break

        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()