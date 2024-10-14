# Python Basics Demo

# This is a comment in Python
# Comments are ignored by the Python Interpreter even if they contain valid code.

# Basic Syntax: Python uses indentation (by convention, 4 spaces) to define a code block

# Variables and Data Types
# In Python, we don't need to declare a variables type. Its dynamic.
age = 25 # Integer 
name = "James" # String
height = 5.8 # Float
is_associate = True # Boolean

# Outputting to console
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is an associate?:", is_associate)

# User Input
# We can use the input() pre-built function to take in data from the console.
# Note: input() always returns a string.
user_name = input("Enter your username: ")
print("Hello, " + user_name + "!")

# Formatted Literal syntax, allows you to drop in variables to your string for outputting
# Notice the f before the opening quotation.
print(f"Hello {user_name}")

# Casting (Type conversion)
# Our input function above always returns strings, which can't be used for things like
# math operations, etc. We need to tell the interpreter to convert our string to whatever
# data type we need it to be.

# First we prompt the user for their age, using input()
user_age_str = input("Enter your age: ") # input() returns a string!
user_age_int = int(user_age_str) # Here, we cast user_age_str of type String into an Integer
print(f"In 5 years, you will be {user_age_int + 5}.") 

# Mathematical Operators 
# Arithematic Operators: +, -, *, /, %, **
a = 10
b = 3
print(a + b) #13
print(a - b) #7
print(a * b) #30
print(a / b) #3.333...
print(a % b) #1
print(a ** b) # 1000 (10^3)

# Strings and string manipulation
greeting = "Hello World!"
print(greeting)
print(greeting.upper()) # Uppercase 
print(greeting.lower()) # Lowercase
print(greeting[0:5]) # Substring - prints out my first 5 characters
print(greeting.replace("World", "Python")) # Replaces part of a string with another.

# Booleans
is_raining = False
print("Is it raining?: ", is_raining)

# Comparison Operators - Evaluate to a boolean
# >, <, ==, >=, <=, is (useful for OOP, checks if two variables refer to the same object in memory)
x = 5
y = 10

print(x > y)
print(x is x)

# Lists (Arrays)
fruit_list = ["apple", "bannana", "mango"]
print(fruit_list)
print(fruit_list[1])
fruit_list.append("orange")
print(fruit_list)
fruit_list.pop()
print(fruit_list)
fruit_list.remove("bannana")
print(fruit_list)

# Range function
# range() is often used in loops, but here we'll just see what it returns for us
numbers_list = list(range(10)) # Generate a list of integer numbers, from 0 to 9
print(numbers_list)

# Tuples are a way to store multiple items in a single variable
# Unlike lists, once created they are immutable.
coordinates = (10.0, 20.1, "pancake's house") # Tuple with two floats + a string
print(coordinates)
print(coordinates[2])

# Sets
# Sets are like lists. But they have distinct behavior. 
# Sets hold unordered collections of unique items

unique_number_set = {1, 2, 2, 2, 3, 3, 4} # Curly braces for a set instead of brackets for a list
print(unique_number_set) # Removes all duplicates, only keeps unique values

unique_number_set.add(6) # Adding to my set, again if I add something that already exists, it will be ignored.
unique_number_set.add(4)
print(unique_number_set)

# Dictionaries
# Dictionaries store key value pairs. Keys have to be unique, values do not have to be unique.
# We look up items in a dictionary via it's key.

student = {
    "name": "Dan",
    "age": 25,
    "major": "Computer Science"
}

print(student)
print(student["age"]) # 25
student["age"] = 26 # Updating a value, accessing it via key
print(student["age"]) # 26
student["gpa"] = 3.9 # Adds a new Key-Value pair
print(student)

# None or NoneType
# None in python represents the absence of a value - essentially our Null
result = None # We have declared a variable result, and given it the value None
print("The result is: ", result)

result = user_age_int
print("The result is now: ", result)