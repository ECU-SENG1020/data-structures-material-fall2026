# defining the Person class
# classes are typically abstractions of real world objects and processes
class Person:
    def __init__(self, name, age):
        # defining instance variables  (properties of the object.  e.g. properties of a person)
        # must prefix properties with self when reading and writing to them
        self.name = name
        self.age = age

    # all instance methods should have 'self' as the first parameter
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")



# first instance of Person (self in class will point to this instance)
p1 = Person("Alice", 30)
p1.greet()

# second instance of Person (self in class will point to this instance)
p2 = Person("Bob", 25)
p2.greet()
