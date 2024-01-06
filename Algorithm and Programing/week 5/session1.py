#okt 13th 2023 

myList = List()
myList2 = [1,2,3,4]
#lists can be modified/ mutable data type 

myStr1 = str()
myStr2 = " "
myStr3 =''

myTuple1 = tuple()
myTuple2 = ()

myNewTuple = tuple(myList2) # converting lists to tuple (changing data types)

# strings and tuple are not mutable/ immutable
_________________________________________________________________________

'''
Dictionary - a mutable data type used specifically for association
- always contains a key and value pair 
{key1:value1,...{keyN:valueN}}

key - immutable and unique (make sure)
value - mutable or immutable 
'''
#creating a lists of student names and their id numbers 
#dictionaries are imuatble
#unsorted collection - non sequential data structures 

keys(), values(), items(), sorted(),

#populating our dictionary 

#putting / adding items to dictionary 
myDict1 = {"BN111":90, "Names":["Mandy","Raisya","Chris","Cassie"], 3.5:(1,2,3,4), True:1}

#access/modify values 
#if the key does not exsist, it will be added i to the dictionary 
#if the key exsist, the value will be updated 

print(myDict1['BN111'])
print(myDict1[3.5])
print(myDict1["Names"])

myDict1["BN111"] = 45
print(myDict1['BN111'])

#print all the keys 
for key in myDict1:
    print(key,':\t',myDict1.get(key))

#print all the values
for values in myDict1.values():
    print(values)






