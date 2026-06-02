from dataclasses import dataclass

@dataclass
class Patient:
    name: str
    age: int
    city: str = "Chennai"

p1 = Patient("Dharun", 20, "Erode")
print(p1)
print(f"Age: {p1.age + 5}")