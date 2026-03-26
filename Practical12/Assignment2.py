#Lab Assignment-2

"""
2. Create a program that reads "employee.xlsx" file of Infosys Software Solutions which includes columns such as Employee ID, Employee Name, Depatment, Designation etc. Construct a program to print the following reports:

a) Print the list of employees working for "Automotive" domain.

b) Print the details of an employee with employee ID given by an end user.

d) Print the list of all the Developers of Infosys.
"""

import pandas as pd

df = pd.read_excel("Practical12/employee.xlsx")

# a)
print(df[df['Department'] == "Automotive"])

# b)
eid = int(input("Enter Employee ID: "))
print(df[df['Employee ID'] == eid])

# d)
print(df[df['Designation'] == "Developer"])