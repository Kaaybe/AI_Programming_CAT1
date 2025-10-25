# Ask user for input
number = int(input("Enter a number: "))

# Check if number is negative
if number < 0:
    print("Invalid input – negative numbers not allowed.")
# Check if number is even or odd
elif number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")