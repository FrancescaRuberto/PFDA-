# Read JSON from the internet
# Author: Francesca Ruberto

import requests

url= "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data)
