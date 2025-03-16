# Change
x = 11
y = None
z = False

a = "USERNAME123"
b = [True, True, 1, 1]
c = {'msg': "Fail!"}

# Don't change
name = "USERNAME"
fail = "Try again!"
if x <= y:
    if name not in a and z in b and c['msg'] == fail:
        print(name if z == True else fail)
# STATIC
# Don't change
name = "USERNAME"
fail = "Try again!"
if x <= y:
    if name not in a and z in b and c['msg'] == fail:
        print(name if z == True else fail)
