num = int(input("enter a numerator"))
num2 = int(input("enter a denominator"))

import math
if num > 0 and num2 > 0:
    math.gcd(num, num2)
    if num2 < num: 
       print("proper fraction")
       
    elif num2 > num:
        print("proper fraction")
else: 
    print("improper fraction")