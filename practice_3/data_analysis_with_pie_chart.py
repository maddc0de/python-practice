import pandas as pd
import matplotlib.pyplot as plt

bestsellers = pd.read_csv("bestsellers_with_british_price.csv")

# remove duplicates
bestsellers = bestsellers.drop_duplicates(subset="Name", keep="last")
print(bestsellers)

# create pie chart showing the distribution between fiction and non-fiction books
number_of_books_by_genre = bestsellers.groupby("Genre")[["Name"]].count().reset_index()

print(number_of_books_by_genre)

plt.pie(number_of_books_by_genre.Name, labels=number_of_books_by_genre.Genre, autopct='%1.1f%%')
plt.show()