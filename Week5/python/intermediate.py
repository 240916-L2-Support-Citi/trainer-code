import json # Prebuilt library for working with JSON
import re # Prebuilt library for working with Regular Expressions

# Namespaces and Scope

global_string = "I am a globally scoped variable." # Global Scope

# Here we define a function in python using the def keyword. 
def outer_function():
    outer_string = "Greetings from my outer function" # Enclosing Scope
    print(outer_string)

    def inner_function():
        inner_string = "This is inside my inner_function" # Local Scope
        print(outer_string)
        print(global_string)
        print(inner_string)

    inner_function()

outer_function()

# Here we will write a function that takes arguments and returns something
def exponent(x, y):

    result = x ** y
    # Using the return keyword to return something when our function is called
    return result

exp_return = exponent(10, 100)
print(exp_return)

# Classes and objects

class Person:

    # This would be a class variable. It is shared amongst ALL instances of this class.
    # Any Person object we create, will have a species variable set to Homo sapiens
    species = "Homo sapiens"

    # Constructor in python is a function called __init__. This is what initializes our object.
    # A python constructor must always include atleast one argument, self
    def __init__(self, name_from_init, age_from_init):
        #Instance variables
        self.name = name_from_init # After we declare the instance variables, we have to take in a value 
        self.age = age_from_init # as an argument from our __init__ function. 

    # Instance method
    def introduce(self): # THis method returns a string with info on our Person object
        return f"My name is {self.name} and I am {self.age} years old."
    
    # Static method - We use the @staticmethod flag to denote a method that belongs to the class itself,
    # not individual objects created of that class.
    @staticmethod
    def talk():
        print("Talking from my static method that belongs to the Person class")

# Calling a static method requires invoking the class itself, not any individual object of that class.
Person.talk() 

# Calling an instance method requires an object of that class, and "belongs" to that object. 
greg = Person("Gregory",29)

print(greg.introduce())

# Inheritance - Python allows for multiple inhertiance... stick to single inheritance unless you find a really
# really really specific usecase for it. 

# To inherit from a class, simply put it into the parenthesis after the class name... almost like 
# taking an argument into a function.
class Employee(Person):

    # Here we define the Employee class constructor... it looks a little different from Person
    def __init__(self, name, age, employee_id):
        # Calling the parent class (in this case, Person) constructor
        # We call the parent classes __init__() constructor using super()
        super().__init__(name, age)

        # This instance variable belongs to Employee only, Person objects will not contain it
        self.employee_id = employee_id

    # Overriding our introduce method, so that when an employee object calls this method, we get
    # this behavior and not the behavior from the parent class.
    def introduce(self):
        return f"My name is {self.name} and my employee id number is: {self.employee_id}"

miguel = Employee("Miguel", 75, 123456789)

print(miguel.introduce())

# Lamdas - Anonymous Functions

# Creating a list of numbers to show off our lambda
numbers = [1,2,3,4]

# Using the map() function
                            # Here we use a lambda to statisfy the map functions
                            # we use the lambda keyword, and then provide a list of arguments similar to any other 
                            # function. 
squared_numbers = list(map(lambda x: x**2, numbers))

# lambda syntax
# lambda arg1, arg2...: code-for-function-definition

# Lambdas can be powerful but they have some drawbacks, namely they can be hard to understand when reading code,
# and they don't allow for code-reuse in other places. 

print(numbers)
print(squared_numbers)


# JSON in Python
pet_dictionary = {
    "name": "pancake",
    "age": 10,
    "color": "white",
    "toys": {
        "toy1": "ball",
        "toy2": "squeaky toy"
    }
}

# Using json.dumps to serialize a dictionary into json format
pet_json = json.dumps(pet_dictionary)
print(pet_json)

# If you need to serialize something that is an object but not a dictionary, call the objects prebuilt __dict__ attribute.
# print(json.dumps(miguel.__dict__)) # This tells the interpreter to convert the miguel object to a dictionary for us

# Storing the miguel json 
miguel_json = json.dumps(miguel.__dict__)

# Using json.loads() to go from json back into a python dictonary
miguel_2_dictionary = json.loads(miguel_json)
print(miguel_2_dictionary)

# Regex (Regular Expressions)
# We can leverage regex to do fast pattern matching in strings
# We can do things like verify that someones phone number matches a certain format
# Verify that something conforms to being a valid email address
# and so on.

site_text = "Contact us at our.info@mycompany.org or support@mywebsite.com or Info.health@us.gov"

# Creating a pattern to look for anything that is an email address in a string. 
# Im going to use an r or raw string literal to avoid any issues with special characters or sequences
# This lets us avoid dealing with things like \n in our pattern string
email_pattern = r"\b[A-Za-z0-9.]+@[A-Za-z0-9]+.[A-Za-z]{3}\b"

# Lets actualy filter our site_text based on that pattern
emails = re.findall(email_pattern, site_text)

print(f"Email addresses found: {emails}")

