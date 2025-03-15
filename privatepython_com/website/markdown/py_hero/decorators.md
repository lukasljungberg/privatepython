# Python Decorators

## Introduction

Python decorators are a powerful feature that allows you to modify the behavior of functions or methods without changing their actual code. They are commonly used for logging, access control, memoization, and more.

A decorator is simply a function that takes another function as an argument, extends or modifies its behavior, and returns a new function.

## Writing a Simple Decorator

A basic decorator function looks like this:

```python
# Defining a simple decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Applying the decorator
@my_decorator
def say_hello():
    print("Hello!")

# Calling the function
say_hello()
```

### Explanation:
1. The `my_decorator` function takes another function (`func`) as an argument.
2. Inside, it defines an inner function `wrapper()` that adds extra behavior before and after calling `func`.
3. It returns the `wrapper` function, which replaces the original function.
4. The `@my_decorator` syntax is a shorthand for `say_hello = my_decorator(say_hello)`.

## Using Decorators with Arguments

Sometimes, we need to pass arguments to decorators. We achieve this by defining a function that returns a decorator:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

### Explanation:
1. `repeat(n)` is a function that returns a decorator.
2. The decorator takes a function and defines a `wrapper()` that calls the function `n` times.
3. `@repeat(3)` applies the decorator with `n = 3`, so `greet("Alice")` prints "Hello, Alice!" three times.

## Using `functools.wraps` for Proper Metadata

Decorators can sometimes obscure function metadata (e.g., `__name__`, `__doc__`). To fix this, use `functools.wraps`:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def add(a, b):
    "Adds two numbers."
    return a + b

print(add.__name__)  # Output: add
print(add.__doc__)   # Output: Adds two numbers.
```

## Common Use Cases for Decorators

1. **Logging:** Automatically log function calls.
2. **Authentication:** Restrict access to certain functions.
3. **Timing Execution:** Measure execution time of functions.
4. **Caching:** Store function results for optimization.
5. **Validation:** Check arguments before executing the function.

## Conclusion

Python decorators are a useful and flexible tool for modifying function behavior. They enhance code readability and reusability by abstracting repetitive patterns.

Try writing your own decorators and using them in different scenarios to fully grasp their power!

