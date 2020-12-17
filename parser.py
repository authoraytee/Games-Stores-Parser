import requests
from bs4 import BeautifulSoup

url = 'https://steampay.com/game/starbound'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
quotes = soup.find('div', class_='product__current-price')

quotes = quotes.text.split()

print(quotes[0])




















