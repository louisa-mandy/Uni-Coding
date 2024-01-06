
Lloyd = {
 "name": "Lloyd",
 "homework": [90.0,97.0,75.0,92.0],
 "quizzes": [88.0,40.0,94.0],
 "tests": [75.0,90.0]
}

Alice = {
 "name": "Alice",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}

Tyler = {
 "name": "Tyler",
 "homework": [0.0, 87.0, 75.0, 22.0],
 "quizzes": [0.0, 75.0, 78.0],
 "tests": [100.0, 100.0]
}

def print_student_info(student):
    print("Name:", student["name"])
    print("Homework:", student["homework"])
    print("Quizzes:", student["quizzes"])
    print("Tests:", student["tests"])
    print()

# Interactive input
student_name = input("Enter student's name (Lloyd, Alice, or Tyler): ").capitalize()

# Check which student was entered and print their information
if student_name == "Lloyd":
    print_student_info(Lloyd)
elif student_name == "Alice":
    print_student_info(Alice)
elif student_name == "Tyler":
    print_student_info(Tyler)
else:
    print("Student not found.")
