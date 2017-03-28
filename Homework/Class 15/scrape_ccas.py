import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

URL = 'https://columbian.gwu.edu/2015-2016'

response = requests.get(URL)
html = response.content

soup = BeautifulSoup(html, 'lxml')

all_pages = soup.select('.menu-mlid-1117 > ul > li > a')

all_pages_rows = []
all_pages_headers = []

def parseTable(table, id):
    list_of_rows = []
    header_list = []
    for row in table.findAll('tr')[0:-1]:
        list_of_cells = []
        for header in row.findAll('th'):
            header_list.append(header.text)
        for cell in row.findAll('td'):
            link = cell.find('a')
            if link:
                list_of_cells.append(urljoin(URL, link['href']))
            else: list_of_cells.append(cell.text)
        if list_of_cells:
            list_of_cells.append(id)
            list_of_rows.append(list_of_cells)

    return header_list, list_of_rows

for i, page in enumerate(all_pages):
    print('Fetching %s' % page['href'])
    current_year = requests.get(urljoin(URL, page['href']))
    current_year_soup = BeautifulSoup(current_year.content, 'lxml')
    table = current_year_soup.find('table')
    header_list, all_rows = parseTable(table, page['href'][1:])
    if i == 0:
        all_pages_headers.extend(header_list)
    all_pages_rows.extend(all_rows)
    time.sleep(1) #Chill out for a second before hitting the page again.

all_pages_headers.append('Year')
all_pages_rows.insert(0, list(all_pages_headers))

outfile = open("gwu_grants.csv", "w")
writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
writer.writerows(all_pages_rows)