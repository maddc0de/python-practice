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

print(volkswagens[0])
