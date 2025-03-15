# Python Syntax Guide

## 1. Variables & Data Types
Variables store data of different types. Python supports integers, floats, strings, booleans, lists, and dictionaries.
```python
x = 10  # Integer
y = 3.14  # Float
name = "Python"  # String
is_active = True  # Boolean
fruits = ["apple", "banana", "cherry"]  # List
details = {"name": "Alice", "age": 25}  # Dictionary
```

## 2. Operators
Operators perform operations on variables and values. Python supports arithmetic, comparison, and logical operators.
```python
# Arithmetic Operators
sum = 5 + 3  # Addition
product = 5 * 3  # Multiplication
power = 2 ** 3  # Exponentiation

# Comparison Operators
print(5 > 3)  # True
print(5 == 5)  # True

# Logical Operators
print(True and False)  # False
print(True or False)  # True
```

## 3. Conditional Statements
Conditional statements (`if`, `elif`, `else`) allow decision-making in programs.
```python
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

## 4. Loops
Loops are used to execute a block of code multiple times. Python supports `for` and `while` loops.
```python
# For Loop
for i in range(5):
    print(i)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1
```

## 5. Functions
Functions encapsulate reusable logic. They are defined using `def`.
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

## 6. Classes & Objects
Python supports object-oriented programming with classes and objects.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}!"

p = Person("Alice", 25)
print(p.greet())
```

## 7. Exception Handling
Exception handling is used to catch and handle runtime errors.
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## 8. File Handling
Python allows reading and writing files using the `open` function.
```python
with open("file.txt", "w") as file:
    file.write("Hello, world!")
```

## 9. List Comprehensions
List comprehensions provide a concise way to create lists.
```python
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

## 10. Lambda Functions
Lambda functions are anonymous, single-expression functions.
```python
add = lambda a, b: a + b
print(add(3, 5))  # 8
```

## 11. Modules & Imports
Modules allow code organization and reuse. They can be imported using `import`.
```python
import math
print(math.sqrt(16))  # 4.0
```

## 12. Decorators
Decorators modify the behavior of functions or methods.
```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
```

## 13. Generators
Generators are functions that yield values one at a time using `yield`.
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)
```

## 14. Threading
Threading allows concurrent execution of code.
```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
```

## 15. Asynchronous Programming
Asynchronous programming allows non-blocking execution using `async` and `await`.
```python
import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello!")

asyncio.run(say_hello())
```

