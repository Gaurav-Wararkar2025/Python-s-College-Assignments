#Lab Assignment-3
"""
a) Develop a Python program that takes a voltage (V) and resistance (R) as inputs from the user and calculates the

current (1) using Ohm's Law.

b) Modify the above program to display the nature of current:

If current 0.5 A, print "Low current"

If 0.5 A current ≤2 A, print "Normal current"

If current 2 A, print "High current
"""

voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (R): "))

current = voltage / resistance

print("Current =", current, "A")


if current < 0.5:
    print("Low current")
elif 0.5 <= current <= 2:
    print("Normal current")
else:
    print("High current")