# Change
class User:
    x = "USERNAME"
    def present_user(self):
        return self.x
    
def the_function(print_this: bool = False, the_list: list = None):
    if print_this:
        print(''.join(the_list))

# Don't change
class Person(User):
    def __init__(self):
        self.x = "NO_USER"
    
    def get_username_as_list(self):
        return list(self.present_user())

user_person = Person()
the_function(the_list=user_person.get_username_as_list())
# STATIC
# Don't change
class Person(User):
    def __init__(self):
        self.x = "NO_USER"
    
    def get_username_as_list(self):
        return list(self.present_user())

user_person = Person()
the_function(the_list=user_person.get_username_as_list())
        
        
