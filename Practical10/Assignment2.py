#Lab Assignment-2

"""
Create a table showing information about 5 states such as:

a) Name of the state
b) Area
c) Population

Generate the following reports:

a) Print the complete information of states

b) Print the name of the State having largest Area

c) Print the name of State having largest population

d) Create a mechanism to calculate the population density of States

e) Determine the name of State with highest population density

"""

import pandas as pd

states = ["Maharashtra", "Gujarat", "Rajasthan", "Karnataka", "Tamil Nadu"]
area = [307713, 196244, 342239, 191791, 130058]
population = [124000000, 70000000, 81000000, 68000000, 78000000]

df = pd.DataFrame({
    "State": states,
    "Area": area,
    "Population": population
})

# a)
print("Complete Information of States:\n")
print(df)

# b)
largest_area_state = df.loc[df['Area'].idxmax(), 'State']
print("\nState with Largest Area:", largest_area_state)

# c)
largest_population_state = df.loc[df['Population'].idxmax(), 'State']
print("\nState with Largest Population:", largest_population_state)

# d)
df['Population Density'] = df['Population'] / df['Area']
print("\nPopulation Density of States:\n")
print(df[['State', 'Population Density']])

# e)
highest_density_state = df.loc[df['Population Density'].idxmax(), 'State']
print("\nState with Highest Population Density:", highest_density_state)