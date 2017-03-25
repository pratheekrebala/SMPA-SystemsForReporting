import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'lxml')
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[0:-1]:
    list_of_cells = []
    for header in row.findAll('th'):
        list_of_cells.append(header.text)

    for cell in row.findAll('td'):
        link = cell.find('a')
        if link:
            list_of_cells.append(urljoin(url, link['href']))
        else: list_of_cells.append(cell.text)

    list_of_rows.append(list_of_cells)

outfile = open("crime.csv", "w")
writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
writer.writerows(list_of_rows)