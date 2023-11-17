import requests
import datetime
import os
# 100 Req / Month


filename = 'count.txt'
devApi = 'devapi.txt'
try:
    # Open the file in read mode
    with open(filename, 'r') as countFile, open(devApi, 'r') as apiK:
        # Read the current count
        current_count = countFile.read()
        apiKey = apiK.read()

        # Check if the count is a number and convert it to an integer
        if current_count.isdigit():
            count = int(current_count) + 1
        else:
            count = 1
except FileNotFoundError:
    # If file does not exist, start with count 1
    count = 1

stockQuotes = '/stock/quotes'
url = 'https://devapi.ai/api/v1/markets' + stockQuotes
params = {'ticker': 'AAPL,TSLA'}
headers = {'Authorization': 'Bearer ' + apiKey}

response = requests.request('GET', url, headers=headers, params=params)
data = response.json()

# Open the file in write mode and update the count
with open(filename, 'w') as countFile:
    countFile.write(str(count))

body_info = data['body']
stockDict = {}

for item in body_info:
    stockDict[item ['symbol']]= item['marketCap']

current_date = datetime.datetime.now().strftime("%Y-%m-%d") 
with open('market_cap_data.txt', 'a') as file:
    file.write(f"Date: {current_date}\n")
    for company, market_cap in stockDict.items():
        file.write(f"{company}: {market_cap}\n")

print(f"Current request count is: {count}")

