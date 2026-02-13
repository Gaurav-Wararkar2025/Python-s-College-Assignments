#Lab Assignment-1

"""
Develop a program that asks the user to enter a series of integers and store them in a Tuple.
Perform the following:

a) Print the total number of items in the Tuple.
b) Print the last item in the Tuple.
c) Print the Tuple elements in reverse order.
d) Print Yes if the Tuple contains an integer 5 and No otherwise.
e) Remove the first and last items from the Tuple, sort the remaining items, and print the result.
"""

nums = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total number of items:", len(nums))

# b) Last item
if len(nums) > 0:
    print("Last item:", nums[-1])
else:
    print("Tuple is empty")

# c) Reverse order
print("Tuple in reverse order:", nums[::-1])

# d) Check if 5 exists
if 5 in nums:
    print("Yes")
else:
    print("No")

# e) Remove first and last items, sort remaining
if len(nums) > 2:
    remaining = nums[1:-1]
    sorted_remaining = tuple(sorted(remaining))
    print("Sorted remaining items:", sorted_remaining)
else:
    print("Not enough elements to remove first and last.")
