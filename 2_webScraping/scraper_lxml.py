# Scrapping Codechef Hard problem list

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.codechef.com/problems/medium'
res = requests.get(url)

page = BeautifulSoup(res.text, 'lxml')
data = page.select('table.dataTable')

data_table = data[0]
prob_tags = data_table.select('a > b')

prob_names = [tag.getText().strip() for tag in prob_tags]

for i in prob_names:
    print(i)

df = pd.DataFrame({'Problem Names: ', prob_names})

df.to_csv('questions.csv', index=False, encoding='utf-8')
