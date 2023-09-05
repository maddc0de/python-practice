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

# convert prices from us dollars to british pounds
modified_books = []

for book in books:
    british_price_book = Book(
        book.name, 
        book.author, 
        book.user_rating, 
        book.reviews, 
        float(book.price) * 0.80, 
        book.year, 
        book.genre
        )
    modified_books.append(british_price_book)

# create and write into a new file the modified_books information
with open("bestsellers_with_british_price.csv", "w", encoding="utf-8", newline='') as british_csvfile:
    writer = csv.writer(british_csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(Book("Name", "Author", "User Rating", "Reviews", "Price", "Year", "Genre"))
    for book in modified_books:
        writer.writerow(book)
