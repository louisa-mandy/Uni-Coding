time = int(input("Enter the number of seconds: "))

hours = time // 3600
minutes = (time // 60) % 60
seconds = time % 60 

print( hours ,":", minutes ,":", seconds )