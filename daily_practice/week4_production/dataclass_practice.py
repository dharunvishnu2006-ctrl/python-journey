from dataclasses import dataclass

@dataclass
class Patient:
    name: str
    age: int
    blood_pressure: float
    city: str = "Chennai"

p1 = Patient("Dharun", 20, 120.5)
p2 = Patient("Amma", 45, 135.0, "Erode")

print(p1)
print(p2)
print(f"Same patient? {p1 == p2}")