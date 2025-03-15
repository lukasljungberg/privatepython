# Python Threads

## Introduction

Threads in Python allow concurrent execution of multiple parts of a program, making it possible to perform multiple tasks at the same time. They are commonly used for tasks like handling multiple network requests, running background processes, or improving application responsiveness.

Python provides built-in support for threading using the `threading` module. However, due to the Global Interpreter Lock (GIL), Python threads are best suited for I/O-bound tasks rather than CPU-intensive ones.

## Creating and Using Threads in Python

### Creating a Simple Thread

You can create a thread by using the `threading.Thread` class and passing a function to it.

```python
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Continue executing main thread
print("Main thread continues...")

# Wait for the thread to finish
thread.join()
print("Thread has finished execution.")
```

### Explanation:
1. The `threading.Thread` class is used to create a new thread.
2. The `start()` method launches the thread and begins executing `print_numbers()` in parallel with the main thread.
3. The `join()` method ensures that the main program waits for the thread to finish execution before exiting.

## Using a Thread Class

Instead of passing a function, you can create a custom thread class by inheriting `threading.Thread`.

```python
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            print(f"Thread running: {i}")

# Create and start the thread
thread = MyThread()
thread.start()

# Wait for thread to complete
thread.join()
print("Custom thread execution completed.")
```

### Explanation:
1. A subclass of `threading.Thread` is created.
2. The `run()` method is overridden to define the thread’s behavior.
3. The thread is started using `start()` and waited for using `join()`.

## Daemon vs Non-Daemon Threads

Python threads can be daemon or non-daemon:
- **Daemon threads** run in the background and exit when the main program exits.
- **Non-daemon threads** (default) block program termination until they complete.

```python
thread = threading.Thread(target=print_numbers, daemon=True)
thread.start()
```

Setting `daemon=True` ensures that the thread will not prevent the program from exiting.

## Synchronizing Threads with Locks

When multiple threads access shared resources, synchronization is needed to prevent race conditions.

```python
lock = threading.Lock()

def critical_section():
    with lock:
        print("Thread is entering critical section")
        time.sleep(2)
        print("Thread is leaving critical section")

# Creating multiple threads
threads = [threading.Thread(target=critical_section) for _ in range(3)]

for t in threads:
    t.start()

for t in threads:
    t.join()
```

### Explanation:
1. A `Lock` is created to ensure only one thread enters the critical section at a time.
2. The `with lock:` statement automatically acquires and releases the lock.
3. Multiple threads execute safely without data corruption.

## When to Use Threads

- **I/O-bound tasks**: Ideal for tasks that involve waiting (e.g., downloading files, reading/writing to disk, network requests).
- **Background tasks**: Running periodic updates or monitoring services.
- **Concurrent processing**: Handling multiple user requests in a web server.

## When Not to Use Threads

- **CPU-bound tasks**: Due to Python's GIL, CPU-intensive tasks (e.g., heavy computations, machine learning training) do not benefit from threads. Use `multiprocessing` instead.

## Conclusion

Threads in Python enable concurrent execution of tasks, making programs more efficient for I/O-bound operations. However, proper synchronization and management are essential to avoid race conditions and ensure smooth execution.

