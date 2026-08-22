
# import entire module
import random
items = ['A','B','C','D','E']
print('***available choices to choose from***')
print(items)
print('***first random choice***')
print(random.choice(items))
print('***second random choice***')
print(random.choice(items))
print()

# import entire module and give it an alias
import random as m
items = ['A','B','C','D','E']
print('***before shuffle***')
print(items)
m.shuffle(items)
print('***after shuffle***')
print(items)
print()

# importing specific object from a module
from math import pow
print(f'2 to the power of 2 is: {pow(2,2)}')

