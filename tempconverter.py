temp = float(input("Enter the temperature: "))

print("Select the conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter 1 or 2: ")


if choice == '1':
    result = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {result}°F")
    
elif choice == '2':
    result = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {result}°C")
    
else:
    print("Invalid choice. Please enter 1 or 2 only.")