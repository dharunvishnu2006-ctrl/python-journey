import re

patient_data = """
Name: Dharun Vishnu
Phone: 9876543210
Email: dharun@gmail.com
Aadhaar: 1234 5678 9012
PIN: 600001
Blood Group: O+
"""
phone = re.search(r'\b\d{10}\b', patient_data)
print("Phone:", phone.group())

email = re.search(r'[\w\.-]+@[\w\.-]+', patient_data)
print("Email:", email.group())

aadhaar = re.search(r'(\d{4}\s\d{4}\s\d{4})', patient_data)
print("Aadhaar:", aadhaar.group().replace(" ", ""))

pin = re.search(r'\b\d{6}\b', patient_data)
print("PIN:", pin.group())