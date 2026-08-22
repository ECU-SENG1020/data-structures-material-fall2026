from SetDataStructure import MySet
from HashedSetDataStructure import MyHashedSet
# # my_list = []
# # my_tuple = ()
# # my_dictionary = {}
# # my_set = set()

# # my_list = [1, 2, 3, 4, 5]
# # my_set = {1, 2, 3, 4, 5}
# # my_tuple = (1, 2, 3, 4, 5)

# # my_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# built_set = set()
# my_set = MySet()
# print(built_set)
# print(my_set) 

# built_set.add(1)
# built_set.add(2)
# built_set.add(3)
# built_set.add(1)
# built_set.add(2)

# built_set.remove(1)
# # built_set.remove(1)

# print(built_set)  # set([1, 2, 3])

# my_set.add(1)
# my_set.add(2)
# my_set.add(3)
# my_set.add(1)
# my_set.remove(1)
# my_set.remove(1)
# print(my_set)   # set([1, 2, 3])

# for i in built_set:
#     print(i)

# for i in my_set:
#     print(i)

# print(my_set)   # set([1, 2, 3])

# my_dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }

# print(my_dict)
# print(my_dict["b"])
# my_dict["d"] = 4
# print(my_dict)
# my_dict["d"] = 5
# print(my_dict)
# # print(my_dict.keys())

# print(my_dict.values())
# print(len(my_dict))
# print(my_dict.items())

# for x in my_dict:
#     print(x)

# for x in my_dict.keys():
#     print(x)

# for x in my_dict.values():
#     print(x)

# for key, value in my_dict.items():
#     print(key, value)
#     print(key + " " + str(value))

# print(hash("Hello"))
# print(hash("Hello"))
# print(hash("hello"))

# my_hashed_set = MyHashedSet()
# print(my_hashed_set)
# my_hashed_set.add("Hello")
# my_hashed_set.add("World")
# print(my_hashed_set)
# # my_hashed_set.remove("Hello")
# print(my_hashed_set)

# for i in my_hashed_set:
#     print(i)



# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# # union
# print("Union: A | B =", A | B)  # {1, 2, 3, 4, 5, 6, 7, 8}
# print("Union: B | A =", B | A)  # {1, 2, 3, 4, 5, 6, 7, 8}

# # intersection
# print("Intersection: A & B =", A & B)  # {4, 5}
# print("Intersection: B & A =", B & A)  # {4, 5}

# # difference
# print("Difference: A - B =", A - B)  # {1, 2, 3}
# print("Difference: B - A =", B - A)  # {8, 6, 7}

my_setA = MySet()
my_setB = MySet()

my_setA.add(1)
my_setA.add(2)
my_setA.add(3)
my_setA.add(4)
my_setA.add(5)

my_setB.add(4)
my_setB.add(5)
my_setB.add(6)
my_setB.add(7)
my_setB.add(8)

print("Union: A | B =",my_setA | my_setB)  # {1, 2, 3, 4, 5, 6, 7, 8}
print("Union: B | A =",my_setB | my_setA)  # {1, 2, 3, 4, 5, 6, 7, 8}

print("Intersection: A & B =",my_setA & my_setB)  # {4, 5}
print("Intersection: B & A =",my_setB & my_setA)  # {4, 5}

print("Difference: A - B =",my_setA- my_setB)  # {1, 2, 3}
print("Difference: B - A =",my_setB - my_setA)  # {8, 6, 7}