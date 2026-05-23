import re

text1 = "Patient Dharun contact: 9876543210"
phone = re.search(r'\d{10}', text1)
print("Phone:", phone.group())

text2 = "Doctors: dr.kumar@apollo.com, dr.priya@aiims.com"
emails = re.findall(r'\w+@\w+\.\w+', text2)
print("Emails:", emails)

pin = "600001"
if re.match(r'^\d{6}$', pin):
    print("Valid PIN code!")
    
text3 = "Patient age: 25, sugar: 180, bp: 140"
cleaned = re.sub(r'\d+', '[VALUE]', text3)
print("Cleaned:", cleaned)