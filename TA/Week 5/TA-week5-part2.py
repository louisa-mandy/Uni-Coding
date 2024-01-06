#create a phonebook program, that stores dictionaries in them. A contact must contain a name, phone number, gmail.
#The phonebook can add, delete, show all contact, and has an exit button for it to stop running. \

names = []
phone_numbers = []
emails = []
num = 1 # num for how many times / looping

for i in range(num):
    name = input("Type in your name please: ")
    phone_number = input("Phone Number: ")
    email = input("Input your email here: ")

    names.append(name)
    phone_numbers.append(phone_number)
    emails.append(email)

print("\nName\t\t\tPhone Number\t\t\tEmail\n")

for i in range(num):
    print("{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], emails[i])) # this code will display ur name, number and email

search_term = input("\nEnter search term: ") # search engine 

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    email = emails[index]
    print("Name: {}, Phone Number: {}, Email: {}".format(search_term, phone_number, email))
else:
    print("Name Not Found")
