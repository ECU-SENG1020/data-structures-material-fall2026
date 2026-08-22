from ListModule import DsList


my_list = DsList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(len(my_list))
print(my_list)

custom_string_list = DsList()
custom_string_list.append('a')
custom_string_list.append('b')
print(custom_string_list)

print(my_list[0])

# Example iteration:
for item in my_list:
    print(item)


# Example contains:
print(3 in my_list)
