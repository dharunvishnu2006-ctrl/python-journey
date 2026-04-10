import json

students = [
    {"name": "Dharun", "marks": 95},
    {"name": "Ram", "marks": 88},
    {"name": "arun", "marks": 78},
    {"name": "muthu", "marks": 82},
    {"name": "saran", "marks": 70}
]
with open("students.json","w")as f:
    json.dump(students,f,indent=2)

print("JSON file created!")    

with open("students.json","r")as f:
    data=json.load(f)
for student in data:
    print(student["name"],"-",student["marks"])   