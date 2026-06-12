from dataclasses import dataclass

@dataclass
class Hospital:
    name: str
    city: str
    beds: int = 100

h1 = Hospital("Apollo", "Chennai")
h2 = Hospital("AIIMS", "Delhi", 500)

print(h1)
print(h2)
print(f"Same hospital? {h1 == h2}")