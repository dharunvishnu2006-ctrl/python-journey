import pandas as pd

patients = {
    "name":  ["Ravi", "Priya", "Kumar", "Meena", "Raja", "Sundar"],
    "age":   [65, 32, 55, 45, 70, 48],
    "bp":    [145, 118, 160, 125, 155, 135],
    "sugar": [180, 95, 210, 110, 190, 140]
}

df = pd.DataFrame(patients)

print("Statistics:")
print(df.describe())

high_bp = df[df["bp"] > 140]

print("\nHigh BP Patients:")
print(high_bp)

high_sugar = df[df["sugar"] > 150]

print("\nHigh Sugar Patients:")
print(high_sugar)

age_above_60 = df[df["age"] > 60].shape[0]

print("\nPatients Age > 60 Count:")
print(age_above_60)