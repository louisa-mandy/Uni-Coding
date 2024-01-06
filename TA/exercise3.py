# Create a program that detects wether a string is eligible to be a vanity plate or not. 
# Vanity plates must start with at least two characters, maximum of 6 characters (letter and number), and a minimum of 2 characters. 
# There can't be a number inbetween letters. 
# The numbers must be at the end. 
# For example, AAA222 would be an acceptable vanity plate. AAA22A would not be acceptable. 
# The first number used cannot be a '0' and the string must only consist of letters and numbers.
# Louisa Mandy Halim - L1AC 


def main():
    plate = input("enter a plate number: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid (s) : 

    # to check the requirements of the letter ( min 2, max 6 ) 
    if len(s) < 2 or len(s) > 6:  
        return False

    #to check the first two letters from the plate to see if its an alphabet or not
    if s[0].isalpha() == False or s[1].isalpha() == False: 
        return False 

    # 0 cant be a number for this plate, this is to check if the plate has the number '0' or not 
    i = 0 
    while i < len(s):
        if s[i].isalpha() == False:  # if i is an alphabet = false 
            if s[i] == '0':
                return False
            
            else : 
                break # breaking the loop once the condition is valid 
        i += 1 
    
    # prohibition of spaces, " ", ?, ' ' , and other unnecesary marks will automatically return to false 
    for c in s: 
        if c in [ ' ', '?', '!', '.', ',' ] :
            return False
    
    # if all of the conditions matches, the result will be true 
    return True 

main()


