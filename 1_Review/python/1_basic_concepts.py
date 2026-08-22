
# printing to the console
# print is built-in python function
print("It's me")

# must define custom methods before you can use them

# create a function that returns None
def greet():
    print("Hello, World!")
    print("Hello again")

def greet2():
    print("Hello, World!: ", end="")

# creates a function that returns a number
def add(num1, num2):
    return num1 + num2

# greet function does not execute until you call it
greet()
greet()

greet2()
greet2()

# prints 3 to the console
print(add(1,2))

# prints None to the console
print(greet())


items = [1,2,3]
items2 = items * 2
print(items2)

items3 = [item * 2 for item in items]
print(items3)

items4 = map(lambda item: item * 2, items)
print(items4)

items5 = list(items4)
print(items5)