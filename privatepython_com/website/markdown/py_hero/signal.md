# Python Signal Handling

## Introduction

The `signal` module in Python provides a way to handle asynchronous events, such as interrupts or termination signals from the operating system. Signals are used to manage inter-process communication and gracefully handle unexpected terminations.

## Understanding Signals in Python

A **signal** is a notification sent to a process to notify it of an event. Some common signals include:
- `SIGINT` (Interrupt, e.g., Ctrl+C)
- `SIGTERM` (Termination request)
- `SIGHUP` (Hangup detected)
- `SIGKILL` (Force kill - cannot be caught or ignored)
- `SIGUSR1` and `SIGUSR2` (User-defined signals)

Python’s `signal` module allows programs to define handlers for these signals and execute custom functions when a signal is received.

## Handling Signals in Python

### Basic Signal Handling

You can handle a signal using `signal.signal(signal_name, handler_function)`, where the `handler_function` is executed when the signal is received.

```python
import signal
import time

def handle_signal(signum, frame):
    print(f"Received signal: {signum}. Gracefully shutting down.")
    exit(0)

# Register signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handle_signal)

print("Press Ctrl+C to exit...")
while True:
    time.sleep(1)
```

### Explanation:
1. `signal.signal(signal.SIGINT, handle_signal)` registers a handler for `SIGINT` (Ctrl+C).
2. When `SIGINT` is received, `handle_signal` executes, printing a message and exiting the program.

## Handling Multiple Signals

You can register multiple signals to handle different types of interrupts:

```python
def handle_usr(signum, frame):
    print(f"Received user signal: {signum}")

signal.signal(signal.SIGUSR1, handle_usr)
signal.signal(signal.SIGUSR2, handle_usr)

print("Waiting for SIGUSR1 or SIGUSR2...")
while True:
    time.sleep(1)
```

### Sending Signals Manually

From another terminal, you can send a signal to the running process using:
```bash
kill -USR1 <process_id>
kill -USR2 <process_id>
```
Find the process ID using `ps aux | grep python`.

## Ignoring Signals

If you want to ignore a specific signal, set its handler to `signal.SIG_IGN`.

```python
signal.signal(signal.SIGTERM, signal.SIG_IGN)
```
This prevents the process from being terminated by `SIGTERM`.

## Resetting to Default Behavior

To restore a signal’s default behavior, use `signal.SIG_DFL`.

```python
signal.signal(signal.SIGINT, signal.SIG_DFL)
```

## Using `signal.setitimer()` for Timers

Python allows sending periodic signals using `setitimer()`, which generates a signal after a specified time interval.

```python
def timeout_handler(signum, frame):
    print("Timeout! Exiting.")
    exit(1)

signal.signal(signal.SIGALRM, timeout_handler)
signal.setitimer(signal.ITIMER_REAL, 5)  # Trigger SIGALRM in 5 seconds

print("Waiting for timeout...")
time.sleep(10)
```

### Explanation:
1. `setitimer(signal.ITIMER_REAL, 5)` schedules `SIGALRM` in 5 seconds.
2. When the signal triggers, `timeout_handler` executes and exits the program.

## When to Use Signals
- Handling process termination (`SIGTERM`, `SIGINT`)
- Gracefully shutting down applications
- Implementing timeout functionality (`SIGALRM`)
- Inter-process communication (`SIGUSR1`, `SIGUSR2`)
- Ignoring unwanted signals

## Limitations of Signals in Python
- Signals are process-wide and do not work well with multi-threading.
- Some signals (like `SIGKILL`) cannot be caught or ignored.
- Works primarily on Unix-based systems; Windows has limited support.

## Conclusion
Signals in Python allow for efficient process control, handling interruptions, and implementing timers. They are useful for graceful shutdowns and inter-process communication but should be used with caution in multi-threaded programs.

