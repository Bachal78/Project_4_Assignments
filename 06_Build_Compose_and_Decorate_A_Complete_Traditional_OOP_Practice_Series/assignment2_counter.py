"""Assignment:
Create a class Counter that keeps track of how many objects have been created.
Use a class variable and a class method with cls to manage and display the count."""
#class variable	Shared by everyone
# (A class variable is a variable that is shared by all instances of a class)

#class method	Changes something for everyone
# (A class method is a method that is bound to the class and not the instance of the class)
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

# Example
c1 = Counter()
c2 = Counter()
c3 = Counter()
Counter.show_count()
