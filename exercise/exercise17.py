import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
title = []
for item in soup.find_all('h3'):
    title.append(item.string)
print(title)