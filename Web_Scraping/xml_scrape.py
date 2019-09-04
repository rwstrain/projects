# @author: Wade Strain
# XML Web Scraping project
# Competing Through Business Analytics
# August 29, 2019

import requests
from lxml import objectify

# Example:
# Parameter: Average Temparature
# Year: 2018
# Month: July
# State: Virginia
# https://www.ncdc.noaa.gov/cag/statewide/rankings/44-tavg-201807/data.xml

# parameters for Average Temp. in Virginia on August, 2016
parameter = 'tavg'
state = '44'        # Virginia is the 44th state alphabetically
month = '08'
year = '2016'

# create url to correct xml site
fixed_site = 'https://www.ncdc.noaa.gov/cag/statewide/rankings/%s-%s-%s%s/data.xml'
site = fixed_site % (state, parameter, year, month)

# get xml file
response = requests.get(site).content
root = objectify.fromstring(response)

my_wm_username = 'rwstrain'

# data items for five-month period April-August 2016
# multiple 'data' fields in xml file; we want 5th data field
print(my_wm_username)
print(root['data'][4]['value'])
print(root['data'][4]['mean'])
print(root['data'][4]['departure'])
print(root['data'][4]['lowRank'])
print(root['data'][4]['highRank'])
