list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]

a = []
b = []

for i in range (len(list1)):
    a.append(str(list1[i]) + " " + str(list2[1-i]))
    b.append(str(list1[1-i]) + " " + str(list2[i]))
    output = a + b 
print(output)

#['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']