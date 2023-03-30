import csv
import json
from pprint import pprint


# 1. you can access parts of strings the same way you do lists
# hey[2] == "y"
# 2. you can add to a list using
#     my_list.append("something")

laureates_beginning_with_a = []

with open("laureates.csv", "r") as f:
    file_reader = csv.DictReader(f)
    laureates = list(file_reader)

for a in laureates:
    if a['name'][0] == "A":
      laureates_beginning_with_a.append(a)    
    
with open("laureates_A.json", "w") as f:
    json.dump(laureates_beginning_with_a, f, indent=2)

pprint(laureates_beginning_with_a)
# pprint(laureates)

