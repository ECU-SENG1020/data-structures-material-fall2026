from random import choice

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def __ge__(self, other):
        return self.age >= other.age

    def __add__(self, other):
        sex = choice(['boy', 'girl'])
        return Person(f'Baby {sex}', 0)


fruits = ["apple", "banana", "cherry"]
print(fruits)

p1 = Person("Alice", 35)
print(p1)

p2 = Person("Bob", 30)
print(p2)

print("Alice is older than Bob: ", p1 >= p2)

p3 = p1 + p2
print(p3)

p4 = p2 + p1
print(p4)

p5 = p1 + p2
print(p5)