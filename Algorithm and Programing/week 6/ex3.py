groceries = [ "banana", "orange", "apple"]

stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}

prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

def bill(food):
    total = 0 
    for i in food: 

        if stock[i] > 0:
            
            stock[i] -= 1
            total += (prices[i] * stock[i])
    return total

print(bill(groceries))