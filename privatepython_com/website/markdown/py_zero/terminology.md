# Programming Basics - Terminology Guide

## Introduction
This document introduces fundamental programming terminology that is essential for beginners. Understanding these terms will help you navigate the world of coding more effectively.

## Basic Terminology

### 1. **Variable**
A variable is a named storage location in memory that holds a value.
```python
x = 10  # 'x' is a variable storing the value 10
```

### 2. **Data Type**
A classification that specifies which type of value a variable can hold (e.g., integers, strings, floats, booleans).
```python
name = "Alice"  # String
temperature = 36.5  # Float
is_raining = False  # Boolean
```

### 3. **Function**
A block of reusable code that performs a specific task.
```python
def greet():
    print("Hello, World!")
```

### 4. **Loop**
A construct that repeats a block of code multiple times.
```python
for i in range(5):
    print(i)  # Prints numbers 0 to 4
```

### 5. **Conditional Statement**
A statement that controls the flow of execution based on conditions.
```python
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### 6. **Array/List**
A collection of elements stored in a single variable.
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Outputs 'apple'
```

### 7. **Class and Object**
A class is a blueprint for creating objects, and an object is an instance of a class.
```python
class Car:
    def __init__(self, brand):
        self.brand = brand

my_car = Car("Toyota")
print(my_car.brand)  # Outputs 'Toyota'
```

### 8. **Module/Library**
A file or collection of files that contain reusable code.
```python
import math
print(math.sqrt(16))  # Outputs 4.0
```

### 9. **Exception Handling**
A mechanism to handle runtime errors gracefully.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### 10. **Algorithm**
A step-by-step procedure to solve a problem.

### 11. **Syntax**
The set of rules that define the structure of a programming language.

### 12. **Compiler & Interpreter**
A compiler converts code into machine language before execution, while an interpreter translates code line by line during execution.

## Conclusion
This guide provides a fundamental understanding of common programming terms. Familiarizing yourself with these concepts will make learning programming easier and more effective.
