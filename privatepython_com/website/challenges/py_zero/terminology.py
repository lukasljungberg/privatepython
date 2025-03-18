# Run the code to say "Hello USERNAME!" one time...
# Change
x = 1
y = 0
z = [0, 2, 4, 6, 8]

# Don't change
for i in z:
    try:
        x = x/x
        print("Try again!")
    except ZeroDivisionError:
        if y in z:
            print("Hello USERNAME!")
# STATIC
# Don't change
for i in z:
    try:
        x = x/x
        print("Try again!")
    except ZeroDivisionError:
        if y in z:
            print("Hello USERNAME!")

