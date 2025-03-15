# Python Data Types Guide

Python provides several built-in data types to store different kinds of values. Below is an explanation of each data type along with examples.

## 1. Numeric Types
Python supports three types of numeric values: integers, floats, and complex numbers.

### Integer (`int`)
Stores whole numbers, positive or negative.
```python
x = 10  # Integer
print(type(x))  # <class 'int'>
```

### Float (`float`)
Stores decimal numbers.
```python
y = 3.14  # Float
print(type(y))  # <class 'float'>
```

### Complex (`complex`)
Stores complex numbers with a real and imaginary part.
```python
z = 2 + 3j  # Complex number
print(type(z))  # <class 'complex'>
```

## 2. Sequence Types
These data types store ordered collections of items.

### String (`str`)
Stores a sequence of characters.
```python
text = "Hello, Python!"  # String
print(type(text))  # <class 'str'>
```

### List (`list`)
A mutable collection of ordered elements.
```python
fruits = ["apple", "banana", "cherry"]  # List
print(type(fruits))  # <class 'list'>
```

### Tuple (`tuple`)
An immutable collection of ordered elements.
```python
coordinates = (10, 20)  # Tuple
print(type(coordinates))  # <class 'tuple'>
```

## 3. Set Types
Unordered collections of unique elements.

### Set (`set`)
A collection of unique and unordered elements.
```python
unique_numbers = {1, 2, 3, 3}  # Set
print(type(unique_numbers))  # <class 'set'>
```

### Frozen Set (`frozenset`)
An immutable version of a set.
```python
frozen_numbers = frozenset({1, 2, 3})  # Frozen set
print(type(frozen_numbers))  # <class 'frozenset'>
```

## 4. Mapping Type
Maps keys to values.

### Dictionary (`dict`)
A key-value pair collection.
```python
person = {"name": "Alice", "age": 25}  # Dictionary
print(type(person))  # <class 'dict'>
```

## 5. Boolean Type
Stores `True` or `False` values.
```python
is_active = True  # Boolean
print(type(is_active))  # <class 'bool'>
```

## 6. Binary Types
Used to store binary data.

### Bytes (`bytes`)
Immutable sequence of bytes.
```python
b = b"Hello"  # Bytes
print(type(b))  # <class 'bytes'>
```

### Bytearray (`bytearray`)
Mutable sequence of bytes.
```python
ba = bytearray(5)  # Bytearray
print(type(ba))  # <class 'bytearray'>
```

### Memoryview (`memoryview`)
A memory-efficient way to access binary data.
```python
mv = memoryview(b"Hello")  # Memoryview
print(type(mv))  # <class 'memoryview'>
```