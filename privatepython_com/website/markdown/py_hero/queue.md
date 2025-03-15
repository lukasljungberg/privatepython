# Python Queue

## Introduction

A **Queue** is a data structure that follows the **First In, First Out (FIFO)** principle. Python provides a built-in `queue` module that offers different types of queues for multi-threaded and multiprocessing applications. Queues are widely used for task scheduling, producer-consumer problems, and managing shared data between threads or processes.

## Types of Queues in Python

Python’s `queue` module provides three types of queues:
1. **Queue (FIFO - First In, First Out)**
2. **LifoQueue (LIFO - Last In, First Out, like a stack)**
3. **PriorityQueue (elements are sorted by priority)**

## Using a Simple FIFO Queue

The `Queue` class in the `queue` module implements a thread-safe FIFO queue.

```python
import queue

# Create a FIFO queue
q = queue.Queue()

# Add items to the queue
q.put("Task 1")
q.put("Task 2")
q.put("Task 3")

# Retrieve items from the queue
while not q.empty():
    item = q.get()
    print("Processing:", item)
    q.task_done()  # Marks task as complete
```

### Explanation:
1. `put()` adds an item to the queue.
2. `get()` retrieves and removes an item from the queue.
3. `task_done()` signals that a task has been processed.
4. The loop continues until the queue is empty.

## Using LIFO Queue (Stack Behavior)

A **LIFO queue** retrieves the most recently added item first, behaving like a stack.

```python
import queue

lifo_q = queue.LifoQueue()
lifo_q.put("First")
lifo_q.put("Second")
lifo_q.put("Third")

while not lifo_q.empty():
    print("Processing:", lifo_q.get())
```

### Output:
```
Processing: Third
Processing: Second
Processing: First
```

## Using a Priority Queue

A **PriorityQueue** retrieves elements in order of priority (smallest value first).

```python
import queue

pq = queue.PriorityQueue()
pq.put((2, "Task 2"))
pq.put((1, "Task 1"))
pq.put((3, "Task 3"))

while not pq.empty():
    priority, task = pq.get()
    print("Processing:", task)
```

### Output:
```
Processing: Task 1
Processing: Task 2
Processing: Task 3
```

### Explanation:
1. Each element in the PriorityQueue is a tuple `(priority, item)`.
2. Items are processed based on priority (smallest value first).

## Using Queues in Multi-threading (Producer-Consumer Model)

Queues are essential in multi-threading to avoid race conditions and ensure thread safety.

```python
import queue
import threading
import time

def producer(q):
    for i in range(5):
        time.sleep(1)
        q.put(f"Task {i}")
        print(f"Produced Task {i}")

def consumer(q):
    while True:
        task = q.get()
        if task is None:
            break
        print(f"Consumed {task}")
        q.task_done()

q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # Stop signal for the consumer
consumer_thread.join()
```

### Explanation:
1. The **producer** generates tasks and adds them to the queue.
2. The **consumer** processes tasks from the queue.
3. The queue ensures safe communication between threads.
4. The `None` value is used as a termination signal for the consumer.

## When to Use Queues

- **Multi-threading:** Safe communication between threads.
- **Task Scheduling:** Manage background tasks efficiently.
- **Producer-Consumer Pattern:** Decouples data production and processing.
- **Asynchronous Processing:** Handles workloads in real-time applications.

## Conclusion

Queues in Python provide an efficient way to handle task management, inter-thread communication, and priority-based execution. Using `queue.Queue`, `LifoQueue`, and `PriorityQueue`, you can implement different types of queuing mechanisms based on your application needs.

