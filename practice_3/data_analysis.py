import pandas as pd

bestsellers = pd.read_csv("bestsellers_with_british_price.csv")
print(bestsellers)
# print(bestsellers.Name)

# remove duplicates
bestsellers = bestsellers.drop_duplicates(subset="Name", keep="last")
print(bestsellers)

# create bar chart showing the author with the most amount of bestselling titles in the given years
  # authors, number of bestselling books
number_of_bestsellers_written = bestsellers.groupby("Author")[["Name"]].count().sort_values("Name", ascending=False).head(10)

print(number_of_bestsellers_written)