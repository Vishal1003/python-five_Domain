# USING beautiful soup
from bs4 import BeautifulSoup

raw_html = open('demo.html').read()
html = BeautifulSoup(raw_html, 'html.parser')

for p in html.select('p'):
    print(p.text)

