# @author: Wade Strain
# HTML Web Scraping
# August 31, 2019

import requests
from bs4 import BeautifulSoup as bsoup

search_url = 'http://publicinterestlegal.org/county-list/'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}

response = requests.get(search_url, headers=header).content

# parse HTML
parsed_html = bsoup(response, 'lxml')
# get rows of data
data_rows = parsed_html.find_all('tr')

my_result_list = []
# go through each row of data and put it in a 2D list
for row in data_rows:
    temp_row = []
    # get the data within each row
    for col in row.find_all('td'):
        temp_row.append(col.text)

    my_result_list.append(temp_row)

print(len(my_result_list))
print(my_result_list)
