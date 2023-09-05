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
vw_golf_prices = []

for vw in volkswagens:
    if (vw.model == "Golf"):
        vw_golf_prices.append(int(vw.price))

golf_average_price = sum(vw_golf_prices) / len(vw_golf_prices)

print(f"average price of all VW Golf models is {round(golf_average_price, 2)}")


# find average milage for VW Polo models registered in 2020
vw_polo_2020_mileages = []

for vw in volkswagens:
    if (vw.model == "Polo" and vw.year == "2020"):
        vw_polo_2020_mileages.append(int(vw.mileage))

polo_average_mileage = sum(vw_polo_2020_mileages) / len(vw_polo_2020_mileages)

print(f"average milage for VW Polo models registered in 2020 is {round(polo_average_mileage)}")