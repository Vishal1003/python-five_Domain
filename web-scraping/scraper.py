from bs4 import BeautifulSoup
import requests

url = "http://www.fabpedigree.com/james/mathmen.htm"

raw_html = requests.get(url)
html = BeautifulSoup(raw_html.text,'html.parser')

for i, li in enumerate(html.select('li')):
    print(i, li.text)