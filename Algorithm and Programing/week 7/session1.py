'''
def whatever(*args,**kwargs)
arguments = argument 
keyword arguments = kwargs 

'''

def orderPizza (size, *toppings, **instructions) : 
    print (f"you have ordered a {size} pizza")
    print (f"with {toppings} toppings")
    for top in toppings:
        print(f"-:{top}") #will print a list / atorist 
    print("instructions : ")
    for k, v in instructions.items():
        print(f'-:{k} {v}')

size = "large"
orderPizza(size,"pepperoni","chesse","pinapple", " note : i want it to be warm", tip = 1000 )

int()



x = ( 1, 2, 3, 4, 5)
print(*x)