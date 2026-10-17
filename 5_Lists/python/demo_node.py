from NodeModule import Node

nodeA = Node("a")

print(nodeA.data)

print(nodeA)

nodeB = Node("b")
print(nodeB)

nodeC = Node("c")
print(nodeC)
print("***********")
nodeA.next = Node("b")
print(nodeA.next)
print(nodeA.next.data)

print(type(nodeA))
print(type(nodeA.next))

nodeA.next.next = Node("c")

print(nodeA.next.next)

print(nodeA.next.next.data)
print("print fourth node")
print(nodeA.next.next.next)

# current_node = nodeA
# count = 0
# while current_node:
#     print(current_node.data)
#     count = count + 1
#     current_node = current_node.next

# print(count)

# builtin_list = ["a","b","c"]
# builtin_list.append("d")
# print(builtin_list)

# # head - first node
# # find the end of the linked list of nodes
# # set next property of last node = to the append(value)

# print(dir(builtin_list))




