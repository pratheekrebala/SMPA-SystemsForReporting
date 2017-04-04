import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import itertools

URL = 'http://m.nationals.mlb.com/js/roster/transactions/%d/%d?v=1000'

YEARS = [2015, 2016, 2017]

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
                list_of_cells.append(cell.text)
            else: list_of_cells.append(cell.text)
        if list_of_cells:
            list_of_cells.append(id)
            list_of_rows.append(list_of_cells)

    return header_list, list_of_rows

for year in YEARS:
    for month in range(1, 13):
        #Skip future dates
        if year < 2017 or (year == 2017 and month <= 4):
            print(month)
            current_page = requests.get(URL % (year, month))
            curr_id = '-'.join(str(x) for x in [year, month])
            current_page_soup = BeautifulSoup(current_page.content, 'lxml')
            table = current_page_soup.find('table')
            if table:
                header_list, all_rows = parseTable(table, curr_id)
                all_pages_rows.extend(all_rows)
                if not all_pages_headers and header_list:
                    all_pages_headers.append(header_list)

all_pages_rows.insert(0, ["Date", "Link", "Transaction", "Month-Year"])
outfile = open("transactions.csv", "w")
writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
writer.writerows(all_pages_rows)