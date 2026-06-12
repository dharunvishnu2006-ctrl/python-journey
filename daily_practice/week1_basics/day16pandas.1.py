import pandas as pd 
data = {
    "city":["chennai","mumbai","chennai","mumbai","delhi","delhi",],
    "product":["rice","oil","rice","sugar","oil","sugar"],
     "sales": [1000, 2000, 1500, 2500, 3000, 1800]
}
df = pd.DataFrame(data)

print(df.groupby("city")["sales"].sum())
print(df.groupby("city")["sales"].agg(["mean", "max"]))
print(df.groupby("city")["sales"].count())