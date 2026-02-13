#Lab Assignment-1

"""
Create a program to store the Prices of sold items on a particular day of a shop in a Tuple.
Perform the following operations:

a) Print the total number of items sold
b) Print the price of cheapest item sold
c) Print the price of costliest item sold
d) Print the price list in ascending order
e) Print the number of costliest items sold on the day
"""

prices = tuple(map(float, input("Enter prices separated by space: ").split()))

# a) Total number of items sold
print("Total items sold:", len(prices))

if len(prices) > 0:
    # b) Cheapest item
    cheapest = min(prices)
    print("Cheapest item price:", cheapest)

    # c) Costliest item
    costliest = max(prices)
    print("Costliest item price:", costliest)

    # d) Ascending order
    print("Prices in ascending order:", tuple(sorted(prices)))

    # e) Number of costliest items sold
    count_costliest = prices.count(costliest)
    print("Number of costliest items sold:", count_costliest)

else:
    print("No items sold.")
