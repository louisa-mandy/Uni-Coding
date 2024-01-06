a = int(input("Enter value for AB: "))
b = int(input("Enter value for BC: "))
c = int(input("Enter value for AC: "))

perimeter = a + b + c 

if a + b < c and a + c < b and b + c < a :
    print("Enter the value of AB : ",a)
    print("Enter the value of BC : ",b)
    print("Enter the value of AC : ",c)
    print("invalid")

else:
    print("Enter the value of AB : ",a)
    print("Enter the value of BC : ",b)
    print("Enter the value of AC : ",c)
    print("valid, the preimeter", perimeter)

    

