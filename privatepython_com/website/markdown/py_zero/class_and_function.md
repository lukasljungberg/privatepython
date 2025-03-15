# Python Classes and Functions Guide

Python allows you to organize code using **functions** and **classes**. Functions group reusable logic, while classes enable object-oriented programming.

## 1. Functions
Functions are reusable blocks of code that perform specific tasks. They are defined using the `def` keyword.

### Function Syntax
```python
def function_name(parameters):
    """Docstring explaining the function."""
    # Function body
    return value  # Optional
```

### Example: Simple Function
```python
def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

### Function Parameters & Return Values
- **Positional Arguments**: Passed in order.
- **Keyword Arguments**: Specified by name.
- **Default Arguments**: Provide a default value.
- **Variable-Length Arguments**: Accept multiple arguments (`*args`, `**kwargs`).

```python
def add(a, b=10):
    """Adds two numbers with a default value for b."""
    return a + b

print(add(5))  # Output: 15
print(add(5, 7))  # Output: 12
```

### Lambda Functions (Anonymous Functions)
Lambda functions are single-expression functions.
```python
square = lambda x: x ** 2
print(square(4))  # Output: 16
```

## 2. Classes
Classes define objects with attributes (variables) and methods (functions).

### Class Syntax
```python
class ClassName:
    def __init__(self, parameters):
        """Constructor method to initialize attributes."""
        self.attribute = value

    def method(self):
        """Defines behavior for the class."""
        return self.attribute
```

### Example: Creating a Class & Object
```python
class Person:
    """Represents a person with a name and age."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 25)
print(person1.introduce())  # Output: My name is Alice and I am 25 years old.
```

### Inheritance (Extending Classes)
A class can inherit from another class to reuse functionality.
```python
class Student(Person):
    """Represents a student, inheriting from Person."""
    def __init__(self, name, age, major):
        super().__init__(name, age)  # Call parent constructor
        self.major = major

    def introduce(self):
        return super().introduce() + f" I study {self.major}."

student1 = Student("Bob", 20, "Computer Science")
print(student1.introduce())  # Output: My name is Bob and I am 20 years old. I study Computer Science.
```

## 3. Class vs. Instance Variables
- **Instance Variables**: Unique to each object (`self.name`).
- **Class Variables**: Shared across all instances (`class_variable`).

```python
class Counter:
    count = 0  # Class variable

    def __init__(self):
        Counter.count += 1  # Increment class variable

print(Counter.count)  # Output: 0
c1 = Counter()
c2 = Counter()
print(Counter.count)  # Output: 2
```