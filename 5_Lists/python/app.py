from ListModule import DsList


my_list = DsList()

# Example append
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Example len()
print("*" * 20)
print(len(my_list))

# Example __str__
print("*" * 20)
print(my_list)

# Example with strings
print("*" * 20)
custom_string_list = DsList()
custom_string_list.append('a')
custom_string_list.append('b')
print(custom_string_list)

# Example using index
print("*" * 20)
print(my_list[0])
my_list[0] = 'A'
print(my_list[0])


# Example iteration:
print("*" * 20)
for item in my_list:
    print(item)

# Example contains:
print("*" * 20)
print(3 in my_list)

# Example slice:
print("*" * 20)
print(my_list[0:6:1])
