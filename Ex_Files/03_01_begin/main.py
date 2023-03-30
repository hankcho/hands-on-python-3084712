import csv
from datetime import datetime
from pprint import pprint


EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to theroy...",
}

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureatehank in laureates:
    if laureatehank["surname"] == "Einstein":
        pprint(laureatehank)
        print("==============================")
        year_date = datetime.strptime(laureatehank["year"], "%Y")
        born_date = datetime.strptime(laureatehank["born"], "%Y-%m-%d")
        print("age", year_date.year - born_date.year)
        print(born_date)
        break

# print()
# print(EINSTEIN)

