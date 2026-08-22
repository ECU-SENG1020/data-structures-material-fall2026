from DsDictionaryModule import DsDictionary

my_dict2 = DsDictionary([("a", 1), ("b", 2)])
print(my_dict2)

my_dict = DsDictionary()
print(dir(my_dict))

# Add items to the dictionary
my_dict["name"] = "Alice"
my_dict["age"] = 25

keys_view = my_dict.keys()
values_view = my_dict.values()
items_view = my_dict.items()

print(keys_view)
print(values_view)
print(items_view)

my_dict["city"] = "New York"

print(keys_view)
print(values_view)
print(items_view)
