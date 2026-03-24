#Lab Assignment-1

"""
Create a Panda Dataframe script by reading a file "books.csv". The "books.csv" contains information regarding the books such as title, name of author, edition, publication year and publishing house, price. Create an application to perform the following operations:

a) Print the complete report of books in a Tabular form.

b) Print the list of available books of a gievn author

c) Print the list of available books of a given publishing house

d) Print the Titles of cheapest & costliest book avaialble

e) Print the list by sorting based on the year of publication
"""

import pandas as pd


df = pd.read_csv("Practical10/books.csv")

# a) 
print("\n--- Complete Books Report ---")
print(df)

# b) 
author_name = input("\nEnter author name: ")
author_books = df[df['author'] == author_name]

print(f"\n--- Books by {author_name} ---")
print(author_books)

# c) 
publisher_name = input("\nEnter publishing house name: ")
publisher_books = df[df['publishing_house'] == publisher_name]

print(f"\n--- Books from {publisher_name} ---")
print(publisher_books)

# d) 
cheapest_book = df.loc[df['price'].idxmin()]
costliest_book = df.loc[df['price'].idxmax()]

print("\n--- Cheapest Book ---")
print(cheapest_book['title'], "-", cheapest_book['price'])

print("\n--- Costliest Book ---")
print(costliest_book['title'], "-", costliest_book['price'])

# e) 
sorted_df = df.sort_values(by='publication_year')

print("\n--- Books Sorted by Publication Year ---")
print(sorted_df)