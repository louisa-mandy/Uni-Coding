list1 = [10,20,30,40]
list2 = [100,200,300,400]
output = []

for i in range (len(list1)):
    output.append(str(list1[i]) + " " + str(list2[3-i]))
print(output)


#output: 
# 10 400
# 20 300
# 30 200
# 40 100