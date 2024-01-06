prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for product, price in prices.items():
    print(product)
    print("price", price)
    print("stock: 0")

total = 0 

for product, price in prices.items():
    stock= 0 
    value = price * stock
    print(f"the Value of {product}: is {value}")
    total += value

print (total)