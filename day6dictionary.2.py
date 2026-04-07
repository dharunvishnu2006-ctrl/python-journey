student = {
    "name": "Dharun",
    "age": 21,
    "city": "Erode",
    "dream": "CISO" 
}
print(student.keys())
print(student.values())

student["College"]= "Kongu Arts and Science"
print(student)

student["age"]=22
print(student["age"])
del student["city"]
print(student)