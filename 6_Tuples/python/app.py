from TupleModule import DsTuple

my_tuple = DsTuple("a", "b", "c")
print("my_tuple = ", my_tuple)
print("length = ", len(my_tuple))
print("item[2] = ", my_tuple[2])
print("contains 'b'? ", ("b" in my_tuple))

other = DsTuple("x", "y")
print("combined = ", my_tuple + other)
print("count('b') = ", len(other))
print("index('b') = ", other.index("b"))


implicit_tuple = 1, 2, 3  # Packing
x, y, z = implicit_tuple  # Unpacking

print(type(implicit_tuple))


class TupleWithPack:
    def __init__(me, iterable=None):
        me.data = [] if iterable is None else list(iterable)

    @classmethod
    def pack(cls, *values):
        return cls(values)   #   TupleWithPack()
    
    @staticmethod
    def greet(name):
        print(f"Hello, {name}")

    @staticmethod
    def is_hashable(obj):
        try:
            hash(obj)
            return True
        except TypeError:
            return False

    # def greet2(name):
    #     print(f"Hello, ${name}")


result = TupleWithPack.pack(1,"school",['a','b','c'])
print(type(result))


TupleWithPack.greet("Deon")
# TupleWithPack.greet2("Joshua")
test = TupleWithPack()
# test.greet2("Brian")
