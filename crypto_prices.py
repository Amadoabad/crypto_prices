import requests
from bs4 import BeautifulSoup as bs
import csv

url = "https://coinmarketcap.com/"
raw = requests.get(url).text
soup = bs(raw, "html.parser")
table = soup.tbody.contents

crypto = []
for i, tr in enumerate(table):
    name_tag, price_tag = tr.contents[2:4]
    if i < 10:
        name = name_tag.p.string
    if i >= 10:
        name = name_tag.find_all("span")[1].string

    price = price_tag.text
    crypto.append({'Name': name, 'Price': price})

path = "./crypto_prices.csv"
field_names = ['Name', 'Price']
# field_names = ['Name', 'OldPrice', 'NewPrice']
# with open(path, 'r') as f:
    # reader = csv.
with open(path, "w", newline="") as f:
    writer = csv.DictWriter(f, field_names)
    writer.writeheader()
    writer.writerows(crypto)