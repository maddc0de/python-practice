import pandas as pd
import matplotlib.pyplot as plt

bestsellers = pd.read_csv("bestsellers_with_british_price.csv")
# print(bestsellers.Name)

# remove duplicates
bestsellers = bestsellers.drop_duplicates(subset="Name", keep="last")
print(bestsellers)

# create bar chart showing the author with the most amount of bestselling titles in the given years
  # compare authors with how many number of bestselling books they have
number_of_bestsellers_written = bestsellers.groupby("Author")[["Name"]].count().sort_values("Name", ascending=False).head(10).reset_index()
print(number_of_bestsellers_written)

  # create bar chart
plt.bar(number_of_bestsellers_written.Author, number_of_bestsellers_written.Name, color="blue", width=0.4)
plt.show()