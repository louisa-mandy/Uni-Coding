#1 b
d = {'a' : 0, 'b': 1, 'c' : 2}
print(d['c'])

#c is the key 
#2 is the value

'''
#2 d - error, because 2 is not a key 
d = {'a' : 0, 'b': 1, 'c' : 2}
print(d[2])
'''

#3 it .get = returns the value, which is 'c' : 2 
d = {'a' : 0, 'b': 1, 'c' : 2}
print(d.get(2, 'c'))


#4 b, print x ( x which is d ), .sorted will sort accoridng to the key 
d = {'a' : 0, 'b': 1, 'c' : 2}
for x in sorted(d):
    print(d[x], end=" ")

#5, it prints the value inside d, which is 0 1 2 / b 
d = {'a' : 0, 'b': 1, 'c' : 2}
for x in sorted(d.values()):
    print(x, end=" ")
# with indention

#6, .items() will print both the key and value ,c 
d = {'a' : 0, 'b': 1, 'c' : 2}
for x in sorted(d.items()):
    print(x, end=" ")
# with indention

#7, it prints the key which is a b c / a 
d = {'a' : 0, 'b': 1, 'c' : 2}
for x in sorted(d.keys()):
    print(x, end=" ")

#8 e, bcs dc is not included inside pres?? 
pres = {'george' : 'washington', 'thomas' : 'jefferson', 'john' : 'adams'}
print(pres.get('washington', 'dc'))









