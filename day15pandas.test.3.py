import pandas as pd
temps = pd.Series(
    [32, 38, 28, 41, 35],
    index=["Chennai", "Delhi", "Mumbai", "Rajasthan", "Bangalore"]
)

print("Temperatures:")
print(temps)

hot_cities = temps[temps > 35]

print("\nHot Cities (>35°C):")
print(hot_cities)

average_temp = temps.mean()

print("\nAverage Temperature:")
print(average_temp)