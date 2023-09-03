import csv
from collections import namedtuple

Book = namedtuple("Book", "name author user_rating reviews price year genre")

books = [] # should be a list of tuples

with open("bestsellers_with_categories.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader) # skips first row
    for row in reader:
        # new_book = Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        new_book = Book(*row) # unpack elements of 'row' iterable
        books.append(new_book)

print(books[0])


# create a list with all of the bestsellers from 2009 to 2012
filtered_bestsellers = []

start_year = 2009
end_year = 2012

for book in books:
    if (start_year <= int(book.year) <= end_year):
      filtered_bestsellers.append(book)

print(f"bestsellers from 2009 to 2012 are: {filtered_bestsellers}")


# how expensive is the most expensive book
most_expensive_book = books[0]

for book in books:
    if (int(book.price) > int(most_expensive_book.price)):
      most_expensive_book = book

print(f"most expensive book is '{most_expensive_book.name}' with the price of £ {most_expensive_book.price}")

