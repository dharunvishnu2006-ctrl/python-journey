import pandas as pd

patients = {
    "name": ["Ravi", "Priya", "Kumar", "Meena", "Raja"],
    "age":  [65, 32, 55, 45, 70],
    "bp":   [145, 118, 160, 125, 155]
}

df = pd.DataFrame(patients)
print(df[df["bp"] > 140])

print(df[(df["age"] > 50) & (df["bp"] > 140)])

print(df.query("bp > 150"))

print(df.iloc[0:3, 0:2])