import json

student = {
    "name":"dharun",
    "age":21,
    "marks":95,
    "dream":"CISO"

}

with open("student.json","w")as f:
    json.dump(student,f,indent=2)

print("JSON file created!")    