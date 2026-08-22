# Tuple Quiz — Multiple Choice

Answer each question by selecting the correct option (A–D). Answers are listed below each question.

1. Which of the following best describes a Python tuple?
   A) An unordered, mutable collection of unique elements
   B) An ordered, mutable sequence of elements
   C) An ordered, immutable collection of objects
   D) A mutable mapping from keys to values

   Answer: C

2. How do you create a single-element tuple containing the number 42?
   A) `(42)`
   B) `[42]`
   C) `(42,)`
   D) `tuple(42)`

   Answer: C

3. Which operation has O(1) complexity on a tuple?
   A) Membership test (`x in t`)
   B) Indexing (`t[i]`)
   C) Concatenation (`t + u`)
   D) Slicing (`t[a:b]`)

   Answer: B

4. What will the expression `t.count(x)` do for a tuple `t`?
   A) Return the index of `x` in `t`
   B) Return how many times `x` appears in `t`
   C) Remove all occurrences of `x` in `t`
   D) Raise a `TypeError`

   Answer: B

5. Which of these is a valid way to create a tuple?
   A) `t = (1, 2, 3)`
   B) `t = 1, 2, 3`
   C) `t = tuple([4,5,6])`
   D) All of the above

   Answer: D

6. What happens if you try to execute `t[0] = 99` on a tuple `t`?
   A) The first element is replaced successfully
   B) A `TypeError` is raised
   C) The tuple converts to a list automatically
   D) The assignment is ignored silently

   Answer: B

7. When is a tuple hashable?
   A) Always, regardless of contents
   B) Never — tuples are mutable
   C) Only if every element inside the tuple is hashable
   D) Only if the tuple contains no numbers

   Answer: C

8. Which method returns the index of the first occurrence of a value in a tuple (or raises an error if missing)?
   A) `t.find(x)`
   B) `t.locate(x)`
   C) `t.index(x)`
   D) `t.position(x)`

   Answer: C

9. Which of the following is true about tuples compared to lists?
   A) Tuples are mutable; lists are immutable
   B) Tuples generally use slightly less memory than lists
   C) Lists are hashable if their elements are hashable
   D) Tuples support `append()` and `extend()`

   Answer: B

10. How can you convert a tuple `t` to a list?
    A) `list(t)`
    B) `t.to_list()`
    C) `tuple(t)`
    D) `t.convert(list)`

    Answer: A

11. Which code correctly unpacks the tuple `(10, 20)` into variables `x` and `y`?
    A) `x = (10, 20)`; `y = None`
    B) `x, y = (10, 20)`
    C) `x = 10; y = 20` only
    D) `x = (10); y = (20)`

    Answer: B

12. What does the starred assignment `a, *rest = (1, 2, 3)` produce for `rest`?
    A) `rest` is `1`
    B) `rest` is `None`
    C) `rest` is `[2, 3]`
    D) `rest` is `(2, 3)`

    Answer: D

13. Why might you prefer a tuple over a list for dictionary keys?
    A) Tuples are mutable and update automatically
    B) Tuples can be hashed (if contents are hashable), lists cannot
    C) Tuples are larger in memory and therefore safer
    D) Lists are not iterable

    Answer: B

14. What will `len(t)` return for a tuple `t`?
    A) The number of elements in `t`
    B) The memory size of `t` in bytes
    C) Always `1` for tuples
    D) Raises an exception

    Answer: A

15. Given `t = (1, [2,3])`, which of the following is true?
    A) `t` is fully immutable; you cannot change any element
    B) You can modify the inner list: `t[1].append(4)` is allowed
    C) `hash(t)` will always succeed
    D) `t.count([2,3])` raises `TypeError`

    Answer: B

16. Which operation creates a new tuple rather than modifying an existing one?
    A) `t.append(4)`
    B) `t += (4,)`
    C) `t[0] = 5`
    D) `t.pop()`

    Answer: B

17. What is the time complexity of checking membership `x in t` for a tuple `t` of length n?
    A) O(1)
    B) O(log n)
    C) O(n)
    D) O(n log n)

    Answer: C

18. Which of these demonstrates creating a tuple from an iterable?
    A) `t = tuple([4,5,6])`
    B) `t = (i for i in [4,5,6])`
    C) `t = list((4,5,6))`
    D) `t = {4,5,6}`

    Answer: A

19. If you want to swap the first and last elements of a 3-tuple `t`, which returned value is correct for `swap_first_last((1,2,3))`?
    A) `(1,2,3)`
    B) `(3,2,1)`
    C) `[3,2,1]`
    D) Raises `TypeError`

    Answer: B

20. Which of the following tuple methods will raise `ValueError` if the element is missing?
    A) `t.count(x)`
    B) `t.index(x)`
    C) `t.find(x)`
    D) `t.locate(x)`

    Answer: B
