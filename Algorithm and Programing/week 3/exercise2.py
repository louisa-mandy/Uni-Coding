#6 second exercise on the 6th session sir jude 

# 1 ans = [1, 2]---> 1 

# 2 ans = 2, it prints the middle row [1,2] == 2
xlist = [1, [1, 2], [1, 2, 3]]
print(xlist[1][1]) 

# 3 
xlist = [1, [1, 2], [1, 2, 3]]
print(xlist[1] + [1])

# it prints [1,2] and it will add another random [1]
# therefore it prints == [1,2,1]

#4 skip 

#5 d, try using python tutor
#all of the formulas gives the same result 
[["hi",2]]

# 6 c, also try using python tutor

# 7 a

# 8 c, jumps / skips a letter

# 9, use .copy to create a new list, so your x/y wont depend on the same list 
# d

# 10, [8] [7]
# the value of x changes from 7 to 8, meanwhile y still has the value of 7 

# 11 

# 12 a
s = "row"
for i in range(len(s)):
 print(s[ : i])

#13 b, starts from 't' --> 'at' --> 'tab'
# use (s[::-1]) to reverse all of the words 
s = "stab"
for i in range(len(s)):
 print(s[i : 0 : -1])

#14 a, reverses the list we have 
s = "stab"
for i in range(len(s)):
 print(s[i : -5 : -1])

#15 c 
s = "stab"
for i in range(len(s)):
 print(s[0 : i : 1])
 
