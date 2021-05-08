import csv
import requests
from bs4 import BeautifulSoup
import pickle

url = 'https://medium.com/better-programming/the-secret-to-being-a-top-developer-is-building-things-d3d058e4e472'
response = requests.get(url)
html = response.content
# soup = BeautifulSoup(response.text,"html.parser")
soup = BeautifulSoup(html,"lxml")
# a = []
# p = []
# ul = []
# li = []
text = []
for txt in soup.find_all('div', attrs={'class': 'z'}):
    a = txt.find_all('a')
    p = txt.find_all('p')
    ul = txt.find_all('ul')
    li = txt.find_all('li')
    text.append(a)
    text.append(p)
    text.append(ul)
    text.append(li)

print(text)

# list_of_rows = []
# for row in table.find_all(''):
    # list_of_cells = []
    # for cell in row.find_all('td'):
        # print(cell.text.replace('&nbsp;', ''))
        # text = cell.text.replace('&nbsp;', '')
        # list_of_cells.append(text)
    # list_of_rows.append(list_of_cells)
# 
# outfile = open("./graphql_related.txt", "wt") #when I use wb error(python TypeError: a bytes-like object is required, not 'str')
# with open('./graphql_related.txt', 'w') as filehandle:
    # filehandle.writelines("%s\n" % place for place in text)
# print(list_of_rows)