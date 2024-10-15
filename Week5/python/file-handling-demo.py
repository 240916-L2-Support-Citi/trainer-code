# In order to work with files on our file-system from within Python
# We need to import os
import os # Importing the os library, that gives us access to operating system utils,  
          # such as reading/writing/creating/deleting files on our machine.

fileName = "./logs/example.txt" # Here Im storing a file name or path, for the file we'll work with.

#String variable to hold what I want to insert into my file.
content = "This is what will eventually be put into my file.\nLets see how the previous character affects my file."

# The string below is what I expect by file to look lile.
# This is what will eventually be put into my file.
# Lets see how the previous character affects my file.

# Part 1: Creating/Writing to the file
with open(fileName, 'w') as file: # Note that 'w' essentially erases any previous contents, and writes the provided new content.
    file.write(content) # If we want to append to the file, and preserve previous entries, use 'a'
print(f"Content succesfully written to {fileName}")

# Part 2: Reading from the file
if os.path.exists(fileName):
    with open(fileName, 'r') as file: # We use 'r' to open a file and read from it.
        existing_contents = file.read()
        print(existing_contents)
else: 
    print(f"{fileName} not found.")

# Part 3: Deleting our file

if os.path.exists(fileName): # If the file does exist....
    os.remove(fileName) # Go ahead and delete it. 
    print(f"{fileName} has been deleted.")
else: 
    print(f"{fileName} not found.")

# Part 4: Reading from the file... AFTER deletion
if os.path.exists(fileName):
    with open(fileName, 'r') as file: # We use 'r' to open a file and read from it.
        existing_contents = file.read()
        print(existing_contents)
else: 
    print(f"{fileName} not found.")