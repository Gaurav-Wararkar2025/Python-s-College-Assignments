#Lab Assignment-1

"""
Develop an application which asks the user to enter a string and prints its statistics as:

a) Number of Vowels
b) Number of Consonants
c) Number of Spaces
d) Number of Lowercase Letters
"""

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
space_count = 0
lowercase_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1
    elif ch.isalpha():  # Checks if character is alphabet
        consonant_count += 1
    
    if ch == " ":
        space_count += 1
    
    if ch.islower():
        lowercase_count += 1

print("Number of Vowels:", vowel_count)
print("Number of Consonants:", consonant_count)
print("Number of Spaces:", space_count)
print("Number of Lowercase Letters:", lowercase_count)
