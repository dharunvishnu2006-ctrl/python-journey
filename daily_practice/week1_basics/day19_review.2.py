import re

patients = [
    "Dharun - 9876543210 - dharun@gmail.com",
    "Rahul - 8765432109 - rahul@yahoo.com",
    "Priya - 7654321098 - priya@apollo.com"
]

for patient in patients:
    phone = re.search(r'\d{10}', patient)
    email = re.search(r'[\w\.-]+@[\w\.-]+', patient)

    print("Phone:", phone.group())
    print("Email:", email.group())
    print("------")