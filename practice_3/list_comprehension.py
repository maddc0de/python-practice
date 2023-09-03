import csv
from collections import namedtuple

Book = namedtuple("Book", "name author user_rating reviews price year genre")

with open("bestsellers_with_categories.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader) # skips first row
    
    # list comprehension
    books = [Book(*row) for row in reader]

# create a list with all of the bestsellers from 2009 to 2012
filtered_bestsellers = [book for book in books if 2009 <= int(book.year) <= 2012]
print(f"bestsellers from 2009 to 2012 are: {filtered_bestsellers}")
