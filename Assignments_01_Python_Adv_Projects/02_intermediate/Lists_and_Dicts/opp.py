class Person:
    def __init__(self, color, age, weight): #property, instance, 
        self.color=color
        self.__age = age #private attribute (encapsulated)
        self.weight =weight
    
    def age(self):
        return self.__age
    #action, behaviour, method
    def walk(self):# self represenet coming buleprints
        print("Walking")
    def running(self):
        print("Running")

Person1= Person("red", "20", "60kg") 
Person2 = Person("blue", "25", "70kg")
print(Person1.color)
print(Person1.age())
print(Person2.color)
Person2.running()


#_engine_status=False (protected) class khud instamal kr sakta hai and subclass bhi
#accessors(public, private, protected), mutators, getters and setters