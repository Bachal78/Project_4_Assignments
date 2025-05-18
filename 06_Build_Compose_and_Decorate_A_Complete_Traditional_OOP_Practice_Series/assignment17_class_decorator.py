"""Create a class decorator add_greeting that
modifies a class to add a greet() method returning "Hello from Decorator!".
Apply it to a class Person"""

def add_greeting(cls):
    class NewClass(cls):
        def greet(self):
            return "Hello from Decorator!"
    return NewClass

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example
p = Person("Ali")
print(p.greet())
