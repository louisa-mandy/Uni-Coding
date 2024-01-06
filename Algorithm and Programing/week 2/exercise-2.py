# 1 foot = 12 inches 
# 1 inch = 2.54 cm 

feet = int(input("enter your height in feet"))
inch = int(input("enter your height in inches"))


result = inch*2.54 + feet*30.48

print (result, "cm")

# enter mass in kg 
# force in N is 55.4
# acceleration is 0.11
# formula F = m*a 

mass = float(input("enter your weight in kg"))
force = float(input("enter force in Newton"))

result = force / mass

print("the mass is", mass,"kg")
print("the force is", force,"N")
print("the acceleration is", result)




