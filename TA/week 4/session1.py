#def
def displayMe(name):
    print("hello" + " " + name )
    ...

displayMe("Mandy")

def displayMe(name,age):
    name += "bla bla bla"
    print("hello" + " " + name + " " + "you are" + " " + str(age) + " " + "years old")

def getAgeEquiv(age):
    if age > 12 and age < 20:
        return " teenager"
    return "too old"
    ...
# the name doesnt matter, but the sequence matter 
myName = input("enter name: ")
myAge = int(input("enter your age"))
displayMe(myName, myAge)