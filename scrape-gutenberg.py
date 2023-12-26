from bs4 import BeautifulSoup
import requests

url_link = "https://www.gutenberg.org/cache/epub/1112/pg1112-images.html"
result = requests.get(url_link).text
doc = BeautifulSoup(result, "html.parser")

print(doc.prettify())
