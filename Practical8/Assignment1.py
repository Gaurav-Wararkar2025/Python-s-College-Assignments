#Lab Assignment-1

"""
a) Construct a program that reads a text file and writes its contents into a new text 
file with the same content, but in uppercase.
"""

def convert_to_uppercase(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            content = src.read()
            dest.write(content.upper())
        print(f"Successfully converted {source_file} to uppercase in {destination_file}")
    except FileNotFoundError:
        print("The source file was not found.")

convert_to_uppercase('input.txt', 'output.txt')