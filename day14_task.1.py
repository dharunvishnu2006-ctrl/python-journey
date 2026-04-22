import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/page/1/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quote_blocks = soup.select("div.quote")
for block in quote_blocks:
    quote = block.select_one("span.text").text
    author = block.select_one("small.author").text
    tags = [tag.text for tag in block.select("a.tag")]
    print(f"Quote: {quote}")
    print(f"Author: {author}")
    print(f"Tags: {tags}")
    print("-" * 50)