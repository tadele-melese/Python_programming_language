# Basics of python
# Variables and Data Types
x = 5                   # integer
y = 3.14                # float
name = "John"           # string
is_student = True       # boolean

# Lists
my_list = [1, 2, 3, 4]                  # list
mixed_list = [1, "hello", True, 3.14]   # mixed data types in a list

# Dictionaries
my_dict = {'name': 'John', 'age': 30}   # dictionary
# If statement
x = 10
if x > 5:
    print("x is greater than 5")

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
# Function definition
def greet(name):
    print("Hello, " + name + "!")
    
# Function call
greet("Alice")
# Class definition
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print("Driving", self.brand, self.model)

# Object instantiation
my_car = Car("Toyota", "Camry")
my_car.drive()
# Input from user
name = input("Enter your name: ")
print("Hello,", name)

# Output to console
age = 25
print("You are", age, "years old.")
