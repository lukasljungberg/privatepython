# Python Standard Library Modules

## 1. `sys` - System-specific parameters and functions

### Description
The `sys` module provides access to system-specific parameters and functions, including command-line arguments and environment information.

### Basic Usage
```python
import sys
print(sys.version)  # Get Python version
print(sys.argv)  # Command-line arguments
```

---
## 2. `os` - Interact with the Operating System

### Description
The `os` module allows interaction with the operating system, such as working with files, directories, and environment variables.

### Basic Usage
```python
import os
print(os.name)  # OS name
print(os.environ.get('HOME'))  # Get environment variable
```

---
## 3. `time` - Time-related Functions

### Description
The `time` module provides functions for working with time, including sleep and getting the current time.

### Basic Usage
```python
import time
print(time.time())  # Current timestamp
print(time.ctime())  # Readable current time
```

---
## 4. `datetime` - Date and Time Manipulation

### Description
The `datetime` module provides classes for manipulating dates and times.

### Basic Usage
```python
from datetime import datetime
print(datetime.now())  # Current date and time
```

---
## 5. `math` - Mathematical Functions

### Description
The `math` module provides mathematical functions such as logarithms, trigonometry, and rounding.

### Basic Usage
```python
import math
print(math.sqrt(16))  # Square root
print(math.pi)  # PI value
```

---
## 6. `random` - Generate Random Numbers

### Description
The `random` module provides functions to generate random numbers and selections.

### Basic Usage
```python
import random
print(random.randint(1, 10))  # Random integer
print(random.choice(['apple', 'banana', 'cherry']))  # Random choice
```

---
## 7. `re` - Regular Expressions

### Description
The `re` module provides functions for pattern matching using regular expressions.

### Basic Usage
```python
import re
pattern = r'\d+'
match = re.search(pattern, 'My number is 1234')
print(match.group())  # Output: 1234
```

---
## 8. `collections` - Specialized Container Data Types

### Description
The `collections` module provides specialized data structures like `Counter`, `deque`, and `defaultdict`.

### Basic Usage
```python
from collections import Counter
data = Counter("banana")
print(data)  # Count occurrences
```

---
## 9. `itertools` - Functions for Working with Iterators

### Description
The `itertools` module provides tools for working with iterators efficiently.

### Basic Usage
```python
import itertools
for item in itertools.permutations([1, 2, 3]):
    print(item)
```

---
## 10. `functools` - Higher-Order Functions

### Description
The `functools` module provides functions like `reduce` and `lru_cache` for functional programming.

### Basic Usage
```python
from functools import lru_cache
@lru_cache
def factorial(n):
    return n * factorial(n-1) if n else 1
print(factorial(5))
```

---
## 11. `operator` - Functional Operators

### Description
The `operator` module provides efficient functions like `itemgetter` and `attrgetter` for working with data.

### Basic Usage
```python
from operator import itemgetter
data = [(1, 'a'), (3, 'c'), (2, 'b')]
sorted_data = sorted(data, key=itemgetter(0))
print(sorted_data)
```

---
## File and Directory Handling Modules

### 12. `os.path` - Work with File Paths
```python
import os
print(os.path.join("folder", "file.txt"))  # Create path
```

### 13. `shutil` - High-Level File Operations
```python
import shutil
shutil.copy("source.txt", "destination.txt")  # Copy file
```

### 14. `pathlib` - Object-Oriented File Paths
```python
from pathlib import Path
p = Path("example.txt")
print(p.exists())  # Check if file exists
```

### 15. `glob` - Pattern-Based File Searching
```python
import glob
print(glob.glob("*.py"))  # List all Python files
```

### 16. `fnmatch` - Unix-Style Filename Matching
```python
import fnmatch
print(fnmatch.fnmatch("data.txt", "*.txt"))  # True
```

