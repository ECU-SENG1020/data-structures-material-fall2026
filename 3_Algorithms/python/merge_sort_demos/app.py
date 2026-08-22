from NodeModule import Node
from list_merge_sort import merge_sort
from linked_list_merge_sort import linked_list_merge_sort

# Example list for students to try
numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print("UNSORTED:")
print(" ".join(str(num) for num in numbers))

# Sort the entire list (0 .. len(numbers)-1)
merge_sort(numbers, 0, len(numbers) - 1)

print("SORTED:")
print(" ".join(str(num) for num in numbers))


print("SORTED DESCENDING:")
merge_sort(numbers, 0, len(numbers) - 1, reverse=True)
print(" ".join(str(num) for num in numbers))

head = Node(10)
head.next = Node(2)
head.next.next = Node(78)
head.next.next.next = Node(4)
head.next.next.next.next = Node(45)
head.next.next.next.next.next = Node(32)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(11)
print("\nUNSORTED LINKED LIST:")
current = head
while current:
    print(current.data, end=" ")
    current = current.next


print("\nSORTED LINKED LIST:")
head = linked_list_merge_sort(head)
current = head
while current:
    print(current.data, end=" ")
    current = current.next

