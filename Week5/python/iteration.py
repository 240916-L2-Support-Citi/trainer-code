# Iteration and Conditionals

# For Loops
# A for loop can iterate over a sequence (a list or range of numbers)

fruit_list = ["apple", "bannana", "mango"]

for fruit in fruit_list: # For loop through a sequence (list)
    print(fruit)

for i in range(3, 21): # For loop with the range function
    print(i)

# If-else
# An if-else block is used to make decisions on which code runs based 
# on a certain condition(s) being met.

student = {
    "name": "Pancake",
    "age": 25,
    "major": "Computer Science",
    "gpa" : 2.1
}

# Basic if-else
if student["major"] == "Computer Science" and student["age"] > 30:
    print("Good luck man.")
else:
    print("Maybe switch to chemical engineering? ")

# We can also have deeper decision trees via nesting.
# Generally, only nest as deep as you absolutely have to.

if student["major"] == "Computer Science":
    if student["gpa"] <= 2.5:
        print("You should probably switch majors.")
    else:
        print("You're good.")
else:
    print("Maybe switch to chemical engineering? ")


# While Loops
# A while-loop will continue as long as a condition remains true

# Simple count-down while loop
count = 10

while count > 0:
    print(count)
    count -= 1 # This is equivilant to count = count - 1. Its just a nice shorthand.



# We can use break to exit a while loop 

while True:
    user_response = input("Enter 'exit' to stop loop: ")
    if user_response == "exit":
        print("Exiting our loop.")
        break # This will exit our while loop

#For loops with an if-else in it
for number in range(1 , 11): # Numbers 1 - 10
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")