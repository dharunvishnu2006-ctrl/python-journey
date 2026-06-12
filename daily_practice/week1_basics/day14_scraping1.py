import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)

print(response.status_code)
print(type(response.text))
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("title")
print(title)
quotes = soup.select("span.text")
print(f"Total quotes found: {len(quotes)}")

authors = soup.find_all("small", class_="author")
for i in range(len(quotes)):
    print(f"Quote: {quotes[i].text}")
    print(f"Author: {authors[i].text}")
    print("---")

import csv

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])
    for i in range(len(quotes)):
        writer.writerow([quotes[i].text, authors[i].text])

print("Saved to quotes.csv!")