import pandas as pd

data = {
    "name": ["Ravi", "Priya", "Kumar", "Meena", "Raja"],
    "age":  [65, 32, 55, 45, 70],
    "bp":   [145, 118, 160, 125, 155],
    "sugar":[180, 95, 210, 110, 190]
}

df = pd.DataFrame(data)

print("Task 1:")
print(df.loc[0:2, ["name", "bp"]])

print("\nTask 2:")
print(df.iloc[0:3, 0:2])

print("\nTask 3:")
print(df.loc[df["name"] == "Kumar", "bp"].values[0])