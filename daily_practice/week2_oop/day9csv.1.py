import csv

with open("students.csv","w",newline="")as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Marks","Grade"])
    writer.writerow(["dharun",95,"A"])
    writer.writerow(["ram",88,"B"])
    writer.writerow(["kumar",76,"C"])

print("CSV file created!")    