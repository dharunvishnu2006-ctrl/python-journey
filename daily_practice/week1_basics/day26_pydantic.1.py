from pydantic import BaseModel, Field


class Patient(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)
    blood_pressure: float
    city: str = "Chennai"


p1 = Patient(name="Dharun", age=20, blood_pressure=120.5)
print(p1)

try:
    p2 = Patient(name="Ravi", age=150, blood_pressure=120.5)
except Exception as e:
    print(f"Error: {e}")
