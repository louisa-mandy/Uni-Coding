# creating a tuple for the numbers in bimay 

course_numero = ("COP 2510", "EGN 3000L", "MAC 2281", "MUH 3016", "PHY 2048")

# a dict for more detailed info, based on the instructions 

jeneng_course = {
    "COP 2510": "Programming Concepts",
    "EGN 3000L": "Foundations of Engineering Lab",
    "MAC 2281": "Calculus I",
    "MUH 3016": "Survey of Jazz",
    "PHY 2048": "General Physics I"
}

names = {
    "COP 2510": "Z. Beasley",
    "EGN 3000L": "J. Anderson",
    "MAC 2281": "A. Makaryus",
    "MUH 3016": "A. Wilkins",
    "PHY 2048": "G. Pradhan"
}

CLASS_TIME = {
    "COP 2510": "MW 12:30pm - 1:45pm",
    "EGN 3000L": "TR 11:00am - 12:15pm",
    "MAC 2281": "MW 9:30am - 10:45am",
    "MUH 3016": "online asynchronous",
    "PHY 2048": "TR 5:00pm - 6:15pm"
}

#create a variable for the user to input a course numero

users_input = input("enter a course number, available from the schedule:")

# checking if the input is valid or not 
if users_input in course_numero:
    course_numero = users_input
    print("Course Details ----------------")
    print(f"Course Name: {jeneng_course[course_numero]}")
    print(f"Instructor name: {names[course_numero]}")
    print(f"Class Time: {CLASS_TIME[course_numero]}")
else:
    print("this number is invalid, please enter a valid course number")


