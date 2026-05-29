from datetime import datetime, timedelta
import re

patients = [
    {"name": "Dharun", "dob": "2005-05-21", "phone": "9876543210"},
    {"name": "Rahul", "dob": "2000-03-15", "phone": "8765432109"},
    {"name": "Priya", "dob": "1995-07-10", "phone": "7654321098"}
]

from datetime import date

dob = datetime.strptime("2005-05-21", "%Y-%m-%d").date()
today = date.today()
age = today.year - dob.year
print(f"Age: {age} years")

birthday_this_year = dob.replace(year=today.year)

if birthday_this_year < today:
    next_birthday = dob.replace(year=today.year + 1)
else:
    next_birthday = birthday_this_year
print("Next Birthday:", next_birthday.strftime("%d/%m/%y"))

phone = "9876543210"
if re.match(r'^\d{10}$', phone):
    print("Valid Phone!")