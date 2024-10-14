# Read JSON from the internet
# Author: Francesca Ruberto

import requests

url= "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
#print(data)

print(data['bpi']['EUR']['rate_float']) 

# key bpi stands for "Bitcoin Price Index in the data dictionary". 
# key "EUR" is the exhange currency
# key "rate_float" contains the numerical value of the exhange, expressed in decimal values. 
