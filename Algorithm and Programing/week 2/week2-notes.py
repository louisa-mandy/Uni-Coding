#relational operators - >, <, >=, <=
#Logical operatord - and, or, not 

x = True
y = False
result = x and y 
#answer = False 

#if clause / indention 
num = int(input("enter a number:"))
if (num%2==0):
    print(f'{num} is even')
else:
    print(f'{num} is odd')

#locate the origin,first, second, third, and fourth quadrant
xCoord = int(input("enter x coordinate:"))
yCoord = int(input("enter y coordinate:"))

if xCoord==0 and yCoord==0:
    print(f'{(xCoord,yCoord)} is in the origin')
elif xCoord > 0 and yCoord > 0:
    print(f'{(xCoord,yCoord)} is in the first quadrant')
elif xCoord < 0 and yCoord > 0:
    print(f'{(xCoord,yCoord)} is in the second quadrant')
elif xCoord < 0 and yCoord < 0:
    print(f'{(xCoord,yCoord)} is in the third quadrant')
elif xCoord > 0 and yCoord < 0:
    print(f'{(xCoord,yCoord)} is in the fourth quadrant')







