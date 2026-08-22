"""Merge sort implementation for singly-linked lists.

This module provides `linked_list_merge_sort(head, reverse=False)` which
performs an in-place merge sort on a singly-linked list whose nodes are
instances of `Node` from `NodeModule`.

Algorithm notes:
- Uses the classic divide-and-conquer merge sort for linked lists.
- Splitting is done with the tortoise-and-hare (slow/fast) technique.
- Merging uses a dummy head node to simplify tail manipulation.
- This implementation is stable and runs in O(n log n) time with O(1)
  auxiliary space (not counting recursion stack), since nodes are relinked
  rather than copied.

Parameters
- head: Node | None - head node of the linked list to sort.
- reverse: bool - if True, sort in descending order. Default is False.

Returns
- Node | None - head of the sorted linked list.

Edge cases handled:
- Empty list (head is None) and single-node lists are returned as-is.
"""

from NodeModule import Node


def linked_list_merge_sort(head, reverse=False):
    """Sort a singly-linked list using merge sort.

    The function returns the head of the sorted list. Setting `reverse=True`
    will produce a descending order sort.

    The `reverse` flag is applied during the merge comparison using an XOR
    trick so the merge logic only needs one comparison expression.
    """

    def _split(head):
        """Split the list into two halves and return (left_head, right_head).

        Uses the slow/fast pointer strategy: `slow` advances one step and
        `fast` advances two steps. When `fast` reaches the end, `slow` is
        at the midpoint. We cut the list by setting `slow.next = None`.

        Returns (head_of_first_half, head_of_second_half).
        """
        if head is None or head.next is None:
            # Zero or one element — nothing to split.
            return head, None
        slow = head
        fast = head.next
        # Advance `fast` by two and `slow` by one until `fast` reaches the end.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # `slow` is just before the midpoint for the split.
        mid = slow.next
        slow.next = None
        return head, mid

    def _merge(a, b):
        """Merge two sorted lists `a` and `b` and return the merged head.

        Uses a dummy node to collect nodes while traversing `a` and `b`.
        The expression `(a.data <= b.data) ^ reverse` controls the comparison
        direction:
        - When `reverse` is False, it behaves like `a.data <= b.data`.
        - When `reverse` is True, XOR flips the result to implement greater-than
          ordering without duplicating the merge logic.

        This merge relinks existing nodes (no new Node objects are created
        except for the dummy), preserving stability.
        """
        dummy = Node()
        tail = dummy
        # Walk both lists and attach the smaller (or larger when reverse)
        # node to `tail.next`, advancing that list's pointer.
        while a and b:
            # XOR used to invert comparison when reverse==True.
            if (a.data <= b.data) ^ reverse:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        # At least one list is exhausted; append the remainder.
        tail.next = a or b
        return dummy.next

    def _merge_sort(node):
        """Recursive merge sort on list starting at `node`.

        Base case: empty or single-node lists are already sorted. Otherwise,
        split, recursively sort both halves, and merge them.
        """
        if node is None or node.next is None:
            return node
        left, right = _split(node)
        left = _merge_sort(left)
        right = _merge_sort(right)
        return _merge(left, right)

    return _merge_sort(head)