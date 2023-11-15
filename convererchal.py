
def meters_to_feet(meters):
    return meters * 3.28084

def liters_to_gallons(liters):
    return liters * 0.264172

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def menu():
    print("Select a conversion option:")
    print("1. Meters to Feet")
    print("2. Liters to Gallons")
    print("3. Kilograms to Pounds")

def main():
    menu()
    choice = int(input("Enter your choice: "))
    value = float(input("Enter the value to be converted: "))

    if choice == 1:
        converted_value = meters_to_feet(value)
        print(f"{value} meters is equal to {converted_value} feet.")
    elif choice == 2:
        converted_value = liters_to_gallons(value)
        print(f"{value} liters is equal to {converted_value} gallons.")
    elif choice == 3:
        converted_value = kilograms_to_pounds(value)
        print(f"{value} kilograms is equal to {converted_value} pounds.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
