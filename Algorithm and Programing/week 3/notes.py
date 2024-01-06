##immuatble object - dtring - "",'' and tuple - ()

myStr = "Hello"

print(myStr[1])
#its gonna print 'e'
# index range ( 0, 1 ,2 ,3 ,4 etc from H e l l o )

# to know the last index use the formula : 
print(myStr[len(myStr)-1])
print(myStr[-1])

# cannot change a signle alphabet, must change the ehole word / string in order to chage it all

myTuple = (10,3.5,"Hi",True)

myTuple[0] # 10

# to check if its a tuple or not 
#myTuple(tuple)


#_________________________________________________________

## mutable object - list - [], a list is an editable object / immuatble object0

myTuple = (10,3.5,"Hi",True)
myList - list(myTuple)
 
myList.append("wow") #your list will add "wow", it allows to change a data at will, while string cannot 

#_________________________________________________________

#loop - while, for ( while loop, for loop )
