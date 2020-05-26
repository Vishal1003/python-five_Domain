# Scarpping names of 100 greatest mathematicians

from bs4 import BeautifulSoup
import requests

url = "http://www.fabpedigree.com/james/mathmen.htm"

raw_html = requests.get(url)
html = BeautifulSoup(raw_html.text,'html.parser')

names = set()
for i, li in enumerate(html.select('li')):
    for name in li.text.split('\n'):
        if len(name) > 0:
            names.add(name.strip())

print(list(names))