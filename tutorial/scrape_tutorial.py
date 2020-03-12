import csv
import requests
from bs4 import BeautifulSoup

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content
soup = BeautifulSoup(html,"lxml")
table = soup.find('tbody', attrs={'class':'stripe'})
# print(table.prettify())

list_of_rows = []
for row in table.find_all('tr'):
    list_of_cells = []
    for cell in row.find_all('td'):
        #print(cell.text.replace('&nbsp;', ''))
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./inmates.csv", "wt") #when I use wb error(python TypeError: a bytes-like object is required, not 'str')
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Suffix", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)
#print(list_of_rows)