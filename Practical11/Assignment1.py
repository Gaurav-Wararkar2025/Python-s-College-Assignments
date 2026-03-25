#Lab Assignment-1

"""
Import sales data of a Cosmetic Company. Analyze it through following ways with visualization using

Matplotlib:

a) Read the total profit of all the months and visualize it using a Line Plot.

b) Read all product sales data and show it using a Multiline Plot.

c) Read face cream and face wash product sales data and show it using the Bar chart.

d) Calculate total sale data for last year for each product and show it using a Pie chart.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Practical11/sales_data.csv")

# a)
profitList = df['total_profit']
monthList = df['month_number']

plt.plot(monthList, profitList)
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.grid()
plt.show()

# b)
plt.plot(monthList, df['facecream'], label='Face Cream')
plt.plot(monthList, df['facewash'], label='Face Wash')
plt.plot(monthList, df['toothpaste'], label='Toothpaste')
plt.plot(monthList, df['bathingsoap'], label='Bathing Soap')
plt.plot(monthList, df['shampoo'], label='Shampoo')
plt.plot(monthList, df['moisturizer'], label='Moisturizer')

plt.title("Sales Data of All Products")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()

# c)
plt.bar(monthList, df['facecream'], label='Face Cream')
plt.bar(monthList, df['facewash'], label='Face Wash')

plt.title("Face Cream and Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# d)
sales_data = [
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum(),
    df['moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.pie(sales_data, labels=labels, autopct='%1.1f%%')
plt.title("Total Sales per Product (Yearly)")
plt.show()