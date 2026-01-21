# Lab Assignment 2

"""
Construct a program to store the following details of a Vendor of a Shop

a) Name of vendor

b) Year of association

c) Contact number

d) eMail ID

Read the details of monthly purchases from Vendor and generate a Annual Purchase/Billing report
"""

# Input vendor details
vendor_name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

monthly_purchases = []

# Input monthly purchase details
print("\nEnter monthly purchase amount:")
for i in range(1, 13):
    amount = float(input(f"Month {i}: "))
    monthly_purchases.append(amount)

# Calculate annual purchase
annual_total = sum(monthly_purchases)

# Display report
print("\n--- Vendor Annual Purchase Report ---")
print("Vendor Name:", vendor_name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)

print("\nMonthly Purchases:")
for i, amount in enumerate(monthly_purchases, start=1):
    print(f"Month {i}: Rs.{amount}")

print("\nTotal Annual Purchase: Rs.", annual_total)