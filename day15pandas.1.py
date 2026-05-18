import pandas as pd

marks = pd.Series([85, 92, 78, 95, 88],
                  index=["Ravi", "Priya", "Kumar", "Meena", "Raja"])
print(marks)
print("Ravi marks:", marks["Ravi"])

patients = {
    "name": ["Ravi", "Priya", "Kumar", "Meena"],
    "age":  [65, 32, 55, 45],
    "bp":   [145, 118, 160, 125]
}

df = pd.DataFrame(patients)
print(df)
print(df.shape)
print(df.describe())