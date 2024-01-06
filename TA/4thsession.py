#name = input("enter a first name")
#name2 = input("enter a last name")

#result = (name + "_" +name2)

#print(result.lower())

snakecase = []
i = input("enter a random name: ")


if i.isupper():
    snakcase.append ("_"+i.lower())
else:
    snakecase.append(i)

result = ''.join(snakecase)

print(result.lower())
  



