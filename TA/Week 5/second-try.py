#create a phonebook program, that stores dictionaries in them. A contact must contain a name, phone number, gmail.
#The phonebook can add, delete, show all contact, and has an exit button for it to stop running. \


names = []
phone_numbers = []
emails = []
num = 1 # num for how many times / looping

def display_entries():
    print("\nName\t\t\tPhone Number\t\t\tEmail\n")
    for i in range(num):
        print("{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i], emails[i])) # this code will display ur name, number and email

def edit_entry(): # editing 
    edit_name = input("Enter the name to edit: ") 
    if edit_name in names:
        index = names.index(edit_name)
        names[index] = input("Enter the new name: ")
        phone_numbers[index] = input("Enter the new phone number: ")
        emails[index] = input("Enter the new email: ")
        print("Entry edited successfully.")
    else:
        print("Name Not Found")

def delete_entry():
    delete_name = input("Enter the name to delete: ")
    if delete_name in names:
        index = names.index(delete_name)
        del names[index]
        del phone_numbers[index]
        del emails[index]
        print("Entry deleted successfully.")
    else:
        print("Name Not Found")

for i in range(num):
    name = input("Type in ur name here : ")
    phone_number = input("type in ur phone number here : ")
    email = input("Input your email here: ")

    names.append(name)
    phone_numbers.append(phone_number)
    emails.append(email)

while True:
    print("\nOptions:")
    print("1. Display Entries")
    print("2. Edit Entry")
    print("3. Delete Entry")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1': # choice for displaying entries
        display_entries()
    elif choice == '2': # for editing entries
        edit_entry()
    elif choice == '3': # for deleting an entry
        delete_entry()
    elif choice == '4': # exit / stop running 
        break
    else:
        print("Invalid choice. Please enter a valid option.")
