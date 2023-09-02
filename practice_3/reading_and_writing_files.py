import csv
from collections import namedtuple

Book = namedtuple("Book", "name author user_rating reviews price year genre")

books = []

with open("bestsellers_with_categories.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader) # skips first row
    for row in reader:
        # new_book = Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        new_book = Book(*row) # unpack elements of 'row' iterable
        books.append(new_book)

print(books[0])
