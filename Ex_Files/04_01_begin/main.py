# from pprint import pprint
import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json"
)

# print(response)

# iterating thru 20 items for testing

# last_20_years = response.json()[1][:20]

# for year in last_20_years:
#   display_width = year["value"] // 10_000_000 # in python you can use underscores to make number more readle, i.e. 10_000_000
#   print(f'{year["date"]}: {year["value"]}', "=" * display_width)
  
last_10_years = response.json()[1][:10]

for year in last_10_years:
  # display_width = year["value"] 
  print(year["date"], "=", year["value"])
  # print(f'{year["date"], "=", year["value"]}')
