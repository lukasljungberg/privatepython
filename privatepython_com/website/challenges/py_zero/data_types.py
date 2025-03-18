# Run the code to say "Hello USERNAME!"
# Change
x = bytes(b"Hello USERNAME!") 
y = "Try again!"
z = (y, x)

a = y

# Don't change
def func():
    if b"USERNAME" not in globals()['a']:
        print(z[0].decode())
    else:
        print(z[1].decode())
func()
# STATIC
# Don't change
def func():
    if b"USERNAME" not in globals()['a']:
        print(z[0].decode())
    else:
        print(z[1].decode())
func()