# 1. prompt the user to enter a line of text 
# 2. split the input line per character and save it in a list
# 3. remove all non - alpha numeric characters
# 4. remove all duplicates 
# 5. sort in ascending order
# 6. display the contents of the list 


input = input("enter a line of text")
list1 = list(input)
print(list1)

newlist = ''.join(char for char in list1 if char.isalnum())
list2 = list(newlist)
list3 = list(set(list2)) #set with no duplicates 
list3.sort()

print(list3)

 

