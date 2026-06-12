import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
response = requests.get("https://jsonplaceholder.typicode.com/posts/5")

data = response.json()

print(data["userId"])
print(data["id"])
print(data["title"])
