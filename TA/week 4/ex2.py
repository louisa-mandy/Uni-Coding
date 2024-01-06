bill = float(input("Enter amount of bill: "))
num_of_people = int(input("Enter number of people: "))
tip = float(input("Enter amount of tip (%): "))

tip_per_person = ( (tip/100) * bill ) / num_of_people
total_per_person = bill / num_of_people + tip_per_person


print("tip amount per person:" ,tip_per_person )
print("total amount per person:" ,total_per_person )