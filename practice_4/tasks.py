import csv
from collections import namedtuple

# turn csv file into a list of namedtuples
Vw = namedtuple("Vw", "model year price transmission mileage fuelType tax mpg engineSize")
volkswagens = []

with open("volkswagen_uk.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)
    for row in reader:
        volkswagen = Vw(*row)
        volkswagens.append(volkswagen)


# print most expensive Volkswagen car listed
most_expensive_volkswagen = volkswagens[0]

for vw in volkswagens:
    if (int(vw.price) > int(most_expensive_volkswagen.price)):
        most_expensive_volkswagen = vw

print(f"most expensive VW car listed is {most_expensive_volkswagen}")


# print the average price of all VW Golf models
all_golf_vw_prices = []

for vw in volkswagens:
    if (vw.model == "Golf"):
        all_golf_vw_prices.append(int(vw.price))

golf_average_price = sum(all_golf_vw_prices) / len(all_golf_vw_prices)
print(round(golf_average_price, 2))