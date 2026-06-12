from dataclasses import dataclass

@dataclass
class Doctor:
    name: str
    specialization: str
    hospital: str = "Apollo"
doctor1 = Doctor("Dr.Ravi", "Cardiology")
doctor2 = Doctor("Dr.Priya", "Neurology", "AIIMS")

print(doctor1)
print(doctor2)