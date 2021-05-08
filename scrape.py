import csv
import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,"lxml")
table = soup.find('tbody')
# print(table.prettify())

list_of_rows = []
for row in table.find_all('tr'):
    list_of_cells = []
    for cell in row.find_all('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

with open('./data.json', 'w') as outfile:
    json.dump(list_of_rows, outfile, sort_keys=True, indent=4)
