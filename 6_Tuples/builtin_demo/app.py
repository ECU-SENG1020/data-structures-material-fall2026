nested = ((1, 2), (3, 4))
print("Nested:", nested)

print(nested[1][0])

x = nested[1]
y = x[0]
print(y)



nums = (5, 10, 15)
print(dir(nums))


print("Min, Max, Sum:", min(nums), max(nums), sum(nums))

# Convert to list to modify
mutable = list(nums)
mutable.append(20)
nums2 = tuple(mutable)
print("Converted, modified, reconverted:", nums2)

print('\nTuple demo complete (Python).')