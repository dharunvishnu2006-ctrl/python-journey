import json

json_string = '{"name": "Dharun", "marks": 95}'
data = json.loads(json_string)
print(data["name"])
print(data["marks"])

student = {"name": "Vishnu", "marks": 88}
result = json.dumps(student, indent=2)
print(result)