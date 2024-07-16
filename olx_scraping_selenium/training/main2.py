# Importing the required libraries.
import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
# Requesting the HTML from the target website.
url = "https://sandbox.oxylabs.io/products"
page = requests.get(url)

# Selecting data.
soup = BeautifulSoup(page.content, "html.parser")
products = soup.find_all("div", class_="product-card")

# Processing data using Regular Expressions.
re_titles = r'class="title css-7u5e79 eag3qlw7">(.*?)<\/h4>'
re_prices = r'class="price-wrapper css-li4v8k eag3qlw4">(.*?)<\/div>'

data = []

for product in products:
   product_html = str(product)
   title = re.findall(re_titles, product_html)
   price = re.findall(re_prices, product_html)
   data.append((title, price))

# Saving the output.
with open("output.txt", "w", encoding="utf-8") as f:
   for title, price in data:
       f.write(f"{title}\t{price}\n")