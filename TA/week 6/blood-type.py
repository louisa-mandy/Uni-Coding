def check_blood_compatibility(donor_blood_type, recipient_blood_type):
    # These are the list of the possible blood type transfusion 
    blood_types = {
        'A+': ['A+', 'AB+'],
        'A-': ['A-', 'AB-'],
        'B+': ['B+', 'AB+'],
        'B-': ['B-', 'AB-'],
        'AB+': ['AB+'],
        'AB-': ['AB-'],
        'O+': ['A+', 'B+', 'AB+', 'O+'],
        'O-': ['A-', 'B-', 'AB-', 'O-']
    }

    # Checking the compatibility: if yes = true, else = false
    if donor_blood_type in blood_types[recipient_blood_type]:
        return f"Blood type {donor_blood_type} can be transfused to {recipient_blood_type} recipient. ( True )"
    else:
        return f"Blood type {donor_blood_type} cannot be transfused to {recipient_blood_type} recipient. ( false )"

# input
donor_type = input("Enter the donor's blood type : ").upper()
recipient_type = input("Enter the recipient's blood type : ").upper()

result = check_blood_compatibility(donor_type, recipient_type)
print(result)
