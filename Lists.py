# List of 9 student names
students = ["Monicah", "Irwine", "Benedict", "Gloria", "Faith", "Teddy", "Sandra", "Drina", "Ryan"]

# For loop to print each name in uppercase with index (1-based as per output)
for index, name in enumerate(students, start=1):
    print(f"{index}. {name.upper()}")