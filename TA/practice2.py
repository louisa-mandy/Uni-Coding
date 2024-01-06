while True : 
    dollars = float(input("Change owed: "))
    if dollars > 0:
        break 

coin = dollars * 100

count = 0
while coins > 0: 
    if coins >= 25: 
        coins -= 25
        count += 1 
    
    elif coins >= 10: 
        coins -= 10
        count += 1

    elif coins >= 5:
        coins -= 5
        count += 1 
    
    else:
        coins -= 1
        count += 1 
    
print(count)


