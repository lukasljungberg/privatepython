# Run the code to say "Hello USERNAME!"
# Change
class User:
    x = "Hello USERNAME!"
    def present_user(self):
        return self.x
    
def the_function(print_this: bool = False, the_str: str = None):
    if print_this:
        print(the_str)
subclass = None
# Don't change
class Person(User):
    def __init__(self):
        self.x = "NO_USER"
    
    def get_username(self):
        return self.present_user()

user_person = Person()
the_function(issubclass(Person, subclass), the_str=user_person.get_username())
# STATIC
# Don't change
class Person(User):
    def __init__(self):
        self.x = "NO_USER"
    
    def get_username(self):
        return self.present_user()

user_person = Person()
the_function(issubclass(Person, subclass), the_str=user_person.get_username())