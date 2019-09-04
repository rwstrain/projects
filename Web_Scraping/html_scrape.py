# @author: Wade Strain
# HTML Web Scraping Project
# Competing Through Business Analytics
# August 31, 2019

import requests
from bs4 import BeautifulSoup as bsoup

my_wm_username = 'rwstrain'
search_url = 'http://publicinterestlegal.org/county-list/'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
response = response.content

# parse HTML
parsed_html = bsoup(response, 'lxml')
# get rows of data; <tr> tags denote table rows
# since this site only has one table, you don't need to denote which table by using an attribute
# ex: parsed_html.find_all('tr', attrs={'id' : 'name of id'}))
# or you can use regular expressions and 'import re' above
# ex: parsed_html.find_all('tr', attrs={'id': re.compile('^beginning of common name')})
data_rows = parsed_html.find_all('tr')

my_result_list = []
# go through each row of data and put it in a 2D list
for row in data_rows:
    temp_row = []
    # <td> tags denote fields within rows
    for col in row.find_all('td'):
        temp_row.append(col.text)

    my_result_list.append(temp_row)

print(my_wm_username)
print(len(my_result_list))
print(my_result_list)
