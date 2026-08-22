
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Wuf")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Meow")