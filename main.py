def temperature_converter():
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit:", f)


def length_converter():
    cm = float(input("Enter length in cm: "))
    m = cm / 100
    km = cm / 100000
    print("Meters:", m)
    print("Kilometers:", km)


def weight_converter():
    kg = float(input("Enter weight in kg: "))
    g = kg * 1000
    print("Grams:", g)


while True:
    print("\n--- UNIT CONVERTER ---")
    print("1. Temperature")
    print("2. Length")
    print("3. Weight")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        temperature_converter()
    elif choice == '2':
        length_converter()
    elif choice == '3':
        weight_converter()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice")