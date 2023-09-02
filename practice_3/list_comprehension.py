import csv
from collections import namedtuple

Book = namedtuple("Book", "name author user_rating reviews price year genre")

with open("bestsellers_with_categories.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader) # skips first row
    
    # list comprehension
    books = [Book(*row) for row in reader]

print(books)
