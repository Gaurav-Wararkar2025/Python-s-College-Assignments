#Lab Assignment-2

"""
Develop an application using file handling to copy the contents of python script into another 
without including the comments. Ask the user about the source and destination file names. Print 
the content of the both the files.
"""

def copy_without_comments():
    source = input("Enter source python file (e.g., script.py): ")
    destination = input("Enter destination file (e.g., cleaned.py): ")

    try:
        with open(source, 'r') as src:
            lines = src.readlines()

        cleaned_lines = [line for line in lines if not line.strip().startswith('#')]

        with open(destination, 'w') as dest:
            dest.writelines(cleaned_lines)

        print("\n--- Source File Content ---")
        with open(source, 'r') as src:
            print(src.read())

        print("\n--- Destination File Content (No Comments) ---")
        with open(destination, 'r') as dest:
            print(dest.read())

    except FileNotFoundError:
        print("Error: One of the files could not be found.")

copy_without_comments()