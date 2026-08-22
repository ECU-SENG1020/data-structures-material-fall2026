# list
# mutable collection of heterogenous data types
fruit_list = ['apple','banana', 'cherry']
# [] - empty list
# my_list = list((1,2,3))
# tuple
# immutable collection of heterogenous data types
fruit_tuple = ('apple','banana','cherry')

# (,) - empty tuple
# my_tuple = tuple([1,2,3])
# x = (5)
# y = (5,)
# dictionary
# collection of key:value pairs
fruit_dictionary = {'a':'apple','b':'banana'}
# {} - empty dictionary
# my_dict = dict([(1,'apple'), (2,'banana')])

# set
# collection of unique values
fruit_set = {'apple','banana', 'cherry','cherry'}

# what is this?
# thing = {}

# empty_set = set(['apple','banana','cherry','apple'])

# converting a tuple to a list using list constructor
fruits2 = list(fruit_tuple)

# iterating over collections

print("***** List *****")
for fruit in fruit_list:
    print(fruit)

print("***** tuple *****")
for fruit in fruit_tuple:
    print(fruit)

print("***** set *****")
for fruit in fruit_set:
    print(fruit)

# x,*y = fruit_tuple
# print(y)

print("***** dictionary *****")
# keys, values, items
for (key,value) in fruit_dictionary.items():
    print(key, value)

for item in fruit_dictionary.items():
    (key, value) = item
    print(f'Key from tuple: {key} - value from tuple: {value}')

for key in fruit_dictionary.keys():
    print(key)

for value in fruit_dictionary.values():
    print(value)


