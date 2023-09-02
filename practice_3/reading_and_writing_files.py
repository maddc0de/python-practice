import csv

books = []

with open("bestsellers_with_categories.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader) # skips first row
    for row in reader: # create dictionary from every row
        new_book = {}
        new_book["name"] = row[0]
        new_book["author"] = row[1]
        new_book["user_rating"] = row[2]
        new_book["reviews"] = row[3]
        new_book["price"] = row[4]
        new_book["year"] = row[5]
        new_book["genre"] = row[6]

        books.append(new_book)

print(books[0])
