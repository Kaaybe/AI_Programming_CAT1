# File: student_info_system.py
# List to store student dictionaries
students_list = []

def save_to_file():
    """Write student data to students.txt"""
    with open("students.txt", "w") as file:
        file.write("Student Information System\n")
        file.write("=========================\n")
        for student in students_list:
            file.write(f"Name: {student['name']}\n")
            file.write(f"Student ID: {student['student_id']}\n")
            file.write(f"Favorite AI Tool: {student['favorite_AI_tool']}\n")
            file.write("-------------------------\n")

# Main program
while True:
    # Ask for student details
    name = input("Enter student name (or 'quit' to exit): ")
    if name.lower() == 'quit':
        break
    student_id = input("Enter student ID: ")
    favorite_AI_tool = input("Enter favorite AI tool: ")

    # Create dictionary for student
    student = {
        "name": name,
        "student_id": student_id,
        "favorite_AI_tool": favorite_AI_tool
    }

    # Append to list
    students_list.append(student)

# Print number of students and details
print(f"\nTotal number of students: {len(students_list)}")
print("\nStudent Details:")
print("================")
for student in students_list:
    print(f"Name: {student['name']}")
    print(f"Student ID: {student['student_id']}")
    print(f"Favorite AI Tool: {student['favorite_AI_tool']}")
    print("----------------")

# Save to file
save_to_file()
print("\nData has been saved to students.txt")