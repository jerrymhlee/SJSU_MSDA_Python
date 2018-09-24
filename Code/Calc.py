##### Lecture1: implement calculation functions in this program ####

# import libraries at the top
import math

# define functions
def add (num1, num2):
    return num1 + num2

def subtract (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

def disk_area(radius):
    return math.pi * radius ** 2

# Start main function here
## demo: add and divide
a = int(input("Please enter the first number: "))
b = int(input("Please enter the first number: "))
print("The result of adding", a, "with", b, "is", add(a,b))
print("The result of dividing", a, "by", b, "is", divide(a,b))

## demo: calculate disk area
print(disk_area(float(input("Please input radius: "))))
