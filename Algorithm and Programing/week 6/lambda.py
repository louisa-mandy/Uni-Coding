numbers = [1,2,3,4,5,6,7,8,9,10]
square_number =  list(map(lambda x : x**2, numbers)) # formula for square numbers 

print(square_number) 


from functools import reduce # import reduce

calculate = reduce(lambda x,y : x*y, numbers) # multiplying all the numbers available in numbers 
print(calculate)

even_numero = filter(lambda x:x%2 == 0, numbers) # % = remainder 
print(list(even_numero))