import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
text = []
for item in soup.find_all('p'):
    if item.string != None:
        text.append(item.string)*

print(text)