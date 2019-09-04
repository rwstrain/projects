# @author: Wade Strain
# JSON Web Scraping Project
# Competing Through Business Analytics
# August 31, 2019

import requests

my_wm_username = 'rwstrain'

# request url of the desired JSON file
search_url = 'https://buckets.peterbeshai.com/api/?player=201939&season=2015'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})

# convert to JSON
root = response.json()

numJumpShotsAttempt = 0
numJumpShotsMade = 0
percJumpShotMade = 0.0

# iterate through all of Curry's shots
for shot in root:
    if(shot['ACTION_TYPE'] == 'Jump Shot'):
        numJumpShotsAttempt += 1
        if(shot['EVENT_TYPE'] == 'Made Shot'):
            numJumpShotsMade += 1

# calculate the percentage of shots made over shots attempted
percJumpShotMade = numJumpShotsMade / numJumpShotsAttempt

print(my_wm_username)
print(numJumpShotsAttempt)
print(numJumpShotsMade)
print(percJumpShotMade)
