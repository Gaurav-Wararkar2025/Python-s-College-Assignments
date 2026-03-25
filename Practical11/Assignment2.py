#Lab Assignment-2

"""
Import a dataset of new recruitments in companies such as Microsoft, Google, Amazon, IBM, Deliotte, Capmemini, ATOS Origin, Amdocs etc.

Generate & visualize reports of new recruitments using:

a) Bar Chart

b) Pie Chart

c) Customize Pie Chart

d) Doughnut Chart

Compare the new recruitments in IBM & Amdocs using visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Company": ["Microsoft", "Google", "Amazon", "IBM", "Deloitte", "Capgemini", "ATOS", "Amdocs"],
    "Recruitments": [120, 150, 180, 90, 110, 130, 80, 70]
}

df = pd.DataFrame(data)

# a) Bar Chart
plt.figure()
plt.bar(df['Company'], df['Recruitments'])
plt.title("New Recruitments by Company")
plt.xlabel("Company")
plt.ylabel("Number of Recruitments")
plt.xticks(rotation=30)
plt.show()

# b) Pie Chart
plt.figure()
plt.pie(df['Recruitments'], labels=df['Company'], autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
plt.figure()
explode = [0, 0, 0, 0.1, 0, 0, 0, 0.1]
plt.pie(df['Recruitments'], labels=df['Company'], autopct='%1.1f%%', explode=explode, shadow=True)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.figure()
wedges, texts, autotexts = plt.pie(df['Recruitments'], labels=df['Company'], autopct='%1.1f%%')
centre_circle = plt.Circle((0, 0), 0.70)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# Comparison IBM vs Amdocs
plt.figure()
comp = df[df['Company'].isin(['IBM', 'Amdocs'])]
plt.bar(comp['Company'], comp['Recruitments'])
plt.title("IBM vs Amdocs Recruitment Comparison")
plt.xlabel("Company")
plt.ylabel("Recruitments")
plt.show()
