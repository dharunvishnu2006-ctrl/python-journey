import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

url = "https://en.wikipedia.org/wiki/List_of_most_populous_cities"
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find_all("table")
print(f"Total tables found: {len(table)}")

table = table[1]
rows = table.find_all("tr")
print(f"total rows: {len(rows)}")

for row in rows[:5]:
    cells = row.find_all(["td","th"])
    cell_text = [cell.text.strip()for cell in cells]
    print(cell_text)