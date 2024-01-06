#Louisa Mandy Halim / L1AC / 2702325552
print("These are the students scores")

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

students = ["Lloyd", "Alice", "Tyler"]

def print_student(students):
    print("name:", students["name"])
    print("homework:", students["homework"])
    print("quizzes:", students["quizzes"])
    print("tests:", students["tests"])
    print()


print(Lloyd)
print(Alice)
print(Tyler)


input() # enter, move to the next code

print("these are the students average scores on each tasks")
Lloyd = {
 "name": "Lloyd",
 "homework": [88.5],
 "quizzes": [74.0],
 "tests": [82.5]
}

Alice = {
 "name": "Alice",
 "homework": [97.5],
 "quizzes": [85.3],
 "tests": [93.0]
}

Tyler = {
 "name": "Tyler",
 "homework": [46.0],
 "quizzes": [51.0],
 "tests": [100.0]
}

students = ["Lloyd", "Alice", "Tyler"]
print(Lloyd)
print(Alice)
print(Tyler)


input() # move to the next code

print("these are the students average scores")
Lloyd = {
 "name": "Lloyd",
 "average-score" : [81.6]
}

Alice = {
 "name": "Alice",
 "average-score" : [91.93]
}

Tyler = {
 "name": "Tyler",
 "average-score" : [65.6]
}

print(Lloyd)
print(Alice)
print(Tyler)


input() # move to the next code

print("These are the students final score")
N
students = ["Lloyd", "Alice", "Tyler"]

def calculate(students):
        
    students_score = students["average-score"]
    students_score2 = students_score[0]

    if students_score2 > 90:
        print ( students, " Grade : A" )
    elif students_score2 > 80:
        print ( students, " Grade : B" )
    elif students_score2 > 70:
        print ( students, " Grade : C" )
    elif students_score2 > 60:
        print ( students, " Grade : D" )
    else:
        print ( students, " Grade : F" )
        
calculate(Lloyd)
calculate(Alice)
calculate(Tyler)
#get the average score
# define the grade to A/B/C/D/F
# test and print the result 

'''
# get_letter_grade(name) = define the score whether it is A, B ,C etc
if students > 90:
    print ( "Grade A" )
elif students > 80:
    print ( "Grade B" )
elif students > 70:
    print ( "Grade C" )
elif students > 60:
    print ( "Grade D" )
else:
    print ( "Grade F" )


print(Lloyd)
print(Alice)
print(Tyler)




# interactive question

name = input("enter a students name").capitalize()

if name == "Lloyd":
    print_student(Lloyd)
elif name == "Alice":
    print_student(Alice)
elif students == "Tyler":
    print_student(Tyler)
else :
    print("please enter the available names (Lloyd, Alice, Tyler)")


'''