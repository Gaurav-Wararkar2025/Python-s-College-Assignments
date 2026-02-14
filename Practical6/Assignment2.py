#Lab Assignment-2

"""
Design a function that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program:

Practice makes perfect

Then, the output should be: PRACTICE MAKES PERFECT
"""

def capitalize_lines():  # Function to capitalize lines
    line = input("Enter a sentence: ")
    print(line.upper())

capitalize_lines()
