import requests
from bs4 import BeautifulSoup

all_quotes = []

for page in range(1, 11):
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    
    for i in range(len(quotes)):
        all_quotes.append({
            "quote": quotes[i].text,
            "author": authors[i].text
        })

print(f"Total quotes scraped: {len(all_quotes)}")
import csv

with open("all_quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(all_quotes)

print("Saved to all_quotes.csv!")